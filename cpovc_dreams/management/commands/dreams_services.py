from django.core.management.base import BaseCommand, CommandError
from cpovc_registry.models import RegPersonsExternalIds
from cpovc_dreams.models import DREAMSServices
from cpovc_ovc.models import OVCRegistration
from cpovc_dreams.get_dreams_services import get_dreams


class Command(BaseCommand):
    help = "Get DREAMS services"


    def handle(self, *args, **options):
        '''Command to handle services.'''
        try:
            ovc_dict = {}
            dreams_never_list = []
            dreams_current_list = []
            dreams = RegPersonsExternalIds.objects.filter(
                identifier_type_id='IDRM', is_void=False)
            person_ids = dreams.values_list('person_id', flat=True)
            dreams_ids = dreams.values_list('identifier', flat=True)
            ovc_ids = OVCRegistration.objects.filter(person_id__in=person_ids)
            for ovc in ovc_ids:
                ovc_dict[ovc.person_id] = ovc.child_cbo_id
            # Discount if has 1 months old updates
            dids = DREAMSServices.objects.filter(dreams_id__in=dreams_ids)
            dreams_ignore_list = dids.filter(
                intervention_date__gte='2024-05-01').distinct(
                'dreams_id').values_list('dreams_id', flat=True)
            dids_never = dids.distinct('dreams_id').values_list('dreams_id', flat=True)
            for did in dreams_ids:
                if did not in dids_never:
                    dreams_never_list.append(did)
            for n_list in dreams_never_list:
                if n_list not in dreams_ignore_list:
                    dreams_current_list.append(n_list) 
        except Exception as e:
            raise CommandError('Error getting services - "%s"' % str(e))

        for dream in dreams:
            dreams_id = dream.identifier
            person_id = dream.person_id
            cbo_id = ovc_dict[person_id] if person_id in ovc_dict else None
            if dreams_id not in dreams_current_list:
                print('DREAMS Ignore for %s %s' % (dreams_id, person_id))
            else:
                dreams_services = get_dreams(dreams_id)
                print('DREAMS Update for %s %s' % (dreams_id, person_id))
                for dservice in dreams_services:
                    dob = dservice['date_of_birth']
                    bcert_no = dservice['birth_certificate_no']
                    county = dservice['county_of_residence']
                    sub_county = dservice['sub_county']
                    ward = dservice['ward']
                    # Split geo locations
                    county_code = county['iebc_code']
                    county_name = county['name']
                    sub_county_code = sub_county['iebc_code']
                    sub_county_name = sub_county['name']
                    ward_code = ward['iebc_code']
                    ward_name = ward['name']
                    services = dservice['services']
                    for service in services:
                        intv_date = service['intervention_date']
                        intv_code = service['intervention_type']['code']
                        intv_name = service['intervention_type']['name']
                        hts_result = service['hts_result'] if service['hts_result'] else ''
                        sessions = service['no_of_sessions_attended']
                        no_sessions = sessions if sessions else None
                        preg_tests = service['pregnancy_test_result']
                        preg_test = preg_tests if preg_tests else ''
                        DREAMSServices.objects.update_or_create(
                            dreams_id=dreams_id, intervention_date=intv_date,
                            intervention_type_code=intv_code,
                            defaults={'person_id': person_id, 'date_of_birth': dob,
                                      'birth_certificate_no': bcert_no,
                                      'county_code': county_code, 'county_name': county_name,
                                      'sub_county_code': sub_county_code,
                                      'sub_county_name': sub_county_name,
                                      'ward_code': ward_code, 'ward_name': ward_name,
                                      'intervention_type_name': intv_name,
                                      'hts_result': hts_result, 'org_unit_id': cbo_id,
                                      'no_of_sessions_attended': no_sessions,
                                      'pregnancy_test_result': preg_test,
                                      'is_void': False})
        self.stdout.write(
            self.style.SUCCESS('Successfully synced services')
        )