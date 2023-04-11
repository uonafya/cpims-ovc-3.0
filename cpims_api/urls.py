from django.urls import path, include

from rest_framework.routers import DefaultRouter

from rest_framework.authtoken.views import obtain_auth_token

from cpims_api import views 

from rest_framework.schemas import get_schema_view;

from django.views.generic import TemplateView;


router = DefaultRouter()


router.register( 'ListBanksViewSet', views.ListBanksViewSet)
router.register( 'FormsLogViewSet', views.FormsLogViewSet)
router.register( 'FormsLogViewSet', views.FormsLogViewSet)
router.register( 'OVCBursaryViewSet', views.OVCBursaryViewSet)
router.register( 'OVCCaseRecordViewSet', views.OVCCaseRecordViewSet)

router.register( 'OVCCaseGeoViewSet', views.OVCCaseGeoViewSet)
router.register( 'OVCEconomicStatusViewSet', views.OVCEconomicStatusViewSet)
router.register( 'OVCFamilyStatusViewSet', views.OVCFamilyStatusViewSet)
router.register( 'OVCHobbiesViewSet', views.OVCHobbiesViewSet)
router.register( 'OVCFriendsViewSet', views.OVCFriendsViewSet)
router.register( 'OVCMedicalViewSet', views.OVCMedicalViewSet)
router.register( 'OVCMedicalSubconditionsViewSet', views.OVCMedicalSubconditionsViewSet)
router.register( 'OVCCaseCategoryViewSet', views.OVCCaseCategoryViewSet)
router.register( 'OVCCaseSubCategoryViewSet', views.OVCCaseSubCategoryViewSet)
router.register( 'OVCReferralViewSet', views.OVCReferralViewSet)
router.register( 'OVCPlacementViewSet', views.OVCPlacementViewSet)

# here
router.register( 'OVCCaseEventsViewSet', views.OVCCaseEventsViewSet)
router.register( 'OVCCaseEventServicesViewSet', views.OVCCaseEventServicesViewSet)
router.register( 'OVCCaseEventCourtViewSet', views.OVCCaseEventCourtViewSet)
router.register( 'OVCCaseEventSummonViewSet', views.OVCCaseEventSummonViewSet)
router.register( 'OVCCaseEventClosureViewSet', views.OVCCaseEventClosureViewSet)
router.register( 'OVCRemindersViewSet', views.OVCRemindersViewSet)
router.register( 'OVCDocumentsViewSet', views.OVCDocumentsViewSet)
router.register( 'OVCPlacementFollowUpViewSet', views.OVCPlacementFollowUpViewSet)
router.register( 'OVCDischargeFollowUpViewSet', views.OVCDischargeFollowUpViewSet)
router.register( 'OVCAdverseEventsFollowUpViewSet', views.OVCAdverseEventsFollowUpViewSet)
router.register( 'OVCAdverseEventsOtherFollowUpViewSet', views.OVCAdverseEventsOtherFollowUpViewSet)
router.register( 'OVCFamilyCareViewSet', views.OVCFamilyCareViewSet)
router.register( 'OVCCareEventsViewSet', views.OVCCareEventsViewSet)
router.register( 'OVCCareAssessmentViewSet', views.OVCCareAssessmentViewSet)
router.register( 'OVCCareEAVViewSet', views.OVCCareEAVViewSet)
router.register( 'OVCCareF1BViewSet', views.OVCCareF1BViewSet)
router.register( 'OVCGokBursaryViewSet', views.OVCGokBursaryViewSet)
router.register( 'OVCCareFormsViewSet', views.OVCCareFormsViewSet) 
router.register( 'OVCCareBenchmarkScoreViewSet', views.OVCCareBenchmarkScoreViewSet)
router.register( 'OVCCareWellbeingViewSet', views.OVCCareWellbeingViewSet) 
router.register( 'OVCCareCasePlanViewSet', views.OVCCareCasePlanViewSet) 
router.register( 'OVCHouseholdDemographicsViewSet', views.OVCHouseholdDemographicsViewSet)
router.register( 'OVCExplanationsViewSet', views.OVCExplanationsViewSet)
router.register( 'OVCReferralsViewSet', views.OVCReferralsViewSet)
router.register( 'OVCMonitoringViewSet', views.OVCMonitoringViewSet)

