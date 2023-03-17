import requests


url = 'http://localhost:8002/api/v1/dreams/'
# url = 'https://test.cpims.net/api/v1/dreams/'

headers = {'Authorization': 'Token 0e7f44df2bbbd92c618b1e7b67adb7484f2d79e6'}
# headers = {'Authorization': 'Token 00766097e1b5321126e8672b3e440c91cb280682'}


data = {'cpims_id': 6}


# response = requests.post(url, json=data, headers=headers)

response = requests.get(url, params=data, headers=headers)

# print (response)
print('==' * 50, 'HEADERS', '==' * 50)
print(response.headers)
print('\n')
print('==' * 50, 'CONTENT', '==' * 50)
print(response.json())

