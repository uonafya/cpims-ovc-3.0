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
        
        
class OVCBursarySerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCBursary
        fields = "__all__"
class OVCCaseRecordSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCaseRecord
        fields = "__all__"
class OVCCaseGeoSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCaseGeo
        fields = "__all__"
class OVCEconomicStatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCEconomicStatus
        fields = "__all__"
class OVCFamilyStatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCFamilyStatus
        fields = "__all__"
class OVCHobbiesSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCHobbies
        fields = "__all__"
class OVCFriendsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCFriends
        fields = "__all__"
class OVCMedicalSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCMedical
        fields = "__all__"
class OVCMedicalSubconditionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCMedicalSubconditions
        fields = "__all__"
class OVCCaseCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCaseCategory
        fields = "__all__"
class OVCCaseSubCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCaseSubCategory
        fields = "__all__"
class OVCReferralSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCReferral
        fields = "__all__"
class OVCNeedsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCNeeds
        fields = "__all__"
class FormsLogSerializers(serializers.ModelSerializer):
    class Meta:
        model = FormsLog
        fields = "__all__"
class FormsAuditTrailSerializers(serializers.ModelSerializer):
    class Meta:
        model = FormsAuditTrail
        fields = "__all__"
class OVCPlacementSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCPlacement
        fields = "__all__"
class OVCCaseEventsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCaseEvents
        fields = "__all__"
class OVCCaseEventServicesSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCaseEventServices
        fields = "__all__"
class OVCCaseEventCourtSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCaseEventCourt
        fields = "__all__"
class OVCCaseEventSummonSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCaseEventSummon
        fields = "__all__"
class OVCCaseEventClosureSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCaseEventClosure
        fields = "__all__"
class OVCRemindersSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCReminders
        fields = "__all__"
class OVCDocumentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCDocuments
        fields = "__all__"
class OVCPlacementFollowUpSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCPlacementFollowUp
        fields = "__all__"
class OVCEducationFollowUpSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCEducationFollowUp
        fields = "__all__"
class OVCEducationLevelFollowUpSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCEducationLevelFollowUp
        fields = "__all__"
class OVCDischargeFollowUpSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCDischargeFollowUp
        fields = "__all__"
class OVCAdverseEventsFollowUpSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCAdverseEventsFollowUp
        fields = "__all__"
class OVCAdverseEventsOtherFollowUpSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCAdverseEventsOtherFollowUp
        fields = "__all__"

class OVCFamilyCareSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCFamilyCare
        fields = "__all__"
class OVCCareEventsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCareEvents
        fields = "__all__"
class OVCCareAssessmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCareAssessment
        fields = "__all__"
class OVCCarePrioritySerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCarePriority
        fields = "__all__"
class OVCCareServicesSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCareServices
        fields = "__all__"
class OVCCareEAVSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCareEAV
        fields = "__all__"
class OVCCareF1BSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCareF1B
        fields = "__all__"
class ListBanksSerializers(serializers.ModelSerializer):
    class Meta:
        model = ListBanks
        fields = "__all__"
class OVCGokBursarySerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCGokBursary
        fields = "__all__"
class OVCCareFormsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCareForms
        fields = "__all__"
class OVCCareBenchmarkScoreSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCareBenchmarkScore
        fields = "__all__"
class OVCCareWellbeingSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCareWellbeing
        fields = "__all__"
class OVCCareCasePlanSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCareCasePlan
        fields = "__all__"
class OVCHouseholdDemographicsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCHouseholdDemographics
        fields = "__all__"
class OVCExplanationsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCExplanations
        fields = "__all__"
class OVCGoalsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCGoals
        fields = "__all__"
class OVCReferralsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCReferrals
        fields = "__all__"
class OVCMonitoringSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCMonitoring
        fields = "__all__"
class OVCMonitoring11Serializers(serializers.ModelSerializer):
    class Meta:
        model = OVCMonitoring11
        fields = "__all__"
class OVCHivStatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCHivStatus
        fields = "__all__"
class OVCHIVRiskScreeningSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCHIVRiskScreening
        fields = "__all__"
class OVCHIVManagementSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCHIVManagement
        fields = "__all__"
class OVCDreamsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCDreams
        fields = "__all__"
class OVCBasicCRSSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCBasicCRS
        fields = "__all__"
class OVCBasicPersonSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCBasicPerson
        fields = "__all__"
class OVCBasicCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCBasicCategory
        fields = "__all__"
class OvcCasePersonsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OvcCasePersons
        fields = "__all__"
