from django.urls import path, include

from rest_framework.routers import DefaultRouter

from cpims_api import views

router = DefaultRouter()
router.register('date_counter', views.)

urlpatterns = [
    path('', include(router.urls)),
]