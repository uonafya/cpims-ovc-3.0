import uuid
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.utils import timezone

from cpovc_ovc.forms import OVCSearchForm
from cpovc_forms.functions import get_person_ids
from cpovc_forms.models import OVCCaseRecord
from cpovc_registry.models import (
    RegPerson, RegPersonsGuardians, RegPersonsSiblings,
    RegPersonsExternalIds)
from cpovc_main.functions import convert_date, get_dict
from cpovc_ovc.functions import (
    get_school, get_health, limit_person_ids_orgs)
from cpovc_pfs.functions import save_school

from .forms import (
    OVCPMTCTRegistrationForm, OVCHEITrackerForm, PREGNANT_WOMEN_ADOLESCENT)
from .models import (
    OVCPMTCTRegistration, PMTCTPregnantWA, PMTCTEvents, PMTCTQuestions,
    PMTCTHEI, OVCHEITracker)
from cpovc_pfs.functions import get_person_org_unit, save_health

from cpovc_ovc.models import OVCHouseHold, OVCFacility


# PMTCT Pages
@login_required
def pmtct_home(request):
    """Some default page for the home page for preventive and FS."""
    try:
        form = OVCSearchForm(data=request.GET)
        afc_ids, case_ids = {}, {}
        search_string = request.GET.get('search_name')
        pids = get_person_ids(request, search_string)
        # Limit this search to my org units
        pids = limit_person_ids_orgs(request, pids)
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
        return render(request, 'pmtct/home.html',
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
        return render(request, 'pmtct/new_registration.html',
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
        return render(request, 'pmtct/new_registration.html',
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
        return render(request, 'pmtct/view_registration.html',
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


def new_pregnantwomen(request, id):

    person = RegPerson.objects.get(pk=int(id))
    if request.method == 'POST':
        data = request.POST
        user_id = request.user.id
        event_type_id = 'WBGA'
        date_of_event = timezone.now()

        """ Save Wellbeing-event """

        # get event counter
        event_counter = PMTCTEvents.objects.filter(
            event_type_id=event_type_id, person=id, is_void=False).count()
        # save event
        # try:
        pmtctevent = PMTCTEvents.objects.create(
            event_type_id=event_type_id,
            event_counter=event_counter,
            event_score=0,
            date_of_event=date_of_event,
            created_by=user_id,
            app_user_id=user_id,
            person=person,
            # house_hold=house_holds
        )

        # get questions for adolescent
        questions = PMTCTQuestions.objects.filter(
            code__startswith='PWA', is_void=False)
        child = OVCPMTCTRegistration .objects.get(person=person)
        care_giver_id = child.caregiver_id
        if care_giver_id:
            care_giver = RegPerson.objects.get(id=care_giver_id)
        else:
            care_giver = None

        for question in questions:
            question_code_q = question.code
            question_ansr_a = data.get(question.question)
            if question_ansr_a is None:
                question_ansr_a = 'No'
            try:
                PMTCTPregnantWA.objects.create(
                    person=RegPerson.objects.get(pk=int(id)),
                    caregiver=care_giver,
                    question=question,
                    question_code=question_code_q,
                    answer=question_ansr_a,
                    timestamp_created=date_of_event,
                    event=pmtctevent,
                )
            except Exception as e:
                error_message = f'PMTCT Pregnant table failed: {e}'
                print(error_message)

        msg = ' saved successful'
        messages.add_message(request, messages.INFO, msg)
        url = reverse('view_pmtct', kwargs={'id': id})
        return HttpResponseRedirect(url)

    # Get request Method
    try:
        ovcreg = get_object_or_404(
            OVCPMTCTRegistration, person_id=id, is_void=False)
        caretaker_id = ovcreg.caregiver_id if ovcreg else None
        ovchh = get_object_or_404(
            OVCHouseHold, head_person=caretaker_id, is_void=False)
        household_id = ovchh.id if ovchh else None
    except Exception as e:
        print(str(e))
        # msg = 'Error getting household identifier: (%s)' % (str(e))
        # messages.add_message(request, messages.ERROR, msg)
        # return HttpResponseRedirect(reverse('forms_registry'))
        household_id = None
    # Get child data
    init_data = RegPerson.objects.filter(pk=id)
    check_fields = ['sex_id', 'relationship_type_id']
    vals = get_dict(field_name=check_fields)
    # ovc_id = int(id)

    event = PMTCTEvents.objects.filter(person_id=id).values_list('event')
    data_test = PMTCTPregnantWA.objects.filter(
        event_id__in=event, is_void=False).values('event_id').distinct()
    data_get = []
    data_dict = []
    for b in range(len(data_test)):
        data_get.append([])
        for n in range(len(data_test)):
            data_array = PMTCTPregnantWA.objects.filter(
                event_id__in=event, is_void=False,
                event_id=data_test[b]['event_id'])
            for one_pwa in data_array:
                data_get[b].append((one_pwa.question_code, one_pwa.answer))
        data_dict.append(dict(data_get[b]))

    form = PREGNANT_WOMEN_ADOLESCENT()
    context = {'form': form,
               'init_data': init_data,
               'vals': vals,
               'person': person,
               'data_get': data_get,
               'data_get': data_dict,
               # 'event_id':event
               }
    return render(request, 'pmtct/new_pregnant_women.html', context)


def edit_pregnantwomen(request, id):
    if request.method == 'POST':
        data = request.POST

        update_time = timezone.now()
        # ovc_event = PMTCTEvents.objects.filter(event=id)
        pmtct_saved = PMTCTPregnantWA.objects.filter(event=id)
        # Update pmtct Table
        try:
            for question in pmtct_saved:
                answer = data.get(question.question_code)
                if answer is None:
                    answer = 'No'
                elif answer == 'AYES':
                    answer = True
                elif answer == 'ANNO':
                    answer = False
                else:
                    answer = 'No'
                PMTCTPregnantWA.objects.filter(event_id=id).update(
                    question=question,
                    answer=answer,
                    timestamp_updated=update_time,
                    event=id
                )
                form = PREGNANT_WOMEN_ADOLESCENT()
                return render(request, 'pmtct/edit_pregnantwomen.html',
                              {
                                  'form': form,
                                  # 'init_data': init_data,
                                  # 'vals': vals,
                                  # 'resultsets': resultsets,
                                  # 'resultsets2': resultsets2
                              })
        except Exception as e:
            print(f'The table pmtct didnt update: {e} ')


def delete_pregnantwomen(request, id, btn_event_pk):
    uid = uuid.UUID(id)
    new_tracker = PMTCTPregnantWA.objects.filter(event_id__in=uid)
    new_tracker1 = PMTCTPregnantWA.objects.filter(
        event_id=uuid.UUID(btn_event_pk))
    new_tracker.update(is_void=True)
    return redirect('new_pregnantwomen', id=new_tracker1.person_id)


def new_hei_tracker(request, id):
    hei8 = hei9 = hei10 = hei11 = hei12 = hei13 = hei14 = hei15 = hei16 = hei17 = hei18 = hei19 = hei20 = hei21 = hei22 = hei23 = hei24 = hei25 = hei26 = hei27 = hei28 = hei29 = hei30 = hei31 = hei32 = hei33 = hei34 = hei35 = hei36 = ''
    contact_date1 = contact_date2 = contact_date3 = contact_date4 = contact_date5 = '1900-01-01'
    try:
        if request.method == 'POST':
            comments = ['WB_AD_GEN_4_2']
            ignore_request_values = ['household_id', 'csrfmiddlewaretoken']

            # household_id = request.POST.get('household_id')
            # hse_uuid = uuid.UUID(household_id)
            # house_holds = OVCHouseHold.objects.get(pk=hse_uuid)
            person = RegPerson.objects.get(pk=int(id))
            event_type_id = 'WBGA'
            date_of_wellbeing_event = timezone.now()

            """ Save Wellbeing-event """
            # get event counter
            event_counter = PMTCTEvents.objects.filter(
                event_type_id=event_type_id, person=id, is_void=False).count()
            # save event
            user_id = request.user.id
            pmtctevent = PMTCTEvents(
                event_type_id=event_type_id,
                event_counter=event_counter,
                event_score=0,
                date_of_event=date_of_wellbeing_event,
                created_by=user_id,
                app_user_id=user_id,
                person=RegPerson.objects.get(pk=int(id)),
            )
            pmtctevent.save()
            # get questions for adolescent
            questions = PMTCTQuestions.objects.filter(code__startswith='HEI')
            ovc_id = int(id)
            child = RegPerson.objects.get(is_void=False, id=ovc_id)
            pmtct_reg = OVCPMTCTRegistration.objects.get(person=child)
            care_giver_id = pmtct_reg.caregiver_id
            for question in questions:
                answer = request.POST.get(question.question)
                if answer is None:
                    answer = ''
                PMTCTHEI(
                    person=RegPerson.objects.get(pk=int(id)),
                    question_code=question.code,
                    question=question,
                    answer=answer,
                    event=pmtctevent,
                    # date_of_event=timezone.now(),
                    question_id=question.question_id,
                    caregiver_id=care_giver_id
                ).save()

            msg = 'hei  saved successful'
            messages.add_message(request, messages.INFO, msg)
            url = reverse('view_pmtct', kwargs={'id': id})
            return HttpResponseRedirect(url)
    except Exception as e:
        msg = 'HEI tracker save error: (%s)' % (str(e))
        messages.add_message(request, messages.ERROR, msg)
        print('Error saving HEI tracker : %s' % str(e))
        url = reverse('view_pmtct', kwargs={'id': id})
        return HttpResponseRedirect(url)

    # get household members/ caretaker/ household_id
    household_id = None
    try:
        ovcreg = get_object_or_404(
            OVCPMTCTRegistration, person_id=id, is_void=False)
        caretaker_id = ovcreg.caregiver_id if ovcreg else None
        ovchh = get_object_or_404(
            OVCHouseHold, head_person=caretaker_id, is_void=False)
        household_id = ovchh.id if ovchh else None
    except Exception as e:
        print('New HEI error', str(e))
        msg = 'Error getting household identifier: (%s)' % (str(e))
        # messages.add_message(request, messages.ERROR, msg)
        # return HttpResponseRedirect(reverse('forms_registry'))

        # get relations
    person = RegPerson.objects.get(pk=int(id))
    guardians = RegPersonsGuardians.objects.select_related().filter(
        child_person=id, is_void=False, date_delinked=None)
    siblings = RegPersonsSiblings.objects.select_related().filter(
        child_person=id, is_void=False, date_delinked=None)
    # Reverse relationship
    osiblings = RegPersonsSiblings.objects.select_related().filter(
        sibling_person=id, is_void=False, date_delinked=None)
    oguardians = RegPersonsGuardians.objects.select_related().filter(
        guardian_person=id, is_void=False, date_delinked=None)

    # get child data
    init_data = RegPerson.objects.filter(pk=id)
    check_fields = ['sex_id', 'relationship_type_id', 'yesno_id']
    vals = get_dict(field_name=check_fields)
    event = PMTCTEvents.objects.filter(person_id=id).values_list('event')
    hei_tracker = PMTCTHEI.objects.filter(
        event_id__in=event, is_void=False).values('event_id').distinct()
    # hei = defaultdict(list)
    hei = []
    hei_dict = []
    for b in range(len(hei_tracker)):
        hei.append([])
        for n in range(len(hei_tracker)):
            hei_array = PMTCTHEI.objects.filter(
                event_id__in=event, is_void=False,
                event_id=hei_tracker[b]['event_id'])
            for one_hei in hei_array:
                hei[b].append((one_hei.question_code, one_hei.answer))
                # hei[0].append(one_hei.event_id)
        hei_dict.append(dict(hei[b]))

        # hei_tracker1 = PMTCTHEI.objects.filter(event_id__in=event, is_void=False)
        # data_get = []
        # for data in hei_tracker1:
        #     data_get.append(data)

        # for w in hei_tracker:
        #     hei = []
        #     hei_array = PMTCTHEI.objects.filter(event_id__in=event, is_void=False, event_id=w['event_id'])
        # for i in range(len(hei_tracker)):
        #         for one_hei in hei_array:
        #             hei.append((one_hei.event_id, one_hei.question_code, one_hei.answer))

    form = OVCHEITrackerForm(initial={'household_id': household_id})
    return render(request,
                  'pmtct/new_hei_tracker.html',
                  {
                      'form': form,
                      'init_data': init_data,
                      'vals': vals,
                      'person': person,
                      'guardians': guardians,
                      'siblings': siblings,
                      'osiblings': osiblings,
                      'oguardians': oguardians,
                      'heidata': hei_dict
                      # 'heidata': hei.items(),
                      # 'data_get': data_get
                  })


def edit_heitracker(request, id):
    """Some default page for Server Errors."""

    try:
        heidata = OVCHEITracker.objects.get(hei_id=id, is_void=False)
        if request.method == 'POST':
            hei2 = request.POST.get('PMTCT_HEI5q')
            hei3 = request.POST.get('PMTCT_HEI6q')
            hei4 = request.POST.get('PMTCT_HEI7q')
            if hei4:
                facility_res = OVCFacility.objects.get(id=hei4).facility_code
            else:
                facility_res = None
            hei5 = request.POST.get('PMTCT_HEI8q')
            hei6 = request.POST.get('PMTCT_HEI9q')
            hei7 = request.POST.get('PMTCT_HEI10q')

            # HEI follow up

            # 1st contact
            contact_date1 = request.POST.get('PMTCT_HEI42q')
            hei8 = request.POST.get('PMTCT_HEI13q')
            hei9 = request.POST.get('PMTCT_HEI14q')
            hei10 = request.POST.get('PMTCT_HEI15q')
            hei11 = request.POST.get('PMTCT_HEI16q')
            hei12 = request.POST.get('PMTCT_HEI17q')

            # 6 weeks
            contact_date2 = request.POST.get('PMTCT_HEI43q')
            hei13 = request.POST.get('PMTCT_HEI18q')
            hei14 = request.POST.get('PMTCT_HEI19q')
            hei15 = request.POST.get('PMTCT_HEI20q')
            hei16 = request.POST.get('PMTCT_HEI21q')
            hei17 = request.POST.get('PMTCT_HEI22q')
            hei18 = request.POST.get('PMTCT_HEI23q')

            # 6 months
            contact_date3 = request.POST.get('PMTCT_HEI44q')
            hei19 = request.POST.get('PMTCT_HEI24q')
            hei20 = request.POST.get('PMTCT_HEI25q')
            hei21 = request.POST.get('PMTCT_HEI26q')
            hei22 = request.POST.get('PMTCT_HEI27q')
            hei23 = request.POST.get('PMTCT_HEI28q')
            hei24 = request.POST.get('PMTCT_HEI29q')

            # 12 months
            contact_date4 = request.POST.get('PMTCT_HEI45q')
            hei25 = request.POST.get('PMTCT_HEI30q')
            hei26 = request.POST.get('PMTCT_HEI31q')
            hei27 = request.POST.get('PMTCT_HEI32q')
            hei28 = request.POST.get('PMTCT_HEI33q')
            hei29 = request.POST.get('PMTCT_HEI34q')
            hei30 = request.POST.get('PMTCT_HEI35q')

            # 18 months
            contact_date5 = request.POST.get('PMTCT_HEI46q')
            hei31 = request.POST.get('PMTCT_HEI36q')
            hei32 = request.POST.get('PMTCT_HEI37q')
            hei33 = request.POST.get('PMTCT_HEI38q')
            hei34 = request.POST.get('PMTCT_HEI39q')
            hei35 = request.POST.get('PMTCT_HEI40q')
            hei36 = request.POST.get('PMTCT_HEI41q')

            # Others
            hei37 = request.POST.get('PMTCT_HEI47q')
            hei38 = request.POST.get('PMTCT_HEI48q')

            # household_id = request.POST.get('household_id')
            # hse_uuid = uuid.UUID(household_id)
            # house_holds = OVCHouseHold.objects.get(pk=hse_uuid)

            # Save all details from the Bursary form
            qry = OVCHEITracker.objects.filter(hei_id=id).update(
                hivstatus=hei2,
                hivpositive=hei3,
                facility=facility_res,
                ccc=hei5,
                vl=hei6,
                vldate=hei7,
                f1date=contact_date1,
                f1hivtest=hei8,
                f1testresults=hei9,
                f1vlresults=hei10,
                f1prophylaxis=hei11,
                f1mode=hei12,
                f2date=contact_date2,
                f2hivtest=hei13,
                f2testresults=hei14,
                f2vlresults=hei15,
                f2prophylaxis=hei16,
                f2immunization=hei17,
                f2mode=hei18,
                f3date=contact_date3,
                f3hivtest=hei19,
                f3testresults=hei20,
                f3vlresults=hei21,
                f3prophylaxis=hei22,
                f3immunization=hei23,
                f3mode=hei24,
                f4date=contact_date4,
                f4hivtest=hei25,
                f4testresults=hei26,
                f4vlresults=hei27,
                f4prophylaxis=hei28,
                f4immunization=hei29,
                f4mode=hei30,
                f5date=contact_date5,
                f5hivtest=hei31,
                f5testresults=hei32,
                f5vlresults=hei33,
                f5prophylaxis=hei34,
                f5immunization=hei35,
                f5mode=hei36,
                reason=hei37,
                comments=hei38
            )

            return redirect('new_hei_tracker', id=heidata.person_id)
        if heidata.facility:
            facility_name = OVCFacility.objects.get(
                facility_code=heidata.facility).facility_name
        else:
            facility_name = ''
        # pdb.set_trace()
        hei = {
            'PMTCT_HEI5q': heidata.hivstatus,
            'PMTCT_HEI6q': heidata.hivpositive,
            'PMTCT_HEI7q': facility_name,
            'PMTCT_HEI8q': heidata.ccc,
            'PMTCT_HEI9q': heidata.vl,
            'PMTCT_HEI10q': heidata.vldate,

            'PMTCT_HEI42q': heidata.f1date,
            'PMTCT_HEI13q': heidata.f1hivtest,
            'PMTCT_HEI14q': heidata.f1testresults,
            'PMTCT_HEI15q': heidata.f1vlresults,
            'PMTCT_HEI16q': heidata.f1prophylaxis,
            'PMTCT_HEI17q': heidata.f1mode,

            'PMTCT_HEI43q': heidata.f2date,
            'PMTCT_HEI18q': heidata.f2hivtest,
            'PMTCT_HEI19q': heidata.f2testresults,
            'PMTCT_HEI20q': heidata.f2vlresults,
            'PMTCT_HEI21q': heidata.f2prophylaxis,
            'PMTCT_HEI22q': heidata.f2immunization,
            'PMTCT_HEI23q': heidata.f2mode,

            'PMTCT_HEI44q': heidata.f3date,
            'PMTCT_HEI24q': heidata.f3hivtest,
            'PMTCT_HEI25q': heidata.f3testresults,
            'PMTCT_HEI26q': heidata.f3vlresults,
            'PMTCT_HEI27q': heidata.f3prophylaxis,
            'PMTCT_HEI28q': heidata.f3immunization,
            'PMTCT_HEI29q': heidata.f3mode,

            'PMTCT_HEI45q': heidata.f4date,
            'PMTCT_HEI30q': heidata.f4hivtest,
            'PMTCT_HEI31q': heidata.f4testresults,
            'PMTCT_HEI32q': heidata.f4vlresults,
            'PMTCT_HEI33q': heidata.f4prophylaxis,
            'PMTCT_HEI34q': heidata.f4immunization,
            'PMTCT_HEI35q': heidata.f4mode,

            'PMTCT_HEI46q': heidata.f5date,
            'PMTCT_HEI36q': heidata.f5hivtest,
            'PMTCT_HEI37q': heidata.f5testresults,
            'PMTCT_HEI38q': heidata.f5vlresults,
            'PMTCT_HEI39q': heidata.f5prophylaxis,
            'PMTCT_HEI40q': heidata.f5immunization,
            'PMTCT_HEI41q': heidata.f5mode,

            'PMTCT_HEI47q': heidata.reason,
            'PMTCT_HEI48q': heidata.comments,
        }

        form = OVCHEITrackerForm(data=hei)
        return render(
            request, 'pmtct/edit_hei_tracker.html',
            {'form': form, 'status': 200})

    except Exception as e:
        print("error with HEI viewing - %s" % (str(e)))
        # raise e
        msg = "Error occured during HEI tracker edit"
        messages.error(request, msg)
        url = reverse('ovc_view', kwargs={'id': id})
        return HttpResponseRedirect(reverse(url))


def delete_heitracker(request, id):
    new_eval = PMTCTHEI.objects.get(hei_id=id)
    PMTCTHEI.objects.filter(event_id=id).update(is_void=True)
    return redirect('new_hei_tracker', id=new_eval.person_id)
