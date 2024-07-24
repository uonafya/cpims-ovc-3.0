from django.urls import path, re_path
from . import views
# This should contain urls related to Dashboards ONLY

g_params = "(?P<rid>\w+)/(?P<county_id>\d+)/(?P<const_id>\d+)/(?P<ward_id>\d+)"
i_params = "(?P<mech_id>\d+)/(?P<ip_id>\d+)/(?P<lip_id>\d+)"
d_params = "(?P<prd>\d+)/(?P<yr>\d+)"

urlpatterns = [
    path(
        'constituency/<int:area_id>/', views.get_constituency,
        name='get_constituency'),
    path('ward/<int:area_id>/', views.get_ward, name='get_ward'),
    path('ip/<int:fund_id>/', views.get_ip, name='get_ip'),
    path('lip/<int:ip_id>/', views.get_lip, name='get_lip'),
    # path('chart/<int:ip_id>/', views.get_chart, name='get_chart'),
    re_path(r'^%s/%s/%s/' % (
        g_params, i_params, d_params), views.get_chart, name='get_chart_data'),
    path('settings/', views.settings, name='settings'),
]
