from datetime import datetime, timedelta
from django.db import connection
from django.forms import NullBooleanField
from django.core.cache import cache
from cpovc_registry.functions import (
    get_client_ip, get_meta_data)

from cpovc_main.functions import get_general_list, convert_date
from cpovc_forms.models import (
    FormsAuditTrail, OVCCareCpara, OVCCareCasePlan,
    OVCCareEvents, OVCEducationFollowUp)
from cpovc_ovc.functions import get_house_hold
from cpovc_registry.models import RegOrgUnit

from .models import (
    OVCGokBursary, OVCCareEAV, OvcCaseInformation, OVCPlacement,
    OVCCaseLocation, OVCCareF1B, OVCProgramRegistration)
from cpovc_ovc.models import OVCFacility

from cpovc_main.models import ListAnswers


def save_audit_trail(request, params, audit_type):
    """Method to save audit trail depending on transaction."""
    try:
        user_id = request.user.id
        ip_address = get_client_ip(request)
        form_id = params['form_id']
        form_type_id = audit_type
        transaction_type_id = params['transaction_type_id']
        interface_id = params['interface_id']
        meta_data = get_meta_data(request)

        print('Audit Trail', params)

        FormsAuditTrail(
            transaction_type_id=transaction_type_id,
            interface_id=interface_id,
            # timestamp_modified=None,
            form_id=form_id,
            form_type_id=form_type_id,
            ip_address=ip_address,
            meta_data=meta_data,
            app_user_id=user_id).save()

    except Exception as e:
        print('Error saving audit - %s' % (str(e)))
        pass
    else:
        pass


def create_fields(field_name=[], default_txt=False):
    """Method to create fields from tools."""
    dict_val = {}
    try:
        my_list = get_general_list(field_names=field_name)
        all_list = my_list.values(
            'item_id', 'item_description_short', 'item_description',
            'item_sub_category')
        for value in all_list:
            # item_description_short = value['item_description_short']
            # item_id = value['item_id']
            item_id = value['item_id']
            item_cat = value['item_sub_category']
            item_details = value['item_description']
            items = {'id': item_id, 'name': item_details}
            if item_cat not in dict_val:
                dict_val[item_cat] = [items]
            else:
                dict_val[item_cat].append(items)
    except Exception as e:
        error = 'Error getting list - %s' % (str(e))
        print(error)
        return {}
    else:
        return dict_val


def create_form_fields(data):
    """Method to create fields."""
    try:
        # print(data)
        dms = {'HG': ['1a', '1s'], 'SC': ['2a', '2s'], 'PG': ['3a', '3s'],
               'PSG': ['4a', '4s'], 'EG': ['5a', '5s'], 'HE': ['6a', '6s']}
        domains = {'HG': {}, 'SC': {}, 'PG': {}, 'PSG': {}, 'EG': {}, 'HE': {}}
        for domain in domains:
            itds = dms[domain]
            for itm in itds:
                itd = itm[-1:]
                if itm in data:
                    domains[domain][itd] = data[itm]
                else:
                    domains[domain][itd] = []
    except Exception as e:
        print('error with domains - %s' % (str(e)))
        return {}
    else:
        return domains


