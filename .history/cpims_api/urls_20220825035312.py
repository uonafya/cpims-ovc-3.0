from django.urls import include, path
from rest_framework import routers

from cpims_api.views import RegOrgUnitViewSet

routers = routers.DefaultRouter()
routers.register(r'reg_org_unit', RegOrgUnitViewSet)

urlurlpatterns = [
    path('', include(routers.urls))
]