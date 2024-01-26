"""Urls for reports."""
from django.urls import path, re_path
# from django.conf.urls import patterns
from . import views
# This should contain urls related to reports ONLY
urlpatterns = [
    # 'cpovc_reports.views',
    path('', views.reports_home, name='reports'),
    path('documents/', views.reports_home, name='document_reports'),
    path('<int:id>/', views.reports_cpims, name='cpims_reports'),
    path('caseload/', views.reports_caseload, name='caseload_reports'),
    path('get_viral_load_report/', views.get_viral_load_report, name='get_viral_load_report'),
    path('manage/', views.manage_reports, name='manage_reports'),
    path('dashboard/', views.manage_dashboard, name='manage_dashboard'),
    re_path(r'^download/(?P<file_name>[0-9A-Za-z_\.=\-\' ]+)$', views.reports_download, name='download_reports'),
    path('generate/', views.reports_generate, name='generate_reports'),
    path('pivot/', views.reports_pivot, name='pivot_reports'),
    path('data/', views.reports_rawdata, name='pivot_rawdata'),
    path('datim/', views.reports_ovc_pivot, name='pivot_ovc_reports'),
    path('datim_mer/', views.reports_ovc_datim_mer_pivot, name='pivot_ovc_reports_mer'),
    path('datim_mer23/', views.reports_ovc_datim_mer23_pivot, name='pivot_ovc_reports_mer23'),
    path('datim_mer24/', views.reports_ovc_datim_mer24_pivot, name='pivot_ovc_reports_mer24'),
    path('datim_mer25/', views.reports_ovc_datim_mer25_pivot, name='pivot_ovc_reports_mer25'),
    path('pepfar/', views.reports_ovc_pepfar, name='pivot_ovc_pepfar'),
    path('kpi/', views.reports_ovc_kpi, name='pivot_ovc_kpi'),
    path('viral_load/', views.viral_load, name='viral_load'),
    path('ovcdata/', views.reports_ovc_rawdata, name='pivot_ovc_rawdata'),
    path('download/', views.reports_ovc_download, name='ovc_download'),
    path('ovc/<int:id>/', views.reports_ovc, name='reports_ovc'),
    path('dashboard/data/', views.dashboard_details, name='dashboard_details'),
    path('cluster/', views.cluster, name='cluster'),
    path('ovc/', views.reports_ovc_list, name='reports_ovc_list'),
    path('bursary/', views.reports_bursary, name='bursary_reports'),
]

