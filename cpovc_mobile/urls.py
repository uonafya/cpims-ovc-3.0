from django.urls import path, re_path
from . import views
# This should contain urls related to Dashboards ONLY

g_params = "(?P<rid>\w+)/(?P<county_id>\d+)/(?P<const_id>\d+)/(?P<ward_id>\d+)"
i_params = "(?P<mech_id>\d+)/(?P<ip_id>\d+)/(?P<lip_id>\d+)"
d_params = "(?P<prd>\d+)/(?P<yr>\d+)"

urlpatterns = [
    path('', views.mobile_home, name='mobile_view'),
    path('approvedata/', views.mobiledataapproval, name='approvedata'),
    path('fetch_child/', views.fetchChildren, name='fetch_child'),
    path('fetch_data/', views.fetchData, name='fetch_data'),
]