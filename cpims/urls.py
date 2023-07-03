"""
CPIMS URL Configuration.

Other urls are import
Put here only urls not specific to app
"""
import cpovc_access
import cpovc_auth
from . import views
import cpovc_dashboard.views as dash_views
from django.urls import include, path, re_path
from django.contrib import admin
from cpovc_auth import urls as auth_urls
from cpovc_registry import urls as registry_urls
from cpovc_forms import urls as forms_urls
from cpovc_reports import urls as reports_urls
from cpovc_gis import urls as gis_urls
from cpovc_hes import urls as hes_urls
from cpovc_ovc import urls as ovc_urls
from cpovc_settings import urls as settings_urls
from data_cleanup import urls as data_cleanup_urls
from cpovc_offline_mode import urls as offline_mode_urls
from django.contrib.auth import views as auth_views
from cpovc_auth.views import password_reset
from django.views.generic import TemplateView
from cpovc_dashboard import urls as dashboard_api_urls
from cpovc_access.forms import StrictPasswordChangeForm
# New changes
from cpovc_preventive import urls as preventive_urls
from cpovc_pmtct import urls as pmtct_urls
# from notifications import urls as noti_urls
# from simple_forums import urls as forum_urls
from cpovc_api import urls as ovc_api_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    # Main
    re_path(r'^$', views.home, name='home'),
    path('accounts/request/', views.access, name='access'),
    path('accounts/terms/<int:id>/', cpovc_access.views.terms, name='terms'),
    path('register/', cpovc_auth.views.register, name='register'),
    path('auth/', include(auth_urls)),
    path('registry/', include(registry_urls)),
    path('forms/', include(forms_urls)),
    path('reports/', include(reports_urls)),
    path('gis/', include(gis_urls)),
    path('hes/', include(hes_urls)),
    path('ovc-care/', include(ovc_urls)),
    path('settings/', include(settings_urls)),
    path('data_cleanup/', include(data_cleanup_urls)),
    # Accounts management
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', cpovc_auth.views.log_in, name='acclogin'),
    path(
        'accounts/password/reset/', password_reset,
        {'template_name': 'registration/password_reset.html'},
        name='password_reset'),
    re_path(
        r'^accounts/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
        cpovc_auth.views.reset_confirm, name='password_reset_confirm'),
    path('reset/', cpovc_auth.views.reset, name='reset'),
    path(
        'accounts/password/change/', auth_views.PasswordChangeView.as_view(),
        {'post_change_redirect': '/accounts/password/change/done/',
         'template_name': 'registration/password_change.html',
         'password_change_form': StrictPasswordChangeForm},
        name='password_change'),
    path(
        'accounts/password/change/done/',
        auth_views.PasswordResetDoneView.as_view(),
        {'template_name': 'registration/password_change_done.html'}),
    # Override
    path('login/', cpovc_auth.views.log_in, name='login'),
    path('logout/', cpovc_auth.views.log_out, name='logout'),
    re_path(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt',
                                                   content_type='text/plain')),
    path('offline_mode/', include(offline_mode_urls)),
    # Dashboards
    path('d/', dash_views.ovc_dashboard, name='ovc_dashboard'),
    path(
        'd/registration/', dash_views.ovc_dashboard_registration,
        name='ovc_registration'),
    path('d/hivstat/', dash_views.ovc_dashboard_hivstat, name='hivstat_dash'),
    path(
        'd/services/', dash_views.ovc_dashboard_services,
        name='services_dash'),
    path('d/cm/', dash_views.ovc_dashboard_cm, name='cm_dash'),
    path('d/MER/', dash_views.ovc_dashboard_MER, name='mer_dash'),
    path('d/epidemic-control/', dash_views.ovc_dashboard_epc, name='epc_dash'),
    path(
        'd/performance/', dash_views.ovc_dashboard_perform,
        name='perform_dash'),
    path('d/glossary/', dash_views.ovc_dashboard_help, name='dash_help'),
    path('dashboard/', dash_views.raw_dashboard, name='raw_dashboard'),
    path(
        'dashboard/<int:did>/', dash_views.raw_dashboard,
        name='raw_dashboard'),
    path('api/v2/', include(dashboard_api_urls)),
    # Preventive and Family Support
    path('ovc-care/preventive/', include(preventive_urls)),
    path('ovc-care/pmtct/', include(pmtct_urls)),
    # Notifications
    # path('notifications/', include(noti_urls, namespace='notifications')),
    # path('forums/', include(forum_urls)),
    path('api/v1/', include(ovc_api_urls)),
    path('api/v4/', include(ovc_api_urls)),
]

handler400 = 'cpims.views.handler_400'
handler404 = 'cpims.views.handler_404'
handler500 = 'cpims.views.handler_500'

admin.site.site_header = 'CPIMS Administration'
admin.site.site_title = 'CPIMS administration'
admin.site.index_title = 'CPIMS admin'
