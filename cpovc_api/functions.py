from datetime import datetime, timedelta
from django.db.models import Count

from cpovc_registry.models import (
    RegPersonsTypes, RegPersonsOrgUnits, RegPerson, RegOrgUnit,
    RegPersonsExternalIds, RegPersonsGeo)
from cpovc_forms.models import (
    OVCCaseRecord, OVCCaseCategory, OVCCareServices, OVCCaseGeo,
    OVCPlacement, OVCCareEvents, OVCCareF1B, OVCCareCasePlan,
    OVCCareForms, OVCCareQuestions, OVCCareBenchmarkScore,
    OVCCareCpara, OVCSubPopulation, OVCCareIndividaulCpara, OVCCareEAV)

from cpovc_auth.models import AppUser
from cpovc_ovc.models import (
    OVCRegistration, OVCHHMembers, OVCHealth)

from cpovc_registry.functions import get_orgs_child
from cpovc_auth.functions import get_attached_units

from cpovc_main.functions import get_dict

from cpovc_dashboard.parameters import PARAMS

from .models import DeviceManagement


def get_attached_orgs(request):
    """Method to get attached units."""
    try:
        orgs = []
        dcs = 'Directorate of Children Services (DCS)'
        person_id = request.user.reg_person_id
        person_orgs = RegPersonsOrgUnits.objects.filter(
            person_id=person_id, is_void=False)
        reg_pri, reg_ovc, reg_pri_name = 2, False, dcs
        all_roles, all_ous = [], []
        for p_org in person_orgs:
            p_roles = []
            org_id = p_org.org_unit_id
            org_name = p_org.org_unit.org_unit_name
            reg_assist = p_org.reg_assistant
            if reg_assist:
                p_roles.append('REGA')
                all_roles.append('REGA')
            reg_prim = p_org.primary_unit
            if reg_prim:
                reg_pri = org_id
                reg_pri_name = org_name
            reg_ovc = p_org.org_unit.handle_ovc
            if reg_ovc:
                p_roles.append('ROVC')
                all_roles.append('ROVC')
                reg_ovc = True
            pvals = {org_id: p_roles}
            orgs.append(pvals)
            all_ous.append(str(org_id))
        # allroles = ','.join(list(set(all_roles)))
        # allous = ','.join(all_ous)
        child_ous = get_child_units([reg_pri])
        vals = {'perms': orgs, 'ou_id': reg_pri,
                'attached_ou': all_ous, 'perms_ou': all_roles,
                'reg_ovc': reg_ovc, 'ou_name': reg_pri_name,
                'ou_attached': child_ous}
    except Exception as e:
        print('Error with dashboard - %s' % (str(e)))
        return {}
    else:
        return vals


