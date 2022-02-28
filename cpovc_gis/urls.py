"""Urls for GIS."""
# from django.urls import path
# from django.conf.urls import patterns
from django.urls import path, include
from . import views
# This should contain urls related to GIS Module ONLY
urlpatterns = [
    # 'cpovc_gis.views',
    path('', views.gis_home, name='gis_home'),
    path('data/', views.gis_data, name='gis_data'),
    ]
