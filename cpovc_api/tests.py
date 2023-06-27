import requests
# from django.test import TestCase

base_url = 'http://127.0.0.1:8005/api'
# base_url = 'https://dev.cpims.net/api'

# url = 'https://dev.cpims.net/api/token/'
# headers = {'Authorization': 'Token %s' % token}

url = base_url + '/token/'
payload = {'username': 'nmugaya', 'password': '1P@ss2022'}
# payload = {'username': 'testuser', 'password': 'T3st4321'}
response = requests.post(url, json=payload)
resp = response.json()

cpims_id = 4041779

token = resp['access']
headers = {'Authorization': 'Bearer %s' % token}

# url = base_url + '/settings/'
url = base_url + '/form/CPT/'

payload = {'ovc_cpims_id': cpims_id, 'date_of_event': '2023-06-13',
           'services': [{'domain_id': 'DHNU', 'service_id': 'CP11HEGs'}]}

payload = {'ovc_cpims_id': cpims_id, 'date_of_event': '2023-06-13',
           'services': [{'domain_id': 'DEDU',
                         'service_id': ['CPTS2e', 'CP96SC'],
                         'goal_id': 'CPTG1sc', 'gap_id': 'CPTG6e',
                         'priority_id': 'CPTG5p',
                         'responsible_id': ['CGH', 'NGO'],
                         'results_id': '', 'reason_id': '',
                         'completion_date': '2023-07-13'}]}

'''
payload = {'field_name': 'olmis_health_service_id'}
'''

response = requests.post(url, json=payload, headers=headers)
# response = requests.get(url, params=payload, headers=headers)

# print(response.headers)
# print(response.text)
print(response.json())
