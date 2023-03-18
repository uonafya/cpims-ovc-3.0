"""Preventing and Family support app urls."""
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.pfs_home, name='pfs_home'),
    path('new/<int:id>/', views.new_pfs, name='new_pfs'),
    path('view/<int:id>/', views.view_pfs, name='view_pfs'),
    path('edit/<int:id>/', views.edit_pfs, name='edit_pfs'),

    # Preventive Registers
    path('register/new/<int:id>/',
         views.preventive_attendance_register,
         name='preventiveattendanceregister'),
    path('register/save/',
         views.save_preventive_register, name='save_preventive_register'),
    path('register/manage/',
         views.manage_preventive_register, name='manage_preventive_register'),
    re_path(
        'register/delete/(?P<id>\d+)/(?P<btn_event_type>\w+)/(?P<btn_event_pk>.+)/',
        views.delete_preventive_event_entry,
        name='delete_preventive_event_entry'),
    re_path(
        'register/edit/(?P<id>\d+)/(?P<btn_event_type>\w+)/(?P<btn_event_pk>.+)/',
        views.edit_preventive_event_entry,
        name='edit_preventive_event_entry'),
    # Version 2 Thinking
    path(
        'register/v2/new/<int:id>/',
        views.new_register_v2, name='new_register'),

    # SINOVUYO
    # Pre and Post evaluations - Caregiver
    path('sinovuyo-caregiver/new/<int:id>/',
         views.new_sinovuyo_evaluation, name='new_sinovuyo_evaluation'),
    path('sinovuyo-caregiver/edit/<uuid:event_id>/',
         views.edit_sinovuyo_evaluation, name='edit_sinovuyo_evaluation'),
    path('sinovuyo-caregiver/delete/',
         views.delete_sinovuyo_evaluation, name='delete_sinovuyo_evaluation'),
    # Pre and Post evaluations - Teen
    path('sinovuyo-teen/new/<int:id>/',
         views.new_sinovuyo_evaluation_teen,
         name='new_sinovuyo_evaluation_teen'),
    path('sinovuyo-teen/edit/<uuid:event_id>/',
         views.edit_sinovuyo_evaluation_teen,
         name='edit_sinovuyo_evaluation_teen'),

    # HCBF
    # Pre and Post evaluations - Teen
    path('hcbf/new/<int:id>/',
         views.new_hcbf_evaluation, name='new_hcbf_evaluation'),
    path('hcbf/edit/<uuid:event_id>/',
         views.edit_hcbf_evaluation, name='edit_hcbf_evaluation'),

    # FMP
    # Pre and Post evaluations - Caregiver
    path('fmp/new/<int:id>/',
         views.new_fmp_evaluation, name='new_fmp_evaluation'),
    path('fmp/edit/<uuid:event_id>/',
         views.edit_fmp_evaluation, name='edit_fmp_evaluation'),

    # CBIM
    # Pre and Post evaluations - Teen
    path('cbim/new/<int:id>/',
         views.new_cbim_evaluation, name='new_cbim_evaluation'),
    path('cbim/edit/<uuid:event_id>/',
         views.edit_cbim_evaluation, name='edit_cbim_evaluation'),
]
