"""Mobile App API URLS."""
from django.urls import path, re_path
from rest_framework_simplejwt import views as jwt_views

from . import views

urlpatterns = [
    #  cpara urls
    path('cpara', views.create_ovc_mobile_cpara_data, name='create-ovc-mobile-data'),
    path('cpara/all/', views.get_all_ovc_mobile_cpara_data, name='get-ovc-mobile-data-list'),
    re_path(r'^cpara/(?P<event_id>[^/]+)/$', views.get_one_ovc_mobile_cpara_data, name='get-ovc-mobile-data'),
    re_path(r'^cpara/(?P<event_id>[^/]+)/update/$', views.update_cpara_is_accepted, name='delete-ovc-mobile-event'),
    re_path(r'^cpara/(?P<event_id>[^/]+)/delete/$', views.delete_ovc_mobile_event, name='delete-ovc-mobile-event'),
    
    # Form 1A and B urls
    path('forms/', views.create_ovc_event, name='create-form-record'),
    path('forms/all/', views.get_all_ovc_events, name='get-all-form-records'),
    re_path(r'^forms/(?P<event_id>[^/]+)/$', views.get_ovc_event, name='get-one-form-record'),
    re_path(r'^forms/(?P<event_id>[^/]+)/update/$', views.update_is_accepted, name='update-one-form-record'),
    re_path(r'^forms/(?P<event_id>[^/]+)/delete/$', views.delete_ovc_event, name='delete-one-form-record'),
    
    # Case plan urls
    path('cpt/', views.create_case_plan_template, name='create-cpt-record'),
    path('cpt/all/', views.get_all_case_plans, name='get-all-cpt-records'),
    re_path(r'^cpt/(?P<event_id>[^/]+)/$', views.get_one_case_plan, name='get-one-cpt-record'),
    re_path(r'^cpt/(?P<event_id>[^/]+)/update/$', views.update_case_plan_is_accepted, name='update-one-cpt-record'),
    re_path(r'^cpt/(?P<event_id>[^/]+)/delete/$', views.delete_case_plan_event, name='delete-one-cpt-record'),
    
    # Fetch all unaccpeted data
    path('all/unaccepted', views.get_all_unaccepted_records, name='fetch-all-unaccepted-data'),
    
    # Fetch all records /with query parameter
    path('unaccepted_records/', views.unaccepted_records, name='fetch-unaccepted-data'),
    
  
    # front end validation urls
    path('', views.mobile_home, name='mobile_view'),
    path('approvedata/', views.mobiledataapproval, name='approvedata'),
    path('fetch_child/', views.fetchChildren, name='fetch_child'),
    path('fetch_data/', views.fetchData, name='fetch_data'),
]

