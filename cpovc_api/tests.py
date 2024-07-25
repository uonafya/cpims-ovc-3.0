import requests
# from django.test import TestCase

# base_url = 'http://127.0.0.1:8005/api'
base_url = 'https://dev.cpims.net/api'

# url = 'https://dev.cpims.net/api/token/'
# headers = {'Authorization': 'Token %s' % token}

url = base_url + '/token/'
payload = {'username': 'nmugaya', 'password': '1P@ss2022'}
# payload = {'username': 'testuser', 'password': 'T3st4321'}
response = requests.post(url, json=payload)
# print(response.text)
resp = response.json()
# print(resp)

cpims_id = 4182489
# 4041779

token = resp['access']
headers = {'Authorization': 'Bearer %s' % token}

# url = base_url + '/caseload/'
url = base_url + '/form/CPR/'


payload = {'ovc_cpims_id': cpims_id, 'date_of_event': '2023-06-28',
           'questions': [{'question_code': 'CP28q', 'answer_id': 'AYES'}],
           'scores': [{'b1': 1, 'b2': 1, 'b3': 1, 'b4': 1, 'b5': 1,
                       'b6': 1, 'b7': 0, 'b8': 0, 'b9': 0}]}
'''
payload = {'ovc_cpims_id': cpims_id, 'date_of_event': '2023-06-13',
           'questions': [{'domain_id': 'DHNU', 'service_id': 'CP11HEGs'}]}

payload = {'ovc_cpims_id': cpims_id, 'date_of_event': '2023-06-13',
           'services': [{'domain_id': 'DEDU',
                         'service_id': ['CPTS2e', 'CP96SC'],
                         'goal_id': 'CPTG1sc', 'gap_id': 'CPTG6e',
                         'priority_id': 'CPTG5p',
                         'responsible_id': ['CGH', 'NGO'],
                         'results_id': '', 'reason_id': '',
                         'completion_date': '2023-07-13'}]}

payload = {'field_name': 'olmis_domain_id'}
payload = {'ovc_cpims_id': cpims_id}
'''

payload = {'ovc_cpims_id': cpims_id, 'date_of_event': '2023-09-04',
           'questions': [{'question_code': 'CP3d', 'answer_id': 'ANNO'},
                         {'question_code': 'CP4d', 'answer_id': 'ANNO'},
                         {'question_code': 'CP5d', 'answer_id': 'ANNO'},
                         {'question_code': 'CP1q', 'answer_id': 'AYES'},
                         {'question_code': 'CP2q', 'answer_id': 'ANNA'},
                         {'question_code': 'CP3q', 'answer_id': 'ANNA'},
                         {'question_code': 'CP5q', 'answer_id': 'AYES'},
                         {'question_code': 'CP6q', 'answer_id': 'ANNA'},
                         {'question_code': 'CP7q', 'answer_id': 'ANNA'},
                         {'question_code': 'CP8q', 'answer_id': 'ANNA'},
                         {'question_code': 'CP9q', 'answer_id': 'ANNA'},
                         {'question_code': 'CP10q', 'answer_id': 'ANNA'},
                         {'question_code': 'CP11q', 'answer_id': 'ANNA'},
                         {'question_code': 'CP12q', 'answer_id': 'AYES'},
                         {'question_code': 'CP13q', 'answer_id': 'AYES'},
                         {'question_code': 'CP14q', 'answer_id': 'AYES'},
                         {'question_code': 'CP15q', 'answer_id': 'ANNA'},
                         {'question_code': 'CP16q', 'answer_id': 'ANNA'},
                         {'question_code': 'CP17q', 'answer_id': 'ANNA'},
                         {'question_code': 'CP18q', 'answer_id': 'AYES'},
                         {'question_code': 'CP19q', 'answer_id': 'AYES'},
                         {'question_code': 'CP20q', 'answer_id': 'AYES'},
                         {'question_code': 'CP21q', 'answer_id': 'AYES'},
                         {'question_code': 'CP22q', 'answer_id': 'AYES'},
                         {'question_code': 'CP23q', 'answer_id': 'AYES'},
                         {'question_code': 'CP24q', 'answer_id': 'AYES'},
                         {'question_code': 'CP25q', 'answer_id': 'ANNO'},
                         {'question_code': 'CP26q', 'answer_id': 'ANNO'},
                         {'question_code': 'CP27q', 'answer_id': 'ANNA'},
                         {'question_code': 'CP28q', 'answer_id': 'ANNA'},
                         {'question_code': 'CP29q', 'answer_id': 'ANNA'},
                         {'question_code': 'CP30q', 'answer_id': 'AYES'},
                         {'question_code': 'CP31q', 'answer_id': 'AYES'},
                         {'question_code': 'CP32q', 'answer_id': 'ANNO'},
                         {'question_code': 'CP33q', 'answer_id': 'ANNA'},
                         {'question_code': 'CP34q', 'answer_id': 'ANNA'},
                         {'question_code': 'CP35q', 'answer_id': 'ANNA'},
                         {'question_code': 'CP36q', 'answer_id': 'ANNA'},
                         {'question_code': 'CP1b', 'answer_id': 'AYES'},
                         {'question_code': 'CP2b', 'answer_id': 'AYES'},
                         {'question_code': 'CP3b', 'answer_id': 'AYES'},
                         {'question_code': 'CP4b', 'answer_id': 'AYES'},
                         {'question_code': 'CP5b', 'answer_id': 'AYES'},
                         {'question_code': 'CP6b', 'answer_id': 'AYES'},
                         {'question_code': 'CP7b', 'answer_id': 'AYES'},
                         {'question_code': 'CP8b', 'answer_id': 'ANNO'},
                         {'question_code': 'CP9b', 'answer_id': 'AYES'}],
           'individual_questions': [], 'scores': [{'b1': 1, 'b2': 1, 'b3': 1,
                                                   'b4': 1, 'b5': 1, 'b6': 1,
                                                   'b7': 1, 'b8': 0, 'b9': 1}]}


