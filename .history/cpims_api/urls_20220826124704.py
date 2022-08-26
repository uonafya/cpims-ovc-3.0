from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

from cpims_api import views

router = DefaultRouter()
router.register('ovc_care_priorioty', views.OVCCarePriorityViewSet)
router.register('ovc_exit', views.OVCExitViewSet)
router.register('ovc_education_follow_up', views.OVCEducationFollowUpViewSet)
router.register('ovc_education_level_follow_up', views.OVCEducationLevelViewSet)
router.register('ovc_viral_load', views.OvcViralLoadViewSet)
router.register('ovc_care_services', views.OvcCareServicesViewSet)
router.register('school_list', views.SchoolListViewSet)
router.register('faciity_list', views.FacilityListViewSet)
router.register('reg_person', views.RegOrgUnitViewSet)
router.register('ovc_registration', views.OVCRegistrationViewSet)
router.register('reg_org_unit', views.RegOrgUnitViewSet)

urlpatterns = [
    path('', include(router.urls)),    
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
