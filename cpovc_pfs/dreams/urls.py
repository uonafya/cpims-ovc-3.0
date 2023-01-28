from django.urls import path
from . import views
# This should contain urls related to DREAMS ONLY

urlpatterns = [
    path('', views.dreams_home, name='dreams_home'),
]