from django.urls import path, include

from rest_framework.routers import DefaultRouter
from 


from cpims_api import views

router = DefaultRouter()
router.register('date_counter', views.Re)

urlpatterns = [
    path('', include(router.urls)),
]