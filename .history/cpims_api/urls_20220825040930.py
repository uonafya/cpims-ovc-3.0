from django.urls import path, include

# routers = routers.DefaultRouter()
# routers.register(r'reg_org_unit', RegOrgUnitViewSet)

urlurlpatterns = [
    # path('', include(routers.urls))
    path('reg_org_unit/', RegOrgUnitViewSet.as_view({'get': 'list'})),
]

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('date_counter', views.DateCounterViewSet)

urlpatterns = [
    path('', include(router.urls)),
]