import requests
# from django.test import TestCase

base_url = 'http://127.0.0.1:8005/api'
# base_url = 'https://dev.cpims.net/api'
# base_url = 'https://dev.cpims.net/mobile'

# url = 'https://dev.cpims.net/api/token/'
# headers = {'Authorization': 'Token %s' % token}

url = base_url + '/token/'
payload = {'username': 'nmugaya', 'password': '1P@ss2022'}
# payload = {'username': 'testuser', 'password': 'T3st4321'}
response = requests.post(url, json=payload)
# print(response.text)
resp = response.json()
# print(resp)

cpims_id = 3696526
# 4041779

token = resp['access']
headers = {'Authorization': 'Bearer %s' % token}

# url = base_url + '/caseload/'
url = base_url + '/form/HMF/'


payload = {'ovc_cpims_id': cpims_id, 'HIV_RA_1A': '2023-11-06', 'HIV_RS_01': 'Yes',
           'HIV_RS_02': 'HIV_Positive', 'HIV_RS_03': '', 'HIV_RS_04': '',
           'HIV_RS_05': '', 'HIV_RS_06': '', 'HIV_RS_09': '', 'HIV_RS_06A': '',
           'HIV_RS_07': '', 'HIV_RS_08': '', 'HIV_RS_10': '',
           'HIV_RS_10A': '', 'HIV_RS_10B': '', 'HIV_RS_11': '',
           'HIV_RS_14': '', 'HIV_RS_15': '', 'HIV_RS_16': '', 'HIV_RS_17': '',
           'HIV_RS_18': '', 'eventID': '', 'HIV_RS_18A': 'A', 'HIV_RS_18B': '',
           'HIV_RS_21': '', 'HIV_RS_22': '', 'HIV_RS_23': '', 'HIV_RS_24': '', 'HIV_RA_3Q6': ''}

payload = {'ovc_cpims_id': cpims_id, 'HIV_MGMT_2_A': '2023-11-07', 
           'HIV_MGMT_1_A': '2023-11-07', 'HIV_MGMT_1_B': '2023-11-03', 'HIV_MGMT_1_C': '40',
           'HIV_MGMT_1_D': '2023-11-06', 'HIV_MGMT_1_E': 'AYES',
           'HIV_MGMT_1_E_DATE': '2023-11-06', '_HIV_MGMT_1_F': 'AYES',
           'HIV_MGMT_1_F_DATE': '2023-11-06', '_HIV_MGMT_1_G': 'AYES',
           'HIV_MGMT_1_G_DATE': '2023-11-04', 'HIV_MGMT_2_B': '3', 'HIV_MGMT_2_C': '180',
           'HIV_MGMT_2_D': '2023-11-02', 'HIV_MGMT_2_E': 'Good', 'HIV_MGMT_2_F': '20',
           'HIV_MGMT_2_G': 'TreatmentPreparation', 'HIV_MGMT_2_H_2': 'Biologicalparent',
           'HIV_MGMT_2_H_3': 'Male', 'HIV_MGMT_2_H_4': '50', 'HIV_MGMT_2_H_5': 'HIV_Positive',
           'HIV_MGMT_2_I_1': '60', 'HIV_MGMT_2_I_DATE': '2023-11-07',
           'HIV_MGMT_2_J': 'DirectObservedTherapy', 'HIV_MGMT_2_K': 'Not Done', 'HIV_MGMT_2_L_1': 'Red',
           'HIV_MGMT_2_L_2': '650', 'HIV_MGMT_2_M': ['TherapeuticFeeding', 'FoodSupport', 'ExclusiveBreastfeeding', 'InfantFeedingCounselling'],
           'HIV_MGMT_2_N': 'Active', '_HIV_MGMT_2_O_1': 'AYES', '_HIV_MGMT_2_O_2': 'Active',
           'HIV_MGMT_2_P': 'Kutibiwa solfest', 'HIV_MGMT_2_Q': '2023-11-07',
           'HIV_MGMT_2_R': 'Wambui Macharia', 'HIV_MGMT_2_S': '07256363'}
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
'''

response = requests.post(url, json=payload, headers=headers)
# response = requests.get(url, params=payload, headers=headers)

# print(response.headers)
# print(response.text)


print(response.json())
# print(len(response.json()))

# print(payload)
