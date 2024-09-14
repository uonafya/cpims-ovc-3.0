from django.contrib.auth.models import update_last_login
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import get_user_model


class TokenAuthenticationView(ObtainAuthToken):
    """Implementation of ObtainAuthToken with last_login update"""
    
    def post(self, request):
        result = super(TokenAuthenticationView, self).post(request)
        currentUserModel = get_user_model()
        try:
            user = currentUserModel.objects.get(username=request.data['username'])
            update_last_login(None, user)
        except Exception as exc:
            return None
        return result