def dcs_dashboard(request, params):
    """Method to get dashboard totals."""
    try:
        dash = {}
        vals = {'TBVC': 0, 'TBGR': 0, 'TWGE': 0, 'TWNE': 0}
        pr_ouid = int(request.session.get('ou_primary', 0))
        if request.user.is_superuser or pr_ouid == 2:
            person_types = RegPersonsTypes.objects.filter(
                is_void=False, date_ended=None).values(
                    'person_type_id').annotate(dc=Count('person_type_id'))
            for person_type in person_types:
                vals[person_type['person_type_id']] = person_type['dc']
            dash['children'] = vals['TBVC']
            dash['caregivers'] = vals['TBGR']
            dash['government'] = vals['TWGE']
            dash['ngo'] = vals['TWNE']
            # Get org units
            org_units = RegOrgUnit.objects.filter(is_void=False).count()
            dash['org_units'] = org_units
            # Case categories to find pending cases
            cases_category = OVCCaseCategory.objects.filter(is_void=False)
            # Case records counts
            case_records = OVCCaseRecord.objects.filter(is_void=False)
            case_counts = cases_category.count()
            dash['case_records'] = case_counts
            # Workforce members
            workforce_members = RegPersonsExternalIds.objects.filter(
                identifier_type_id='IWKF', is_void=False).count()
            workforce_members = AppUser.objects.distinct(
                'reg_person_id').count()
            dash['workforce_members'] = workforce_members
            # Get pending
            cases = case_records.filter(case_stage=0).values_list(
                'case_id', flat=True).distinct()
            pending_count = cases_category.filter(
                case_id_id__in=cases).count()
            dash['pending_cases'] = pending_count
            # Child registrations
            ptypes = RegPersonsTypes.objects.filter(
                person_type_id='TBVC', is_void=False,
                date_ended=None).values_list('person_id', flat=True)
            cregs = RegPerson.objects.filter(id__in=ptypes).values(
                'created_at').annotate(unit_count=Count('created_at'))
            # Institution Population
            dash['inst_pop'] = {'B': 0, 'G': 0}
        else:
            # Org units
            cbo_id = request.session.get('ou_primary', 0)
            cbo_ids = request.session.get('ou_attached', [])
            print(cbo_ids)
            org_id = int(cbo_id)
            org_ids = get_orgs_child(org_id)
            # Workforce members using Appuser
            person_orgs = RegPersonsOrgUnits.objects.select_related().filter(
                org_unit_id__in=org_ids, is_void=False,
                date_delinked=None).values_list('person_id', flat=True)
            users = AppUser.objects.filter(
                reg_person_id__in=person_orgs)
            user_ids = users.values_list('id', flat=True)
            print('user ids', user_ids)
            users_count = users.count()
            dash['workforce_members'] = users_count
            person_types = RegPersonsTypes.objects.filter(
                is_void=False, date_ended=None,
                person__created_by_id__in=user_ids).values(
                    'person_type_id').annotate(dc=Count('person_type_id'))
            for person_type in person_types:
                vals[person_type['person_type_id']] = person_type['dc']
            dash['children'] = vals['TBVC']
            dash['caregivers'] = vals['TBGR']
            dash['government'] = vals['TWGE']
            dash['ngo'] = vals['TWNE']
            # Get org units
            orgs_count = len(org_ids) - 1 if len(org_ids) > 1 else 1
            dash['org_units'] = orgs_count
            # Org unit cases
            case_ids = OVCCaseGeo.objects.select_related().filter(
                report_orgunit_id__in=org_ids,
                is_void=False).values_list('case_id_id', flat=True)
            # Case records counts
            case_records = OVCCaseRecord.objects.filter(
                case_id__in=case_ids, is_void=False)
            # Case categories to find pending cases
            cases_category = OVCCaseCategory.objects.filter(
                is_void=False, case_id_id__in=case_ids)
            case_counts = cases_category.count()
            dash['case_records'] = case_counts
            # Get pending
            cases = case_records.filter(
                case_stage=0, case_id__in=case_ids).values_list(
                'case_id', flat=True).distinct()
            pending_count = cases_category.filter(
                case_id_id__in=cases).count()
            dash['pending_cases'] = pending_count
            # Child registrations
            ptypes = RegPersonsTypes.objects.filter(
                person_type_id='TBVC', is_void=False,
                date_ended=None).values_list('person_id', flat=True)
            cregs = RegPerson.objects.filter(
                id__in=ptypes, created_by_id__in=user_ids).values(
                'created_at').annotate(unit_count=Count('created_at'))
            # Institution Population
            inst_pop = {'B': 0, 'G': 0}
            ou_type = request.session.get('ou_type', None)
            print('OU TYPE', ou_type)
            if ou_type:
                inst_id = request.session.get('ou_primary', 0)
                ou_attached = request.session.get('ou_attached', 0)
                print('OU ID', inst_id, ou_attached)
                inst_pops = OVCPlacement.objects.filter(
                    residential_institution_name=str(inst_id),
                    is_active=True, is_void=False).values(
                    'person__sex_id').annotate(
                    dcount=Count('person__sex_id'))
                for ipop in inst_pops:
                    if str(ipop['person__sex_id']) == 'SFEM':
                        inst_pop['G'] = ipop['dcount']
                    else:
                        inst_pop['B'] = ipop['dcount']
            dash['inst_pop'] = inst_pop
        # OVC
        oregs = OVCRegistration.objects.values(
            'registration_date').annotate(
            unit_count=Count('registration_date'))
        child_regs, case_regs, ovc_regs = {}, {}, {}
        for creg in cregs:
            the_date = creg['created_at']
            # cdate = '1900-01-01'
            cdate = the_date.strftime('%d-%b-%y')
            # child_regs[str(cdate)] = creg['unit_count']
        for oreg in oregs:
            the_date = oreg['registration_date']
            # cdate = the_date.strftime('%d-%b-%y')
            # ovc_regs[str(cdate)] = oreg['unit_count']
        # Case Records
        ovc_regs = case_records.values(
            'date_case_opened').annotate(unit_count=Count('date_case_opened'))
        for ovc_reg in ovc_regs:
            the_date = ovc_reg['date_case_opened']
            # cdate = '1900-01-01'
            # cdate = the_date.strftime('%d-%b-%y')
            # case_regs[str(cdate)] = ovc_reg['unit_count']
        # Case categories Top 5
        case_categories = cases_category.values(
            'case_category').annotate(unit_count=Count(
                'case_category')).order_by('-unit_count')
        dash['child_regs'] = child_regs
        dash['ovc_regs'] = []
        dash['case_regs'] = case_regs
        dash['case_cats'] = []
    except Exception as e:
        print('error with dash - %s' % (str(e)))
        dash = {}
        dash['children'] = 0
        dash['caregivers'] = 0
        dash['government'] = 0
        dash['ngo'] = 0
        dash['org_units'] = 0
        dash['case_records'] = 0
        dash['workforce_members'] = 0
        dash['pending_cases'] = 0
        dash['child_regs'] = []
        dash['ovc_regs'] = []
        dash['case_regs'] = []
        dash['case_cats'] = 0
        # Institution Population
        dash['inst_pop'] = {'B': 0, 'G': 0}
        return dash
    else:
        return dash