def save_form1b(request, person_id, edit=0):
    """Method to save form 1B."""
    try:
        user_id = request.user.id
        domains = {'SC': 'DSHC', 'PS': 'DPSS', 'HG': 'DHNU',
                   'EG': 'DEDU', 'SA': 'DPRO', 'ST': 'DHES',
                   'HE': 'DHNU'}
        if edit:
            print('F1B edit')
        else:
            f1b_date = request.POST.get('olmis_service_date')
            caretaker_id = request.POST.get('caretaker_id')
            f1bs = request.POST.getlist('f1b[]')
            # print('save', f1b_date, f1bs)
            hh = get_house_hold(caretaker_id)
            hhid = hh.id if hh else None
            event_date = convert_date(f1b_date)
            event_type_id = 'FM1B'
            newev = OVCCareEvents(
                event_type_id=event_type_id, created_by=user_id,
                person_id=caretaker_id, house_hold_id=hhid,
                date_of_event=event_date)
            newev.save()
            event_id = newev.pk
            # Attach services
            for f1bitm in f1bs:
                f1b = str(f1bitm)
                # Domain ids change - prefix 2 to suffix 3rd and 4th last
                did = f1b[-4:][:2] if f1b.startswith('CP') else f1b[:2]
                domain = domains[did]
                OVCCareF1B(event_id=event_id, domain=domain,
                           entity=f1b).save()
            # Save Crtical Event if exists CEVT
            cevents = request.POST.getlist('caregiver_critical_event')
            if cevents:
                for c_event in cevents:
                    OVCCareEAV(
                        entity='CEVT',
                        attribute=event_type_id,
                        value=c_event,
                        event_id=event_id
                    ).save()

    except Exception as e:
        print('error saving form 1B - %s' % (str(e)))
        return None
    else:
        return True


def save_cpara_form_by_domain(
        id, question, answer, house_hold, caregiver,
        event, date_event, exceptions=[]):
    answer_value = {'AYES': 'Yes',
                    'ANNO': 'No',
                    'ANA': 'Na'}
    if question.code.lower() == 'cp2d':
        if answer == '':
            answer = NullBooleanField
        if answer is not None:
            answer = convert_date(answer)
            answer = answer.date().strftime(format='%Y-%m-%d')
        else:
            answer = '1900-01-01'
    if answer is None:
        answer = 'No'
    if question.code not in exceptions:
        # pdb.set_trace()

        answer = answer_value[answer]
    try:
        OVCCareCpara.objects.create(
            person_id=id,
            question=question,
            caregiver=caregiver,
            answer=answer,
            household=house_hold,
            question_type=question.question_type,
            domain=question.domain,
            event=event,
            date_of_event=date_event
        )
        # pdb.set_trace()
    except Exception as e:
        print('%s :error saving cpara - %s' % (question.code, str(e)))
        return False


