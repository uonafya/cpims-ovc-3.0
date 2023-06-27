from datetime import datetime
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from cpovc_ovc.models import OVCRegistration, OVCHealth
from cpovc_registry.models import RegPersonsGeo, RegPersonsExternalIds
from cpovc_forms.models import OVCCareEvents, OVCCareServices

from cpovc_main.functions import get_dict
from cpovc_main.models import SetupList
from .functions import (
    dcs_dashboard, get_attached_orgs, get_vals, save_form, validate_ovc)

from cpovc_dashboard.parameters import PARAMS


def api_home(request):
    """ Method for home."""
    try:
        Response = {"status": 0, "message": "Method NOT Allowed"}
        return JsonResponse(
            Response, content_type='application/json', safe=False)
    except Exception as e:
        raise e
    else:
        pass


@api_view(['GET', 'POST'])
def dashboard(request):
    """Method to handle DREAMS."""
    try:
        user_orgs = get_attached_orgs(request)
        print(user_orgs)
        results = dcs_dashboard(request, user_orgs)
        results['org_unit'] = user_orgs['ou_name']
        results['org_unit_id'] = user_orgs['ou_id']
        '''
        results = {"active": 132294, "ever_registered": 307005,
                   "caregivers": 171142, "workforce": 487,
                   "other_org_units": 36, "households": 154,
                   "org_unit": "USAID 4TheChild", "org_unit_id": 7226}
        '''
        msg = 'Partner details Found'
        if request.method == 'GET':
            user_id = request.query_params.get('user_id')
            print(user_id)
        results['details'] = msg
    except Exception as e:
        msg = 'Error getting Partner details - %s' % (str(e))
        return Response({'details': msg})
    else:
        return Response(results)


'''
cbo_id
cbo
ward_id
ward
consituency_id
constituency
countyid
county

cpims_ovc_id
ovc_names
gender
dob
date_of_birth
age
age_at_reg
agerange
birthcert
bcertnumber
ovcdisability
ncpwdnumber

ovchivstatus
artstatus

facility_id
facility
facility_mfl_code
date_of_linkage
ccc_number
duration_on_art
viral_load
date_of_event
suppression

chv_id
chv_names

caregiver_id
caregiver_names
caregiver_dob
caregiver_age
phone
caregiver_relation
caregiver_gender
caregiver_nationalid
caregiverhivstatus
household
caregiver_type

father_alive
mother_alive

schoollevel
school_id
school_name
class

registration_date
duration_in_program
immunization
eligibility

exit_status
exit_date
exit_reason
'''


