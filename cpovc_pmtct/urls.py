from django.urls import path
from . import views
# This should contain urls related to OVC ONLY

urlpatterns = [
    path('', views.pmtct_home, name='pmtct_home'),
    path('new/<int:id>/', views.new_pmtct, name='new_pmtct'),
    path('view/<int:id>/', views.view_pmtct, name='view_pmtct'),
    path('edit/<int:id>/', views.edit_pmtct, name='edit_pmtct'),

    # Pregnant Women Adolescent
    path('pregnant-wa/new/<int:id>/',
         views.new_pregnantwomen, name='new_pregnantwomen'),
    path('pregnant-wa/edit/<int:id>/',
         views.edit_pregnantwomen, name='pregnantwomen'),
    path('delete_pregnant-wa/<int:id>/',
         views.delete_pregnantwomen, name='delete_pregnantwomen'),

    # HEI Tracker
    path('hei-tracker/new/<int:id>/',
         views.new_hei_tracker, name='new_hei_tracker'),
    path('hei-tracker/edit/<uuid:id>/',
         views.edit_heitracker, name='edit_heitracker'),
    path('hei-tracker/delete/<uuid:id>/',
         views.delete_heitracker, name='delete_heitracker'),
]
