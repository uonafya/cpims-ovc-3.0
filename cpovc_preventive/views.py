import json
import uuid
from datetime import datetime
from django.utils import timezone
from django.db.models import Count

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib import messages

from cpovc_forms.forms import OVCSearchForm
from cpovc_forms.functions import get_person_ids, get_ovc_program
from cpovc_forms.models import OVCCaseRecord
from cpovc_registry.models import (
    RegPerson, RegPersonsGeo, RegPersonsGuardians, RegPersonsSiblings,
    RegPersonsExternalIds, RegPersonsOrgUnits)

from cpovc_main.functions import (
    convert_date, get_dict, translate, get_days_difference,
    get_list, convert_date)
from cpovc_ovc.functions import get_school, limit_person_ids_orgs
from cpovc_ovc.models import OVCHHMembers, OVCHouseHold, OVCRegistration
from cpovc_preventive.functions import (
    save_school, save_household, get_house_hold, save_ebi, save_event)
from .forms import OVCPreventiveRegistrationForm
from .models import (
    OVCPreventiveRegistration, OVCPreventiveEvents,
    OVCPreventiveEbi, OVCPreventiveService, OVCPreventiveEvaluation)

from .forms import (
    PREVENTIVE_ATTENDANCE_REGISTER_FORM, OVCSinovuyoCaregiverAssessmentForm,
    OVCSinovuyoTeenAssessmentForm, OVCHCBFAssessmentForm, OVCFMPAssessmentForm,
    OVCCBIMAssessmentForm)
from .settings import PROGS

from .functions import save_evaluation, save_ebi_service


