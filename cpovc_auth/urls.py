"""URLs for authentication module."""
from django.urls import path
from . import views
# This should contain urls related to auth app ONLY
urlpatterns = [
    path('', views.home, name='auth_home'),
    path('register/', views.register, name='register'),
    path('ping/', views.user_ping, name='user_ping'),
    path('roles/', views.roles_home, name='roles_home'),
    path('roles/edit/<int:user_id>/', views.roles_edit,
         name='roles_edit'),
]