def ovc_dashboard(request, params):
    """Method to get dashboard totals."""
    try:
        dash = {}
        today = datetime.now()
        start_date = today - timedelta(days=30)
        vals = {'TBVC': 0, 'TBGR': 0, 'TWGE': 0, 'TWNE': 0}
        person_types = RegPersonsTypes.objects.filter(
            is_void=False, date_ended=None).values(
            'person_type_id').annotate(dc=Count('person_type_id'))
        for person_type in person_types:
            vals[person_type['person_type_id']] = person_type['dc']
        dash['children'] = vals['TBVC']
        dash['caregivers'] = vals['TBGR']
        dash['government'] = vals['TWGE']
        dash['ngo'] = vals['TWNE']
        # OVC Filters using params
        cbo_id = params['ou_primary'] if 'ou_primary' in params else 0
        org_ids = params['attached_ou'] if 'attached_ou' in params else []
        reg_ovc = params['reg_ovc'] if 'reg_ovc' in params else 0
        # Case records
        case_records = OVCCaseRecord.objects.filter(
            date_case_opened__gte=start_date, is_void=False)
        case_counts = case_records.count()
        dash['case_records'] = case_counts
        # Case categories to find pending cases
        pending_cases = OVCCaseCategory.objects.filter(
            date_of_event__gte=start_date, is_void=False)
        pending_count = pending_cases.exclude(
            case_id__summon_status=True).count()
        dash['pending_cases'] = pending_count
        # Child registrations
        ptypes = RegPersonsTypes.objects.filter(
            person_type_id='TBVC', is_void=False,
            date_ended=None).values_list('person_id', flat=True)
        # Get org units
        orgs_count = len(org_ids) - 1 if len(org_ids) > 1 else 1
        dash['org_units'] = orgs_count
        # Case records counts
        person_orgs = RegPersonsOrgUnits.objects.select_related().filter(
            org_unit_id__in=org_ids, is_void=False,
            date_delinked=None).values_list('person_id', flat=True)
        users_count = AppUser.objects.filter(
            reg_person_id__in=person_orgs).count()
        dash['workforce_members'] = users_count
        # For OVC
        child_regs, case_regs, ovc_regs = {}, {}, {}
        if request.user.is_superuser:
            regs = OVCRegistration.objects.filter(is_void=False)
        else:
            regs = OVCRegistration.objects.filter(
                is_void=False, child_cbo_id__in=org_ids)
        # Default values for IP summary
        am, af, em, ef, sm, sf, gm, gf = 0, 0, 0, 0, 0, 0, 0, 0
        # Get guardians
        guardian_genders = regs.values('caretaker__sex_id').annotate(
            total=Count('caretaker_id', distinct=True)).order_by('total')
        for gs in guardian_genders:
            g_gender = gs['caretaker__sex_id']
            g_count = gs['total']
            if g_gender:
                gg = str(g_gender)
                if gg == 'SMAL':
                    gm = g_count
                else:
                    gf = g_count
        guardian_count = regs.values('caretaker_id').distinct().count()
        dash['caregivers'] = guardian_count
        # Get households
        child_ids = regs.values_list('person_id', flat=True)
        hh_count = OVCHHMembers.objects.filter(
            person_id__in=child_ids).values(
            'house_hold_id').distinct().count()
        if request.user.is_superuser:
            oregs = OVCRegistration.objects.filter(
                registration_date__gte=start_date).values(
                'registration_date').annotate(
                unit_count=Count('registration_date'))
            cregs = RegPerson.objects.filter(
                created_at__gte=start_date, id__in=ptypes).values(
                'created_at').annotate(unit_count=Count('created_at'))
        else:
            oregs = OVCRegistration.objects.filter(
                child_cbo_id__in=org_ids,
                registration_date__gte=start_date).values(
                'registration_date').annotate(
                unit_count=Count('registration_date'))
            # Child registrations
            cregs = RegPerson.objects.filter(
                created_at__gte=start_date, id__in=ptypes)
            if reg_ovc:
                cregs = cregs.filter(id__in=child_ids)
            cregs = cregs.values('created_at').annotate(
                unit_count=Count('created_at'))
        dash['household'] = hh_count
        sqs = regs.values('is_active').annotate(
            total=Count('is_active')).order_by('total')
        # Get breakdown by Genders
        ovc_cls = regs.values(
            'is_active', 'person__sex_id').annotate(
            total=Count('person__sex_id')).order_by('total')
        ovc_schs = regs.filter(is_active=True).exclude(
            school_level='SLNS').values(
            'person__sex_id').annotate(
            total=Count('person__sex_id')).order_by('total')
        for ovc_sch in ovc_schs:
            child = ovc_sch['total']
            ovc_sex = str(ovc_sch['person__sex_id'])
            if ovc_sex == 'SMAL':
                sm = child
            else:
                sf = child
        for ovc_cl in ovc_cls:
            child = ovc_cl['total']
            status = ovc_cl['is_active']
            ovc_sex = str(ovc_cl['person__sex_id'])
            if status:
                if ovc_sex == 'SMAL':
                    am = child
                else:
                    af = child
            else:
                if ovc_sex == 'SMAL':
                    em = child
                else:
                    ef = child
        ovc_summ = {'m0': em + am, 'm1': am, 'm2': sm, 'm3': 0,
                    'm4': gm, 'f0': ef + af, 'f1': af,
                    'f2': sf, 'f3': 0, 'f4': gf}
        # Person types
        exited_ovc, active_child = 0, 0
        for sq in sqs:
            child = sq['total']
            status = sq['is_active']
            if status:
                active_child = child
            else:
                exited_ovc = child
        dash['children'] = active_child
        dash['children_all'] = exited_ovc + active_child
        for creg in cregs:
            the_date = creg['created_at']
            cdate = the_date.strftime('%d-%b-%y')
            child_regs[str(cdate)] = creg['unit_count']
        for oreg in oregs:
            the_date = oreg['registration_date']
            cdate = the_date.strftime('%d-%b-%y')
            ovc_regs[str(cdate)] = oreg['unit_count']
        # Case Records / OVC Services
        ovc_summ['m3'] = 0
        ovc_summ['f3'] = 0
        dash['ovc_summary'] = ovc_summ
        # Case categories Top 5

        dash['ovc_regs'] = []
        dash['case_regs'] = []
        dash['case_cats'] = {}
        dash['criteria'] = {}
    except Exception as e:
        print(
            'error - {}'.format(str(e)))
        dash = {}
        dash['children'] = 0
        dash['children_all'] = 0
        dash['guardian'] = 0
        dash['government'] = 0
        dash['ngo'] = 0
        dash['org_units'] = 0
        dash['case_records'] = 0
        dash['workforce_members'] = 0
        dash['pending_cases'] = 0
        dash['child_regs'] = []
        dash['ovc_regs'] = []
        dash['case_regs'] = []
        dash['case_cats'] = 0
        dash['household'] = 0
        dash['criteria'] = {}
        dash['ovc_summary'] = {}
        return dash
    else:
        return dash