class OvcCaseInformationSerializers(serializers.ModelSerializer):
    class Meta:
        model = OvcCaseInformation
        fields = "__all__"
class OVCCaseLocationSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCaseLocation
        fields = "__all__"
class OVCCareQuestionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCareQuestions
        fields = "__all__"
class OVCCareCpara_upgradeSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCareCpara_upgrade
        fields = "__all__"
class OVCSubPopulationSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCSubPopulation
        fields = "__all__"
class OVCCareIndividaulCparaSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCareIndividaulCpara
        fields = "__all__"
        
class SchoolListSerializers(serializers.ModelSerializer):
    class Meta:
        model = SchoolList
        fields = "__all__"
class
class FacilityListSerializers(serializers.ModelSerializer):
    class Meta:
        model = FacilityList
        fields = "__all__"
class
class SetupGeographySerializers(serializers.ModelSerializer):
    class Meta:
        model = SetupGeography
        fields = "__all__"
class
class SetupLocationSerializers(serializers.ModelSerializer):
    class Meta:
        model = SetupLocation
        fields = "__all__"
class
class SetupListSerializers(serializers.ModelSerializer):
    class Meta:
        model = SetupList
        fields = "__all__"
class
class FormsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Forms
        fields = "__all__"
class
class ListQuestionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ListQuestions
        fields = "__all__"
class
class ListAnswersSerializers(serializers.ModelSerializer):
    class Meta:
        model = ListAnswers
        fields = "__all__"
class
class FormGenAnswersSerializers(serializers.ModelSerializer):
    class Meta:
        model = FormGenAnswers
        fields = "__all__"
class
class FormGenTextSerializers(serializers.ModelSerializer):
    class Meta:
        model = FormGenText
        fields = "__all__"
class
class FormGenDatesSerializers(serializers.ModelSerializer):
    class Meta:
        model = FormGenDates
        fields = "__all__"
class
class FormGenNumericSerializers(serializers.ModelSerializer):
    class Meta:
        model = FormGenNumeric
        fields = "__all__"
class
class AdminUploadFormsSerializers(serializers.ModelSerializer):
    class Meta:
        model = AdminUploadForms
        fields = "__all__"
class
class FormPersonParticipationSerializers(serializers.ModelSerializer):
    class Meta:
        model = FormPersonParticipation
        fields = "__all__"
class
class FormOrgUnitContributionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = FormOrgUnitContributions
        fields = "__all__"
class
class FormResChildrenSerializers(serializers.ModelSerializer):
    class Meta:
        model = FormResChildren
        fields = "__all__"
class
class FormResWorkforceSerializers(serializers.ModelSerializer):
    class Meta:
        model = FormResWorkforce
        fields = "__all__"
class
class AdminPreferencesSerializers(serializers.ModelSerializer):
    class Meta:
        model = AdminPreferences
        fields = "__all__"
class
class CoreAdverseConditionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = CoreAdverseConditions
        fields = "__all__"
class
class CoreServicesSerializers(serializers.ModelSerializer):
    class Meta:
        model = CoreServices
        fields = "__all__"
class
class CoreEncountersSerializers(serializers.ModelSerializer):
    class Meta:
        model = CoreEncounters
        fields = "__all__"
class
class CoreEncountersNotesSerializers(serializers.ModelSerializer):
    class Meta:
        model = CoreEncountersNotes
        fields = "__all__"
class
class AdminCaptureSitesSerializers(serializers.ModelSerializer):
    class Meta:
        model = AdminCaptureSites
        fields = "__all__"
class
class AdminDownloadSerializers(serializers.ModelSerializer):
    class Meta:
        model = AdminDownload
        fields = "__all__"
class
class CaptureTaskTrackerSerializers(serializers.ModelSerializer):
    class Meta:
        model = CaptureTaskTracker
        fields = "__all__"
class
class ListReportsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ListReports
        fields = "__all__"
class
class ListReportsParametersSerializers(serializers.ModelSerializer):
    class Meta:
        model = ListReportsParameters
        fields = "__all__"
class
class ReportsSetsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReportsSets
        fields = "__all__"
class
class ReportsSetsOrgUnitsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReportsSetsOrgUnits
        fields = "__all__"
class
class RegTempSerializers(serializers.ModelSerializer):
    class Meta:
        model = RegTemp
        fields = "__all__"
class
Serializers(serializers.ModelSerializer):
class Meta:
    model = class

fields = "__all__"
