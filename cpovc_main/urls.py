from django.urls import path, re_path
from . import views

urlpatterns = [
    # Start CPIMS Dashboard
    path('public_dashboard/registration/', views.public_dashboard_reg, name='public_dashboard_reg'),
    path('public_dashboard/hivstat/', views.public_dashboard_hivstat, name='public_dashboard_hivstat'),
    path('public_dashboard/served/', views.public_dashboard_served, name='public_dashboard_served'),
    path('public_dash/', views.public_dash, name='public_dash'),
    path('public_dashboard/', views.public_dashboard_reg, name='public_dashboard_reg'),
    # APIs
    path('get_locality_data/', views.get_locality_data, name='get_locality_data'),
    re_path(r'^hiv_stats_pub_data/(?P<org_level>\w+)/(?P<area_id>.*)/', views.get_pub_data, name='get_pub_data'),
    re_path(r'^hiv_stats_ovc_active/(?P<org_level>\w+)/(?P<area_id>.*)/', views.get_ovc_active_hiv_status, name='ovc_active_hiv_status'),
    re_path(r'^get_hiv_suppression_data/(?P<org_level>\w+)/(?P<area_id>.*)/', views.get_hiv_suppression_data, name='get_hiv_suppression_data'),
    # # ####
    re_path(r'^get_total_ovc_ever/(?P<org_level>\w+)/(?P<area_id>.*)/', views.get_total_ovc_ever, name='get_total_ovc_ever'),
    re_path(r'^get_total_ovc_ever_exited/(?P<org_level>\w+)/(?P<area_id>.*)/', views.get_total_ovc_ever_exited, name='get_total_ovc_ever_exited'),
    re_path(r'^get_total_wout_bcert_at_enrol/(?P<org_level>\w+)/(?P<area_id>.*)/', views.get_total_wout_bcert_at_enrol, name='get_total_wout_bcert_at_enrol'),
    re_path(r'^get_total_w_bcert_2date/(?P<org_level>\w+)/(?P<area_id>.*)/', views.get_total_w_bcert_2date, name='get_total_w_bcert_2date'),
    re_path(r'^get_total_s_bcert_aft_enrol/(?P<org_level>\w+)/(?P<area_id>.*)/', views.get_total_s_bcert_aft_enrol, name='get_total_s_bcert_aft_enrol'),
    path('fetch_cbo_list/', views.fetch_cbo_list, name='fetch_cbo_list'),
    re_path(r'^get_ever_tested_hiv/(?P<org_level>\w+)/(?P<area_id>.*)/', views.get_ever_tested_hiv, name='get_ever_tested_hiv'),
    #
    re_path(r'^get_new_ovcregs_by_period/(?P<org_level>\w+)/(?P<area_id>.*)/(?P<funding_partner>.*)/(?P<funding_part_id>.*)/(?P<period_type>.*)/', views.get_new_ovcregs_by_period, name='get_new_ovcregs_by_period'),
    #
    re_path(r'^get_active_ovcs_by_period/(?P<org_level>\w+)/(?P<area_id>.*)/(?P<funding_partner>.*)/(?P<funding_part_id>.*)/(?P<period_type>.*)/', views.get_active_ovcs_by_period, name='get_active_ovcs_by_period'),
    #
    re_path(r'^get_exited_ovcs_by_period/(?P<org_level>\w+)/(?P<area_id>.*)/(?P<funding_partner>.*)/(?P<funding_part_id>.*)/(?P<period_type>.*)/', views.get_exited_ovcs_by_period, name='get_exited_ovcs_by_period'),
    #
    re_path(r'^get_exited_hsehlds_by_period/(?P<org_level>\w+)/(?P<area_id>.*)/(?P<funding_partner>.*)/(?P<funding_part_id>.*)/(?P<period_type>.*)/', views.get_exited_hsehlds_by_period, name='get_exited_hsehlds_by_period'),

    re_path(r'^get_served_bcert_by_period/(?P<org_level>\w+)/(?P<area_id>.*)/(?P<month_year>.*)/', views.get_served_bcert_by_period, name='get_served_bcert_by_period'),
    re_path(r'^get_u5_served_bcert_by_period/(?P<org_level>\w+)/(?P<area_id>.*)/(?P<month_year>.*)/', views.get_u5_served_bcert_by_period, name='get_u5_served_bcert_by_period'),
    re_path(r'^get_ovc_served_stats/(?P<org_level>\w+)/(?P<area_id>.*)/(?P<funding_partner>.*)/(?P<funding_part_id>.*)/(?P<period_type>.*)/', views.get_ovc_served_stats, name='get_ovc_served_stats'),
    # endAPIs
]
