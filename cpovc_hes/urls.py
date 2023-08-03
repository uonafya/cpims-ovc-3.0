from django.urls import path
from .views import  *

# This should contain urls related to registry ONLY

urlpatterns = [
    # path('', views.si_home, name='SI_home'),


    path('new/hes', new_hes, name='new_hes'),


]