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
        
class OVCBursarySerializers(serializers.ModelSerializer):
class OVCCaseRecordSerializers(serializers.ModelSerializer):
class OVCCaseGeoSerializers(serializers.ModelSerializer):
class OVCEconomicStatusSerializers(serializers.ModelSerializer):
class OVCFamilyStatusSerializers(serializers.ModelSerializer):
class OVCHobbiesSerializers(serializers.ModelSerializer):
class OVCFriendsSerializers(serializers.ModelSerializer):
class OVCMedicalSerializers(serializers.ModelSerializer):
class OVCMedicalSubconditionsSerializers(serializers.ModelSerializer):
class OVCCaseCategorySerializers(serializers.ModelSerializer):
class OVCCaseSubCategorySerializers(serializers.ModelSerializer):
class OVCInterventionsSerializers(serializers.ModelSerializer):
class OVCReferralSerializers(serializers.ModelSerializer):
class OVCNeedsSerializers(serializers.ModelSerializer):
class FormsLogSerializers(serializers.ModelSerializer):
class FormsAuditTrailSerializers(serializers.ModelSerializer):
class OVCPlacementSerializers(serializers.ModelSerializer):
class OVCCaseEventsSerializers(serializers.ModelSerializer):
class OVCCaseEventServicesSerializers(serializers.ModelSerializer):
class OVCCaseEventCourtSerializers(serializers.ModelSerializer):
class OVCCaseEventSummonSerializers(serializers.ModelSerializer):
class OVCCaseEventClosureSerializers(serializers.ModelSerializer):
class OVCRemindersSerializers(serializers.ModelSerializer):
class OVCDocumentsSerializers(serializers.ModelSerializer):
class OVCPlacementFollowUpSerializers(serializers.ModelSerializer):
class OVCEducationFollowUpSerializers(serializers.ModelSerializer):
class OVCEducationLevelFollowUpSerializers(serializers.ModelSerializer):
class OVCDischargeFollowUpSerializers(serializers.ModelSerializer):
class OVCAdverseEventsFollowUpSerializers(serializers.ModelSerializer):
class OVCAdverseEventsOtherFollowUpSerializers(serializers.ModelSerializer):
class OVCAdverseMedicalEventsFollowUpSerializers(serializers.ModelSerializer):
class OVCFamilyCareSerializers(serializers.ModelSerializer):
class OVCCareEventsSerializers(serializers.ModelSerializer):
class OVCCareAssessmentSerializers(serializers.ModelSerializer):
class OVCCarePrioritySerializers(serializers.ModelSerializer):
class OVCCareServicesSerializers(serializers.ModelSerializer):
class OVCCareEAVSerializers(serializers.ModelSerializer):
class OVCCareF1BSerializers(serializers.ModelSerializer):
class ListBanksSerializers(serializers.ModelSerializer):
class OVCGokBursarySerializers(serializers.ModelSerializer):
class OVCCareFormsSerializers(serializers.ModelSerializer):
class OVCCareBenchmarkScoreSerializers(serializers.ModelSerializer):
class OVCCareWellbeingSerializers(serializers.ModelSerializer):
class OVCCareCasePlanSerializers(serializers.ModelSerializer):
class OVCHouseholdDemographicsSerializers(serializers.ModelSerializer):
class OVCExplanationsSerializers(serializers.ModelSerializer):
class OVCGoalsSerializers(serializers.ModelSerializer):
class OVCReferralsSerializers(serializers.ModelSerializer):
class OVCMonitoringSerializers(serializers.ModelSerializer):
class OVCMonitoring11Serializers(serializers.ModelSerializer):
class OVCHivStatusSerializers(serializers.ModelSerializer):
class OVCHIVRiskScreeningSerializers(serializers.ModelSerializer):
class OVCHIVManagementSerializers(serializers.ModelSerializer):
class OVCDreamsSerializers(serializers.ModelSerializer):
class OVCBasicCRSSerializers(serializers.ModelSerializer):
class OVCBasicPersonSerializers(serializers.ModelSerializer):
class OVCBasicCategorySerializers(serializers.ModelSerializer):
class OvcCasePersonsSerializers(serializers.ModelSerializer):
class OvcCaseInformationSerializers(serializers.ModelSerializer):
class OVCCaseLocationSerializers(serializers.ModelSerializer):
class OVCCareQuestionsSerializers(serializers.ModelSerializer):
class OVCCareCpara_upgradeSerializers(serializers.ModelSerializer):
class OVCSubPopulationSerializers(serializers.ModelSerializer):
class OVCCareIndividaulCparaSerializers(serializers.ModelSerializer):
