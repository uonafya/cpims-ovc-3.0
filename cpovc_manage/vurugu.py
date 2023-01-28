import requests

base_url = 'https://vm.cpims.net/json'
user_name = 'admin'
user_pass = 'admin'

def login_api():
    """Method to login to get key details."""
    try:
        url = '%s/auth/login' % base_url
        logins = {'userName': user_name, 'password': user_pass}
        r = requests.post(url, json = logins)
    except Exception as e:
        return None
    else:
        return r.json()


def save_vm_changes(case_id, payload):
	"""Method to save changes to VM."""
	try:
		response =  login_api()
		key = response['key']
		headers = {'userId': user_name, 'key': key}
		url = '%s/app/answer/single/%s' % (base_url, case_id)
		r = requests.put(url, headers=headers, json = payload)
	except Exception as e:
		raise e
	else:
		return r.json()



if __name__ == '__main__':
    case_id = 'f318c2c7-e650-48b0-9681-f2dc6fea4719'
    payload = {"verification_status" : "002"}
    # payload = {"case_serial" : "CCO/39/221/5/29/1197/2020"}
    # payload = {"case_reporter" : "CRCO"}
    resp = save_changes(case_id, payload)
    print(resp)