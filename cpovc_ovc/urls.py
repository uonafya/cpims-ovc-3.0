"""OVC care section urls."""
from django.urls import path, re_path
# from django.conf.urls import patterns
from . import views
# This should contain urls related to registry ONLY
urlpatterns = [
    # 'cpovc_ovc.views',
    path('', views.ovc_home, name='ovc_home'),
    path('ovc/search/', views.ovc_search, name='ovc_search'),
    path('ovc/new/<int:id>/', views.ovc_register, name='ovc_register'),
    path('ovc/edit/<int:id>/', views.ovc_edit, name='ovc_edit'),
    path('ovc/view/<int:id>/', views.ovc_view, name='ovc_view'),
    path('ovc/manage/', views.ovc_manage, name='ovc_manage'),
    re_path(r'^hh/view/(?P<hhid>[0-9A-Za-z_\-]+)/$', views.hh_manage, name='hh_manage'),
    ]
