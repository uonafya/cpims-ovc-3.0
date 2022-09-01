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
        
        
class OVCBursary(models.Model):
class OVCCaseRecord(models.Model):
class OVCCaseGeo(models.Model):
class OVCEconomicStatus(models.Model):
class OVCFamilyStatus(models.Model):
class OVCHobbies(models.Model):
class OVCFriends(models.Model):
class OVCMedical(models.Model):
class OVCMedicalSubconditions(models.Model):
class OVCCaseCategory(models.Model):
class OVCCaseSubCategory(models.Model):
class OVCInterventions(models.Model):
class OVCReferral(models.Model):
class OVCNeeds(models.Model):
class FormsLog(models.Model):
class FormsAuditTrail(models.Model):
class OVCPlacement(models.Model):
class OVCCaseEvents(models.Model):
class OVCCaseEventServices(models.Model):
class OVCCaseEventCourt(models.Model):
class OVCCaseEventSummon(models.Model):
class OVCCaseEventClosure(models.Model):
class OVCReminders(models.Model):
class OVCDocuments(models.Model):
class OVCPlacementFollowUp(models.Model):
class OVCEducationFollowUp(models.Model):
class OVCEducationLevelFollowUp(models.Model):
class OVCDischargeFollowUp(models.Model):
class OVCAdverseEventsFollowUp(models.Model):
class OVCAdverseEventsOtherFollowUp(models.Model):
class OVCAdverseMedicalEventsFollowUp(models.Model):
class OVCFamilyCare(models.Model):
class OVCCareEvents(models.Model):
class OVCCareAssessment(models.Model):
class OVCCarePriority(models.Model):
class OVCCareServices(models.Model):
class OVCCareEAV(models.Model):
class OVCCareF1B(models.Model):
class ListBanks(models.Model):
class OVCGokBursary(models.Model):
class OVCCareForms(models.Model):
class OVCCareBenchmarkScore(models.Model):
class OVCCareWellbeing(models.Model):
class OVCCareCasePlan(models.Model):
class OVCHouseholdDemographics(models.Model):
class OVCExplanations(models.Model):
class OVCGoals(models.Model):
class OVCReferrals(models.Model):
class OVCMonitoring(models.Model):
class OVCMonitoring11(models.Model):
class OVCHivStatus(models.Model):
class OVCHIVRiskScreening(models.Model):
class OVCHIVManagement(models.Model):
class OVCDreams(models.Model):
class OVCBasicCRS(models.Model):
class OVCBasicPerson(models.Model):
class OVCBasicCategory(models.Model):
class OvcCasePersons(models.Model):
class OvcCaseInformation(models.Model):
class OVCCaseLocation(models.Model):
class OVCCareQuestions(models.Model):
class OVCCareCpara_upgrade(models.Model):
class OVCSubPopulation(models.Model):
class OVCCareIndividaulCpara(models.Model):
        

