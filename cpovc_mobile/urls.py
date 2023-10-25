"""Mobile App API URLS."""
from django.urls import path, re_path
from . import views

urlpatterns = [
    #  cpara urls
    path('cpara/', views.create_ovc_mobile_cpara_data,
         name='create-ovc-mobile-data'),
    path('cpara/all/', views.get_all_ovc_mobile_cpara_data,
         name='get-ovc-mobile-data-list'),
    re_path(r'^cpara/(?P<ovc_id>[^/]+)/$',
            views.get_one_ovc_mobile_cpara_data, name='get-ovc-mobile-data'),
    re_path(r'^cpara/update/(?P<event_id>[^/]+)$',
            views.update_cpara_is_accepted, name='delete-ovc-mobile-event'),
    re_path(r'^cpara/delete/(?P<event_id>[^/]+)$',
            views.delete_ovc_mobile_event, name='delete-ovc-mobile-event'),

    # Form 1A and B urls

    re_path(r'^form/(?P<form_id>[0-9A-Z]{3})/$', views.create_ovc_event, name='create-form-record'),
    path('forms/<str:form_type>/', views.get_all_ovc_events, name='get-all-form-records'),
    path('forms/update/<uuid:id>', views.update_is_accepted, name='update-one-form-record'),
    re_path(r'^forms/(?P<form_type>[^/]+)/(?P<ovc_id>[^/]+)$', views.get_ovc_event, name='get-one-form-record'),
    re_path(r'^forms/delete/(?P<event_id>[^/]+)$', views.delete_ovc_event, name='delete-one-form-record'),
    

    # Case plan urls
    path('cpt/', views.create_case_plan_template, name='create-cpt-record'),
    path('cpt/all/', views.get_all_case_plans, name='get-all-cpt-records'),
    re_path(r'^cpt/(?P<ovc_id>[^/]+)/$', views.get_one_case_plan, name='get-one-cpt-record'),
    re_path(r'^cpt/update/(?P<unique_service_id>[^/]+)$', views.update_case_plan_is_accepted, name='update-one-cpt-record'),
    re_path(r'^cpt/delete/(?P<event_id>[^/]+)$', views.delete_case_plan_event, name='delete-one-cpt-record'),
    
    # Fetch all unaccepeted data
    path('unaccepted_records', views.get_all_unaccepted_records, name='fetch-all-unaccepted-data'),
    
    # Fetch all records BY form type
    path('unaccepted_records/<str:form_type>/', views.unaccepted_records, name='fetch-unaccepted-data'),
    # re_path(r'^unaccepted_records/(?P<form_type>[0-9A-Z]{3})/$',views.unaccepted_records, name='fetch-unaccepted-data'),
    
  
    # front end validation urls
    path('', views.mobile_home, name='mobile_view'),
    path('approvedata/', views.mobiledataapproval, name='approvedata'),
    path('fetch_child/', views.fetchChildren, name='fetch_child'),
    path('fetch_data/', views.fetchData, name='fetch_data'),
]
