from django.conf.urls import url
from django.urls import path, include

from cpims_api.views import RegOrgUnitViewSet

# routers = routers.DefaultRouter()
# routers.register(r'reg_org_unit', RegOrgUnitViewSet)

urlurlpatterns = [
    # path('', include(routers.urls))
    path('reg_org_unit/', RegOrgUnitViewSet.as_view()),
]