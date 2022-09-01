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
    OVCCarePriority
)




from django.contrib.auth import authenticate

from django.contrib.auth.models import update_last_login
from rest_framework import serializers

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
        
class OVCBursary
class OVCCaseRecord
class OVCCaseGeo
class OVCEconomicStatus
class OVCFamilyStatus
class OVCHobbies
class OVCFriends
class OVCMedical
class OVCMedicalSubconditions
class OVCCaseCategory
class OVCCaseSubCategory
class OVCInterventions
class OVCReferral
class OVCNeeds
class FormsLog
class FormsAuditTrail
class OVCPlacement
class OVCCaseEvents
class OVCCaseEventServices
class OVCCaseEventCourt
class OVCCaseEventSummon
class OVCCaseEventClosure
class OVCReminders
class OVCDocuments
class OVCPlacementFollowUp
class OVCEducationFollowUp
class OVCEducationLevelFollowUp
class OVCDischargeFollowUp
class OVCAdverseEventsFollowUp
class OVCAdverseEventsOtherFollowUp
class OVCAdverseMedicalEventsFollowUp
class OVCFamilyCare
class OVCCareEvents
class OVCCareAssessment
class OVCCarePriority
class OVCCareServices
class OVCCareEAV
class OVCCareF1B
class ListBanks
class OVCGokBursary
class OVCCareForms
class OVCCareBenchmarkScore
class OVCCareWellbeing
class OVCCareCasePlan
class OVCHouseholdDemographics
class OVCExplanations
class OVCGoals
class OVCReferrals
class OVCMonitoring
class OVCMonitoring11
class OVCHivStatus
class OVCHIVRiskScreening
class OVCHIVManagement
class OVCDreams
class OVCBasicCRS
class OVCBasicPerson
class OVCBasicCategory
class OvcCasePersons
class OvcCaseInformation
class OVCCaseLocation
class OVCCareQuestions
class OVCCareCpara_upgrade
class OVCSubPopulation
class OVCCareIndividaulCpara
