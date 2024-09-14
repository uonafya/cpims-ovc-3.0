import json
import requests

from django.conf import settings
from django.db import connection
from django.utils import timezone

from datetime import timedelta


from cpovc_ovc.models import (
    OVCRegistration, OVCViralload, OVCHealth, OVCVLTracker)


class UpdateVL(object):
    """Update ovc_viral_load"""

    def __init__(self):
        self.api_url_base = settings.NASCOP_BASE_URL
        self.login_url = settings.NASCOP_LOGIN_URL
        self.email = settings.NASCOP_USERNAME
        self.password = settings.NASCOP_PASSWORD
        self.api_results_url = settings.NASCOP_RESULTS_URL


    def generate_token(self):
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        credentials = {"email": self.email, "password": self.password}
        # print(credentials)
        response = requests.post(
            self.login_url, headers=headers, data=credentials)

        if response.status_code == 200:
            json_token = json.loads(response.content)
            # print(json.loads(response.content.decode('utf-8')))
            print('Login to EID/VL Successful')
            api_token = json_token.get('token')
            return api_token
        else:
            print(response)

    def get_viral_load(self, token, facility, patientID):
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        api_url = '{0}{1}/{2}'.format(self.api_results_url, facility, patientID)
        response = requests.get(api_url, headers=headers)
        status_code = response.status_code
        if response.status_code == 200:
            json_object = json.loads(response.content)
            data_list = []
            for test in json_object:
                patient = test.get('PatientID')
                date_tested = test.get('DateTested')
                result = test.get('Result')
                data = (patient, date_tested, result)
                data_list.append(data)
            return status_code, data_list
        elif response.status_code == 404:
            print('[!] [{0}] URL not found: [{1}]'.format(
                response.status_code, api_url))
            return status_code, None
        elif response.status_code == 401:
            print('[!] [{0}] Authentication Failed'.format(
                response.status_code), response.content)
            return status_code, None
        elif response.status_code == 400:
            print('[!] [{0}] Bad Request for PatientID: {1}'.format(
                response.status_code, patientID), response.content)
            return status_code, None
        elif response.status_code >= 300:
            print('[!] [{0}] Unexpected Redirect'.format(
                response.status_code), response.content)
            return status_code, None
        elif response.status_code >= 500:
            print('[!] [{0}] Server Error'.format(
                response.status_code), response.content)
            return status_code, None
        else:
            print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(
                response.status_code, response.content))
            return 500, None

    def vl_to_int(self, string):
        if not string:
            return int(-995)
        elif "< LDL" in string:
            return int(0)
        elif "INVALID" in string:
            return int(-998)
        elif "FAILED" in string:
            return int(-999)
        elif "COLLECT" in string:
            return int(-997)
        elif "TARGET" in string:
            return int(-994)
        elif not string.strip():
            return int(-996)
        else:
            return ''.join([i for i in string if i.isdigit()])

    def save_data(self):
        '''Get the data - Limit to 2000 at any run - limit cron to min hourly'''
        try:
            # timestamp_synced__isnull=True
            # eid_validated=True
            # person_id=3418769
            api_token = self.generate_token()
            time_threshold = timezone.now() - timedelta(days=7)
            vls = OVCVLTracker.objects.filter(
                timestamp_synced__lte=time_threshold,
                is_active=True, is_void=False).order_by('-person_id')[:2000]
            for vl in vls:
                ts = timezone.now()
                person_id = vl.person_id
                facility_code = vl.mfl_code
                ccc_number = vl.ccc_number.strip()
                if '-' in ccc_number:
                    ccc_number = ccc_number.replace('-', '')
                # Get the data
                facility_code_ccc = (facility_code, ccc_number)
                status_code, viral_load_records = self.get_viral_load(
                    api_token, facility_code, ccc_number)
                validated = False
                print('Person ID', person_id)
                # Exclude timestamp update when status code is credentials related
                if status_code == 401 or status_code > 500:
                    ts = None
                if viral_load_records:
                    validated = True
                    for record in viral_load_records:
                        date_tested = record[1]
                        result = record[2]
                        vl_result = result.upper() if result else result
                        result_to_int = self.vl_to_int(vl_result)
                        # check if record exists using date and result
                        if date_tested:
                            vlt, created = OVCViralload.objects.update_or_create(
                                person_id=person_id, viral_date=date_tested,
                                viral_load=result_to_int,
                                defaults={'is_void': 'False' })
                            # if a new record change source to integration
                            if created:
                                vlt.viral_source = 'DSSI'
                                vlt.save()
                print(person_id, ccc_number, validated, status_code, viral_load_records, ts)
                vl.timestamp_synced = ts
                vl.eid_validated = validated
                vl.save()
        except Exception as e:
            print('Error updating VL results - %s' % (str(e)))
            pass
        else:
            pass


    def update_tracker(self):
        """ UPdate VL tracking."""
        try:
            cnt = 0
            tracking = OVCVLTracker.objects.filter(is_void=False)
            track_actives = tracking.filter(is_active=False)
            track_active_list = track_actives.values_list('person_id', flat=True)
            vls = OVCHealth.objects.filter(is_void=False).exclude(
                person_id__in=track_active_list)
            active_list = vls.values_list('person_id', flat=True)
            non_actives = OVCRegistration.objects.filter(
                person_id__in=active_list, is_active=False)
            non_active_list = non_actives.values_list('person_id', flat=True)
            print('Updating full list', vls.count())
            print('Exited', non_actives.count())
            for vl in vls:
                cnt += 1
                if cnt % 1000 == 0:
                    print('Update VL', cnt)
                person_id = vl.person_id
                facility_id = vl.facility_id
                ccc_number = vl.ccc_number
                mfl_code = vl.facility.facility_code      
                vlt, created = OVCVLTracker.objects.update_or_create(
                    person_id=person_id, is_void=False,
                    defaults={'facility_id': facility_id,
                              'ccc_number': ccc_number,
                              'mfl_code': mfl_code })
                if created:
                    vlt.timestamp_synced = None
                    vlt.save()
            # Bulk update exited in Tracker
            update_tracking = tracking.filter(
                is_active=True, person_id__in=non_active_list).update(is_active=True)
            print('Records Updated', vls.count())
        except Exception as e:
            print('error exiting - %s' % (str(e)))
            raise e
        else:
            pass