# PAST CPT
def get_past_cpt(ovc_id):
    # past cpt
    all_cpt_events = OVCCareEvents.objects.filter(
        event_type_id='CPAR', person_id=ovc_id, is_void=False)

    caseplan_events = []
    try:
        for one_caseplan_event in all_cpt_events:
            one_event_stable = []
            one_event_safe = []
            one_event_healthy = []
            one_event_school = []

            all_cpt = OVCCareCasePlan.objects.filter(
                event=one_caseplan_event, is_void=False)
            if all_cpt:
                for one_cpt in all_cpt:
                    comp_date = one_cpt.completion_date.strftime('%d-%b-%Y')
                    ac_date = one_cpt.actual_completion_date
                    actual_comp_date = ac_date.strftime('%d-%b-%Y')
                    cid = one_cpt.case_plan_id
                    if one_cpt.domain == 'DHNU':
                        one_event_healthy.append({
                            'cid': cid,
                            'ev_domain': one_cpt.domain,
                            'ev_goal': one_cpt.goal,
                            'ev_need': one_cpt.need,
                            'ev_priority': one_cpt.priority,
                            'ev_services': one_cpt.cp_service,
                            'ev_results': one_cpt.results,
                            'ev_reasons': one_cpt.reasons,
                            'ev_completion_date': comp_date,
                            'ev_responsible': one_cpt.responsible,
                            'ev_person': ovc_id,
                            'ev_actual_completion_date': actual_comp_date,
                            'ev_reasons': one_cpt.reasons,
                            'ev_results': one_cpt.results
                        })
                    elif one_cpt.domain == 'DHES':
                        one_event_stable.append({
                            'cid': cid,
                            'ev_domain': one_cpt.domain,
                            'ev_goal': one_cpt.goal,
                            'ev_need': one_cpt.need,
                            'ev_priority': one_cpt.priority,
                            'ev_services': one_cpt.cp_service,
                            'ev_results': one_cpt.results,
                            'ev_reasons': one_cpt.reasons,
                            'ev_completion_date': comp_date,
                            'ev_responsible': one_cpt.responsible,
                            'ev_person': ovc_id,
                            'ev_actual_completion_date': actual_comp_date,
                            'ev_reasons': one_cpt.reasons,
                            'ev_results': one_cpt.results
                        })
                    elif one_cpt.domain == 'DPRO':
                        one_event_safe.append({
                            'cid': cid,
                            'ev_domain': one_cpt.domain,
                            'ev_goal': one_cpt.goal,
                            'ev_need': one_cpt.need,
                            'ev_priority': one_cpt.priority,
                            'ev_services': one_cpt.cp_service,
                            'ev_results': one_cpt.results,
                            'ev_reasons': one_cpt.reasons,
                            'ev_completion_date': comp_date,
                            'ev_responsible': one_cpt.responsible,
                            'ev_person': ovc_id,
                            'ev_actual_completion_date': actual_comp_date,
                            'ev_reasons': one_cpt.reasons,
                            'ev_results': one_cpt.results
                        })
                    elif one_cpt.domain == 'DEDU':
                        one_event_school.append({
                            'cid': cid,
                            'ev_domain': one_cpt.domain,
                            'ev_goal': one_cpt.goal,
                            'ev_need': one_cpt.need,
                            'ev_priority': one_cpt.priority,
                            'ev_services': one_cpt.cp_service,
                            'ev_results': one_cpt.results,
                            'ev_reasons': one_cpt.reasons,
                            'ev_completion_date': comp_date,
                            'ev_responsible': one_cpt.responsible,
                            'ev_person': ovc_id,
                            'ev_actual_completion_date': actual_comp_date,
                            'ev_reasons': one_cpt.reasons,
                            'ev_results': one_cpt.results
                        })
            ev_date = one_caseplan_event.date_of_event.strftime('%d-%b-%Y')
            caseplan_events.append({
                'error': False,
                'event_ovc': ovc_id,
                'event_id': one_caseplan_event.pk,
                'event_date': ev_date,
                'event_stable': one_event_stable,
                'event_safe': one_event_safe,
                'event_healthy': one_event_healthy,
                'event_school': one_event_school
            })
        # print(("get_past_cpt successful::::::::::::", caseplan_events))
        return caseplan_events
    except Exception as e:
        caseplan_events = []
        caseplan_events.append({
            'error': True,
            'msg': '%s :error fetching past CPT - %s' % (ovc_id, str(e))
        })
        print('%s :error fetching past CPT - %s' % (ovc_id, str(e)))
        # return False
        return caseplan_events


def get_facility_list():
    """Method to get list of facilities."""
    try:
        initial_list = [('', 'Please Select')]
        flist = OVCFacility.objects.filter().values_list('id', 'facility_name')
        facility_list = initial_list + list(flist)
    except Exception as e:
        print('Error - %s' % e)
        return []
    else:
        return facility_list


def get_organization_list():
    """Method to get list of facilities."""
    try:
        initial_list = [('', 'Please Select')]
        flist = RegOrgUnit.objects.filter().values_list('id', 'org_unit_name')
        org_unit_name = initial_list + list(flist)
    except Exception as e:
        print('Error - %s' % e)
        return []
    else:
        return org_unit_name


