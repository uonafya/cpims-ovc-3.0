from django.shortcuts import render
from cpovc_forms.forms import OVCSearchForm
from .forms import OVCPMTCTRegistrationForm

# from cpovc_forms.functions import get_person_ids
from .models import OVCPMTCTRegistration
from cpovc_forms.models import OVCCaseRecord
from cpovc_registry.models import (
    RegPerson, RegPersonsGuardians, RegPersonsSiblings,
    RegPersonsExternalIds)

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from cpovc_main.functions import convert_date, get_dict


# PMTCT Pages
def pmtct_home(request):
    """Some default page for the home page for preventive and FS."""
    try:
        form = OVCSearchForm(data=request.GET)
        # form = SearchForm(data=request.POST)
        # person_type = 'TBVC'
        afc_ids, case_ids = {}, {}
        search_string = request.GET.get('search_name')
        # pids = get_person_ids(request, search_string)
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
        print('fps error - %s' % (str(e)))
        raise e


def new_pmtct(request, id):
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
            ccc_number = request.POST.get('ccc_number')
            facility_id = request.POST.get('facility_id')
            cbo_id = 1
            caregiver_contact = '0700001001'
            # request.POST.get('cbo_id')
            school_level = request.POST.get('school_level')
            school_id = request.POST.get('school_id')
            if school_level == 'SLNS':
                school_id = None
            registration_date = request.POST.get('registration_date')
            reg_date = convert_date(registration_date)
            obj, created = OVCPMTCTRegistration.objects.update_or_create(
                person_id=person_id, is_void=False,
                defaults={'ccc_no': ccc_number, 'child_cbo_id': cbo_id,
                          'school_id': school_id, 'created_by_id': user_id,
                          'facility': facility_id,
                          'caregiver_contact': caregiver_contact,
                          'registration_date': reg_date},
            )
            action = "Created" if created else "edited"
            msg = "Child registration %s Successfully in the Program" % action
            messages.info(request, msg)
            url = reverse('view_pmtct', kwargs={'id': id})
            return HttpResponseRedirect(url)
        else:
            cbo_id = 1
            cbo_uid = 1
            initial['cbo_uid'] = cbo_uid
            initial['cbo_id'] = cbo_id
            initial['cbo_uid_check'] = cbo_uid
            if 'ISOV' in params:
                initial['bcert_no'] = params['ISOV']
                initial['has_bcert'] = 'on'
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
        return render(request, 'pfs/pmtct/new_registration.html',
                      {'form': form, 'child': child, 'levels': levels})
    except Exception as e:
        print('fps error - %s' % (str(e)))
        raise e


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
            ccc_number = request.POST.get('ccc_number')
            facility_id = request.POST.get('facility_id')
            cbo_id = 1
            caregiver_contact = '0700001001'
            # request.POST.get('cbo_id')
            school_level = request.POST.get('school_level')
            cbo_id = 1
            # request.POST.get('cbo_id')
            school_level = request.POST.get('school_level')
            school_id = request.POST.get('school_id')
            facility_id = request.POST.get('facility_id')
            link_date = request.POST.get('link_date')
            art_status = request.POST.get('art_status')
            if school_level == 'SLNS':
                school_id = None
            registration_date = request.POST.get('registration_date')
            reg_date = convert_date(registration_date)
            date_linked = convert_date(link_date) if link_date else None
            obj, created = OVCPMTCTRegistration.objects.update_or_create(
                person_id=person_id, is_void=False,
                defaults={'ccc_no': ccc_number, 'child_cbo_id': cbo_id,
                          'school_id': school_id, 'created_by_id': user_id,
                          'facility_id': facility_id, 'link_date': date_linked,
                          'caregiver_contact': caregiver_contact,
                          'art_status': art_status,
                          'registration_date': reg_date},
            )
            action = "Created" if created else "edited"
            msg = "Child registration %s Successfully in the Program" % action
            messages.info(request, msg)
            url = reverse('view_pmtct', kwargs={'id': id})
            return HttpResponseRedirect(url)
        else:
            ovc = OVCPMTCTRegistration.objects.get(
                is_void=False, person_id=person_id)
            cbo_id = 1
            cbo_uid = 1
            the_date = convert_date(ovc.registration_date, '%Y-%m-%d')
            the_link_date = convert_date(ovc.link_date, '%Y-%m-%d')
            reg_date = the_date.strftime('%d-%b-%Y')
            link_date = the_link_date.strftime('%d-%b-%Y')
            school_level = 'SLNS'
            initial['registration_date'] = reg_date
            initial['ccc_number'] = ovc.ccc_no
            initial['facility_id'] = ovc.facility_id
            initial['facility'] = ovc.facility.facility_name
            initial['school_level'] = school_level
            initial['art_status'] = ovc.art_status
            initial['link_date'] = link_date
            initial['cbo_uid'] = cbo_uid
            initial['cbo_id'] = cbo_id
            initial['cbo_uid_check'] = cbo_uid
            if 'ISOV' in params:
                initial['bcert_no'] = params['ISOV']
                initial['has_bcert'] = 'on'
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
                       'allow_edit': allow_edit})
    except Exception as e:
        print('fps error - %s' % (str(e)))
        raise e


def view_pmtct(request, id):
    """View page for New preventive and FS."""
    try:
        ovc_id = int(id)
        child = RegPerson.objects.get(is_void=False, id=ovc_id)
        creg = OVCPMTCTRegistration.objects.get(
            is_void=False, person_id=ovc_id)
        check_fields = ['relationship_type_id', 'pfs_intervention_id']
        vals = get_dict(field_name=check_fields)
        return render(request, 'pfs/pmtct/view_registration.html',
                      {'creg': creg, 'child': child, 'vals': vals})
    except Exception as e:
        print('error - %s' % e)
        msg = "Child not registered in any Program"
        messages.error(request, msg)
        url = reverse('new_pfs', kwargs={'id': id})
        return HttpResponseRedirect(url)
    else:
        pass

