"""Urls for Settings."""
from django.urls import path, re_path
from django.conf.urls import patterns

# This should contain urls related to settings ONLY
urlpatterns = patterns(
    'cpovc_settings.views',
    path('', 'settings_home', name='settings_home'),
    re_path(r'^reports/d/(?P<file_name>[0-9_\-_A-Za-z_\._A-Za-z]+)$',
        'archived_reports', name='archived_reports'),
    re_path(r'^reports/r/(?P<file_name>[0-9_\-_A-Za-z_\._A-Za-z]+)$',
        'remove_reports', name='remove_reports'),
    path('reports/', 'settings_reports', name='settings_reports'),
    path('facilities/', 'settings_facilities', name='settings_facilities'),
    path('schools/', 'settings_schools', name='settings_schools'),
    path('data/', 'settings_rawdata', name='settings_rawdata'),
    path('changes/', 'change_notes', name='change_notes'),)