def get_person_ids(request, name):
    """Method to get persons."""
    try:
        pids = []
        if name.isnumeric():
            sql = "SELECT id FROM reg_person WHERE id = %s" % name
            sql += " AND is_void=False"
        else:
            name = name.replace("'", "''")
            names = name.split()
            query = ("SELECT id FROM reg_person WHERE to_tsvector"
                     "(first_name || ' ' || surname || ' '"
                     " || COALESCE(other_names,''))"
                     " @@ to_tsquery('english', '%s') AND is_void=False"
                     " ORDER BY date_of_birth DESC")
            # " OFFSET 10 LIMIT 10")
            vals = ' & '.join(names)
            sql = query % (vals)
        print(sql)
        with connection.cursor() as cursor:
            cursor.execute(sql)
            row = cursor.fetchall()
            pids = [r[0] for r in row]
    except Exception as e:
        print('Error getting results - %s' % (str(e)))
        return []
    else:
        print(pids)
        return pids


def update_case_stage(request, case, stage=1):
    """Method to update case stage from pending."""
    try:
        case.case_stage = stage
        case.save()
    except Exception as e:
        print("Error changing case stage - %s" % str(e))


def get_exit(period, units, start_date, e_date):
    """Method to get exit date."""
    try:
        print(period, units, start_date, e_date)
        periods = {}
        periods['CPYR'] = {'name': 'Years', 'units': 365}
        periods['CPMN'] = {'name': 'Months', 'units': 30}
        periods['CPWK'] = {'name': 'Weeks', 'units': 7}
        periods['CPDA'] = {'name': 'Days', 'units': 7}
        total_days = 0
        today = datetime.now().date()
        if units in periods:
            unit = periods[units]
            total_days = unit['units'] * period
        exit_date = start_date + timedelta(days=total_days)
        no_days = exit_date - today
        if e_date:
            no_days = e_date - start_date
        dys = no_days.days
        ck = 'to committal expiry'
        if dys < 0:
            ck = 'after committal expiry'
            no_days = today - exit_date
        print('exit', total_days, start_date, exit_date, dys)
        # Get More
        years = ((no_days.total_seconds()) / (365.242 * 24 * 3600))
        years_int = int(years)

        months = (years - years_int) * 12
        months_int = int(months)

        days = (months - months_int) * (365.242 / 12)
        days_int = int(days)
        years_val = '' if years_int == 0 else '%s years ' % (years_int)
        mon_check = years_int > 0 and months_int > 0
        months_val = '%s months ' % (months_int) if mon_check else ''
        pds = '%s%s%s days' % (years_val, months_val, days_int)
    except Exception as e:
        print('Error calculating exit - %s' % str(e))
        return 'No committal info', ''
    else:
        return pds, ck


def get_stay(admission_date, exit_date):
    """Method to get exit date."""
    try:
        if not exit_date:
            exit_date = datetime.now().date()
        no_days = exit_date - admission_date
        # Get More
        years = ((no_days.total_seconds()) / (365.242 * 24 * 3600))
        years_int = int(years)

        months = (years - years_int) * 12
        months_int = int(months)

        days = (months - months_int) * (365.242 / 12)
        days_int = int(days)
        years_val = '' if years_int == 0 else '%s years ' % (years_int)
        mon_check = years_int > 0 and months_int > 0
        months_val = '%s months ' % (months_int) if mon_check else ''
        pds = '%s%s%s days' % (years_val, months_val, days_int)
    except Exception as e:
        print('Error calculating exit - %s' % str(e))
        return None
    else:
        return pds


