"""Preventing and Family support app urls."""
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.pfs_home, name='pfs_home'),
    path('new/<int:id>/', views.new_pfs, name='new_pfs'),
    path('view/<int:id>/', views.view_pfs, name='view_pfs'),
    path('edit/<int:id>/', views.edit_pfs, name='edit_pfs'),

    # Preventive Registers
    path('preventiveattendanceregister/new/<int:id>/',
         views.preventive_attendance_register,
         name='preventiveattendanceregister'),
    path('preventiveattendanceregister/save/',
         views.save_preventive_register, name='save_preventive_register'),
    path('preventiveattendanceregister/manage/',
         views.manage_preventive_register, name='manage_preventive_register'),
    re_path('preventiveattendanceregister/delete/(?P<id>\d+)/(?P<btn_event_type>\w+)/(?P<btn_event_pk>.+)/', views.delete_preventive_event_entry,
            name='delete_preventive_event_entry'),
    re_path('preventiveattendanceregister/edit/(?P<id>\d+)/(?P<btn_event_type>\w+)/(?P<btn_event_pk>.+)/', views.edit_preventive_event_entry,
            name='edit_preventive_event_entry'),
]