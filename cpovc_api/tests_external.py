import requests
from params import credentials

# base_url = 'http://127.0.0.1:8006/api'
# base_url = 'https://dev.cpims.net/api'
base_url = 'https://ovc.childprotection.uonbi.ac.ke/api/'


def getToken():
    url = base_url + '/token/'
    response = requests.post(url, json=credentials)
    resp = response.json()
    # print(resp)
    token = resp['access']
    # refresh = resp['refresh']
    return token


# cpims_id = '1685038'
cpims_id = 3587315
token = getToken()

headers = {'Authorization': 'Bearer %s' % token}

print(token)

url = base_url + '/form/F1A/'
# payload = {'deviceID': 'AF32FE3E10291E53'}
payload = {'ovc_cpims_id': cpims_id}

# payload = {'field_name': 'sex_id', 'field_name': 'ovc_domain_id'}

response = requests.get(url, params=payload, headers=headers)
# response = requests.get(url, headers=headers).json()

# headers = {'Authorization': 'Bearer %s' % token}

# payload = {"refresh": token}

# response = requests.post(url, json=payload, headers=headers).json()

print(response)
print(response.json())


# Correct GET request
# response = requests.get(url, params=payload, headers=headers).json()

# Correct POST request


# response = requests.post(url, json=payload, headers=headers).json()