def save_bursary(request, person_id):
    """Method to save bursary details."""
    try:
        adm_school = request.POST.get('in_school')
        school_id = request.POST.get('school_id')
        county_id = request.POST.get('child_county')
        constituency_id = request.POST.get('child_constituency')
        sub_county = request.POST.get('child_sub_county')
        location = request.POST.get('child_location')
        sub_location = request.POST.get('child_sub_location')
        village = request.POST.get('child_village')
        nearest_school = request.POST.get('nearest_school')
        nearest_worship = request.POST.get('nearest_worship')
        val_in_school = request.POST.get('in_school')
        in_school = True if val_in_school == 'AYES' else False
        school_class = request.POST.get('school_class')
        primary_school = request.POST.get('pri_school_name')
        school_marks = request.POST.get('kcpe_marks')
        father_names = request.POST.get('father_name')
        val_father_alive = request.POST.get('father_alive')
        father_alive = True if val_father_alive == 'AYES' else False
        father_telephone = request.POST.get('father_contact')
        mother_names = request.POST.get('mother_name')
        val_mother_alive = request.POST.get('mother_alive')
        mother_alive = True if val_mother_alive == 'AYES' else False
        mother_telephone = request.POST.get('mother_contact')
        guardian_names = request.POST.get('guardian_name')
        guardian_telephone = request.POST.get('guardian_contact')
        guardian_relation = request.POST.get('guardian_relation')
        val_same_household = request.POST.get('living_with')
        same_household = True if val_same_household == 'AYES' else False
        val_father_chronic_ill = request.POST.get('father_ill')
        fc_ill = True if val_father_chronic_ill == 'AYES' else False
        father_chronic_illness = request.POST.get('father_illness')
        val_father_disabled = request.POST.get('father_disabled')
        father_disabled = True if val_father_disabled == 'AYES' else False
        father_disability = request.POST.get('father_disability')
        val_father_pension = request.POST.get('father_pension')
        father_pension = True if val_father_pension == 'AYES' else False
        father_occupation = request.POST.get('father_occupation')
        val_mother_chronic_ill = request.POST.get('mother_ill')
        mc_ill = True if val_mother_chronic_ill == 'AYES' else False
        mother_chronic_illness = request.POST.get('mother_illness')
        val_mother_disabled = request.POST.get('mother_disabled')
        mother_disabled = True if val_mother_disabled == 'AYES' else False
        mother_disability = request.POST.get('mother_disability')
        val_mother_pension = request.POST.get('mother_pension')
        mother_pension = True if val_mother_pension == 'AYES' else False
        mother_occupation = request.POST.get('mother_occupation')

        fees_amount = request.POST.get('fees_amount')
        fees_balance = request.POST.get('balance_amount')
        school_secondary = request.POST.get('school_name')
        school_county_id = request.POST.get('school_county')
        school_constituency_id = request.POST.get('school_constituency')
        school_sub_county = request.POST.get('school_sub_county')
        school_location = request.POST.get('school_location')
        school_sub_location = request.POST.get('school_sub_location')
        school_village = request.POST.get('school_village')
        school_email = request.POST.get('school_email')
        school_telephone = request.POST.get('school_telephone')
        school_type = request.POST.get('school_type')
        school_category = request.POST.get('school_category')
        school_enrolled = request.POST.get('school_enrolled')

        school_bank_id = request.POST.get('bank')
        school_bank_branch = request.POST.get('bank_branch')
        school_bank_account = request.POST.get('bank_account')
        school_recommend_by = request.POST.get('recommend_principal')
        school_recommend_date = convert_date(
            request.POST.get('recommend_principal_date'))
        chief_recommend_by = request.POST.get('recommend_chief')
        chief_recommend_date = convert_date(
            request.POST.get('recommend_chief_date'))
        chief_telephone = request.POST.get('chief_telephone')
        csac_approved = request.POST.get('approved_csac')
        approved_amount = request.POST.get('approved_amount')
        scco_name = request.POST.get('scco_name')
        val_scco_signed = request.POST.get('signed_scco')
        scco_signed = True if val_scco_signed == 'AYES' else False
        scco_sign_date = convert_date(request.POST.get('date_signed_scco'))
        csac_chair_name = request.POST.get('csac_chair_name')
        val_csac_signed = request.POST.get('signed_csac')
        csac_signed = True if val_csac_signed == 'AYES' else False
        csac_sign_date = convert_date(request.POST.get('date_signed_csac'))
        application_date = convert_date(request.POST.get('application_date'))
        app_user_id = request.user.id
        # add missing fields

        nemis = request.POST.get('nemis_no')
        father_idno = request.POST.get('father_id')
        mother_idno = request.POST.get('mother_id')
        year_of_bursary_award = request.POST.get('year_of_bursary_award')
        eligibility_score = request.POST.get('eligibility_scores')
        date_of_issue = convert_date(request.POST.get('date_of_issue'))
        status_of_student = request.POST.get('status_of_student')

        obj, created = OVCEducationFollowUp.objects.get_or_create(
            school_id=school_id, person_id=person_id,
            defaults={'admitted_to_school': adm_school},
        )
        # Save all details from the Bursary form
        gok_bursary = OVCGokBursary(
            person_id=person_id, county_id=county_id,
            constituency_id=constituency_id,
            sub_county=sub_county, location=location,
            sub_location=sub_location, village=village,
            nearest_school=nearest_school,
            nearest_worship=nearest_worship, in_school=in_school,
            school_class=school_class, primary_school=primary_school,
            school_marks=school_marks, father_names=father_names,
            father_alive=father_alive, father_telephone=father_telephone,
            mother_names=mother_names, mother_alive=mother_alive,
            mother_telephone=mother_telephone, guardian_names=guardian_names,
            guardian_telephone=guardian_telephone,
            guardian_relation=guardian_relation, same_household=same_household,
            father_chronic_ill=fc_ill,
            father_chronic_illness=father_chronic_illness,
            father_disabled=father_disabled,
            father_disability=father_disability,
            father_pension=father_pension,
            father_occupation=father_occupation,
            mother_chronic_ill=mc_ill,
            mother_chronic_illness=mother_chronic_illness,
            mother_disabled=mother_disabled,
            mother_disability=mother_disability,
            mother_pension=mother_pension,
            mother_occupation=mother_occupation,
            fees_amount=fees_amount, fees_balance=fees_balance,
            school_secondary=school_secondary,
            school_county_id=school_county_id,
            school_constituency_id=school_constituency_id,
            school_sub_county=school_sub_county,
            school_location=school_location,
            school_sub_location=school_sub_location,
            school_village=school_village, school_telephone=school_telephone,
            school_email=school_email, school_type=school_type,
            school_category=school_category, school_enrolled=school_enrolled,
            school_bank_id=school_bank_id,
            school_bank_branch=school_bank_branch,
            school_bank_account=school_bank_account,
            school_recommend_by=school_recommend_by,
            school_recommend_date=school_recommend_date,
            chief_recommend_by=chief_recommend_by,
            chief_recommend_date=chief_recommend_date,
            chief_telephone=chief_telephone,
            csac_approved=csac_approved, approved_amount=approved_amount,
            ssco_name=scco_name, scco_signed=scco_signed,
            scco_sign_date=scco_sign_date, csac_chair_name=csac_chair_name,
            csac_signed=csac_signed, csac_sign_date=csac_sign_date,
            app_user_id=app_user_id, application_date=application_date,
            nemis=nemis,
            father_idno=father_idno,
            mother_idno=mother_idno,
            year_of_bursary_award=year_of_bursary_award,
            eligibility_score=eligibility_score,
            date_of_issue=date_of_issue,
            status_of_student=status_of_student)
        gok_bursary.save()
    except Exception as e:
        print('Error saving bursary - %s' % (str(e)))


