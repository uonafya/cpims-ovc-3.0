from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.views import APIView

from cpovc_ovc.models import OVCRegistration, OVCHealth
from cpovc_registry.models import RegPersonsGeo, RegPersonsExternalIds

from cpovc_main.models import SetupList
from .functions import (
    dcs_dashboard, ovc_dashboard, get_attached_orgs, save_form,
    validate_ovc, get_ovc_data, get_services_data, get_caseload,
    access_manager, handle_notification)

from cpovc_dashboard.parameters import PARAMS
from .params import SID, SIDS, META_IDS, STATUSES


class APIRoot(APIView):

    """
    This page serves as the entry point to the entire API for
    Child Protection Information Management System (CPIMS).

    # Exploring the API
    There are two ways to explore this API:

     * the [Swagger](http://swagger.io/)
     [**sandbox** ( click here )](/api/docs/swagger/#!/api)

     * the [browsable API ( click here )](/api/docs/redoc/)

    # Authentication

    Anonymous users have **read only** access to *most* ( not all ) views.
    If you want to try out the `POST`, `PUT`, `PATCH` and `DELETE` actions,
    you will need to log in using three provided methods. Username/password 
    (Session), JSON Web Token (JWT) or Basic Token.

    For the experimental sandbox, you can get suitable credentials from
    [the documentation](https://cpims-docs.readthedocs.io/en/latest/). For a live
    instance, you need to request for access from the Directorate of 
    Children Services (DCS).
    """
    def get_view_name(self):
        return "CPIMS API - Home"

    def get(self, request, format=None):
        return Response()


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


@api_view(['POST'])
def token_validate(request):
    """ Method for home."""
    try:
        print('User', request.user.id)
        device, status_code = access_manager(request, 'POST')
        message = STATUSES[status_code] if status_code in STATUSES else 'Error'
        response = {"message": message}
        if status_code == 0:
            http_status = status.HTTP_200_OK
        else:
            http_status = 250 + status_code
    except Exception:
        response = {"message": "Error or Method NOT Allowed"}
        return Response(response, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(response, status=http_status)


@api_view(['GET', 'POST'])
def dashboard(request):
    """Method to handle Dashboards."""
    try:
        user_orgs = get_attached_orgs(request)
        print('User orgs', user_orgs)
        reg_ovc = user_orgs['reg_ovc'] if 'reg_ovc' in user_orgs else False
        if reg_ovc:
            results = ovc_dashboard(request, user_orgs)
        else:
            results = dcs_dashboard(request, user_orgs)
        results['org_unit'] = user_orgs['ou_name']
        results['org_unit_id'] = user_orgs['ou_id']
        msg = 'Partner details Found'
        if request.method == 'GET':
            user_id = request.query_params.get('user_id')
            print(user_id)
        results['details'] = msg
        print(results)
    except Exception as e:
        msg = 'Error getting Partner details - %s' % (str(e))
        return Response({'details': msg})
    else:
        return Response(results)


@api_view(['GET', 'POST'])
def caseload(request):
    """Method to handle Caseload."""
    try:
        print('TRACK_Caseload', request.META)
        results = []
        msg = 'Partner OVC details Found'
        device, status_code = access_manager(request)
        print('Device Status', status_code, device)
        # Override for testing to be removed in Production
        status_code = 0
        if status_code == 0:
            http_status = status.HTTP_200_OK
        else:
            http_status = 250 + status_code
            handle_notification(request, status_code)
        if request.method == 'GET':
            if status_code < 4:
                results = get_caseload(request, 0)
            else:
                results = []
        elif request.method == 'POST':
            print('POST method to update some OVC data')
        # results['details'] = msg
    except Exception as e:
        msg = 'Error getting Partner details - %s' % (str(e))
        print(msg)
        return Response([], status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(results, status=http_status)


@api_view(['GET', 'POST'])
def metadata(request):
    try:
        qs = SetupList.objects.filter(
            field_name__in=META_IDS, is_void=False)
        results = qs.values(
            "field_name", "item_id", "item_description",
            "item_sub_category", "the_order")
    except Exception as e:
        print("error getting metadata - %s" % str(e))
        return Response([])
    else:
        return Response(results)


@api_view(['GET', 'POST'])
def registration(request):
    try:
        results = get_caseload(request, 0)
        return results
    except Exception as e:
        raise e


@api_view(['GET', 'POST'])
def settings(request):
    try:
        results = []
        field_name = request.query_params.get(
            'field_name', None)
        if field_name and field_name in SIDS:
            if field_name in SID:
                f_field = SID[field_name]
                f_name = f_field['id']
                f_filter = f_field['filter'] if 'filter' in f_field else None
            else:
                f_name = field_name
                f_filter = None
            results = SetupList.objects.filter(
                field_name=f_name, is_void=False)
            if f_filter:
                f_field, f_value = f_filter.split('__')
                results = results.filter(**{f_field: f_value})
            results = results.values(
                'item_id', 'item_description',
                'item_sub_category', 'the_order')
        else:
            results = []
            for fname in SID:
                fdname = SID[fname]['name']
                fds = {"id": fname, "name": fdname}
                results.append(fds)
    except Exception as e:
        print("Error settings - %s" % str(e))
        return Response([])
    else:
        return Response(results)


@api_view(['GET', 'POST'])
@renderer_classes([JSONRenderer])
def form_data(request, form_id):
    """Method to handle Forms ID."""
    try:
        print('TRACK_Caseload', request.META)
        results = {}
        if request.method == 'GET':
            msg = 'OVC Form details Found'
            ovc_cpims_id = request.query_params.get('ovc_cpims_id')
            results = get_ovc_data(request, ovc_cpims_id, form_id)
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
                services = get_services_data(request, ovc_id, 'FSAM')
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


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def form_unapproved(request):
    """Method to handle Forms ID."""
    try:
        results = []
    except Exception as e:
        msg = "Error getting Partner details - %s" % (str(e))
        print(msg)
        return Response([])
    else:
        return Response(results)
