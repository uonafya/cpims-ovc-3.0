"""Urls for Settings."""
from django.urls import path, re_path
from django.conf.urls import patterns

# This should contain urls related to settings ONLY
urlpatterns = patterns(
    'cpovc_manage.views',
    path('', 'manage_home', name='manage_home'),
    path('travel/', 'home_travel', name='home_travel'),
    path('integration/', 'integration_home', name='integration_home'),
    path('travel/edit/<int:id>/', 'edit_travel', name='edit_travel'),
    path('travel/view/<int:id>/', 'view_travel', name='view_travel'),
    path('travel/pdf/<int:id>/', 'travel_report', name='travel_report'),
    # Integrations
    re_path(r'^api/(?P<case_id>[0-9A-Za-z_\-{32}\Z]+)/$',
        'process_integration', name='process_integration'),
    re_path(r'^doc/(?P<doc_id>\d+)/(?P<case_id>[0-9A-Za-z_\-{32}\Z]+)/$',
        'get_document', name='get_document'),
    path('dq/', 'dq_home', name='dq_home'),
    path('se/', 'se_home', name='se_home'),
    path('sedata/', 'se_data', name='se_data'),
    # DQA
    path('dq/', 'dq_home', name='dq_home'),
    path('dqdata/', 'dq_data', name='dq_data'),
)