def get_placement(request, ou_id, person_id):
    """Method to get organizatin units."""
    try:
        placement = OVCPlacement.objects.get(
            residential_institution_id=ou_id,
            person_id=person_id, is_active=True)
    except Exception as e:
        print('Child has not been placed - %s' % e)
        return None
    else:
        return placement


def get_questions(set_id, default_txt=None):
    """Method to get set of questions list."""
    try:
        cache_key = 'question_list_%s' % (set_id)
        cache_list = cache.get(cache_key)
        if cache_list:
            v_list = cache_list
            print('FROM Cache %s' % (cache_key))
        else:
            v_list = ListAnswers.objects.filter(
                answer_set_id=set_id, is_void=False)
            cache.set(cache_key, v_list, 300)
        my_list = v_list.values_list(
            'answer_code', 'answer').order_by('the_order')
        if default_txt:
            initial_list = ('', default_txt)
            final_list = [initial_list] + list(my_list)
            return final_list
    except Exception as e:
        print('error - %s' % (e))
        return ()
    else:
        return my_list


def save_case_info(request, case, item_type, item_id, item_detail):
    """method to save additional case information."""
    try:
        case_id = case.case_id
        person_id = case.person_id
        obj, created = OvcCaseInformation.objects.update_or_create(
            case_id=case_id, person_id=person_id, info_type=item_type,
            info_item=item_id, is_void=False,
            defaults={'info_detail': item_detail},
        )
        print('Saved', obj, created)
    except Exception as e:
        print('Error saving case info - %s' % (e))
        raise e
    else:
        return obj


