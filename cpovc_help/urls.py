"""Urls for Settings."""
from django.urls import path, re_path
from django.conf.urls import patterns

# This should contain urls related to settings ONLY
urlpatterns = patterns(
    'cpovc_help.views',
    path('downloads/', 'help_downloads', name='help_downloads'),
    re_path(r'^download/(?P<name>[0-9A-Za-z_\-\.]+)$', 'doc_download', name='doc_download'),
    path('faq/', 'help_faq', name='help_faq'),
)