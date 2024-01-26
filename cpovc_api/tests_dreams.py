import requests

# base_url = 'http://127.0.0.1:8005/api'
base_url = 'https://dev.cpims.net/api'

token = '02b17c10a8a17fae8fa16bb8fc63ce8665441553'

# url = 'https://dev.cpims.net/api/token/'
headers = {'Authorization': 'Token %s' % token}

url = base_url + '/dreams/'

cpims_id = 4041779

payload = {'cpims_id': cpims_id}

# response = requests.post(url, json=payload, headers=headers)
response = requests.get(url, params=payload, headers=headers)

# print(response.headers)
# print(response.text)
print(response.json())
print(len(response.json()))
