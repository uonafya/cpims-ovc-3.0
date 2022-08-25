from django.urls import path, include

from rest_framework.routers import DefaultRouter

from cpims_api import views

router = DefaultRouter()
router.register('reg_org_unit', views.RegOrgUnitViewSet,)

urlpatterns = [
    path('', include(router.urls)),
]