payload = {'ovc_cpims_id': cpims_id, 'date_of_event': '2023-09-04',
           'individual_questions': [],
           'questions': [{'question_code': 'CP3d', 'answer_id': 'ANNO'},
                         {'question_code': 'CP4d', 'answer_id': 'ANNO'},
                         {'question_code': 'CP5d', 'answer_id': 'ANNO'},
                         {'question_code': 'CP1q', 'answer_id': 'AYES'},
                         {'question_code': 'CP2q', 'answer_id': 'AYES'},
                         {'question_code': 'CP3q', 'answer_id': 'ANNA'},
                         {'question_code': 'CP5q', 'answer_id': 'AYES'},
                         {'question_code': 'CP6q', 'answer_id': 'ANNA'},
                         {'question_code': 'CP7q', 'answer_id': 'ANNA'},
                         {'question_code': 'CP8q', 'answer_id': 'ANNA'},
                         {'question_code': 'CP9q', 'answer_id': 'AYES'},
                         {'question_code': 'CP10q', 'answer_id': 'AYES'},
                         {'question_code': 'CP11q', 'answer_id': 'AYES'},
                         {'question_code': 'CP12q', 'answer_id': 'AYES'},
                         {'question_code': 'CP13q', 'answer_id': 'AYES'},
                         {'question_code': 'CP14q', 'answer_id': 'AYES'},
                         {'question_code': 'CP15q', 'answer_id': 'AYES'},
                         {'question_code': 'CP16q', 'answer_id': 'AYES'},
                         {'question_code': 'CP17q', 'answer_id': 'AYES'},
                         {'question_code': 'CP18q', 'answer_id': 'ANNA'},
                         {'question_code': 'CP19q', 'answer_id': 'ANNA'},
                         {'question_code': 'CP20q', 'answer_id': 'ANNA'},
                         {'question_code': 'CP21q', 'answer_id': 'ANNA'},
                         {'question_code': 'CP22q', 'answer_id': 'ANNO'},
                         {'question_code': 'CP23q', 'answer_id': 'AYES'},
                         {'question_code': 'CP24q', 'answer_id': 'AYES'},
                         {'question_code': 'CP25q', 'answer_id': 'ANNO'},
                         {'question_code': 'CP26q', 'answer_id': 'ANNO'},
                         {'question_code': 'CP27q', 'answer_id': 'ANNO'},
                         {'question_code': 'CP28q', 'answer_id': 'ANNA'},
                         {'question_code': 'CP29q', 'answer_id': 'ANNA'},
                         {'question_code': 'CP30q', 'answer_id': 'AYES'},
                         {'question_code': 'CP31q', 'answer_id': 'AYES'},
                         {'question_code': 'CP32q', 'answer_id': 'ANNO'},
                         {'question_code': 'CP33q', 'answer_id': 'AYES'},
                         {'question_code': 'CP34q', 'answer_id': 'ANNO'},
                         {'question_code': 'CP35q', 'answer_id': 'AYES'},
                         {'question_code': 'CP36q', 'answer_id': 'AYES'},
                         {'question_code': 'CP1b', 'answer_id': 1},
                         {'question_code': 'CP2b', 'answer_id': 1},
                         {'question_code': 'CP3b', 'answer_id': 1},
                         {'question_code': 'CP4b', 'answer_id': 1},
                         {'question_code': 'CP5b', 'answer_id': 0},
                         {'question_code': 'CP6b', 'answer_id': 1},
                         {'question_code': 'CP7b', 'answer_id': 1},
                         {'question_code': 'CP8b', 'answer_id': 0},
                         {'question_code': 'CP9b', 'answer_id': 0}],
           'scores': [{'b1': 1, 'b2': 1, 'b3': 1, 'b4': 1,
                       'b5': 0, 'b6': 1, 'b7': 1, 'b8': 0, 'b9': 0}]
           }


response = requests.post(url, json=payload, headers=headers)
# response = requests.get(url, params=payload, headers=headers)

# print(response.headers)
# print(response.text)


print(response.json())
# print(len(response.json()))

# print(payload)