def get_case_info(request, case_id):
    """Method to get all case info for a case."""
    try:
        case_infos = OvcCaseInformation.objects.filter(
            case_id=case_id, is_void=False)
    except Exception as e:
        raise e
    else:
        return case_infos


def save_case_other_geos(case_id, person_id, params={}):
    """Save Persons other geo ares."""
    try:
        country_code = params['country'] if 'country' in params else None
        city = params['city'] if 'city' in params else None
        location = params['location'] if 'location' in params else None
        sub_loc = params['sub_location'] if 'sub_location' in params else None
        geo, created = OVCCaseLocation.objects.update_or_create(
            case_id=case_id, person_id=person_id,
            defaults={'report_country_code': country_code, 'report_city': city,
                      'report_location_id': location,
                      'report_sublocation_id': sub_loc,
                      'is_void': False},)
    except Exception as e:
        error = 'Error saving other geos -%s' % (str(e))
        print(error)
        return None, None
    else:
        return geo, created


def save_critical_event(request, person_id, event_type_id, cevents):
    """Method to save critical event."""
    try:
        date_of_cevent = request.POST.get('olmis_service_date')
        if date_of_cevent:
            date_of_cevent = convert_date(date_of_cevent)

        # Save Critical Event
        event_counter = OVCCareEvents.objects.filter(
            event_type_id=event_type_id,
            person_id=person_id,
            is_void=False).count()

        ovccareevent = OVCCareEvents(
            event_type_id=event_type_id,
            event_counter=event_counter,
            event_score=0,
            date_of_event=date_of_cevent,
            created_by=request.user.id,
            person_id=person_id
        )
        ovccareevent.save()
        event_id = ovccareevent.pk

        # Critical Events [CEVT]
        for event in cevents:
            OVCCareEAV(
                entity='CEVT',
                attribute=event_type_id,
                value=event,
                event_id=event_id
            ).save()
    except Exception as e:
        print('Error saving CG critical event - %s' % (e))
        pass
    else:
        pass


def save_ovc_program(request, person_id, ovc_prog):
    """Method to save ovc_programs to avoid registry
       creating new entries to different tables."""
    try:
        print('Enroll to OVC program')
        user_id = request.user.id
        reg_date = request.POST.get('registration_date', '1900-01-01')
        cbo_id = request.POST.get('cbo_unit_id')
        chv_id = request.POST.get('chv_unit_id')
        prog, created = OVCProgramRegistration.objects.update_or_create(
            person_id=person_id, program=ovc_prog,
            defaults={'child_cbo_id': cbo_id, 'child_chv_id': chv_id,
                      'created_by_id': user_id,
                      'registration_date': reg_date, 'is_void': False})
    except Exception as e:
        print('Error saving program - %s' % (str(e)))
        return None
    else:
        return prog


def get_ovc_program(request, person_id, ovc_prog):
    """Method to Program enrollments."""
    try:
        program = OVCProgramRegistration.objects.get(
            person_id=person_id, program=ovc_prog)
    except Exception as e:
        print('Child not initiated in a program - %s' % e)
        return None
    else:
        return program
