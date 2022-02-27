"""Urls for GIS."""
from django.urls import path
from django.conf.urls import patterns

# This should contain urls related to GIS Module ONLY
urlpatterns = patterns(
    'cpovc_gis.views',
    path('', 'gis_home', name='gis_home'),
    path('data/', 'gis_data', name='gis_data'),)