@api_view(['GET', 'POST'])
def caseload(request):
    """Method to handle DREAMS."""
    try:
        results = []
        eligibity = []
        ovcs = OVCRegistration.objects.filter(is_void=False)[:200]
        check_fields = ['sex_id', 'hiv_status_id', 'exit_reason_id',
                        'immunization_status_id']
        vals = get_dict(field_name=check_fields)
        for ovc in ovcs:
            ovc_id = ovc.person_id
            dob = str(ovc.person.date_of_birth)
            reg_date = str(ovc.registration_date)
            onames = ovc.person.other_names
            ovc_sex = get_vals(ovc.person.sex_id, vals)
            hiv_status = get_vals(ovc.hiv_status, vals)
            art_status = get_vals(ovc.art_status, vals)
            #
            imm_status = ovc.immunization_status
            immunization_status = get_vals(
                imm_status, vals) if imm_status != 'None' else None
            # Exit
            exit_status = 'ACTIVE' if ovc.is_active else 'EXITED'
            exit_date = str(ovc.exit_date) if ovc.exit_date else ovc.exit_date
            exit_reason = get_vals(ovc.exit_reason, vals)
            name = '%s %s%s' % (ovc.person.first_name,
                                ovc.person.surname,
                                ' %s' % onames if onames else '')
            child = {"cbo_id": ovc.child_cbo_id,
                     "cbo": ovc.child_cbo.org_unit_name,
                     "cpims_ovc_id": ovc_id, "ovc_names": name,
                     "sex": ovc_sex, "ovchivstatus": hiv_status,
                     "artstatus": art_status, "eligibility": eligibity,
                     "date_of_birth": dob, 'registration_date': reg_date,
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
        msg = 'Partner OVC details Found'
        if request.method == 'GET':
            org_unit_id = request.query_params.get('org_unit_id')
            print(org_unit_id)
        # results['details'] = msg
    except Exception as e:
        msg = 'Error getting Partner details - %s' % (str(e))
        print(msg)
        return Response([])
    else:
        return Response(results)


@api_view(['GET', 'POST'])
def registration(request):
    try:
        return caseload(request)
    except Exception as e:
        raise e


@api_view(['GET', 'POST'])
def settings(request):
    try:
        results = []
        field_name = request.query_params.get(
            'field_name', 'case_category_id')
        if field_name is not None:
            results = SetupList.objects.filter(
                field_name=field_name, is_void=False).values(
                'item_id', 'item_description',
                'item_sub_category', 'the_order')
    except Exception:
        return Response([])
    else:
        return Response(results)


@api_view(['GET', 'POST'])
def form_data(request, form_id):
    """Method to handle Forms ID."""
    try:
        results = {}
        if request.method == 'GET':
            msg = 'OVC Form details Found'
            ovc_cpims_id = request.query_params.get('ovc_cpims_id')
            results = {"cpims_id": ovc_cpims_id, "name": "Test child",
                       "date_of_birth": "2020-01-01"}
        elif request.method == 'POST':
            person_id = request.data.get('ovc_cpims_id')
            event_date = request.data.get('date_of_event')
            services = request.data.get('services')
            print('ALL Data', person_id, event_date, form_id, request.data)
            ovc_access = validate_ovc(request, person_id)
            if ovc_access:
                msg = save_form(
                    request, person_id, event_date, form_id, services)
            else:
                msg = "You do not have access to this OVC by IP / LIP"
        results['details'] = msg
    except Exception as e:
        msg = 'Error getting Partner details - %s' % (str(e))
        return Response([])
    else:
        return Response(results)


@api_view(['GET', 'POST'])
def dreams(request):
    """DREAMS Query endpoints."""
    try:
        results = {}
        check_fields = ['olmis_education_service_id', 'olmis_pss_service_id',
                        'olmis_hes_service_id', 'olmis_health_service_id',
                        'olmis_protection_service_id']
        if request.method == 'GET':
            ovc_id = request.query_params.get('cpims_id')
            dreams_id = request.query_params.get('dreams_id')
            nupi_no = request.query_params.get('nupi_no')
            nemis_no = request.query_params.get('nemis_no')
            bcert_no = request.query_params.get('birth_cert_no')
            bnoti_no = request.query_params.get('birth_notification_no')
            print('ID', ovc_id)
            qs = None
            if ovc_id:
                qtype = 'CPIMS ID'
                qs = OVCRegistration.objects.filter(
                    person_id=ovc_id, is_void=False)
            elif dreams_id:
                qtype = 'DREAMS ID'
                ext_ids = RegPersonsExternalIds.objects.filter(
                    identifier_type_id='ISOV', identifier=dreams_id,
                    is_void=False).first()
                qs = OVCRegistration.objects.filter(
                    person_id=ext_ids.person_id, is_void=False)
            elif nupi_no:
                qtype = 'NUPI Number'
            elif nemis_no:
                qtype = 'NEMIS Number'
            elif bcert_no:
                qtype = 'Birth Certificate Number'
            elif bnoti_no:
                qtype = 'Birth Notification Number'
            else:
                qtype = 'Query not Implemented'
            if qs:
                queryset = qs[0]
                if queryset.hiv_status in ['HSTP', 'HHEI']:
                    health = OVCHealth.objects.get(
                        person_id=ovc_id, is_void=False)
                    if health:
                        facility_name = health.facility.facility_name
                        results['ccc_number'] = health.ccc_number
                        results['date_of_linkage'] = health.date_linked
                        results['facility_name'] = facility_name
                # Primary information
                results['date_of_birth'] = queryset.person.date_of_birth
                results['ovc_enrollment_date'] = queryset.registration_date
                # Other identifiers
                results['nemis_no'] = None
                results['nupi_no'] = None
                # Geo locations
                geos = RegPersonsGeo.objects.filter(
                    person_id=ovc_id, is_void=False)
                ward_id, ward_name = None, None
                const_id, const_name = None, None
                county_id, county_name = None, None
                for geo in geos:
                    if geo.area.area_type_id == 'GWRD':
                        ward_id = geo.area.area_code
                        ward_name = geo.area.area_name
                    if geo.area.area_type_id == 'GDIS':
                        const_id = geo.area.area_code
                        const_name = geo.area.area_name
                        county_id = geo.area.parent_area_id
                if county_id:
                    county_id = str(county_id).zfill(3)
                    county_name = PARAMS[county_id]
                results['county'] = {'code': county_id, 'name': county_name}
                results['constituency'] = {'code': const_id,
                                           'name': const_name}
                results['ward'] = {'code': ward_id, 'name': ward_name}
                # Services
                today = datetime.now()
                year = today.strftime('%Y')
                month = today.strftime('%m')
                yr_padd = 1
                if int(month) < 9:
                    yr_padd = 2
                year = int(year) - yr_padd
                start_date = '%s-09-01' % (year)
                # print(year, month, start_date)
                services = []
                vals = get_dict(field_name=check_fields)
                ovc_care_events = OVCCareEvents.objects.filter(
                    person_id=ovc_id, date_of_event__gte=start_date,
                    event_type_id='FSAM',
                    is_void=False).order_by('-date_of_event')
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
                results['services'] = services
                msg = 'OVC details for DREAMS found using %s' % (qtype)
            else:
                msg = 'OVC details for DREAMS Not found using %s' % (qtype)
        else:
            msg = 'Method not Implemented'
        results['details'] = msg
    except Exception as e:
        msg = 'Error getting OVC details for DREAMS - %s' % (str(e))
        return Response({'details': msg})
    else:
        return Response(results)
