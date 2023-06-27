from django.urls import path, re_path
from . import views
# This should contain urls related to Dashboards ONLY

g_params = "(?P<rid>\w+)/(?P<county_id>\d+)/(?P<const_id>\d+)/(?P<ward_id>\d+)"
i_params = "(?P<mech_id>\d+)/(?P<ip_id>\d+)/(?P<lip_id>\d+)"
d_params = "(?P<prd>\d+)/(?P<yr>\d+)"

urlpatterns = [
    path('', views.ovc_dashboard, name='ovc_dashboard_v2'),
    path(
        'constituency/<int:area_id>/', views.get_constituency,
        name='get_constituency'),
    path('ward/<int:area_id>/', views.get_ward, name='get_ward'),
    path('ip/<int:fund_id>/', views.get_ip, name='get_ip'),
    path('lip/<int:ip_id>/', views.get_lip, name='get_lip'),
    # path('chart/<int:ip_id>/', views.get_chart, name='get_chart'),
    re_path(r'^api/%s/%s/%s/' % (
        g_params, i_params, d_params), views.get_chart, name='get_chart_data'),
    path('settings/', views.settings, name='settings'),
    path(
        'registration/', views.ovc_dashboard_registration,
        name='ovc_registration'),
    path('hivstat/', views.ovc_dashboard_hivstat, name='hivstat_dash'),
    path(
        'services/', views.ovc_dashboard_services,
        name='services_dash'),
    path('cm/', views.ovc_dashboard_cm, name='cm_dash'),
    path('MER/', views.ovc_dashboard_MER, name='mer_dash'),
    path('epidemic-control/', views.ovc_dashboard_epc, name='epc_dash'),
    path(
        'performance/', views.ovc_dashboard_perform,
        name='perform_dash'),
    path('glossary/', views.ovc_dashboard_help, name='dash_help'),
]
