from dataclasses import fields
import imp
from pyexpat import model
from statistics import mode
from rest_framework import serializers

# models
from cpovc_access import models

# cpovc_registry
from cpovc_registry.models import (
    OVCCheckin,
    OVCSibling,
    PersonsMaster,
    RegBiometric,
    RegOrgUnit,
    RegOrgUnitsAuditTrail, 
    RegPerson, 
    RegOrgUnitContact,
    RegOrgUnitExternalID,
    RegOrgUnitGeography,
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

# cpovc_ovc
from cpovc_ovc.models import (
    OVCHouseHold,
    OVCRegistration, 
    OVCViralload, 
    OVCExit
)

# cpovc_main
from cpovc_main.models   import (
    FacilityList, 
    SchoolList
)

# cpovc_forms
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


class RegOrgUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegOrgUnit
        fields  = "__all__"
        
class OVCRegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCRegistration
        fields  = "__all__"

class RegPersonSerializers(serializers.ModelSerializer):
    class Meta: 
        model = RegPerson
        fields = "__all__"
        
class FacilityListSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = FacilityList
        fields = "__all__"
        
class SchoolistSeriallizers(serializers.ModelSerializer):
    
    class Meta:
        model = SchoolList
        fields = "__all__"
    
    
class OvcCareServicesSerializers(serializers.ModelSerializer):
    class Meta:
        model =  OVCCareServices
        fields = "__all__"

class OvcViralLoadSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCViralload
        fields = "__all__"
        
class OVCEducationFollowUpSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = OVCEducationFollowUp
        fields = "__all__"
        
class OVCEducationLevelFollowUpSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OVCEducationLevelFollowUp
        fields = "__all__"
        
class OVCExitSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OVCExit
        fields = "__all__"
        
class OVCCarePrioritySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OVCCarePriority
        fields = "__all__"
        
class RegOrgUnitContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RegOrgUnitContact
        fields = "__all__"
        
class RegOrgUnitExternalIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegOrgUnitExternalID
        fields =  "__all__"
        
class RegOrgUnitGeographySerializer(serializers.ModelSerializer):
    class Meta:
        model = RegOrgUnitGeography
        fields = "__all__"
        
class RegPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegPerson
        fields = "__all__"
        
class RegBiometricSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegBiometric
        fields = "__all__"
        
class RegPersonsGuardiansSerialzer(serializers.ModelSerializer):
    
    class Meta:
        model = RegPersonsGuardians
        fields = "__all__"
        
class RegPersonsSiblingsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RegPersonsSiblings
        fields = "__all__"
        
        
class RegPersonsTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegPersonsTypes
        fields = "__all__"
        
class RegPersonsGeoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RegPersonsGeo
        fields = "__all__"

class RegPersonsExternalIdsSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = RegPersonsExternalIds
        fields = "__all__"
        
class RegPersonsContactSerialzer(serializers.ModelSerializer):
    class Meta:
        model = RegPersonsContact
        fields = "__all__"
        
class RegPersonsOrgUnitsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RegPersonsOrgUnits
        fields = "__all__"
        
class RegPersonsWorkforceIdsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RegPersonsWorkforceIds
        fields = "__all__"
        
class RegPersonsBeneficiaryIdsSerializers(serializers.ModelSerializer):
    class Meta:
        model = RegPersonsBeneficiaryIds
        fields = "__all__"
        
class RegOrgUnitsAuditTrailSerializers(serializers.ModelSerializer):
    class Meta:
        model = RegOrgUnitsAuditTrail
        fields = "__all__"
        
class RegPersonsAuditTrailSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = RegPersonsAuditTrail
        fields = "__all__"
        
class OVCSiblingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OVCSibling
        fields = "__all__"
    
# no urls here
class OVCCheckinSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = OVCCheckin
        fields = "__all__"
        
class OVCHouseHoldSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCHouseHold
        fields = "__all__"
        
class PersonsMasterSerializers(serializers.ModelSerializer):
    
    class Meta:
        
        model = PersonsMaster
        fields = "__all__"
        
        
class OVCBursarySerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCBursary
        fields = "__all__"

class OVCCaseRecordSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCCaseRec
        fields = "__all__"

class OVCCaseGeoSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCCaseGeo
        fields = "__all__"

class OVCEconomicStatusSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCEconomi
        fields = "__all__"

class OVCFamilyStatusSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCFamilyS
        fields = "__all__"

class OVCHobbiesSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCHobbies
        fields = "__all__"

class OVCFriendsSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCFriends
        fields = "__all__"

class OVCMedicalSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCMedical
        fields = "__all__"

class OVCMedicalSubconditionsSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCMedical
        fields = "__all__"

class OVCCaseCategorySerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCCaseCat
        fields = "__all__"

class OVCCaseSubCategorySerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCCaseSub
        fields = "__all__"

class OVCInterventionsSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCInterve
        fields = "__all__"

class OVCReferralSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCReferra
        fields = "__all__"

class OVCNeedsSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCNeedsSe
        fields = "__all__"

class FormsLogSerializers(serializers.ModelSerializers):
    class Meta:
        model = FormsLogSe
        fields = "__all__"

class FormsAuditTrailSerializers(serializers.ModelSerializers):
    class Meta:
        model = FormsAudit
        fields = "__all__"

class OVCPlacementSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCPlaceme
        fields = "__all__"

class OVCCaseEventsSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCCaseEve
        fields = "__all__"

class OVCCaseEventServicesSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCCaseEve
        fields = "__all__"

class OVCCaseEventCourtSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCCaseEve
        fields = "__all__"

class OVCCaseEventSummonSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCCaseEve
        fields = "__all__"

class OVCCaseEventClosureSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCCaseEve
        fields = "__all__"

class OVCRemindersSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCReminde
        fields = "__all__"

class OVCDocumentsSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCDocumen
        fields = "__all__"

class OVCPlacementFollowUpSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCPlaceme
        fields = "__all__"

class OVCEducationFollowUpSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCEducati
        fields = "__all__"

class OVCEducationLevelFollowUpSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCEducati
        fields = "__all__"

class OVCDischargeFollowUpSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCDischar
        fields = "__all__"

class OVCAdverseEventsFollowUpSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCAdverse
        fields = "__all__"

class OVCAdverseEventsOtherFollowUpSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCAdverse
        fields = "__all__"

class OVCAdverseMedicalEventsFollowUpSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCAdverse
        fields = "__all__"

class OVCFamilyCareSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCFamilyC
        fields = "__all__"

class OVCCareEventsSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCCareEve
        fields = "__all__"

class OVCCareAssessmentSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCCareAss
        fields = "__all__"

class OVCCarePrioritySerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCCarePri
        fields = "__all__"

class OVCCareServicesSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCCareSer
        fields = "__all__"

class OVCCareEAVSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCCareEAV
        fields = "__all__"

class OVCCareF1BSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCCareF1B
        fields = "__all__"

class ListBanksSerializers(serializers.ModelSerializers):
    class Meta:
        model = ListBanksS
        fields = "__all__"

class OVCGokBursarySerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCGokBurs
        fields = "__all__"

class OVCCareFormsSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCCareFor
        fields = "__all__"

class OVCCareBenchmarkScoreSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCCareBen
        fields = "__all__"

class OVCCareWellbeingSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCCareWel
        fields = "__all__"

class OVCCareCasePlanSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCCareCas
        fields = "__all__"

class OVCHouseholdDemographicsSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCHouseho
        fields = "__all__"

class OVCExplanationsSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCExplana
        fields = "__all__"

class OVCGoalsSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCGoalsSe
        fields = "__all__"

class OVCReferralsSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCReferra
        fields = "__all__"

class OVCMonitoringSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCMonitor
        fields = "__all__"

class OVCMonitoring11Serializers(serializers.ModelSerializers):
    class Meta:
        model = OVCMonitor
        fields = "__all__"

class OVCHivStatusSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCHivStat
        fields = "__all__"

class OVCHIVRiskScreeningSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCHIVRisk
        fields = "__all__"

class OVCHIVManagementSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCHIVMana
        fields = "__all__"

class OVCDreamsSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCDreamsS
        fields = "__all__"

class OVCBasicCRSSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCBasicCR
        fields = "__all__"

class OVCBasicPersonSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCBasicPe
        fields = "__all__"

class OVCBasicCategorySerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCBasicCa
        fields = "__all__"

class OvcCasePersonsSerializers(serializers.ModelSerializers):
    class Meta:
        model = OvcCasePer
        fields = "__all__"

class OvcCaseInformationSerializers(serializers.ModelSerializers):
    class Meta:
        model = OvcCaseInf
        fields = "__all__"

class OVCCaseLocationSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCCaseLoc
        fields = "__all__"

class OVCCareQuestionsSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCCareQue
        fields = "__all__"

class OVCCareCpara_upgradeSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCCareCpa
        fields = "__all__"

class OVCSubPopulationSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCSubPopu
        fields = "__all__"

class OVCCareIndividaulCparaSerializers(serializers.ModelSerializers):
    class Meta:
        model = OVCCareInd
        fields = "__all__"

        

