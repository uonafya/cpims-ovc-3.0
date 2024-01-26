import requests

url = 'https://www.cartographie.ceni.cd/mapapi.php?value=13&type=pres&circ=province'
payload = {"value": 13, "type": "pres", "circ": "province"}

headers =  {"Host": "www.cartographie.ceni.cd",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Origin": "https://cartographie.ceni.cd",
            "Connection": "keep-alive",
            "Referer": "https://cartographie.ceni.cd/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site"}
response = requests.get(url, params=payload, headers=headers, verify=False)
# resp = response.json()
print(response)
# print(resp)

print('Final', response.text)

with open('data.json', 'wb') as f:
    f.write(data)