def get_vals(val, vals):
    """Method to convert value to User readable"""
    try:
        fval = vals[val] if val in vals else val
    except Exception:
        return val
    else:
        return fval


def validate_ovc(request, ovc_cpims_id):
    """Method to get household ID."""
    try:
        ovc = OVCRegistration.objects.get(
            person_id=ovc_cpims_id, is_void=False)
        cbo_id = ovc.child_cbo_id
        ous = get_user_org_unit(request, 4)
        child_ous = get_child_units(ous)
        for ou in ous:
            child_ous.append(int(ou))
        cbo_access = True if cbo_id in child_ous else False
        print('VAR Check', cbo_id, ous, child_ous, cbo_access)
    except Exception:
        return None
    else:
        return cbo_access


def get_child_units(org_ids):
    """Method to do the organisation tree."""
    try:
        # print org_ids
        orgs = RegOrgUnit.objects.filter(
            parent_org_unit_id__in=org_ids).values_list('id', flat=True)
        print('Check Org Unit level - %s' % (str(orgs)))
    except Exception as e:
        print('No parent unit - %s' % (str(e)))
        return []
    else:
        return list(orgs)


def get_household(request, person_id):
    """Method to get household ID."""
    try:
        '''
        child = RegPerson.objects.get(is_void=False, id=ovc_id)
        care_giver = RegPerson.objects.get(
            id=OVCRegistration.objects.get(person=child).caretaker_id)
        '''
        household = OVCHHMembers.objects.filter(
            is_void=False, person_id=person_id).first()
        hhid = household.house_hold_id if household else None
    except Exception:
        return None
    else:
        return hhid


def get_event_count(request, person_id, ev_type_id):
    """Method to get household ID."""
    try:
        event_counter = OVCCareEvents.objects.filter(
            event_type_id=ev_type_id, person_id=person_id,
            is_void=False).count()
    except Exception:
        return 0
    else:
        return event_counter


def get_user_org_unit(request, item_id=1):
    """Method to get user primary unit."""
    try:
        print('U', request.user.username)
        ou_vars = get_attached_units(request.user, False)
        print('OUP', ou_vars)
        primary_ou, primary_name, attached_ou = 0, '', ''
        attached_ous = []
        if ou_vars:
            primary_ou = ou_vars['primary_ou']
            primary_name = ou_vars['primary_name']
            attached_ous = ou_vars['attached_ous']
    except Exception:
        return ''
    else:
        if item_id == 4:
            return attached_ous
        if item_id == 3:
            return attached_ou
        elif item_id == 2:
            return primary_ou
        else:
            return primary_name


