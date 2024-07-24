from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from cpovc_ovc.forms import OVCSearchForm
from cpovc_forms.functions import get_person_ids
from cpovc_forms.models import OVCCaseRecord
from cpovc_registry.models import (
    RegPerson, RegPersonsGuardians, RegPersonsSiblings,
    RegPersonsExternalIds)
from cpovc_main.functions import convert_date, get_dict
from cpovc_ovc.functions import get_school, get_health
from cpovc_pfs.functions import save_school

from .forms import OVCPMTCTRegistrationForm
from .models import OVCPMTCTRegistration
from cpovc_pfs.functions import get_person_org_unit, save_health


# PMTCT Pages
@login_required
def pmtct_home(request):
    """Some default page for the home page for preventive and FS."""
    try:
        form = OVCSearchForm(data=request.GET)
        afc_ids, case_ids = {}, {}
        search_string = request.GET.get('search_name')
        pids = get_person_ids(request, search_string)
        cases = RegPerson.objects.filter(is_void=False, id__in=pids)
        # Get case record sheet details
        crss = OVCCaseRecord.objects.filter(is_void=False, person_id__in=pids)
        for crs in crss:
            case_ids[crs.person_id] = {'clv': 1, 'cid': crs.case_id}
        # Check if there is a filled Preventive Form
        afcs = OVCPMTCTRegistration.objects.filter(
            is_void=False, person_id__in=pids)
        for afc in afcs:
            afc_ids[afc.person_id] = {'cid': afc.pk,
                                      'clv': 2, 'cdt': afc.registration_date}
        for case in cases:
            pid = case.id
            cid = afc_ids[pid]['cid'] if pid in afc_ids else 'N/A'
            cdt = afc_ids[pid]['cdt'] if pid in afc_ids else 'N/A'
            clvf = case_ids[pid]['clv'] if pid in case_ids else 0
            crs_id = case_ids[pid]['cid'] if pid in case_ids else None
            clv = afc_ids[pid]['clv'] if pid in afc_ids else clvf
            setattr(case, 'case_t', str(cid))
            setattr(case, 'case_date', cdt)
            setattr(case, 'case_level', clv)
            setattr(case, 'case_id', crs_id)
        return render(request, 'pfs/pmtct/home.html',
                      {'status': 200, 'cases': cases, 'form': form})
    except Exception as e:
        print('PMTCT-OVC home error - %s' % (str(e)))
        raise e


