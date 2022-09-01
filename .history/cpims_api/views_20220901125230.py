from django.shortcuts import render

from rest_framework import viewsets



# models
from cpovc_registry.models import (
    OVCCheckin,
    OVCSibling,
    PersonsMaster,
    RegBiometric,
    RegOrgUnit,
    RegOrgUnitGeography,
    RegOrgUnitsAuditTrail,
    RegPerson,
    RegOrgUnitContact,
    RegOrgUnitExternalID,
    RegPersonsAuditTrail,
    RegPersonsBeneficiaryIds,
    RegPersonsContact,
    RegPersonsExternalIds,
    RegPersonsGeo,
    RegPersonsGuardians,
    RegPersonsOrgUnits,
    RegPersonsSiblings,
    RegPersonsTypes,
    RegPersonsWorkforceIds
)
from cpovc_ovc.models import (
    OVCHouseHold,
    OVCRegistration, 
    OVCViralload, 
    OVCExit
)
from cpovc_main.models   import (
    FacilityList, 
    SchoolList
)
from cpovc_forms.models  import (
    OVCCareServices, 
    OVCEducationFollowUp,
    OVCEducationLevelFollowUp, 
    OVCCarePriority,
    OVCBursary,
    OVCCaseRecord,
    OVCCaseGeo,
    OVCEconomicStatus,
    OVCFamilyStatus,
    OVCHobbies,
    OVCFriends,
    OVCMedical,
    OVCMedicalSubconditions,
    OVCCaseCategory,
    OVCCaseSubCategory,
    OVCReferral,
    OVCNeeds,
    FormsLog,
    FormsAuditTrail,
    OVCPlacement,
    OVCCaseEvents,
    OVCCaseEventServices,
    OVCCaseEventCourt,
    OVCCaseEventSummon,
    OVCCaseEventClosure,
    OVCReminders,
    OVCDocuments,
    OVCPlacementFollowUp,
    OVCDischargeFollowUp,
    OVCAdverseEventsFollowUp,
    OVCAdverseEventsOtherFollowUp,
    OVCFamilyCare,
    OVCCareEvents,
    OVCCareAssessment,
    OVCCareEAV,
    OVCCareF1B,
    ListBanks,
    OVCGokBursary,
    OVCCareForms,
    OVCCareBenchmarkScore,
    OVCCareWellbeing,
    OVCCareCasePlan,
    OVCHouseholdDemographics,
    OVCExplanations,
    OVCGoals,
    OVCReferrals,
    OVCMonitoring,
    OVCMonitoring11,
    OVCHivStatus,
    OVCHIVRiskScreening,
    OVCHIVManagement,
    OVCDreams,
    OVCBasicCRS,
    OVCBasicPerson,
    OVCBasicCategory,
    OvcCasePersons,
    OvcCaseInformation,
    OVCCaseLocation,
    OVCCareQuestions,
    OVCCareCpara_upgrade,
    OVCSubPopulation,
    OVCCareIndividaulCpara,
)
# 

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Create your views here.
from cpims_api.serializers import (
    OVCCheckinSerializers,
    OVCHouseHoldSerializers,
    OVCSiblingSerializer,
    PersonsMasterSerializers,
    RegBiometricSerializer,
    RegOrgUnitGeographySerializer,
    RegOrgUnitSerializer,
    OVCRegistrationSerializers,
    RegOrgUnitsAuditTrailSerializers,
    RegPersonSerializers,
    FacilityListSerializers,
    RegPersonsAuditTrailSerializers,
    RegPersonsBeneficiaryIdsSerializers,
    RegPersonsContactSerialzer,
    RegPersonsExternalIdsSerializers,
    RegPersonsGeoSerializer,
    RegPersonsGuardiansSerialzer,
    RegPersonsOrgUnitsSerializer,
    RegPersonsSiblingsSerializer,
    RegPersonsTypesSerializer,
    RegPersonsWorkforceIdsSerializer,
    SchoolistSeriallizers,
    OvcCareServicesSerializers,
    OvcViralLoadSerializers,
    OVCEducationFollowUpSerializers,
    OVCEducationLevelFollowUpSerializer,
    OVCExitSerializer,
    OVCCarePrioritySerializer,
    RegOrgUnitContactSerializer,
    RegOrgUnitExternalIDSerializer,
    
    OVCBursarySerializers,
    OVCCaseRecordSerializers,
    OVCCaseGeoSerializers,
    OVCEconomicStatusSerializers,
    OVCFamilyStatusSerializers,
    OVCHobbiesSerializers,
    OVCFriendsSerializers,
    OVCMedicalSerializers,
    OVCMedicalSubconditionsSerializers,
    OVCCaseCategorySerializers,
    OVCCaseSubCategorySerializers,
    OVCReferralSerializers,
    OVCNeedsSerializers,
    FormsLogSerializers,
    FormsAuditTrailSerializers,
    OVCPlacementSerializers,
    OVCCaseEventsSerializers,
    OVCCaseEventServicesSerializers,
    OVCCaseEventCourtSerializers,
    OVCCaseEventSummonSerializers,
    OVCCaseEventClosureSerializers,
    OVCRemindersSerializers,
    OVCDocumentsSerializers,
    OVCPlacementFollowUpSerializers,
    OVCDischargeFollowUpSerializers,
    OVCAdverseEventsFollowUpSerializers,
    OVCAdverseEventsOtherFollowUpSerializers,
    OVCFamilyCareSerializers,
    OVCCareEventsSerializers,
    OVCCareAssessmentSerializers,
    OVCCareEAVSerializers,
    OVCCareF1BSerializers,
    ListBanksSerializers,
    OVCGokBursarySerializers,
    OVCCareFormsSerializers,
    OVCCareBenchmarkScoreSerializers,
    OVCCareWellbeingSerializers,
    OVCCareCasePlanSerializers,
    OVCHouseholdDemographicsSerializers,
    OVCExplanationsSerializers,
    OVCGoalsSerializers,
    OVCReferralsSerializers,
    OVCMonitoringSerializers,
    OVCMonitoring11Serializers,
    OVCHivStatusSerializers,
    OVCHIVRiskScreeningSerializers,
    OVCHIVManagementSerializers,
    OVCDreamsSerializers,
    OVCBasicCRSSerializers,
    OVCBasicPersonSerializers,
    OVCBasicCategorySerializers,
    OvcCasePersonsSerializers,
    OvcCaseInformationSerializers,
    OVCCaseLocationSerializers,
    OVCCareQuestionsSerializers,
    OVCCareCpara_upgradeSerializers,
    OVCSubPopulationSerializers,
    OVCCareIndividaulCparaSerializers,

)

class RegOrgUnitViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = RegOrgUnit.objects.all()
    serializer_class = RegOrgUnitSerializer
    

class OVCRegistrationViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCRegistration.objects.all()
    serializer_class = OVCRegistrationSerializers
    
class RegpersonViewSet(viewsets.ModelViewSet):
    permission_classes  = (IsAuthenticated)
    queryset = RegPerson.objects.all()
    serializer_class = RegPersonSerializers
    
class FacilityListViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = FacilityList.objects.all()
    serializer_class = FacilityListSerializers
    
class SchoolListViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset  = SchoolList.objects.all()
    serializer_class = SchoolistSeriallizers
    
class OvcCareServicesViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset =  OVCCareServices.objects.all()
    serializer_class = OvcCareServicesSerializers

class OvcViralLoadViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCViralload.objects.all()
    serializer_class = OvcViralLoadSerializers
    

class OVCEducationLevelViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCEducationLevelFollowUp.objects.all()
    serializer_class = OVCEducationLevelFollowUpSerializer
    
    
class OVCEducationFollowUpViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCEducationFollowUp.objects.all()
    serializer_class = OVCEducationFollowUpSerializers
    
class OVCExitViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCExit.objects.all()
    serializer_class = OVCExitSerializer  
    
    
class OVCCarePriorityViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCarePriority.objects.all()
    serializer_class = OVCCarePrioritySerializer  
    
class RegOrgUnitContactViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = RegOrgUnitContact.objects.all()
    serializer_class = RegOrgUnitContactSerializer
    
class RegOrgUnitExternalIDViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = RegOrgUnitExternalID.objects.all()
    serializer_class = RegOrgUnitExternalIDSerializer
    
class RegOrgUnitGeographyViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = RegOrgUnitGeography.objects.all()
    serializer_class = RegOrgUnitGeographySerializer
    
class RegPersonViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = RegPerson.objects.all()
    serializer_class = RegPersonSerializers
    
class RegBiometricViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = RegBiometric.objects.all()
    serializer_class = RegBiometricSerializer
    
class RegPersonsGuardiansViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = RegPersonsGuardians.objects.all()
    serializer_class = RegPersonsGuardiansSerialzer
    
class RegPersonsSiblingsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = RegPersonsSiblings.objects.all()
    serializer_class = RegPersonsSiblingsSerializer
    
class RegPersonsTypesViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = RegPersonsTypes.objects.all()
    serializer_class = RegPersonsTypesSerializer
    
class RegPersonsGeoViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = RegPersonsGeo.objects.all()
    serializer_class = RegPersonsGeoSerializer
    
class RegPersonsExternalIdsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = RegPersonsExternalIds.objects.all()
    serializer_class = RegPersonsExternalIdsSerializers
    
class RegPersonsContactViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = RegPersonsContact.objects.all()
    serializer_class = RegPersonsContactSerialzer
    
class RegPersonsOrgUnitsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = RegPersonsOrgUnits.objects.all()
    serializer_class = RegPersonsOrgUnitsSerializer
    
class RegPersonsWorkforceIdsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = RegPersonsWorkforceIds.objects.all()
    serializer_class = RegPersonsWorkforceIdsSerializer    
    
class RegPersonsBeneficiaryIdsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = RegPersonsBeneficiaryIds.objects.all()
    serializer_class = RegPersonsBeneficiaryIdsSerializers
    
class RegOrgUnitsAuditTrailViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = RegOrgUnitsAuditTrail.objects.all()
    serializer_class = RegOrgUnitsAuditTrailSerializers
    
class RegPersonsAuditTrailViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = RegPersonsAuditTrail.objects.all()
    serializer_class = RegPersonsAuditTrailSerializers

class OVCSiblingViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCSibling.objects.all()
    serializer_class = OVCSiblingSerializer
    
# no urls here
class OVCCheckinViewSets(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCheckin.objects.all()
    serializer_class = OVCCheckinSerializers
    
class OVCHouseHoldViewSets(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCHouseHold.objects.all()
    serializer_class = OVCHouseHoldSerializers
    
class PersonsMasterViewSets(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = PersonsMaster.objects.all()
    serializer_class = PersonsMasterSerializers
    
class OVCBursaryViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCBursary.objects.all()
class OVCCaseRecordViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCaseRecord.objects.all()
class OVCCaseGeoViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCaseGeo.objects.all()
class OVCEconomicStatusViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCEconomicStatus.objects.all()
class OVCFamilyStatusViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCFamilyStatus.objects.all()
class OVCHobbiesViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCHobbies.objects.all()
class OVCFriendsViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCFriends.objects.all()
class OVCMedicalViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCMedical.objects.all()
class OVCMedicalSubconditionsViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCMedicalSubconditions.objects.all()
class OVCCaseCategoryViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCaseCategory.objects.all()
class OVCCaseSubCategoryViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCaseSubCategory.objects.all()
class OVCReferralViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCReferral.objects.all()
class OVCNeedsViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCNeeds.objects.all()
# FormsLog,
# FormsAuditTrail,
class OVCPlacementViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCPlacement.objects.all()
class OVCCaseEventsViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCaseEvents.objects.all()
class OVCCaseEventServicesViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCaseEventServices.objects.all()
class OVCCaseEventCourtViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCaseEventCourt.objects.all()
class OVCCaseEventSummonViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCaseEventSummon.objects.all()
class OVCCaseEventClosureViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCaseEventClosure.objects.all()
class OVCRemindersViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCReminders.objects.all()
class OVCDocumentsViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCDocuments.objects.all()
class OVCPlacementFollowUpViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCPlacementFollowUp.objects.all()
class OVCDischargeFollowUpViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCDischargeFollowUp.objects.all()
class OVCAdverseEventsFollowUpViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCAdverseEventsFollowUp.objects.all()
class OVCAdverseEventsOtherFollowUpViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCAdverseEventsOtherFollowUp.objects.all()
class OVCFamilyCareViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCFamilyCare.objects.all()
class OVCCareEventsViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCareEvents.objects.all()
class OVCCareAssessmentViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCareAssessment.objects.all()
class OVCCareEAVViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCareEAV.objects.all()
class OVCCareF1BViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCareF1B.objects.all()
# ListBanks,
class OVCGokBursaryViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCGokBursary.objects.all()
class OVCCareFormsViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCareForms.objects.all()
class OVCCareBenchmarkScoreViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCareBenchmarkScore.objects.all()
class OVCCareWellbeingViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCareWellbeing.objects.all()
class OVCCareCasePlanViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCareCasePlan.objects.all()
class OVCHouseholdDemographicsViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCHouseholdDemographics.objects.all()
class OVCExplanationsViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCExplanations.objects.all()
class OVCGoalsViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCGoals.objects.all()
class OVCReferralsViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCReferrals.objects.all()
class OVCMonitoringViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCMonitoring.objects.all()
class OVCMonitoring11ViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCMonitoring11.objects.all()
class OVCHivStatusViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCHivStatus.objects.all()
class OVCHIVRiskScreeningViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCHIVRiskScreening.objects.all()
class OVCHIVManagementViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCHIVManagement.objects.all()
class OVCDreamsViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCDreams.objects.all()
class OVCBasicCRSViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCBasicCRS.objects.all()
class OVCBasicPersonViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCBasicPerson.objects.all()
class OVCBasicCategoryViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCBasicCategory.objects.all()
class OvcCasePersonsViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OvcCasePersons.objects.all()
class OvcCaseInformationViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OvcCaseInformation.objects.all()
class OVCCaseLocationViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCaseLocation.objects.all()
class OVCCareQuestionsViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCareQuestions.objects.all()
class OVCCareCpara_upgradeViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCareCpara_upgrade.objects.all()
class OVCSubPopulationViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCSubPopulation.objects.all()
class OVCCareIndividaulCparaViewSet(viewsets.ModelViewset):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCareIndividaulCpara.objects.all()



    