def save_event(request, person_id, event_date, hhid, ev_type_id='FM1B'):
    """Method to save event."""
    try:
        user_id = request.user.id
        event = OVCCareEvents(
            event_type_id=ev_type_id, created_by=user_id,
            person_id=person_id, house_hold_id=hhid,
            date_of_event=event_date)
        event.save()
        event_id = event.pk
    except Exception as e:
        raise e
    else:
        return event_id


def save_form(request, person_id, event_date, form_id, services, scores=[]):
    """Method to save forms."""
    try:
        # Forms settings
        fms = {'F1A': 'FSAM', 'F1B': 'FM1B', 'CPT': 'CPAR', 'CPR': 'cpr'}
        ev_type_id = fms[form_id] if form_id in fms else 'F1A'
        caregiver = OVCRegistration.objects.filter(person_id=person_id).first()
        caregiver_id = caregiver.caretaker_id
        if ev_type_id == 'FM1B':
            person_id = caregiver_id
        hhid = get_household(request, person_id)
        event_id = save_event(request, person_id, event_date, hhid, ev_type_id)
        org_unit_name = get_user_org_unit(request)
        # Forms data save
        if form_id == 'F1A':
            # Form 1A - Services to the OVC
            for service in services:
                service_domain = service['domain_id']
                service_id = service['service_id']
                ev_date = 'service_date'
                iserv_date = service[ev_date] if ev_date in service else None
                service_date = iserv_date if iserv_date else event_date
                OVCCareServices(
                    domain=service_domain,
                    service_provided=service_id,
                    service_provider=org_unit_name,
                    date_of_encounter_event=service_date,
                    event_id=event_id,
                ).save()
            # Critical events
            cevents = request.data.get('critical_events', [])
            for cevent in cevents:
                critical_event_id = cevent['event_id']
                OVCCareEAV(
                    entity="CEVT",
                    attribute="FSAM",
                    value=critical_event_id,
                    event_id=event_id
                ).save()
        elif form_id == 'F1B':
            # Form 1B - Services to the Caregiver
            for service in services:
                service_domain = service['domain_id']
                service_id = service['service_id']
                OVCCareF1B(event_id=event_id, domain=service_domain,
                           entity=service_id).save()
            # Critical events
            cevents = request.data.get('critical_events')
            for cevent in cevents:
                critical_event_id = cevent['event_id']
                OVCCareEAV(
                    entity="CEVT",
                    attribute="FSAM",
                    value=critical_event_id,
                    event_id=event_id
                ).save()
        elif form_id == 'CPT':
            # Case Plan Template
            ddate = '1900-01-01'
            acd = 'actual_completion_date'
            dpe = 'date_of_prev_event'
            for service in services:
                service_domain = service['domain_id']
                service_ids = service['service_id']
                goal_id = service['goal_id']
                gap_id = service['gap_id']
                priority_id = service['priority_id']
                responsible_id = service['responsible_id']
                results_id = service['results_id']
                reason_id = service['reason_id']
                prev_date = service[dpe] if dpe in service else '1900-01-01'
                comp_date = service['completion_date']
                acomp_date = service[acd] if acd in service else None
                # Dates
                date_of_prev_event = prev_date if prev_date else None
                completion_date = comp_date if comp_date else None
                actual_completion_date = acomp_date if acomp_date else ddate

                # Form ID
                cp_form_id = OVCCareForms.objects.get(
                    name='OVCCareCasePlan').pk
                for service_id in service_ids:
                    OVCCareCasePlan(
                        domain=service_domain,
                        goal=goal_id,
                        person_id=person_id,
                        caregiver_id=caregiver_id,
                        household_id=hhid,
                        need=gap_id,
                        priority=priority_id,
                        cp_service=service_id,
                        responsible=responsible_id,
                        date_of_previous_event=date_of_prev_event,
                        date_of_event=event_date,
                        form_id=cp_form_id,
                        completion_date=completion_date,
                        actual_completion_date=actual_completion_date,
                        results=results_id,
                        reasons=reason_id,
                        case_plan_status='D',
                        event_id=event_id
                    ).save()
        elif form_id == 'CPR':
            # Case Plan Achievement Readiness Assessment (CPARA)
            print('Form CPARA')
            # Answer mappings
            answers, ianswers = {}, {}
            all_iqtns = ['CP15q', 'CP16q', 'CP17q']
            amaps = {'AYES': True, 'ANNO': False,
                     'ANA': 'Na', 'ANNA': 'Na'}
            qtns = request.data.get('questions')
            iqtns = request.data.get('individual_questions')
            scores = request.data.get('scores')
            sub_pops = request.data.get('ovc_subpopulation')
            d_previous = request.data.get('date_of_previous_event')
            date_previous = d_previous if d_previous else None
            print('Questions', qtns)
            print('Scores', scores)
            print('Individual Questions', iqtns)
            # Answers to dict
            all_ans, all_ians = {}, {}
            if qtns:
                for qtn in qtns:
                    q_code = qtn['question_code']
                    ans_id = qtn['answer_id']
                    if ans_id is None:
                        f_answer = None
                    else:
                        f_answer = amaps[ans_id] if ans_id in amaps else 'No'
                    all_ans[q_code] = f_answer
            # Individual answers
            if iqtns:
                for ind_ovcs in iqtns:
                    ind_code = ind_ovcs["question_code"]
                    ans_id = ind_ovcs["answer_id"]
                    if ans_id is None:
                        ind_answer = None
                    else:
                        ind_answer = amaps[ans_id] if ans_id in amaps else 'No'
                    all_ians[ind_code] = ind_answer
            questions = OVCCareQuestions.objects.filter(
                code__startswith='CP', is_void=False).values()
            for question in questions:
                qtnid = question['code']
                # db_ans[qtnid] = question
                if qtnid in all_ans:
                    f_ans = all_ans[qtnid]
                    question['answer_id'] = f_ans
                else:
                    question['answer_id'] = 'False'
                answers[qtnid] = question
                # Individual questions
                if qtnid in all_iqtns:
                    if qtnid in all_ians:
                        f_ans = all_ians[qtnid]
                        question['answer_id'] = f_ans
                        ianswers[qtnid] = question
            # Save questions for HH
            for ans in answers:
                answer = answers[ans]
                OVCCareCpara.objects.create(
                    person_id=person_id,
                    caregiver_id=caregiver_id,
                    question_id=answer['question_id'],
                    question_code=answer['code'],
                    answer=answer['answer_id'],
                    household_id=hhid,
                    question_type=answer['question_type'],
                    domain=answer['domain'],
                    event_id=event_id,
                    date_of_event=event_date,
                    date_of_previous_event=date_previous
                )
            # Save questions for individual HH members
            print('CPARA Check', ianswers)
            if iqtns:
                for ind_ovcs in iqtns:
                    ind_ovc = ind_ovcs["ovc_cpims_id"]
                    ind_code = ind_ovcs["question_code"]
                    print('ICPARA', ind_ovcs)
                    for ians in ianswers:
                        ianswer = ianswers[ians]
                        i_code = ianswer['code']
                        print('ICPAARA', ianswer)
                        if i_code == ind_code:
                            OVCCareIndividaulCpara.objects.create(
                                person_id=ind_ovc,
                                caregiver_id=caregiver_id,
                                question_code=i_code,
                                question_id=ianswer['question_id'],
                                answer=ind_answer,
                                household_id=hhid,
                                question_type=ianswer['question_type'],
                                domain=ianswer['domain'],
                                date_of_event=event_date,
                                date_of_previous_event=date_previous,
                                event_id=event_id
                            )
            # OVC sub population
            if sub_pops:
                for sub_pop in sub_pops:
                    ovc_sid = sub_pop['ovc_cpims_id']
                    criteria_id = sub_pop['criteria']
                    OVCSubPopulation.objects.create(
                        person_id=ovc_sid,
                        criteria=criteria_id,
                        event_id=event_id,
                        date_of_event=event_date
                    )
            # Save scores by array IDS - None is Zero
            ovc_score = [0 for i in range(0, 9)]
            if scores:
                for bm in scores:
                    for itm in bm:
                        bv = bm[itm]
                        idx = int(itm.replace('b', '')) - 1
                        ovc_score[idx] = int(bv)
                OVCCareBenchmarkScore.objects.create(
                    household_id=hhid,
                    benchmark_1=int(ovc_score[0]),
                    benchmark_2=int(ovc_score[1]),
                    benchmark_3=int(ovc_score[2]),
                    benchmark_4=int(ovc_score[3]),
                    benchmark_5=int(ovc_score[4]),
                    benchmark_6=int(ovc_score[5]),
                    benchmark_7=int(ovc_score[6]),
                    benchmark_8=int(ovc_score[7]),
                    benchmark_9=int(ovc_score[8]),
                    score=sum([int(i) for i in ovc_score]),
                    event_id=event_id,
                    date_of_event=event_date,
                    care_giver_id=caregiver_id)
    except Exception as e:
        msg = 'Error saving form - %s' % (str(e))
        return msg
    else:
        msg = 'Form %s details saved successfully' % form_id
        return msg


