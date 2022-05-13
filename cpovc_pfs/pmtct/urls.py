from django.urls import path
from . import views
# This should contain urls related to OVC ONLY

urlpatterns = [
    path('', views.pmtct_home, name='pmtct_home'),
    path('new/<int:id>/', views.new_pmtct, name='new_pmtct'),
    path('view/<int:id>/', views.view_pmtct, name='view_pmtct'),
    path('edit/<int:id>/', views.edit_pmtct, name='edit_pmtct'),
]