@login_required
def pfs_home(request):
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
        afcs = OVCPreventiveRegistration.objects.filter(
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
        return render(request, 'preventive/home.html',
                      {'status': 200, 'cases': cases, 'form': form})
    except Exception as e:
        print('fps error - %s' % (str(e)))
        raise e


@login_required
def new_pfs(request, id):
    """New page for New preventive and FS."""
    try:
        params, gparams = {}, {}
        initial = {}
        person_id = int(id)
        child = RegPerson.objects.get(is_void=False, id=person_id)
        fname = child.first_name
        guardians = RegPersonsGuardians.objects.filter(
            is_void=False, child_person_id=child.id)
        # Check in Comprehensive
        try:
            comp = OVCRegistration.objects.get(
                is_void=False, person_id=person_id)
        except Exception:
            comp = None
        if comp:
            msg = "%s - Proceed to Preventive Program" % (fname)
            msg += " (Comprehensive Active)"
            messages.error(request, msg)
            # url = reverse('pfs_home')
            # return HttpResponseRedirect(url)
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
        # Get CBOs from program initiation table
        ovc = get_ovc_program(request, person_id, 'PPRE')
        if request.method == 'POST':
            form = OVCPreventiveRegistrationForm(guids=pids, data=request.POST)
            user_id = request.user.id
            intervention = request.POST.get('intervention')
            cbo_id = request.POST.get('cbo_id')
            school_level = request.POST.get('school_level')
            school_id = request.POST.get('school_id')
            if school_level == 'SLNS' or school_level == '':
                school_id = None
            else:
                save_school(request, person_id, school_level)
            registration_date = request.POST.get('registration_date')
            reg_date = convert_date(registration_date)
            # Pick the First one >> Users will pick later
            if guardians:
                caregiver_id = guardians.first().guardian_person_id
            else:
                caregiver_id = None
            obj, created = OVCPreventiveRegistration.objects.update_or_create(
                person_id=person_id, is_void=False,
                defaults={'intervention': intervention, 'child_cbo_id': cbo_id,
                          'school_id': school_id, 'created_by_id': user_id,
                          'caregiver_id': caregiver_id,
                          'registration_date': reg_date},
            )
            action = "Created" if created else "edited"
            msg = "OVC (Preventive) registration %s Successfully" % action
            messages.info(request, msg)
            url = reverse('view_pfs', kwargs={'id': id})
            return HttpResponseRedirect(url)
        # Not a POST
        cbo_id = ovc.child_cbo_id if ovc else 1
        initial['cbo_id'] = cbo_id
        if 'ISOV' in params:
            initial['bcert_no'] = params['ISOV']
            initial['has_bcert'] = 'on'
        form = OVCPreventiveRegistrationForm(
            guids=pids, initial=initial)
        # Class levels
        check_fields = ['relationship_type_id']
        vals = get_dict(field_name=check_fields)
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
        return render(request, 'preventive/new_registration.html',
                      {'form': form, 'child': child, 'levels': levels,
                       'ovc': ovc, 'guardians': guardians, 'edits': 0,
                       'siblings': siblings, 'extids': extids,
                       'vals': vals, 'extids': gparams})
    except Exception as e:
        print('fps error - %s' % (str(e)))
        raise e


@login_required
def edit_pfs(request, id):
    """New page for New preventive and FS."""
    try:
        params, gparams = {}, {}
        initial = {}
        person_id = int(id)
        child = RegPerson.objects.get(is_void=False, id=person_id)
        creg = OVCPreventiveRegistration.objects.get(
            is_void=False, person_id=person_id)
        guardians = RegPersonsGuardians.objects.filter(
            is_void=False, child_person_id=child.id)
        # Get siblings
        siblings = RegPersonsSiblings.objects.filter(
            is_void=False, child_person_id=child.id)
        guids, chids = [], []
        for guardian in guardians:
            guids.append(guardian.guardian_person_id)
        guids.append(child.id)
        for sibling in siblings:
            chids.append(sibling.sibling_person_id)
        pids = {'guids': guids, 'chids': chids}
        # Existing
        extids = RegPersonsExternalIds.objects.filter(
            person_id__in=guids)
        for extid in extids:
            if extid.person_id == child.id:
                params[extid.identifier_type_id] = extid.identifier
            else:
                gkey = '%s_%s' % (extid.person_id, extid.identifier_type_id)
                gparams[gkey] = extid.identifier
        # Org units
        orgs = RegPersonsOrgUnits.objects.filter(
            person_id=person_id, is_void=False)
        if request.method == 'POST':
            print(request.POST)
            form = OVCPreventiveRegistrationForm(guids=pids, data=request.POST)
            user_id = request.user.id
            intervention = request.POST.get('ebi')
            edit_type = int(request.POST.get('edits', 0))
            cbo_id = int(request.POST.get('cbo_id'))
            if edit_type == 1 and cbo_id == 1:
                cbo_id = request.POST.get('cbo')
            school_level = request.POST.get('school_level')
            school_id = request.POST.get('school_id')
            if school_level == 'SLNS':
                school_id = None
            else:
                save_school(request, person_id, school_level)
            registration_date = request.POST.get('registration_date')
            reg_date = convert_date(registration_date)
            obj, created = OVCPreventiveRegistration.objects.update_or_create(
                person_id=person_id, is_void=False,
                defaults={'intervention': intervention, 'child_cbo_id': cbo_id,
                          'school_id': school_id, 'created_by_id': user_id,
                          'registration_date': reg_date},
            )
            # Handle households
            cg_id = obj.caregiver_id
            if cg_id:
                save_household(request, cg_id, person_id)
            action = "Created" if created else "edited"
            msg = "OVC (Preventive) registration %s Successfully" % action
            messages.info(request, msg)
            url = reverse('view_pfs', kwargs={'id': id})
            return HttpResponseRedirect(url)
        # Default Get method
        ovc = OVCPreventiveRegistration.objects.get(
            is_void=False, person_id=person_id)
        cbo_id = ovc.child_cbo_id
        reg_date = ovc.registration_date.strftime('%d-%b-%Y')
        initial['registration_date'] = reg_date
        # Get School information
        school_level = 'Not Provided'
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
        initial['intervention'] = ovc.intervention
        initial['cbo_id'] = cbo_id
        form = OVCPreventiveRegistrationForm(
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
        check_fields = ['relationship_type_id']
        vals = get_dict(field_name=check_fields)
        return render(request, 'preventive/new_registration.html',
                      {'form': form, 'child': child, 'levels': levels,
                       'allow_edit': allow_edit, 'sch_class': sch_class,
                       'school': school, 'ovc': ovc, 'guardians': guardians,
                       'extids': gparams, 'vals': vals, 'edits': 1,
                       'orgs': orgs, 'creg': creg})
    except Exception as e:
        print('fps error - %s' % (str(e)))
        raise e


@login_required
def view_pfs(request, id):
    """View page for New preventive and FS."""
    try:
        ovc_id = int(id)
        child = RegPerson.objects.get(is_void=False, id=ovc_id)
        creg = OVCPreventiveRegistration.objects.get(
            is_void=False, person_id=ovc_id)
        check_fields = ['school_level_id', 'pfs_intervention_id',
                        'class_level_id', 'school_type_id',
                        'art_status_id', 'hiv_status_id',
                        'relationship_type_id']
        vals = get_dict(field_name=check_fields)
        school_level = 'SLNS'
        school = get_school(ovc_id)
        # Get Summaries for the view page
        summs = OVCPreventiveEvents.objects.filter(
            person_id=ovc_id, is_void=False).values(
            'event_type_id').annotate(dcount=Count('event_type_id'))
        ssumms = OVCPreventiveService.objects.filter(
            person_id=ovc_id, is_void=False).values(
            'ebi_service_client').annotate(
            dcount=Count('ebi_service_client'))
        # print(ssumms)
        summary = {'EBI': 0, 'SINO_CG': 0, 'SINO_TN': 0,
                   'FMP_CG': 0, 'HCBF_TN': 0, 'CBIM_TN': 0}
        for smm in summs:
            summary[smm['event_type_id']] = smm['dcount']
            if smm['event_type_id'].startswith('SINO_CG'):
                summary['SINO_CG'] = summary['SINO_CG'] + smm['dcount']
            if smm['event_type_id'].startswith('SINO_TN'):
                summary['SINO_TN'] = summary['SINO_TN'] + smm['dcount']
            if smm['event_type_id'].startswith('FMP_CG'):
                summary['FMP_CG'] = summary['FMP_CG'] + smm['dcount']
            if smm['event_type_id'].startswith('HCBF_TN'):
                summary['HCBF_TN'] = summary['HCBF_TN'] + smm['dcount']
            if smm['event_type_id'].startswith('CBIM_TN'):
                summary['CBIM_TN'] = summary['CBIM_TN'] + smm['dcount']
        for ssmm in ssumms:
            summary[ssmm['ebi_service_client']] = ssmm['dcount']
        if school:
            school_level = school.school_level
        # Just use the caregiver details directly
        guardians = RegPersonsGuardians.objects.filter(
            is_void=False, child_person_id=child.id)
        # Get external ids
        guids = []
        params, gparams = {}, {}
        for guardian in guardians:
            guids.append(guardian.guardian_person_id)
        guids.append(child.id)
        extids = RegPersonsExternalIds.objects.filter(
            person_id__in=guids)
        for extid in extids:
            if extid.person_id == child.id:
                params[extid.identifier_type_id] = extid.identifier
            else:
                gkey = '%s_%s' % (extid.person_id, extid.identifier_type_id)
                gparams[gkey] = extid.identifier
        return render(request, 'preventive/view_registration.html',
                      {'creg': creg, 'child': child, 'vals': vals,
                       'school': school, 'school_level': school_level,
                       'summary': summary, 'guardians': guardians,
                       'extids': gparams})
    except Exception as e:
        print('error - %s' % e)
        msg = "Child not registered in any Program"
        messages.error(request, msg)
        url = reverse('new_pfs', kwargs={'id': id})
        return HttpResponseRedirect(url)
    else:
        pass


def preventive_attendance_register(request, id):
    if request.method == 'POST':
        pass
    else:
        form = PREVENTIVE_ATTENDANCE_REGISTER_FORM(initial={'person': id})
        check_fields = ['sex_id']
        vals = get_dict(field_name=check_fields)
        init_data = RegPerson.objects.filter(pk=id)
        return render(request,
                      'preventive/new_preventive_attendance_register.html',
                      {'form': form, 'init_data': init_data,
                       'vals': vals, 'id': id})


def save_preventive_register(request):
    jsonResponse = []
    try:
        if request.method == 'POST':

            args = int(request.POST.get('args'))
            person = request.POST.get('person')
            int_person_id = int(person)

            registration_details = OVCPreventiveRegistration.objects.get(
                person_id=int(person))

            child = RegPerson.objects.get(id=person)
            # username = request.user.get_username()
            user_id = request.user.id

            hh = get_house_hold(request, int_person_id)
            hh_id = hh.id if hh else None

            print(request.POST)

            sess_date = request.POST.get('session_date_id')
            date_of_assessment = convert_date(sess_date) if sess_date else None
            date_today = datetime.now()

            if args == 1:
                event_type_id = 'EBI'
                event_counter = OVCPreventiveEvents.objects.filter(
                    event_type_id=event_type_id, person=person,
                    is_void=False).count()

                # preventive_assessment_provided_list
                olmis_assessment_provided_list = request.POST.get(
                    'olmis_assessment_provided_list')
                # pdb.set_trace()
                preventive_grouping_id = 'GROUP ID'
                if olmis_assessment_provided_list:
                    olmis_assessment_data = json.loads(
                        olmis_assessment_provided_list)
                    ovcpreventiveevent = OVCPreventiveEvents(
                        event_type_id=event_type_id,
                        event_counter=event_counter,
                        event_score=0,
                        date_of_event=date_today,
                        created_by=user_id,
                        app_user_id=user_id,
                        person_id=int_person_id,
                        house_hold_id=hh_id
                    )
                    ovcpreventiveevent.save()

                    for assessment_data in olmis_assessment_data:
                        olmis_intervention_prevention = assessment_data['olmis_intervention_prevention']
                        completed_all_session = assessment_data['holmis_completed_all_sessions']
                        session_attended = assessment_data['olmis_session_attended_days']
                        session_date = assessment_data['olmis_session_date']

                        if session_date:

                            ebi_session_type = ''

                            date_of_encounter_event = ''
                            # pdb.set_trace()
                            if 'SESS' in session_attended:
                                ebi_session_type = 'GENERAL'  # 'General'
                                date_of_encounter_event = session_date
                            else:
                                ebi_session_type = 'MAKE UP'  # "make up"
                                date_of_encounter_event = session_date
                            print('EBI', ebi_session_type,
                                  date_of_encounter_event)
                            try:
                                prov_cbo = registration_details.child_cbo
                                ebi_place = RegPersonsGeo.objects.filter(
                                    person_id=int_person_id, is_void=False).first()
                                OVCPreventiveEbi(
                                    person_id=int_person_id,
                                    domain=olmis_intervention_prevention,
                                    ebi_provided="",
                                    ebi_provider=prov_cbo,
                                    ebi_session=session_attended,
                                    ebi_session_type=ebi_session_type,
                                    place_of_ebi=ebi_place,
                                    date_of_encounter_event=convert_date(
                                        date_of_encounter_event),
                                    event=ovcpreventiveevent,
                                ).save()

                            except Exception as e:
                                print(e)

            if args == 2:
                # service_domain = 'XYZ'
                event_type_id = 'SERVICE'
                event_counter = OVCPreventiveEvents.objects.filter(
                    event_type_id=event_type_id, person=person,
                    is_void=False).count()

                olmis_assessment_provided_list = request.POST.get(
                    'olmis_assessment_provided_list')

                ovcpreventiveevent = OVCPreventiveEvents(
                    event_type_id=event_type_id,
                    event_counter=event_counter,
                    event_score=0,
                    date_of_event=date_today,
                    created_by=user_id,
                    app_user_id=user_id,
                    person_id=int_person_id,
                    house_hold_id=hh_id
                )
                ovcpreventiveevent.save()

                service_provided_list = request.POST.get(
                    'olmis_assessment_provided_list')
                if service_provided_list:
                    service_provided_list = json.loads(service_provided_list)
                    # pdb.set_trace()
                    for service in service_provided_list:
                        boolean_service_offered = service.get(
                            "olmis_reffered_for_service")
                        service_offered = service.get("olmis_reffered_service")
                        service_made = service.get("olmis_service_made")
                        date_of_encounter = service.get(
                            "olmis_date_of_encounter")
                        ebi_place = RegPersonsGeo.objects.filter(
                            person_id=int_person_id, is_void=False).first()
                        OVCPreventiveService(
                            person_id=int_person_id,
                            domain='SERVICE',
                            ebi_service_provided="serv",
                            ebi_provider=registration_details.child_cbo,
                            ebi_service_client=service.get('olmis_client'),
                            ebi_service_reffered=service_offered,
                            ebi_service_completed=service_made,
                            place_of_ebi_service=ebi_place,
                            date_of_encounter_event=convert_date(
                                date_of_encounter),
                            event=ovcpreventiveevent
                        ).save()
            msg = 'Updated Successful'
            jsonResponse.append({'msg': msg})
    except Exception as e:
        msg = 'Save Error: (%s)' % (str(e))
    jsonResponse.append({'msg': msg})
    return JsonResponse(
        jsonResponse, content_type='application/json', safe=False)


def manage_preventive_register(request):
    msg = ''
    preventiveEventsData = []

    try:

        person = request.POST.get('person')
        ovcpreventiveevents = OVCPreventiveEvents.objects.filter(
            person_id=person).order_by('-date_of_event')

        for event in ovcpreventiveevents:

            # Get Register and Services
            ovccaregister = OVCPreventiveEbi.objects.filter(event_id=event.pk)
            ovccareservice = OVCPreventiveService.objects.filter(
                event_id=event.pk)

            for ovccareg in ovccaregister:
                # pdb.set_trace()
                reg = translate(ovccareg.domain) + ',' + translate(ovccareg.ebi_session_type) + ',' + translate(
                    ovccareg.ebi_session) + ',' + translate(ovccareg.date_of_encounter_event.strftime('%d-%b-%Y'))
                # event_keywords.append(ovccareg.ebi_provided)
                encounter_date = ovccareg.date_of_encounter_event
                itm = {
                        'event_pk': str(event.pk),
                        'event_type': 'EBI',
                        'event_details': reg,
                        'event_keyword_group': ovccareg.ebi_provided,
                        'event_date': encounter_date.strftime('%d-%b-%Y')
                    }
                preventiveEventsData.append(itm)
            for ovcservice in ovccareservice:
                sref = translate(ovcservice.ebi_service_reffered) if ovcservice.ebi_service_reffered else None
                scom = translate(ovcservice.ebi_service_completed) if ovcservice.ebi_service_completed else None
                srefs = sref + '(R) ' if sref else ''
                scoms = scom + '(C) ' if scom else ''
                if scoms and srefs:
                    servs = srefs + ' / ' + scoms
                else:
                    servs = srefs + '' + scoms
                serv = servs + ',' + translate(
                    ovcservice.ebi_service_provided) + ',' + translate(
                    ovcservice.ebi_service_client)
                encounter_date = ovcservice.date_of_encounter_event
                itm = {
                        'event_pk': str(event.pk),
                        'event_type': 'SERVICE',
                        'event_details': serv,
                        'event_keyword_group': ovccareg.ebi_provided,
                        'event_date': encounter_date.strftime('%d-%b-%Y')
                     }
                preventiveEventsData.append(itm)

        return JsonResponse(preventiveEventsData,
                            content_type='application/json',
                            safe=False)
    except Exception as e:
        msg = 'An error occured : %s' % str(e)
        print(str(e))
        preventiveEventsData.append({'msg': msg})
    return JsonResponse(preventiveEventsData,
                        content_type='application/json',
                        safe=False)


def delete_preventive_event_entry(request, id, btn_event_pk, btn_event_type):
    jsonForm1AData = []
    try:
        entry_id = uuid.UUID(btn_event_pk)
        if btn_event_type == 'EBI':
            OVCPreventiveEbi.objects.filter(event_id=entry_id).delete()

        elif btn_event_type == 'SERVICE':
            OVCPreventiveService.objects.filter(event_id=entry_id).delete()
        msg = 'Deleted successfully'
    except Exception as e:
        msg = 'An error occured : %s' % str(e)
        print(str(e))
    jsonForm1AData.append({'msg': msg})
    return JsonResponse(jsonForm1AData,
                        content_type='application/json',
                        safe=False)


def edit_preventive_event_entry(request, id, btn_event_pk, btn_event_type):
    if request.method == 'GET':
        init_data = RegPerson.objects.filter(pk=id)
        check_fields = ['sex_id']
        vals = get_dict(field_name=check_fields)
        form = PREVENTIVE_ATTENDANCE_REGISTER_FORM(initial={'person': id})
        # OVCF1AForm(initial={'person': id})
        event_obj = OVCPreventiveEvents.objects.get(pk=btn_event_pk)
        event_id = uuid.UUID(btn_event_pk)

        d_event = OVCPreventiveEvents.objects.filter(pk=event_id)[
            0].timestamp_created
        delta = get_days_difference(d_event)
        print(delta)
        if delta < 90:
            if btn_event_type == 'EBI':
                ovc_care_assessments = OVCPreventiveEbi.objects.filter(
                    event=event_id)

                service_type_list = []
                olmis_assessment_domain_list = get_list(
                    'attendance_reg_domains', 'Please Select')
                date_of_event_edit = event_obj.date_of_event
                for ovc_care_assessment in ovc_care_assessments:
                    domain_entry = {}
                    assessment_entry = []

                    domain_full_name = ''
                    for domain in olmis_assessment_domain_list:
                        if domain[0] == ovc_care_assessment.domain:
                            domain_full_name = domain

                    assessment_entry.append(domain_full_name[0])
                    assessment_entry.append(
                        translate(ovc_care_assessment.ebi_session))
                    assessment_entry.append(
                        translate(ovc_care_assessment.date_of_encounter_event))
                    assessment_entry.append(translate(ovc_care_assessment.pk))
                    domain_entry[ovc_care_assessment.pk] = assessment_entry
                    service_type_list.append(domain_entry)

                    form = PREVENTIVE_ATTENDANCE_REGISTER_FORM(
                        initial={'person': id})
                    date_of_event_edit = str(date_of_event_edit)

                return render(request,
                              'preventive/edit_preventive_register.html',
                              {'form': form, 'init_data': init_data,
                               'vals': vals, 'event_pk': btn_event_pk,
                               'event_type': btn_event_type,
                               'service_type_list': service_type_list,
                               'date_of_event_edit': date_of_event_edit})

            elif btn_event_type == 'SERVICE':
                preventive_reg_services = OVCPreventiveService.objects.filter(
                    event=event_obj)
                service_type_list = []
                olmis_assessment_domain_list = get_list(
                    'attendance_reg_domains', 'Please Select')
                date_of_event_edit = event_obj.date_of_event
                for services in preventive_reg_services:

                    domain_entry = {}
                    service_entry = []

                    domain_full_name = ''

                    service_entry.append(services.ebi_service_client)
                    service_entry.append(services.ebi_service_reffered)
                    service_entry.append(services.date_of_encounter_event)
                    service_entry.append(services.event_id)
                    service_entry.append(services.pk)
                    service_entry.append(services.ebi_service_provided)

                    # date_of_encounter_event
                    # domain_entry[ovc_care_assessment.pk] = assessment_entry
                service_type_list.append(service_entry)

                form = PREVENTIVE_ATTENDANCE_REGISTER_FORM(
                    initial={'person': id})
                date_of_event_edit = str(date_of_event_edit)
                # pdb.set_trace()

                return render(request,
                              'preventive/edit_preventive_register.html',
                              {'form': form, 'init_data': init_data,
                               'vals': vals, 'event_pk': btn_event_pk,
                               'event_type': btn_event_type,
                               'service_type_list': service_type_list,
                               'date_of_event_edit': date_of_event_edit})

        else:
            err_msgg = "Can't alter after 90 days"
            return render(request,
                          'preventive/edit_preventive_register.html',
                          {'form': form, 'init_data': init_data,
                           'vals': vals, 'event_pk': btn_event_pk,
                           'event_type': btn_event_type,
                           'err_msgg': err_msgg})

    if request.method == 'POST':
        args_value = int(request.POST.get('args'))
        person = request.POST.get('person')
        primary_key = uuid.UUID(request.POST.get("btn_event_pk"))

        registration_details = OVCPreventiveRegistration.objects.get(
            person_id=int(person))

        child = RegPerson.objects.get(id=person)
        # username = request.user.get_username()
        user_id = request.user.id
        int_person_id = int(person)

        hh = get_house_hold(request, int_person_id)
        hh_id = hh.id if hh else None

        print(request.POST)

        sess_date = request.POST.get('session_date_id')
        date_of_assessment = convert_date(sess_date) if sess_date else None
        date_today = datetime.now()
        if args_value == 1:

            event_type_id = 'EBI'
            event_counter = OVCPreventiveEvents.objects.filter(
                event_type_id=event_type_id, person=person,
                is_void=False).count()
            # preventive_assessment_provided_list
            olmis_assessment_provided_list = request.POST.get(
                'olmis_assessment_provided_list')

            preventive_grouping_id = 'GROUP ID'
            if olmis_assessment_provided_list:
                olmis_assessment_data = json.loads(
                    olmis_assessment_provided_list)

                olmis_intervention_prevention = olmis_assessment_data.get(
                    "olmis_intervention_prevention")
                session_attended = olmis_assessment_data.get(
                    'olmis_session_attended_days')
                session_date = olmis_assessment_data.get('olmis_session_date')

                if session_date:
                    ebi_session_type = ''

                    date_of_encounter_event = ''
                    # pdb.set_trace()
                    if 'SESS' in session_attended:
                        ebi_session_type = 'GENERAL'  # 'General'
                        date_of_encounter_event = session_date
                    else:
                        ebi_session_type = 'MAKE UP'  # "make up"
                        date_of_encounter_event = session_date
                    try:
                        #
                        OVCPreventiveEbi.objects.filter(
                            event=primary_key).update(
                                domain=olmis_intervention_prevention,
                                ebi_provided="",
                                ebi_session=session_attended,
                                ebi_session_type=ebi_session_type,
                                date_of_encounter_event=convert_date(
                                    date_of_encounter_event),
                        )

                        msg = {'message': 'Save Successful'}
                        return JsonResponse(
                            msg, content_type='application/json', safe=False)

                    except Exception as e:
                        print(e)

        if args_value == 2:
            serveice_domain = 'HHNN'
            event_type_id = 'SERVICE'
            event_counter = OVCPreventiveEvents.objects.filter(
                event_type_id=event_type_id, person=person,
                is_void=False).count()

            olmis_assessment_provided_list = request.POST.get(
                'olmis_assessment_provided_list')

            ovcpreventiveevent = OVCPreventiveEvents(
                event_type_id=event_type_id,
                event_counter=event_counter,
                event_score=0,
                date_of_event=date_today,
                created_by=user_id,
                app_user_id=user_id,
                person_id=int_person_id,
                house_hold_id=hh_id
            )
            ovcpreventiveevent.save()

            service_provided_list = request.POST.get(
                'olmis_assessment_provided_list')
            # pdb.set_trace()
            if service_provided_list:
                service_provided_list = json.loads(service_provided_list)
                for service in service_provided_list:
                    service_offered = service.get("olmis_reffered_service")
                    service_made = service.get("olmis_service_made")
                    date_of_encounter = service.get("olmis_date_of_encounter")
                    ebi_place = RegPersonsGeo.objects.filter(
                        person_id=int_person_id, is_void=False).first()

                    OVCPreventiveService.objects.filter(
                        event=primary_key).update(
                            person_id=int_person_id,
                            domain=serveice_domain,
                            ebi_service_provided="serv",
                            ebi_provider=registration_details.child_cbo,
                            ebi_service_client=service.get('olmis_client'),
                            ebi_service_reffered=service_offered,
                            ebi_service_completed=service_made,
                            place_of_ebi_service=ebi_place,
                            date_of_encounter_event=convert_date(
                                date_of_encounter),
                            event=ovcpreventiveevent
                    )
        msg = [{'msg': 'Save Successful'}]
        return JsonResponse(msg, content_type='application/json', safe=False)


@login_required
def new_register_v2(request, id):
    """Some default page for the home page for preventive and FS."""
    try:
        person_id = int(id)
        child = RegPerson.objects.get(is_void=False, id=person_id)
        creg = OVCPreventiveRegistration.objects.get(
            is_void=False, person_id=person_id)
        form = OVCSearchForm(data=request.GET)
        domain = creg.intervention
        cbo_id = creg.child_cbo_id
        # Get settings
        sessions, make_ups = [], []
        prog = PROGS[domain] if domain in PROGS else PROGS['DEFAULT']
        total_sessions = prog['sessions'] + 1
        ebi_name = prog['name']
        ebi_domain = prog['code']
        if request.method == 'POST':
            print(request.POST)
            session_ids = request.POST.getlist("session_id_check")
            make_up_ids = request.POST.getlist("make_up_id_check")
            for session_id in session_ids:
                ev_id = 'event_id_sess%s' % (session_id)
                old_event_id = request.POST.get(ev_id)
                if old_event_id:
                    event_id = uuid.UUID(old_event_id)
                else:
                    event = save_event(request, 'EBI', person_id)
                    event_id = event.pk
                sess_date = request.POST.get('date_attended_%s' % (session_id))
                print('Index', session_id, sess_date, domain)
                if sess_date:
                    save_ebi(
                        request, person_id, cbo_id, event_id, 'GENERAL',
                        ebi_domain, session_id, sess_date)
            for session_id in make_up_ids:
                ev_id = 'event_id_mkps%s' % (session_id)
                old_event_id = request.POST.get(ev_id)
                if old_event_id:
                    event_id = uuid.UUID(old_event_id)
                else:
                    event = save_event(request, 'EBI', person_id)
                    event_id = event.pk
                sess_date = request.POST.get('date_attended_%s' % (session_id))
                if sess_date:
                    save_ebi(
                        request, person_id, cbo_id, event_id, 'MAKE UP',
                        ebi_domain, session_id, sess_date)
            msg = "Register updated Successfully"
            messages.info(request, msg)
            url = reverse('new_register', kwargs={'id': id})
            return HttpResponseRedirect(url)
        # Attendances
        atts, evs = {}, {}
        attendances = OVCPreventiveEbi.objects.filter(person_id=person_id)
        for attendance in attendances:
            sess_id = attendance.ebi_session
            doe = attendance.date_of_encounter_event
            event_date = doe.strftime('%d-%b-%Y') if doe else ''
            atts[sess_id] = event_date
            evs[sess_id] = attendance.event_id
        for i in range(1, total_sessions):
            sid = 'SESS%s' % i
            e_date = atts[sid] if sid in atts else ''
            ev_id = evs[sid] if sid in evs else ''
            sessions.append({'id': i, 'event_date': e_date, 'event_id': ev_id})
        for i in range(1, 5):
            sid = 'MKPS%s' % i
            e_date = atts[sid] if sid in atts else ''
            ev_id = evs[sid] if sid in evs else ''
            make_ups.append({'id': i, 'event_date': e_date, 'event_id': ev_id})
        # Settings
        check_fields = ['sex_id']
        vals = get_dict(field_name=check_fields)
        return render(request, 'preventive/new_register.html',
                      {'status': 200, 'creg': creg, 'form': form,
                       'ovc': child, 'sessions': sessions, 'vals': vals,
                       'make_ups': make_ups, 'ebi_name': ebi_name})
    except Exception as e:
        print('fps error - %s' % (str(e)))
        raise e


@login_required
def new_service_v2(request, id):
    """Some default page for the home page for preventive and FS."""
    try:
        person_id = int(id)
        child = RegPerson.objects.get(is_void=False, id=person_id)
        creg = OVCPreventiveRegistration.objects.get(
            is_void=False, person_id=person_id)
        form = OVCSearchForm(data=request.GET)
        domain = creg.intervention
        cbo_id = creg.child_cbo_id
        # Get settings
        sessions, make_ups = [], []
        prog = PROGS[domain] if domain in PROGS else PROGS['DEFAULT']
        total_sessions = prog['sessions'] + 1
        ebi_name = prog['name']
        client_type = 'CLOVC'
        if request.method == 'POST':
            print(request.POST)
            for ssid in request.POST:
                if ssid.startswith('SESS') or ssid.startswith('MKPS'):
                    sessions = request.POST.get(ssid)
                    if sessions == 'on':
                        spref = 'SESS' if ssid.startswith('SESS') else 'MKPS'
                        sid = ssid.replace(spref, '').split('_')[0]
                        ev_id = 'event_id_%s' % (sid)
                        ev_date = 'event_date_%s' % (sid)
                        session_number = '%s%s' % (spref, sid)
                        event_uid = request.POST.get(ev_id)
                        session_date = request.POST.get(ev_date)
                        service_date = convert_date(session_date)
                        ss_id, service_id, service_type = ssid.split('_')
                        event_id = uuid.UUID(event_uid)
                        service_detail = None
                        if service_id == 'SROTH':
                            service_detail = request.POST.get(
                                '%s%s_SROTH_T' % (spref, sid))
                        print('Index', ssid, service_date,
                              session_number, service_id, service_type,
                              event_id, client_type, service_detail)
                        # Save to DB
                        save_ebi_service(
                            request, person_id, cbo_id, event_id,
                            client_type, service_date, session_number,
                            service_id, service_type, service_detail)
                        # TO DO - How to handle unchecking
            msg = "%s Caregiver Services - Updated Successfully" % (ebi_name)
            messages.info(request, msg)
            url = reverse('view_pfs', kwargs={'id': id})
            return HttpResponseRedirect(url)
        # Attendances
        atts, evs, servs = {}, {}, {}
        attendances = OVCPreventiveEbi.objects.filter(
            person_id=person_id, is_void=False)
        services = OVCPreventiveService.objects.filter(
            person_id=person_id, is_void=False, ebi_service_client=client_type)
        # Organize attendances for presentation
        for attendance in attendances:
            sess_id = attendance.ebi_session
            doe = attendance.date_of_encounter_event
            event_date = doe.strftime('%d-%b-%Y') if doe else ''
            atts[sess_id] = event_date
            evs[sess_id] = attendance.event_id
        # Organize services for presentation
        for service in services:
            sls = {}
            sref = service.ebi_service_reffered
            scom = service.ebi_service_completed
            soth = service.ebi_service_other
            if sref:
                sls[sref + '_R'] = 'checked'
            if scom:
                sls[scom + '_C'] = 'checked'
            if soth:
                sls['SROTH_T'] = soth
            serv_prov = service.ebi_service_provided
            servs[serv_prov] = sls
        for i in range(1, total_sessions):
            sid = 'SESS%s' % i
            e_date = atts[sid] if sid in atts else ''
            ev_id = evs[sid] if sid in evs else ''
            serv = servs[sid] if sid in servs else {}
            sessions.append({'id': i, 'event_date': e_date,
                             'event_id': ev_id, 'services': serv})
        for i in range(1, 5):
            mid = 'MKPS%s' % i
            e_date = atts[mid] if mid in atts else ''
            ev_id = evs[mid] if mid in evs else ''
            make_ups.append({'id': i, 'event_date': e_date, 'event_id': ev_id})
        # Settings
        check_fields = ['sex_id']
        vals = get_dict(field_name=check_fields)
        return render(request, 'preventive/new_service.html',
                      {'status': 200, 'creg': creg, 'form': form,
                       'ovc': child, 'sessions': sessions, 'vals': vals,
                       'make_ups': make_ups, 'ebi_name': ebi_name})
    except Exception as e:
        print('fps error - %s' % (str(e)))
        raise e


@login_required
def new_service_caregiver_v2(request, id):
    """Some default page for the home page for preventive and FS."""
    try:
        person_id = int(id)
        child = RegPerson.objects.get(is_void=False, id=person_id)
        creg = OVCPreventiveRegistration.objects.get(
            is_void=False, person_id=person_id)
        form = OVCSearchForm(data=request.GET)
        domain = creg.intervention
        cbo_id = creg.child_cbo_id
        # Get settings
        sessions, make_ups = [], []
        prog = PROGS[domain] if domain in PROGS else PROGS['DEFAULT']
        total_sessions = prog['sessions'] + 1
        ebi_name = prog['name']
        client_type = 'CLCGV'
        if request.method == 'POST':
            print(request.POST)
            for ssid in request.POST:
                if ssid.startswith('SESS') or ssid.startswith('MKPS'):
                    sessions = request.POST.get(ssid)
                    if sessions == 'on':
                        spref = 'SESS' if ssid.startswith('SESS') else 'MKPS'
                        sid = ssid.replace(spref, '').split('_')[0]
                        ev_id = 'event_id_%s' % (sid)
                        ev_date = 'event_date_%s' % (sid)
                        session_number = '%s%s' % (spref, sid)
                        event_uid = request.POST.get(ev_id)
                        session_date = request.POST.get(ev_date)
                        service_date = convert_date(session_date)
                        ss_id, service_id, service_type = ssid.split('_')
                        event_id = uuid.UUID(event_uid)
                        service_detail = None
                        if service_id == 'SROTH':
                            service_detail = request.POST.get(
                                '%s%s_SROTH_T' % (spref, sid))
                        print('Index', ssid, service_date,
                              session_number, service_id, service_type,
                              event_id, client_type, service_detail)
                        # Save to DB
                        save_ebi_service(
                            request, person_id, cbo_id, event_id,
                            client_type, service_date, session_number,
                            service_id, service_type, service_detail)
                        # TO DO - How to handle unchecking
            msg = "%s Caregiver Services - Updated Successfully" % (ebi_name)
            messages.info(request, msg)
            url = reverse('view_pfs', kwargs={'id': id})
            return HttpResponseRedirect(url)
        # Attendances
        atts, evs, servs = {}, {}, {}
        attendances = OVCPreventiveEbi.objects.filter(
            person_id=person_id, is_void=False)
        services = OVCPreventiveService.objects.filter(
            person_id=person_id, is_void=False, ebi_service_client=client_type)
        # Organize attendances for presentation
        for attendance in attendances:
            sess_id = attendance.ebi_session
            doe = attendance.date_of_encounter_event
            event_date = doe.strftime('%d-%b-%Y') if doe else ''
            atts[sess_id] = event_date
            evs[sess_id] = attendance.event_id
        # Organize services for presentation
        for service in services:
            sls = {}
            sref = service.ebi_service_reffered
            scom = service.ebi_service_completed
            soth = service.ebi_service_other
            if sref:
                sls[sref + '_R'] = 'checked'
            if scom:
                sls[scom + '_C'] = 'checked'
            if soth:
                sls['SROTH_T'] = soth
            serv_prov = service.ebi_service_provided
            servs[serv_prov] = sls
        for i in range(1, total_sessions):
            sid = 'SESS%s' % i
            e_date = atts[sid] if sid in atts else ''
            ev_id = evs[sid]
            serv = servs[sid] if sid in servs else {}
            sessions.append({'id': i, 'event_date': e_date,
                             'event_id': ev_id, 'services': serv})
        for i in range(1, 5):
            mid = 'MKPS%s' % i
            e_date = atts[mid] if mid in atts else ''
            ev_id = evs[mid] if mid in evs else ''
            make_ups.append({'id': i, 'event_date': e_date, 'event_id': ev_id})
        # Settings
        check_fields = ['sex_id']
        vals = get_dict(field_name=check_fields)
        return render(request, 'preventive/new_service_caregiver.html',
                      {'status': 200, 'creg': creg, 'form': form,
                       'ovc': child, 'sessions': sessions, 'vals': vals,
                       'make_ups': make_ups, 'ebi_name': ebi_name})
    except Exception as e:
        print('fps error - %s' % (str(e)))
        raise e


@login_required
def new_sinovuyo_evaluation(request, id):
    """Method for New Sinovuyo Evaluation."""
    try:
        form = OVCSinovuyoCaregiverAssessmentForm()
        ovc_id = int(id)
        ovc = OVCPreventiveRegistration.objects.get(person_id=ovc_id)
        # household = OVCHHMembers.objects.filter(person_id=ovc_id).first()
        # house_hold_id = household.house_hold_id if household else None
        # house_hold = OVCHouseHold.objects.get(id=house_hold_id)
        print('CG', ovc.caregiver)
        caregiver_id = ovc.caregiver_id
        care_giver = {}
        if caregiver_id:
            care_giver = RegPerson.objects.get(id=caregiver_id)
        if request.method == 'POST':
            datasets = {}
            assessment_type = request.POST.get('type_of_assessment')
            date_of_assessment = request.POST.get('date_of_assessment')
            assessment_date = convert_date(date_of_assessment)
            print(request.POST)
            for pst in request.POST:
                if pst.startswith('SINO_CG'):
                    datasets[pst] = request.POST.get(pst)
            ass_type = 'A' if assessment_type == 'EPRE' else 'B'
            event_type_id = 'SINO_CG_%s' % (ass_type)
            # Save function
            save_evaluation(
                request, event_type_id, assessment_date, ovc_id,
                caregiver_id, datasets)
            # Save the form details here
            msg = 'SINOVUYO Caregiver Assessment saved successfully'
            messages.add_message(request, messages.SUCCESS, msg)
            url = reverse('view_pfs', kwargs={'id': ovc_id})
            return HttpResponseRedirect(url)
        else:
            check_fields = ['school_level_id', 'literacy_lvl_id', 'yesno_id',
                            'evaluation_type_id', 'employed_id',
                            'my_behaviour_id', 'dsp_times_id', 'often_id',
                            'relationship_caregiver_id', 'father_mortality_id',
                            'mother_mortality_id', 'under_care_id',
                            'agree_level_id', 'feeling_sad_id']
            vals = get_dict(field_name=check_fields)
            events = OVCPreventiveEvents.objects.filter(
                event_type_id__startswith='SINO_CG',
                person_id=ovc_id, is_void=False)
            for event in events:
                ev_id = event.pk
                qtns = OVCPreventiveEvaluation.objects.filter(event_id=ev_id)
                for ans in qtns:
                    qtn_code = ans.question_number
                    qtn_answer = ans.question_answer
                    setattr(event, qtn_code, qtn_answer)
        return render(
            request, 'preventive/sinovuyo/new_caregiver_evaluation.html',
            {'form': form, 'care_giver': care_giver, 'events': events,
             'vals': vals, 'ovc': ovc})
    except Exception as e:
        raise e
    else:
        pass


@login_required
def edit_sinovuyo_evaluation(request, event_id):
    """Method for New Sinovuyo Evaluation."""
    try:
        event = OVCPreventiveEvents.objects.get(pk=event_id)
        answers = OVCPreventiveEvaluation.objects.filter(event_id=event_id)
        ovc_id = event.person_id
        ovc = OVCPreventiveRegistration.objects.get(person_id=ovc_id)
        now = timezone.now()
        if request.method == 'POST':
            assessment_type = request.POST.get('type_of_assessment')
            date_of_assessment = request.POST.get('date_of_assessment')
            assessment_date = convert_date(date_of_assessment)
            datasets = {}
            # Update events table first
            ass_type = 'A' if assessment_type == 'EPRE' else 'B'
            event_type_id = 'SINO_CG_%s' % (ass_type)
            event.date_of_event = assessment_date
            event.event_type_id = event_type_id
            event.save(update_fields=['date_of_event', 'event_type_id'])
            for pst in request.POST:
                if pst.startswith('SINO_CG'):
                    datasets[pst] = request.POST.get(pst)
            for qstn in datasets:
                answer = datasets[qstn]
                prevev, ctd = OVCPreventiveEvaluation.objects.update_or_create(
                    person_id=ovc_id, event_id=event_id,
                    question_number=qstn,
                    defaults={'timestamp_updated': now,
                              'question_answer': answer,
                              'is_void': False})
            msg = 'SINOVUYO caregiver Assessment edited successfully'
            messages.add_message(request, messages.SUCCESS, msg)
            url = reverse('view_pfs', kwargs={'id': ovc_id})
            return HttpResponseRedirect(url)
        ass_type = 'EPRE' if event.event_type_id == 'SINO_CG_A' else 'EPOS'
        event_date = event.date_of_event.strftime('%d-%b-%Y')
        initial = {'type_of_assessment': ass_type}
        initial['date_of_assessment'] = event_date
        for ans in answers:
            qtn_code = ans.question_number
            qtn_answer = ans.question_answer
            if qtn_code.startswith('SINO_CG'):
                initial[qtn_code] = qtn_answer
        form = OVCSinovuyoCaregiverAssessmentForm(initial=initial)
        return render(
            request, 'preventive/sinovuyo/new_caregiver_evaluation.html',
            {'form': form, 'ovc': ovc})
    except Exception as e:
        raise e
    else:
        pass


@login_required
def delete_evaluation(request):
    """Method for New Sinovuyo Evaluation."""
    try:
        response = {'message': 'Record deleted successfully'}
        response['deleted'] = 1
        if request.method == 'POST':
            response['deleted'] = 1
            event_id = request.POST.get('event_id')
            events = OVCPreventiveEvents.objects.get(pk=event_id)
            answers = OVCPreventiveEvaluation.objects.filter(event_id=event_id)
            d_event = events.timestamp_created
            delta = get_days_difference(d_event)
            print('delta', delta)
            if delta > 90:
                response['deleted'] = 0
                response['message'] = "Can not delete record after 90 days"
            else:
                events.is_void = True
                events.save(update_fields=['is_void'])
                # Too many items just hard delete answers
                answers.delete()
        return JsonResponse(
            response, content_type='application/json', safe=False)
    except Exception as e:
        response = {'message': 'Error deleting record - %s' % (str(e))}
        response['deleted'] = 0
        return JsonResponse(
            response, content_type='application/json', safe=False)
    else:
        pass


@login_required
def new_sinovuyo_evaluation_teen(request, id):
    """Method for New Sinovuyo Evaluation for teens."""
    try:
        form = OVCSinovuyoTeenAssessmentForm()
        ovc_id = int(id)
        event_pref = 'SINO_TN'
        ovc = OVCPreventiveRegistration.objects.get(person_id=ovc_id)
        caregiver_id = ovc.caregiver_id
        care_giver = {}
        if caregiver_id:
            care_giver = RegPerson.objects.get(id=caregiver_id)
        if request.method == 'POST':
            datasets = {}
            assessment_type = request.POST.get('type_of_assessment')
            date_of_assessment = request.POST.get('date_of_assessment')
            assessment_date = convert_date(date_of_assessment)
            print(request.POST)
            for pst in request.POST:
                if pst.startswith(event_pref):
                    datasets[pst] = request.POST.get(pst)
            ass_type = 'A' if assessment_type == 'EPRE' else 'B'
            event_type_id = '%s_%s' % (event_pref, ass_type)
            # Save function
            save_evaluation(
                request, event_type_id, assessment_date, ovc_id,
                caregiver_id, datasets)
            # Save the form details here
            msg = 'SINOVUYO Teen Assessment saved successfully'
            messages.add_message(request, messages.SUCCESS, msg)
            url = reverse('view_pfs', kwargs={'id': ovc_id})
            return HttpResponseRedirect(url)
        else:
            check_fields = ['school_level_id', 'literacy_lvl_id', 'yesno_id',
                            'evaluation_type_id', 'employed_id',
                            'my_behaviour_id', 'dsp_times_id', 'often_id',
                            'relationship_caregiver_id', 'father_mortality_id',
                            'mother_mortality_id', 'under_care_id',
                            'agree_level_id', 'feeling_sad_id']
            vals = get_dict(field_name=check_fields)
            events = OVCPreventiveEvents.objects.filter(
                event_type_id__startswith=event_pref,
                person_id=ovc_id, is_void=False)
            for event in events:
                ev_id = event.pk
                qtns = OVCPreventiveEvaluation.objects.filter(event_id=ev_id)
                for ans in qtns:
                    qtn_code = ans.question_number
                    qtn_answer = ans.question_answer
                    setattr(event, qtn_code, qtn_answer)
        return render(
            request, 'preventive/sinovuyo/new_teen_evaluation.html',
            {'form': form, 'care_giver': care_giver, 'events': events,
             'vals': vals, 'ovc': ovc})
    except Exception as e:
        raise e
    else:
        pass


@login_required
def edit_sinovuyo_evaluation_teen(request, event_id):
    """Method for New Sinovuyo Evaluation for teens."""
    try:
        event = OVCPreventiveEvents.objects.get(pk=event_id)
        answers = OVCPreventiveEvaluation.objects.filter(event_id=event_id)
        ovc_id = event.person_id
        ovc = OVCPreventiveRegistration.objects.get(person_id=ovc_id)
        event_pref = 'SINO_TN'
        now = timezone.now()
        if request.method == 'POST':
            assessment_type = request.POST.get('type_of_assessment')
            date_of_assessment = request.POST.get('date_of_assessment')
            assessment_date = convert_date(date_of_assessment)
            datasets = {}
            # Update events table first
            ass_type = 'A' if assessment_type == 'EPRE' else 'B'
            event_type_id = '%s_%s' % (event_pref, ass_type)
            event.date_of_event = assessment_date
            event.event_type_id = event_type_id
            event.save(update_fields=['date_of_event', 'event_type_id'])
            for pst in request.POST:
                if pst.startswith(event_pref):
                    datasets[pst] = request.POST.get(pst)
            for qstn in datasets:
                answer = datasets[qstn]
                prevev, ctd = OVCPreventiveEvaluation.objects.update_or_create(
                    person_id=ovc_id, event_id=event_id,
                    question_number=qstn,
                    defaults={'timestamp_updated': now,
                              'question_answer': answer,
                              'is_void': False})
            msg = 'SINOVUYO Teen Assessment edited successfully'
            messages.add_message(request, messages.SUCCESS, msg)
            url = reverse('view_pfs', kwargs={'id': ovc_id})
            return HttpResponseRedirect(url)
        ass_type = 'EPRE' if event.event_type_id == 'SINO_TN_A' else 'EPOS'
        event_date = event.date_of_event.strftime('%d-%b-%Y')
        initial = {'type_of_assessment': ass_type}
        initial['date_of_assessment'] = event_date
        for ans in answers:
            qtn_code = ans.question_number
            qtn_answer = ans.question_answer
            if qtn_code.startswith(event_pref):
                initial[qtn_code] = qtn_answer
        form = OVCSinovuyoTeenAssessmentForm(initial=initial)
        return render(
            request, 'preventive/sinovuyo/new_teen_evaluation.html',
            {'form': form, 'ovc': ovc})
    except Exception as e:
        raise e
    else:
        pass


@login_required
def new_hcbf_evaluation(request, id):
    """Method for New HCBF evaluation."""
    try:
        form = OVCHCBFAssessmentForm()
        ovc_id = int(id)
        event_pref = 'HCBF_TN'
        ovc = OVCPreventiveRegistration.objects.get(person_id=ovc_id)
        caregiver_id = ovc.caregiver_id
        care_giver = {}
        if caregiver_id:
            care_giver = RegPerson.objects.get(id=caregiver_id)
        if request.method == 'POST':
            datasets = {}
            assessment_type = request.POST.get('type_of_assessment')
            date_of_assessment = request.POST.get('date_of_assessment')
            assessment_date = convert_date(date_of_assessment)
            print(request.POST)
            for pst in request.POST:
                if pst.startswith(event_pref):
                    datasets[pst] = request.POST.get(pst)
            ass_type = 'A' if assessment_type == 'EPRE' else 'B'
            event_type_id = '%s_%s' % (event_pref, ass_type)
            # Save function
            save_evaluation(
                request, event_type_id, assessment_date, ovc_id,
                caregiver_id, datasets)
            # Save the form details here
            msg = 'HCBF Assessment saved successfully'
            messages.add_message(request, messages.SUCCESS, msg)
            url = reverse('view_pfs', kwargs={'id': ovc_id})
            return HttpResponseRedirect(url)
        else:
            check_fields = ['school_level_id', 'literacy_lvl_id', 'yesno_id',
                            'rate_times_id', 'count_times_id']
            vals = get_dict(field_name=check_fields)
            events = OVCPreventiveEvents.objects.filter(
                event_type_id__startswith=event_pref,
                person_id=ovc_id, is_void=False)
            for event in events:
                ev_id = event.pk
                qtns = OVCPreventiveEvaluation.objects.filter(event_id=ev_id)
                for ans in qtns:
                    qtn_code = ans.question_number
                    qtn_answer = ans.question_answer
                    setattr(event, qtn_code, qtn_answer)
        return render(
            request, 'preventive/hcbf/new_evaluation.html',
            {'form': form, 'care_giver': care_giver, 'events': events,
             'vals': vals, 'ovc': ovc})
    except Exception as e:
        raise e
    else:
        pass


@login_required
def edit_hcbf_evaluation(request, event_id):
    """Method for New Sinovuyo Evaluation for teens."""
    try:
        event = OVCPreventiveEvents.objects.get(pk=event_id)
        answers = OVCPreventiveEvaluation.objects.filter(event_id=event_id)
        ovc_id = event.person_id
        ovc = OVCPreventiveRegistration.objects.get(person_id=ovc_id)
        event_pref = 'HCBF_TN'
        now = timezone.now()
        if request.method == 'POST':
            assessment_type = request.POST.get('type_of_assessment')
            date_of_assessment = request.POST.get('date_of_assessment')
            assessment_date = convert_date(date_of_assessment)
            datasets = {}
            # Update events table first
            ass_type = 'A' if assessment_type == 'EPRE' else 'B'
            event_type_id = '%s_%s' % (event_pref, ass_type)
            event.date_of_event = assessment_date
            event.event_type_id = event_type_id
            event.save(update_fields=['date_of_event', 'event_type_id'])
            for pst in request.POST:
                if pst.startswith(event_pref):
                    datasets[pst] = request.POST.get(pst)
            for qstn in datasets:
                answer = datasets[qstn]
                prevev, ctd = OVCPreventiveEvaluation.objects.update_or_create(
                    person_id=ovc_id, event_id=event_id,
                    question_number=qstn,
                    defaults={'timestamp_updated': now,
                              'question_answer': answer,
                              'is_void': False})
            msg = 'HCBF Assessment edited successfully'
            messages.add_message(request, messages.SUCCESS, msg)
            url = reverse('view_pfs', kwargs={'id': ovc_id})
            return HttpResponseRedirect(url)
        ass_type = 'EPRE' if event.event_type_id == 'HCBF_TN_A' else 'EPOS'
        event_date = event.date_of_event.strftime('%d-%b-%Y')
        initial = {'type_of_assessment': ass_type}
        initial['date_of_assessment'] = event_date
        for ans in answers:
            qtn_code = ans.question_number
            qtn_answer = ans.question_answer
            if qtn_code.startswith(event_pref):
                initial[qtn_code] = qtn_answer
        form = OVCHCBFAssessmentForm(initial=initial)
        return render(
            request, 'preventive/hcbf/new_evaluation.html',
            {'form': form, 'ovc': ovc})
    except Exception as e:
        raise e
    else:
        pass


@login_required
def new_fmp_evaluation(request, id):
    """Method for New HCBF evaluation."""
    try:
        form = OVCFMPAssessmentForm()
        ovc_id = int(id)
        event_pref = 'FMP_CG'
        ovc = OVCPreventiveRegistration.objects.get(person_id=ovc_id)
        caregiver_id = ovc.caregiver_id
        care_giver = {}
        if caregiver_id:
            care_giver = RegPerson.objects.get(id=caregiver_id)
        if request.method == 'POST':
            datasets = {}
            assessment_type = request.POST.get('type_of_assessment')
            date_of_assessment = request.POST.get('date_of_assessment')
            assessment_date = convert_date(date_of_assessment)
            print(request.POST)
            for pst in request.POST:
                if pst.startswith(event_pref):
                    datasets[pst] = request.POST.get(pst)
            ass_type = 'A' if assessment_type == 'EPRE' else 'B'
            event_type_id = '%s_%s' % (event_pref, ass_type)
            # Save function
            save_evaluation(
                request, event_type_id, assessment_date, ovc_id,
                caregiver_id, datasets)
            # Save the form details here
            msg = 'FMP Assessment saved successfully'
            messages.add_message(request, messages.SUCCESS, msg)
            url = reverse('view_pfs', kwargs={'id': ovc_id})
            return HttpResponseRedirect(url)
        else:
            check_fields = ['school_level_id', 'rate_truth_id', 'yesno_id',
                            'rate_times_id', 'count_times_id',
                            'ctip_yesno_otdk']
            vals = get_dict(field_name=check_fields)
            events = OVCPreventiveEvents.objects.filter(
                event_type_id__startswith=event_pref,
                person_id=ovc_id, is_void=False)
            for event in events:
                ev_id = event.pk
                qtns = OVCPreventiveEvaluation.objects.filter(event_id=ev_id)
                for ans in qtns:
                    qtn_code = ans.question_number
                    qtn_answer = ans.question_answer
                    setattr(event, qtn_code, qtn_answer)
        return render(
            request, 'preventive/fmp/new_evaluation.html',
            {'form': form, 'care_giver': care_giver, 'events': events,
             'vals': vals, 'ovc': ovc})
    except Exception as e:
        raise e
    else:
        pass


@login_required
def edit_fmp_evaluation(request, event_id):
    """Method for edit FMP Evaluation for teens."""
    try:
        event = OVCPreventiveEvents.objects.get(pk=event_id)
        answers = OVCPreventiveEvaluation.objects.filter(event_id=event_id)
        ovc_id = event.person_id
        ovc = OVCPreventiveRegistration.objects.get(person_id=ovc_id)
        event_pref = 'FMP_CG'
        now = timezone.now()
        if request.method == 'POST':
            assessment_type = request.POST.get('type_of_assessment')
            date_of_assessment = request.POST.get('date_of_assessment')
            assessment_date = convert_date(date_of_assessment)
            datasets = {}
            # Update events table first
            ass_type = 'A' if assessment_type == 'EPRE' else 'B'
            event_type_id = '%s_%s' % (event_pref, ass_type)
            event.date_of_event = assessment_date
            event.event_type_id = event_type_id
            event.save(update_fields=['date_of_event', 'event_type_id'])
            for pst in request.POST:
                if pst.startswith(event_pref):
                    datasets[pst] = request.POST.get(pst)
            for qstn in datasets:
                answer = datasets[qstn]
                prevev, ctd = OVCPreventiveEvaluation.objects.update_or_create(
                    person_id=ovc_id, event_id=event_id,
                    question_number=qstn,
                    defaults={'timestamp_updated': now,
                              'question_answer': answer,
                              'is_void': False})
            msg = 'FMP Assessment edited successfully'
            messages.add_message(request, messages.SUCCESS, msg)
            url = reverse('view_pfs', kwargs={'id': ovc_id})
            return HttpResponseRedirect(url)
        ass_type = 'EPRE' if event.event_type_id == 'FMP_CG_A' else 'EPOS'
        event_date = event.date_of_event.strftime('%d-%b-%Y')
        initial = {'type_of_assessment': ass_type}
        initial['date_of_assessment'] = event_date
        for ans in answers:
            qtn_code = ans.question_number
            qtn_answer = ans.question_answer
            if qtn_code.startswith(event_pref):
                initial[qtn_code] = qtn_answer
        form = OVCFMPAssessmentForm(initial=initial)
        return render(
            request, 'preventive/fmp/new_evaluation.html',
            {'form': form, 'ovc': ovc})
    except Exception as e:
        raise e
    else:
        pass


@login_required
def new_cbim_evaluation(request, id):
    """Method for New HCBF evaluation."""
    try:
        form = OVCCBIMAssessmentForm()
        ovc_id = int(id)
        event_pref = 'CBIM_TN'
        ovc = OVCPreventiveRegistration.objects.get(person_id=ovc_id)
        caregiver_id = ovc.caregiver_id
        care_giver = {}
        if caregiver_id:
            care_giver = RegPerson.objects.get(id=caregiver_id)
        if request.method == 'POST':
            datasets = {}
            assessment_type = request.POST.get('type_of_assessment')
            date_of_assessment = request.POST.get('date_of_assessment')
            assessment_date = convert_date(date_of_assessment)
            print(request.POST)
            for pst in request.POST:
                if pst.startswith(event_pref):
                    datasets[pst] = request.POST.get(pst)
            ass_type = 'A' if assessment_type == 'EPRE' else 'B'
            event_type_id = '%s_%s' % (event_pref, ass_type)
            # Save function
            save_evaluation(
                request, event_type_id, assessment_date, ovc_id,
                caregiver_id, datasets)
            # Save the form details here
            msg = 'CBIM Assessment saved successfully'
            messages.add_message(request, messages.SUCCESS, msg)
            url = reverse('view_pfs', kwargs={'id': ovc_id})
            return HttpResponseRedirect(url)
        else:
            check_fields = ['school_level_id', 'agree_level_id', 'yesno_id',
                            'cbim_coaching_id', 'rate_abuse_id',
                            'age_rate_id', 'race_id', 'rate_likely_id']
            vals = get_dict(field_name=check_fields)
            events = OVCPreventiveEvents.objects.filter(
                event_type_id__startswith=event_pref,
                person_id=ovc_id, is_void=False)
            for event in events:
                ev_id = event.pk
                qtns = OVCPreventiveEvaluation.objects.filter(event_id=ev_id)
                for ans in qtns:
                    qtn_code = ans.question_number
                    qtn_answer = ans.question_answer
                    setattr(event, qtn_code, qtn_answer)
        return render(
            request, 'preventive/cbim/new_evaluation.html',
            {'form': form, 'care_giver': care_giver, 'events': events,
             'vals': vals, 'ovc': ovc})
    except Exception as e:
        raise e
    else:
        pass


@login_required
def edit_cbim_evaluation(request, event_id):
    """Method for edit FMP Evaluation for teens."""
    try:
        event = OVCPreventiveEvents.objects.get(pk=event_id)
        answers = OVCPreventiveEvaluation.objects.filter(event_id=event_id)
        ovc_id = event.person_id
        ovc = OVCPreventiveRegistration.objects.get(person_id=ovc_id)
        event_pref = 'CBIM_TN'
        now = timezone.now()
        if request.method == 'POST':
            assessment_type = request.POST.get('type_of_assessment')
            date_of_assessment = request.POST.get('date_of_assessment')
            assessment_date = convert_date(date_of_assessment)
            datasets = {}
            # Update events table first
            ass_type = 'A' if assessment_type == 'EPRE' else 'B'
            event_type_id = '%s_%s' % (event_pref, ass_type)
            event.date_of_event = assessment_date
            event.event_type_id = event_type_id
            event.save(update_fields=['date_of_event', 'event_type_id'])
            for pst in request.POST:
                if pst.startswith(event_pref):
                    datasets[pst] = request.POST.get(pst)
            for qstn in datasets:
                answer = datasets[qstn]
                prevev, ctd = OVCPreventiveEvaluation.objects.update_or_create(
                    person_id=ovc_id, event_id=event_id,
                    question_number=qstn,
                    defaults={'timestamp_updated': now,
                              'question_answer': answer,
                              'is_void': False})
            msg = 'CBIM Assessment edited successfully'
            messages.add_message(request, messages.SUCCESS, msg)
            url = reverse('view_pfs', kwargs={'id': ovc_id})
            return HttpResponseRedirect(url)
        ass_type = 'EPRE' if event.event_type_id == 'FMP_CG_A' else 'EPOS'
        event_date = event.date_of_event.strftime('%d-%b-%Y')
        initial = {'type_of_assessment': ass_type}
        initial['date_of_assessment'] = event_date
        for ans in answers:
            qtn_code = ans.question_number
            qtn_answer = ans.question_answer
            if qtn_code.startswith(event_pref):
                initial[qtn_code] = qtn_answer
        form = OVCCBIMAssessmentForm(initial=initial)
        return render(
            request, 'preventive/cbim/new_evaluation.html',
            {'form': form, 'ovc': ovc})
    except Exception as e:
        raise e
    else:
        pass