@login_required
def new_pmtct(request, id):
    """New page for New PMTCT."""
    try:
        params, gparams = {}, {}
        initial = {}
        person_id = int(id)
        child = RegPerson.objects.get(is_void=False, id=person_id)
        sex = child.sex_id
        age = child.years
        fname = child.first_name
        if sex == 'SMAL' or age < -5:
            msg = "%s - Does not qualify to PMTCT-OVC Program" % (fname)
            messages.error(request, msg)
            url = reverse('pmtct_home')
            return HttpResponseRedirect(url)
        guardians = RegPersonsGuardians.objects.filter(
            is_void=False, child_person_id=child.id)
        # Get siblings
        siblings = RegPersonsSiblings.objects.filter(
            is_void=False, child_person_id=child.id)
        print('p', params, 'gp', gparams)
        guids, chids = [], []
        for guardian in guardians:
            guids.append(guardian.guardian_person_id)
        guids.append(child.id)
        for sibling in siblings:
            chids.append(sibling.sibling_person_id)
        pids = {'guids': guids, 'chids': chids}
        print(pids)
        # Existing
        extids = RegPersonsExternalIds.objects.filter(
            person_id__in=guids)
        for extid in extids:
            if extid.person_id == child.id:
                params[extid.identifier_type_id] = extid.identifier
            else:
                gkey = '%s_%s' % (extid.person_id, extid.identifier_type_id)
                gparams[gkey] = extid.identifier
        if request.method == 'POST':
            form = OVCPMTCTRegistrationForm(guids=pids, data=request.POST)
            user_id = request.user.id
            hiv_status = request.POST.get('hiv_status')
            # health details
            if hiv_status == 'HSTP':
                save_health(request, person_id)
            cbo_id = request.POST.get('cbo_id')
            caregiver_contact = request.POST.get('caregiver_contact')
            school_level = request.POST.get('school_level')
            school_id = request.POST.get('school_id')
            if school_level == 'SLNS':
                school_id = None
            else:
                save_school(request, person_id, school_level)
            registration_date = request.POST.get('registration_date')
            reg_date = convert_date(registration_date)
            obj, created = OVCPMTCTRegistration.objects.update_or_create(
                person_id=person_id, is_void=False,
                defaults={'child_cbo_id': cbo_id, 'school_id': school_id,
                          'created_by_id': user_id, 'hiv_status': hiv_status,
                          'caregiver_contact': caregiver_contact,
                          'registration_date': reg_date},
            )
            action = "Created" if created else "edited"
            msg = "PMTCT-OVC registration %s Successfully" % action
            messages.info(request, msg)
            url = reverse('view_pmtct', kwargs={'id': id})
            return HttpResponseRedirect(url)
        # Default GET page
        org_unit_id = get_person_org_unit(request, person_id)
        org_id = request.session.get('ou_primary', 0)
        cbo_id = org_unit_id if org_unit_id else org_id
        initial['cbo_id'] = cbo_id
        form = OVCPMTCTRegistrationForm(guids=pids, initial=initial)
        # Class levels
        levels = {}
        levels["SLNS"] = []
        levels["SLEC"] = ["BABY,Baby Class", "MIDC,Middle Class",
                          "PREU,Pre-Unit"]
        levels["SLPR"] = ["CLS1,Class 1", "CLS2,Class 2", "CLS3,Class 3",
                          "CLS4,Class 4", "CLS5,Class 5", "CLS6,Class 6",
                          "CLS7,Class 7", "CLS8,Class 8"]
        levels["SLSE"] = ["FOM1,Form 1", "FOM2,Form 2", "FOM3,Form 3",
                          "FOM4,Form 4", "FOM5,Form 5", "FOM6,Form 6"]
        levels["SLUN"] = ["YER1,Year 1", "YER2,Year 2", "YER3,Year 3",
                          "YER4,Year 4", "YER5,Year 5", "YER6,Year 6"]
        levels["SLTV"] = ["TVC1,Year 1", "TVC2,Year 2", "TVC3,Year 3",
                          "TVC4,Year 4", "TVC5,Year 5"]
        return render(request, 'pfs/pmtct/new_registration.html',
                      {'form': form, 'child': child, 'levels': levels})
    except Exception as e:
        print('New PMTCT-OVC error - %s' % (str(e)))
        raise e


