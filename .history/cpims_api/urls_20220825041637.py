from django.urls import path, include

from rest_framework.routers import DefaultRouter

from cpims_api import views

urlpatterns = [
    path('', views.RegOrgUnitViewSet.as_view()),
]