from django.urls import path, re_path
from django.conf.urls import patterns

# This should contain urls related to Dashboards ONLY

g_params = "(?P<rid>\w+)/(?P<county_id>\d+)/(?P<const_id>\d+)/(?P<ward_id>\d+)"
i_params = "(?P<ip_id>\d+)/(?P<lip_id>\d+)"
d_params = "(?P<prd>\d+)/(?P<yr>\d+)"

urlpatterns = patterns(
    'cpovc_dashboard.views',
    # Geo Settings
    path('constituency/<int:area_id>/',
        'get_constituency', name='get_constituency'),
    path('ward/<int:area_id>/', 'get_ward', name='get_ward'),
    path('lip/<int:ip_id>/', 'get_lip', name='get_lip'),
    re_path(r'^%s/%s/%s/' % (g_params, i_params, d_params), 'get_chart'),
    # county_id, const_id, ward_id, ip, lip
)