def get_ovc_data(request, ovc_cpims_id, form_id):
    """Method to get OVC past events."""
    try:
        results = {}
        fms = {'F1A': 'FSAM', 'F1B': 'FM1B', 'CPT': 'CPAR', 'CPR': 'cpr'}
        ovc_access = validate_ovc(request, ovc_cpims_id)
        if ovc_access:
            qs = OVCRegistration.objects.filter(
                person_id=ovc_cpims_id, is_void=False)
            if qs:
                queryset = qs[0]
                if queryset.hiv_status in ['HSTP', 'HHEI']:
                    health = OVCHealth.objects.get(
                        person_id=ovc_cpims_id, is_void=False)
                    if health:
                        facility_name = health.facility.facility_name
                        results["ccc_number"] = health.ccc_number
                        results["date_of_linkage"] = health.date_linked
                        results["facility_name"] = facility_name
                # Primary information
                results["ovc_cpims_id"] = ovc_cpims_id
                results["ovc_names"] = queryset.person.all_names
                results["date_of_birth"] = queryset.person.date_of_birth
                results["ovc_enrollment_date"] = queryset.registration_date
                exit_status = "ACTIVE" if queryset.is_active else "EXITED"
                results["exit_status"] = exit_status
                results["exit_date"] = queryset.exit_date
                # CBO
                results["cbo_id"] = queryset.child_cbo_id
                results["cbo_name"] = queryset.child_cbo.org_unit_name
                # CHV
                results["chv_cpims_id"] = queryset.child_chv_id
                results["chv_names"] = queryset.child_chv.all_names
                # Caregiver
                results["caregiver_cpims_id"] = queryset.caretaker_id
                results["caregiver_names"] = queryset.caretaker.all_names
                # Other identifiers
                results["nemis_no"] = None
                results["nupi_no"] = None
                # Geo locations
                geos = RegPersonsGeo.objects.filter(
                    person_id=ovc_cpims_id, is_void=False)
                ward_id, ward_name = None, None
                const_id, const_name = None, None
                county_id, county_name = None, None
                for geo in geos:
                    if geo.area.area_type_id == "GWRD":
                        ward_id = geo.area.area_code
                        ward_name = geo.area.area_name
                    if geo.area.area_type_id == "GDIS":
                        const_id = geo.area.area_code
                        const_name = geo.area.area_name
                        county_id = geo.area.parent_area_id
                if county_id:
                    county_id = str(county_id).zfill(3)
                    county_name = PARAMS[county_id]
                results["county"] = {"code": county_id, "name": county_name}
                results["constituency"] = {"code": const_id,
                                           "name": const_name}
                results["ward"] = {"code": ward_id, "name": ward_name}
            # Services
            ev_tid = fms[form_id] if form_id in fms else 'FSAM'
            services = get_services_data(request, ovc_cpims_id, ev_tid)
            results["services"] = services
        else:
            results["message"] = "No permission to access OVC by IP/LIP"
    except Exception:
        return {"message": "Error occured"}
    else:
        return results


