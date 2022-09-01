from django.shortcuts import render
from cpims_api import serializers

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
    
class OVCBursaryViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCBursary.objects.all()
    serializers_class =OVCBursary 
class OVCCaseRecordViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCaseRecord.objects.all()
    serializers_class =OVCCaseRecord 
class OVCCaseGeoViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCaseGeo.objects.all()
    serializers_class =OVCCaseGeo 
class OVCEconomicStatusViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCEconomicStatus.objects.all()
    serializers_class =OVCEconomicStatus 
class OVCFamilyStatusViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCFamilyStatus.objects.all()
    serializers_class =OVCFamilyStatus 
class OVCHobbiesViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCHobbies.objects.all()
    serializers_class =OVCHobbies 
class OVCFriendsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCFriends.objects.all()
    serializers_class =OVCFriends 
class OVCMedicalViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCMedical.objects.all()
    serializers_class =OVCMedical 
class OVCMedicalSubconditionsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCMedicalSubconditions.objects.all()
    serializers_class =OVCMedicalSubconditions 
class OVCCaseCategoryViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCaseCategory.objects.all()
    serializers_class =OVCCaseCategory 
class OVCCaseSubCategoryViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCaseSubCategory.objects.all()
    serializers_class =OVCCaseSubCategory 
class OVCReferralViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCReferral.objects.all()
    serializers_class =OVCReferral 
class OVCNeedsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCNeeds.objects.all()
    serializers_class =OVCNeeds 
# FormsLog,
# FormsAuditTrail,
class OVCPlacementViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCPlacement.objects.all()
    serializers_class =OVCPlacement 
class OVCCaseEventsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCaseEvents.objects.all()
    serializers_class =OVCCaseEvents 
class OVCCaseEventServicesViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCaseEventServices.objects.all()
    serializers_class =OVCCaseEventServices 
class OVCCaseEventCourtViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCaseEventCourt.objects.all()
    serializers_class =OVCCaseEventCourt 
class OVCCaseEventSummonViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCaseEventSummon.objects.all()
    serializers_class =OVCCaseEventSummon 
class OVCCaseEventClosureViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCaseEventClosure.objects.all()
    serializers_class =OVCCaseEventClosure 
class OVCRemindersViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCReminders.objects.all()
    serializers_class =OVCReminders 
class OVCDocumentsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCDocuments.objects.all()
    serializers_class =OVCDocuments 
class OVCPlacementFollowUpViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCPlacementFollowUp.objects.all()
    serializers_class =OVCPlacementFollowUp 
class OVCDischargeFollowUpViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCDischargeFollowUp.objects.all()
    serializers_class =OVCDischargeFollowUp 
class OVCAdverseEventsFollowUpViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCAdverseEventsFollowUp.objects.all()
    serializers_class =OVCAdverseEventsFollowUp 
class OVCAdverseEventsOtherFollowUpViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCAdverseEventsOtherFollowUp.objects.all()
    serializers_class =OVCAdverseEventsOtherFollowUp 
class OVCFamilyCareViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCFamilyCare.objects.all()
    serializers_class =OVCFamilyCare 
class OVCCareEventsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCareEvents.objects.all()
    serializers_class =OVCCareEvents 
class OVCCareAssessmentViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCareAssessment.objects.all()
    serializers_class =OVCCareAssessment 
class OVCCareEAVViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCareEAV.objects.all()
    serializers_class =OVCCareEAV 
class OVCCareF1BViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCareF1B.objects.all()
    serializers_class =OVCCareF1B 
# ListBanks,
class OVCGokBursaryViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCGokBursary.objects.all()
    serializers_class =OVCGokBursary 
class OVCCareFormsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCareForms.objects.all()
    serializers_class =OVCCareForms 
class OVCCareBenchmarkScoreViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCareBenchmarkScore.objects.all()
    serializers_class =OVCCareBenchmarkScore 
class OVCCareWellbeingViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCareWellbeing.objects.all()
    serializers_class =OVCCareWellbeing 
class OVCCareCasePlanViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCareCasePlan.objects.all()
    serializers_class =OVCCareCasePlan 
class OVCHouseholdDemographicsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCHouseholdDemographics.objects.all()
    serializers_class =OVCHouseholdDemographics 
class OVCExplanationsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCExplanations.objects.all()
    serializers_class =OVCExplanations 
class OVCGoalsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCGoals.objects.all()
    serializers_class =OVCGoals 
class OVCReferralsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCReferrals.objects.all()
    serializers_class =OVCReferrals 
class OVCMonitoringViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCMonitoring.objects.all()
    serializers_class =OVCMonitoring 
class OVCMonitoring11ViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCMonitoring11.objects.all()
    serializers_class =OVCMonitoring11 
class OVCHivStatusViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCHivStatus.objects.all()
    serializers_class =OVCHivStatus 
class OVCHIVRiskScreeningViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCHIVRiskScreening.objects.all()
    serializers_class =OVCHIVRiskScreening 
class OVCHIVManagementViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCHIVManagement.objects.all()
    serializers_class =OVCHIVManagement 
class OVCDreamsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCDreams.objects.all()
    serializers_class =OVCDreams 
class OVCBasicCRSViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCBasicCRS.objects.all()
    serializers_class =OVCBasicCRS 
class OVCBasicPersonViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCBasicPerson.objects.all()
    serializers_class =OVCBasicPerson 
class OVCBasicCategoryViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCBasicCategory.objects.all()
    serializers_class =OVCBasicCategory 
class OvcCasePersonsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OvcCasePersons.objects.all()
    serializers_class =OvcCasePersons 
class OvcCaseInformationViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OvcCaseInformation.objects.all()
    serializers_class =OvcCaseInformation 
class OVCCaseLocationViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCaseLocation.objects.all()
    serializers_class =OVCCaseLocation 
class OVCCareQuestionsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCareQuestions.objects.all()
    serializers_class =OVCCareQuestions 
class OVCCareCpara_upgradeViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCareCpara_upgrade.objects.all()
    serializers_class =OVCCareCpara_upgrade 
class OVCSubPopulationViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCSubPopulation.objects.all()
    serializers_class =OVCSubPopulation 
class OVCCareIndividaulCparaViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCareIndividaulCpara.objects.all()
    serializers_class =OVCCareIndividaulCpara 



    


