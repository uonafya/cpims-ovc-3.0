"""
cpims URL Configuration.

Other urls are import
Put here only urls not specific to app
"""
import logging

import cpovc_access
import cpovc_auth
import cpovc_dashboard
from . import views
from django.urls import include, path, re_path
from django.contrib import admin
from cpovc_auth import urls as auth_urls
from cpovc_registry import urls as registry_urls
from cpovc_forms import urls as forms_urls
from cpovc_reports import urls as reports_urls
from cpovc_gis import urls as gis_urls
# from cpovc_api import urls as api_urls
from cpovc_ovc import urls as ovc_urls
from cpovc_settings import urls as settings_urls
from data_cleanup import urls as data_cleanup_urls
from cpovc_offline_mode import urls as offline_mode_urls
# from django.contrib.auth.views import (
#     password_reset_done, password_change, password_change_done)
from django.contrib.auth import views as auth_views
from cpovc_auth.views import password_reset
from django.views.generic import TemplateView
from cpovc_dashboard import urls as dashboard_api_urls
from cpovc_access.forms import StrictPasswordChangeForm


urlpatterns = [
    path('admin/', admin.site.urls),  # Keep
    # path('admin/', include(admin.site.urls), name='admin'),
    # re_path(r'^$', cpovc_auth.views.log_in, name='home'),
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
    # path('home/', views.home, name='home'),
    re_path(r'^$', views.home, name='home'),
# url(r'^home/$', views.home, name='home'),
    path('accounts/request/', views.access, name='access'),
    path('accounts/terms/<int:id>/', cpovc_access.views.terms,
        name='terms'),
    path('login/', cpovc_auth.views.log_in, name='login'),
    path('logout/', cpovc_auth.views.log_out, name='logout'),
    path('register/', cpovc_auth.views.register, name='register'),
    path('auth/', include(auth_urls)),
    path('registry/', include(registry_urls)),
    path('forms/', include(forms_urls)),
    path('reports/', include(reports_urls)),
    path('gis/', include(gis_urls)),
    # path('api/', include(api_urls)),
    path('ovcare/', include(ovc_urls)),
    path('settings/', include(settings_urls)),
    path('data_cleanup/', include(data_cleanup_urls)),
    path('accounts/login/', cpovc_auth.views.log_in, name='acclogin'),
    path('accounts/password/reset/', password_reset,
        {'template_name': 'registration/password_reset.html'},
        name='password_reset'),
    # path('accounts/password/reset/done/', password_reset_done,
    #     {'template_name': 'registration/password_reset_done.html'},
    #     name='password_reset_done'),
    re_path(r'^accounts/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
        cpovc_auth.views.reset_confirm, name='password_reset_confirm'),
    path('reset/', cpovc_auth.views.reset, name='reset'),
    path('accounts/password/change/', auth_views.PasswordChangeView.as_view(),
        {'post_change_redirect': '/accounts/password/change/done/',
         'template_name': 'registration/password_change.html',
         'password_change_form': StrictPasswordChangeForm},
        name='password_change'),
    path('accounts/password/change/done/', auth_views.PasswordResetDoneView.as_view(),
        {'template_name': 'registration/password_change_done.html'}),
    re_path(r'^F57665A859FE7CFCDB6C8935196374AD\.txt$',
        TemplateView.as_view(template_name='comodo.txt',
                             content_type='text/plain')),
    re_path(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt',
                                               content_type='text/plain')),

    path('offline_mode/', include(offline_mode_urls)),
    #url(r'^dashboard/$', cpovc_dashboard.views.ovc_dashboard, name='ovc_dashboard'),
    path('d/', cpovc_dashboard.views.ovc_dashboard, name='ovc_dashboard'),
    path('d/hivstat/', cpovc_dashboard.views.ovc_dashboard_hivstat, name='hivstat_dash'),
    path('d/services/', cpovc_dashboard.views.ovc_dashboard_services, name='services_dash'),
    path('d/cm/', cpovc_dashboard.views.ovc_dashboard_cm, name='cm_dash'),
    path('api/v2/', include(dashboard_api_urls)),
]

handler400 = 'cpims.views.handler_400'
handler404 = 'cpims.views.handler_404'
handler500 = 'cpims.views.handler_500'

admin.site.site_header = 'CPIMS Administration'
admin.site.site_title = 'CPIMS administration'
admin.site.index_title = 'CPIMS admin'