def get_services_data(request, ovc_cpims_id, event_type_id='FSAM'):
    """ method to get services."""
    try:
        services = []
        check_fields = ['olmis_education_service_id', 'olmis_pss_service_id',
                        'olmis_hes_service_id', 'olmis_health_service_id',
                        'olmis_protection_service_id', 'form1b_items']
        vals = get_dict(field_name=check_fields)
        start_date = get_start_date()
        person_id = ovc_cpims_id
        if event_type_id == 'FM1B':
            person = OVCRegistration.objects.filter(
                person_id=person_id, is_void=False)
            person_id = person[0].caretaker_id
        ovc_care_events = OVCCareEvents.objects.filter(
            person_id=person_id, date_of_event__gte=start_date,
            event_type_id=event_type_id,
            is_void=False).order_by('-date_of_event')
        print('EVENT', event_type_id, start_date)
        # Form 1A
        if event_type_id == 'FSAM':
            for ovc_event in ovc_care_events:
                event_id = ovc_event.pk
                service_date = ovc_event.date_of_event
                ovccare_services = OVCCareServices.objects.filter(
                    event_id=event_id, is_void=False)
                for ovccare_service in ovccare_services:
                    service_code = ovccare_service.service_provided
                    service_name = get_vals(service_code, vals)
                    servs = {'date': service_date, 'code': service_code,
                             'name': service_name}
                    services.append(servs)
        elif event_type_id == 'FM1B':
            for ovc_event in ovc_care_events:
                event_id = ovc_event.pk
                service_date = ovc_event.date_of_event
                events = OVCCareF1B.objects.filter(
                    event_id=event_id, is_void=False)
                for ovc_event in events:
                    print('Form 1B EV', ovc_event)
                    service_code = ovc_event.entity
                    service_name = get_vals(service_code, vals)
                    servs = {'date': service_date, 'code': service_code,
                             'name': service_name}
                    services.append(servs)
        elif event_type_id == 'CPAR':
            services = []
        elif event_type_id == 'cpr':
            services = []
    except Exception:
        return []
    else:
        return services


def get_start_date():
    """Method to get start date."""
    try:
        today = datetime.now()
        year = today.strftime('%Y')
        month = today.strftime('%m')
        yr_padd = 1
        if int(month) < 9:
            yr_padd = 2
        year = int(year) - yr_padd
        start_date = '%s-09-01' % (year)
    except Exception:
        return '1900-01-01'
    else:
        return start_date


