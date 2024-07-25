from django.urls import path
from cpovc_dreams import views

# This should contain urls related to DREAMS ONLY

urlpatterns = [
    path('', views.dreams_home, name='dreams_home'),
    # path('view/<uuid:id>/', views.view_dreams, name='view_dreams'),

]