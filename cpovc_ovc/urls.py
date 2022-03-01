"""OVC care section urls."""
from django.urls import path

# This should contain urls related to registry ONLY
urlpatterns = [
    'cpovc_ovc.views',
    path(r'^$', 'ovc_home', name='ovc_home'),
    path(r'^ovc/search/$', 'ovc_search', name='ovc_search'),
    path(r'^ovc/new/(?P<id>\d+)/$',
        'ovc_register', name='ovc_register'),
    path(r'^ovc/edit/(?P<id>\d+)/$',
        'ovc_edit', name='ovc_edit'),
    path(r'^ovc/view/(?P<id>\d+)/$',
        'ovc_view', name='ovc_view'),
    path(r'^ovc/manage/$', 'ovc_manage', name='ovc_manage'),
    path(r'^hh/view/(?P<hhid>[0-9A-Za-z_\-]+)/$',
        'hh_manage', name='hh_manage'),
    ]
