"""Mobile App API URLS."""
from django.urls import path, re_path
from rest_framework_simplejwt import views as jwt_views

from . import views

urlpatterns = [
    # path('', views.api_home, name='api_home'),
    path('', views.APIRoot.as_view(), name='api_home'),
    # Authentication
    path(
        'token/', jwt_views.TokenObtainPairView.as_view(),
        name='token_obtain_pair'),
    path(
        'token/refresh/', jwt_views.TokenRefreshView.as_view(),
        name='token_refresh'),
    path(
        'token/validate/', views.token_validate, name='token_validate'),
    # Setttings
    path('settings/', views.settings, name='api_settings'),

    # Dashboards
    path('dashboard/', views.dashboard, name='api_dashboard'),

    # My caseload / data - By CHV or IP/LIP
    path('caseload/', views.caseload, name='api_caseload'),
    path('registrations/', views.registration, name='api_reglist'),

    # Forms data - GET / POST
    re_path(r"^form/(?P<form_id>[0-9A-Z]{3})/$", views.form_data),

    # DREAMS
    path('dreams/', views.dreams, name='dreams'),

    # Mobile App
    path('forms/', views.form_unapproved, name='unapproved_form'),
    path('metadata/', views.metadata, name='get_metadata'),
    path('subpop/', views.sub_pop, name='sub_pop'),
    path('cpara/', views.cpara, name='sub_pop'),
    path('caseplan/', views.caseplan, name='sub_pop'),
    path('form1a/', views.form1a, name='sub_pop'),
    path('form1b/', views.form1b, name='sub_pop'),
]
