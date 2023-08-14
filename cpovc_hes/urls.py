from django.urls import path
from cpovc_hes import views

# This should contain urls related to registry ONLY

urlpatterns = [
    path('', views.hes_home, name='hes_home'),
    path('new/<int:id>/', views.new_hes, name='new_hes'),
    path('view/<uuid:id>', views.view_hes, name='view_hes'),


]