router.register( 'OVCMonitoring11ViewSet', views.OVCMonitoring11ViewSet) #not working

router.register( 'OVCHivStatusViewSet', views.OVCHivStatusViewSet)
router.register( 'OVCHIVRiskScreeningViewSet', views.OVCHIVRiskScreeningViewSet)
router.register( 'OVCHIVManagementViewSet', views.OVCHIVManagementViewSet)
router.register( 'OVCBasicCRSViewSet', views.OVCBasicCRSViewSet) 
router.register( 'OVCBasicPersonViewSet', views.OVCBasicPersonViewSet)
router.register( 'OVCBasicCategoryViewSet', views.OVCBasicCategoryViewSet) 
router.register( 'OvcCasePersonsViewSet', views.OvcCasePersonsViewSet)
router.register( 'OvcCaseInformationViewSet', views.OvcCaseInformationViewSet) 
router.register( 'OVCCaseLocationViewSet', views.OVCCaseLocationViewSet)
router.register( 'OVCCareQuestionsViewSet', views.OVCCareQuestionsViewSet) 
router.register( 'OVCCareCpara_upgradeViewSet', views.OVCCareCpara_upgradeViewSet)  # not working
router.register( 'OVCSubPopulationViewSet', views.OVCSubPopulationViewSet)
router.register( 'OVCCareIndividaulCparaViewSet', views.OVCCareIndividaulCparaViewSet)

# done endpoints
router.register('persons_master', views.PersonsMasterViewSets   )
router.register('ovc_household', views.OVCHouseHoldViewSets   )
router.register('ovc_chekins', views.OVCCheckinViewSets   )
router.register('ovc_sibling', views.OVCSiblingViewSet   )
router.register('reg_person_audit_trail', views.RegPersonsAuditTrailViewSet)
router.register('reg_org_unit_audit_trail', views.RegOrgUnitsAuditTrailViewSet)
router.register('reg_person_benefiaciary', views.RegPersonsBeneficiaryIdsViewSet)
router.register('reg_person_workforce', views.RegPersonsWorkforceIdsViewSet)
router.register('reg_person_ou', views.RegPersonsOrgUnitsViewSet)
router.register('reg_person_contact', views.RegPersonsContactViewSet)
router.register('reg_person_external_ids', views.RegPersonsExternalIdsViewSet)
router.register('reg_person_geo', views.RegPersonsGeoViewSet)
router.register('reg_person_types', views.RegPersonsTypesViewSet)
router.register('reg_person_siblings', views.RegPersonsSiblingsViewSet)
router.register('reg_person_gurdians', views.RegPersonsGuardiansViewSet)
router.register('reg_biometric', views.RegBiometricViewSet)
router.register('reg_person', views.RegPersonViewSet)
router.register('reg_org_unit_geography', views.RegOrgUnitGeographyViewSet)
router.register('reg_org_unit_external_id', views.RegOrgUnitExternalIDViewSet)
router.register('reg_org_unit_contact', views.RegOrgUnitContactViewSet)
router.register('ovc_care_priorioty', views.OVCCarePriorityViewSet)
router.register('ovc_exit', views.OVCExitViewSet)
router.register('ovc_education_follow_up', views.OVCEducationFollowUpViewSet)
router.register('ovc_education_level_follow_up', views.OVCEducationLevelViewSet)
router.register('ovc_viral_load', views.OvcViralLoadViewSet)
router.register('ovc_care_services', views.OvcCareServicesViewSet)
router.register('school_list', views.SchoolListViewSet)
router.register('facility_list', views.FacilityListViewSet, basename="facility_list")
router.register('reg_person', views.RegOrgUnitViewSet)
router.register('ovc_registration', views.OVCRegistrationViewSet)
router.register('reg_org_unit', views.RegOrgUnitViewSet)

# #dash
router.register('dashboard', views.MobileDashboardViewSet, basename="dashboard")

urlpatterns = [
    path('', include(router.urls)),    
    path('token-auth', obtain_auth_token, name='api_token_auth'),
    path('api_schema', get_schema_view(title='CPIMS API', description='Guide for the CPIMS REST API schema'), name='api_schema'),
    path('api_docs', TemplateView.as_view(template_name='swagger-ui.html',
        extra_context={'schema_url':'api_schema'}), name='api_docs'),
    path('docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'api_schema'}
        ), name='swagger-ui'),
]


