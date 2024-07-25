from django.urls import path, include
from . import views
urlpatterns = [
    path('templates/', views.templates, name='templates'),
    path('data/', views.fetch_data, name='fetch_data'),
    path('services/', views.fetch_services, name='fetch_services'),
    path('submit/', views.submit_form, name='submit_form'),
]
    # 'cpovc_offline_mode.views',
    # url(r'^templates/$', 'templates', name='templates'),
    # url(r'^data/$', 'fetch_data', name='fetch_data'),
    # url(r'^services/$', 'fetch_services', name='fetch_services'),
    # url(r'^submit/$', 'submit_form', name='submit_form'),

