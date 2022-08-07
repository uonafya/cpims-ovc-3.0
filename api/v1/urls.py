from .views import regperson_list, regperson_detail
from django.urls import path

urlpatterns =  [
    path('regperson/', regperson_list),
    path('regperson/<int:pk>/', regperson_detail),
]