def get_caseload(request, allow_exit=1):
    """Method to get caseload."""
    try:
        results = []
        eligibility = []
        org_unit_id = request.query_params.get('org_unit_id')
        chv_cpims_id = request.query_params.get('chv_cpims_id')
        is_active = request.query_params.get('active')
        if not allow_exit:
            is_active = 'TRUE'
        ovcs = OVCRegistration.objects.filter(
            is_void=False, caretaker_id__isnull=False)
        if chv_cpims_id:
            ovcs = ovcs.filter(child_chv_id=chv_cpims_id)
        if is_active:
            active = True if is_active.upper() == 'TRUE' else False
            ovcs = ovcs.filter(is_active=active)
        if org_unit_id:
            ou_ids = [org_unit_id]
        else:
            ous = get_attached_orgs(request)
            ou_ids = ous['attached_ou'] if 'attached_ou' in ous else []
        print('OU IDS', ou_ids)
        ovcs = ovcs.filter(child_cbo_id__in=ou_ids)[:10000]
        print('F RES', ovcs)
        check_fields = ['sex_id', 'hiv_status_id', 'exit_reason_id',
                        'immunization_status_id']
        vals = get_dict(field_name=check_fields)
        print('API ous', ous, ovcs)
        for ovc in ovcs:
            ovc_id = ovc.person_id
            dob = str(ovc.person.date_of_birth)
            reg_date = str(ovc.registration_date)
            onames = ovc.person.other_names
            cg_onames = ovc.caretaker.other_names
            ovc_sex = get_vals(ovc.person.sex_id, vals)
            hiv_status = get_vals(ovc.hiv_status, vals)
            art_status = get_vals(ovc.art_status, vals)
            #
            imm_status = ovc.immunization_status
            immunization_status = get_vals(
                imm_status, vals) if imm_status != 'None' else None
            # Exit
            exit_status = 'ACTIVE' if ovc.is_active else 'EXITED'
            exit_date = ovc.exit_date
            exit_reason = get_vals(ovc.exit_reason, vals)
            name = '%s %s%s' % (ovc.person.first_name,
                                ovc.person.surname,
                                ' %s' % onames if onames else '')
            cg_name = '%s %s%s' % (ovc.caretaker.first_name,
                                   ovc.caretaker.surname,
                                   ' %s' % cg_onames if cg_onames else '')
            child = {"cbo_id": ovc.child_cbo_id,
                     "cbo": ovc.child_cbo.org_unit_name,
                     "ovc_cpims_id": ovc_id, "ovc_names": name,
                     "ovc_first_name": ovc.person.first_name,
                     "ovc_surname": ovc.person.surname,
                     "ovc_other_names": onames, "ovc_names": name,
                     "age": ovc.person.years,
                     "sex": ovc_sex, "ovchivstatus": hiv_status,
                     "artstatus": art_status, "date_of_birth": dob,
                     "caregiver_cpims_id": ovc.caretaker_id,
                     "caregiver_names": cg_name,
                     "caregiver_first_name": ovc.caretaker.first_name,
                     "caregiver_surname": ovc.caretaker.surname,
                     "caregiver_other_names": cg_onames,
                     "chv_cpims_id": ovc.child_chv_id,
                     'registration_date': reg_date,
                     "eligibility": eligibility,
                     "immunization": immunization_status,
                     "exit_status": exit_status, "exit_date": exit_date,
                     "exit_reason": exit_reason
                     }
            if ovc.hiv_status in ['HSTP', 'HHEI']:
                ovc_health = OVCHealth.objects.filter(
                    person_id=ovc_id, is_void=False)
                if ovc_health:
                    for health in ovc_health:
                        facility_name = health.facility.facility_name
                        child['ccc_number'] = health.ccc_number
                        child['date_of_linkage'] = health.date_linked
                        child['facility_name'] = facility_name
            results.append(child)
    except Exception as e:
        print('Error getting case load - %s' % str(e))
        return []
    else:
        return results


def access_manager(request):
    """Method to handle access management."""
    try:
        status = 9
        device = None
        device_id = request.query_params.get('deviceID')
        user_id = request.user.id
        user_devices = DeviceManagement.objects.filter(
            user_id=user_id, is_void=False)
        if user_devices:
            if user_devices.count() > 1:
                status = 5
            else:
                device = user_devices.first()
                if device.is_blocked:
                    status = 4
                elif device.is_active:
                    status = 1
                    if device.device_id != device_id:
                        status = 3
                else:
                    status = 2
        if status == 9 and device_id:
            reg_devices = DeviceManagement.objects.filter(
                device_id=device_id, is_void=False)
            if reg_devices:
                status = 6
            else:
                device, created = DeviceManagement.objects.get_or_create(
                    device_id=device_id, user_id=user_id,
                    defaults={'is_blocked': False, 'is_void': False})
                if created:
                    print('New Device added %s' % str(device_id))
                else:
                    print('Device Blocked', 'Void', device_id)
    except Exception as e:
        print('Error mapping device and user %s' % (str(e)))
        return None, 0
    else:
        return device, status