@login_required
def edit_pmtct(request, id):
    """New page for New preventive and FS."""
    try:
        params, gparams = {}, {}
        initial = {}
        person_id = int(id)
        child = RegPerson.objects.get(is_void=False, id=person_id)
        guardians = RegPersonsGuardians.objects.filter(
            is_void=False, child_person_id=child.id)
        # Get siblings
        siblings = RegPersonsSiblings.objects.filter(
            is_void=False, child_person_id=child.id)
        print('p', params, 'gp', gparams)
        guids, chids = [], []
        for guardian in guardians:
            guids.append(guardian.guardian_person_id)
        guids.append(child.id)
        for sibling in siblings:
            chids.append(sibling.sibling_person_id)
        pids = {'guids': guids, 'chids': chids}
        print(pids)
        # Existing
        extids = RegPersonsExternalIds.objects.filter(
            person_id__in=guids)
        for extid in extids:
            if extid.person_id == child.id:
                params[extid.identifier_type_id] = extid.identifier
            else:
                gkey = '%s_%s' % (extid.person_id, extid.identifier_type_id)
                gparams[gkey] = extid.identifier
        if request.method == 'POST':
            form = OVCPMTCTRegistrationForm(guids=pids, data=request.POST)
            user_id = request.user.id
            caregiver_contact = request.POST.get('caregiver_contact')
            school_level = request.POST.get('school_level')
            school_id = request.POST.get('school_id')
            hiv_status = request.POST.get('hiv_status')
            if hiv_status == 'HSTP':
                save_health(request, person_id)
            cbo_id = request.POST.get('cbo_id')
            if school_level == 'SLNS':
                school_id = None
            else:
                save_school(request, person_id, school_level)
            registration_date = request.POST.get('registration_date')
            reg_date = convert_date(registration_date)
            obj, created = OVCPMTCTRegistration.objects.update_or_create(
                person_id=person_id, is_void=False,
                defaults={'child_cbo_id': cbo_id, 'school_id': school_id,
                          'created_by_id': user_id, 'hiv_status': hiv_status,
                          'caregiver_contact': caregiver_contact,
                          'registration_date': reg_date},
            )
            action = "Created" if created else "edited"
            msg = "PMTCT-OVC registration %s Successfully." % action
            messages.info(request, msg)
            url = reverse('view_pmtct', kwargs={'id': id})
            return HttpResponseRedirect(url)
        # GET Method
        ovc = OVCPMTCTRegistration.objects.get(
            is_void=False, person_id=person_id)
        reg_date = ovc.registration_date.strftime('%d-%b-%Y')
        # Get health
        health = get_health(person_id)
        link_date, ccc_no, facility_name = '', '', ''
        facility_id, art_status = '', ''
        if health:
            ccc_no = health.ccc_no
            art_status = health.art_status
            facility_id = health.facility_id
            link_date = health.link_date.strftime('%d-%b-%Y')
        # Initial values
        initial['registration_date'] = reg_date
        initial['ccc_number'] = ccc_no
        initial['facility_id'] = facility_id
        initial['facility'] = facility_name
        initial['art_status'] = art_status
        initial['hiv_status'] = ovc.hiv_status
        initial['link_date'] = link_date
        initial['cbo_id'] = ovc.child_cbo_id
        initial['caregiver_contact'] = ovc.caregiver_contact
        # Get School information
        school_level = 'SLNS'
        sch_class, sch_adm_type = '', ''
        school_id, school_name = '', ''
        school = get_school(person_id)
        if school:
            sch_class = school.school_class
            sch_adm_type = school.admission_type
            school_id = school.school_id
            school_name = school.school.school_name
            school_level = school.school_level
        initial['school_level'] = school_level
        initial['school_class'] = sch_class
        initial['school_name'] = school_name
        initial['school_id'] = school_id
        initial['admission_type'] = sch_adm_type

        form = OVCPMTCTRegistrationForm(
            guids=pids, initial=initial)
        # Class levels
        levels = {}
        levels["SLNS"] = []
        levels["SLEC"] = ["BABY,Baby Class", "MIDC,Middle Class",
                          "PREU,Pre-Unit"]
        levels["SLPR"] = ["CLS1,Class 1", "CLS2,Class 2", "CLS3,Class 3",
                          "CLS4,Class 4", "CLS5,Class 5", "CLS6,Class 6",
                          "CLS7,Class 7", "CLS8,Class 8"]
        levels["SLSE"] = ["FOM1,Form 1", "FOM2,Form 2", "FOM3,Form 3",
                          "FOM4,Form 4", "FOM5,Form 5", "FOM6,Form 6"]
        levels["SLUN"] = ["YER1,Year 1", "YER2,Year 2", "YER3,Year 3",
                          "YER4,Year 4", "YER5,Year 5", "YER6,Year 6"]
        levels["SLTV"] = ["TVC1,Year 1", "TVC2,Year 2", "TVC3,Year 3",
                          "TVC4,Year 4", "TVC5,Year 5"]
        allow_edit = True
        return render(request, 'pfs/pmtct/new_registration.html',
                      {'form': form, 'child': child, 'levels': levels,
                       'allow_edit': allow_edit, 'sch_class': sch_class,
                       'school': school})
    except Exception as e:
        print('PMTCT-OVC edit error - %s' % (str(e)))
        raise e


@login_required
def view_pmtct(request, id):
    """View page for New preventive and FS."""
    try:
        ovc_id = int(id)
        child = RegPerson.objects.get(is_void=False, id=ovc_id)
        creg = OVCPMTCTRegistration.objects.get(
            is_void=False, person_id=ovc_id)
        check_fields = ['school_level_id', 'pfs_intervention_id',
                        'class_level_id', 'school_type_id',
                        'art_status_id', 'hiv_status_id']
        vals = get_dict(field_name=check_fields)
        school_level = 'SLNS'
        school = get_school(ovc_id)
        if school:
            school_level = school.school_level
        return render(request, 'pfs/pmtct/view_registration.html',
                      {'creg': creg, 'child': child, 'vals': vals,
                       'school': school, 'school_level': school_level})
    except Exception as e:
        print('PMTCT-OVC view error - %s' % e)
        msg = "OVC/Caregiver not registered in PMTCT-OVC Program"
        messages.error(request, msg)
        url = reverse('new_pfs', kwargs={'id': id})
        return HttpResponseRedirect(url)
    else:
        pass

