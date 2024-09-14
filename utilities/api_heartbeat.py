import json
import requests
from django.conf import settings
from django.utils import timezone
from rest_framework.authtoken.models import Token
from cpovc_auth.models import CPOVCProfile


class APIHeartbeat(object):
    '''
        Check status of API Integrations and save in Admin Profile
    '''

    def __init__(self):
        self.API_OUT = settings.API_OUT
        self.API_IN = settings.API_IN


    def basic_token(self, token, token_url):
        # Check internally if token is still valid
        headers = {'Authorization': 'Token %s' % token}
        response = requests.post(token_url, headers=headers, data={})
        return response.status_code


    def jwt_token(self, params):
        # Login using the shared details and combinations
        token_url = params['url']
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        credentials = { params['user_field']: params['username'], 
                        "password": params['password']}
        response = requests.post(token_url, headers=headers, data=credentials)
        return response.status_code


    def jwt_json_token(self, params):
        # Login using the shared details and combinations
        token_url = params['url']
        headers = {'Content-Type': 'application/json'}
        credentials = { params['user_field']: params['username'], 
                        "password": params['password']}
        response = requests.post(token_url, headers=headers, json=credentials)
        return response.status_code


    def oauth_token(self, params):
        # generate token for oauth.
        token_url = params['url']
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        credentials = { "grant_type": params['grant_type'], 
                        "username": params['username'], 
                        "password": params['password'], 
                        "scope": params['scope'], 
                        "client_id": params['client_id'],
                        "client_secret": params['client_secret']}
        response = requests.post(token_url, headers=headers, data=credentials)
        return response.status_code


    def update_profile(self, system_id, status_id, ts):
        """Method to update profile details."""
        try:
            details = {}
            user_id = 1
            myprofile = CPOVCProfile.objects.filter(user_id=1).first()
            if myprofile:
                details = eval(myprofile.details)
            details[system_id] = {'status': status_id, 'ts': ts}
            htb, created = CPOVCProfile.objects.update_or_create(
                                user_id=user_id,
                                defaults={
                                'is_void': 'False', 'timestamp_updated': ts,
                                'details': str(details) })
        except Exception as e:
            raise e
        else:
            pass

    
    def get_status(self):
        # loop in the integrations and try log in.
        try:
            # Integrations IN using Basic Token
            token_url = settings.TOKEN_CHECK_URL
            statuses_in = self.API_IN
            tokens = Token.objects.all()
            for token in tokens:
                key = token.key
                username = token.user.username
                if username in statuses_in:
                    resp = self.basic_token(key, token_url)
                    ts = timezone.now()
                    print(username, resp)
                    self.update_profile(username.upper(), resp, str(ts))
            # Integrations OUT using others like JWT
            statuses_out = self.API_OUT
            for status in statuses_out:
                login_url = getattr(settings, '%s_LOGIN_URL' % (status))
                username = getattr(settings, '%s_USERNAME' % (status))
                password = getattr(settings, '%s_PASSWORD' % (status))
                user_field = getattr(settings, '%s_USER_FIELD' % (status), 'username')
                # Basic Token
                basic_token = getattr(settings, '%s_TOKEN' % (status), None)
                # JWT JSON validation
                jwt_json = getattr(settings, '%s_JSON' % (status), None)
                # For oauth
                grant_type = getattr(settings, '%s_GRANT_TYPE' % (status), None)
                scope = getattr(settings, '%s_SCOPE' % (status), None)
                client_id = getattr(settings, '%s_CLIENT_ID' % (status), None)
                client_secret = getattr(settings, '%s_CLIENT_SECRET' % (status), None)
                params = {'url': login_url, 'username': username, 'password': password,
                          'user_field': user_field, 'grant_type': grant_type,
                          'scope': scope, 'client_id': client_id,
                          'client_secret': client_secret }
                if grant_type:
                    resp = self.oauth_token(params)
                elif basic_token:
                    resp = self.basic_token(basic_token, login_url)
                elif jwt_json:
                    resp = self.jwt_json_token(params)
                else:
                    resp = self.jwt_token(params)
                print(status, resp)
                ts = timezone.now()
                self.update_profile(status, resp, str(ts))
            # Save the details in Admin Profile
        except Exception as e:
            raise e
        else:
            pass


