"""Preventing and Family support app urls."""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.pfs_home, name='pfs_home'),
    path('new/<int:id>/', views.new_pfs, name='new_pfs'),
    path('view/<int:id>/', views.view_pfs, name='view_pfs'),
    path('edit/<int:id>/', views.edit_pfs, name='edit_pfs'),
]