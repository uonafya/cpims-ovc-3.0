"""OVC care section urls."""
from django.urls import  path

# This should contain urls related to registry ONLY
from cpovc_ovc.views import ovc_register, ovc_edit, ovc_view

urlpatterns = [
    'cpovc_ovc.views',
    path('$', 'ovc_home', name='ovc_home'),
    path('ovc/search/$', 'ovc_search', name='ovc_search'),
    path('ovc/new/<int:id>/', ovc_register, name='ovc_register'),
    path('ovc/edit/<int:id>/', ovc_edit, name='ovc_edit'),
    path('ovc/view/<int:id>/', ovc_view, name='ovc_view'),
    path('ovc/manage/$', 'ovc_manage', name='ovc_manage'),
    path('hh/view/<hhid>[0-9A-Za-z_\-]+)/$', 'hh_manage', name='hh_manage'),
    ]
