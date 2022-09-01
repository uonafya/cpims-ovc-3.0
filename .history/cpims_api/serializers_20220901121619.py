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
    OVCBursary
    OVCCASEREC,
    OVCCASEGEO,
    OVCECONOMI,
    OVCFAMILYS,
    OVCHOBBIES,
    OVCFRIENDS,
    OVCMEDICAL,
    OVCMEDICAL,
    OVCCASECAT,
    OVCCASESUB,
    OVCINTERVE,
    OVCREFERRA,
    OVCNEEDSSE,
    # FormsLogSe
    # FormsAudit
    OVCPLACEME,
    OVCCASEEVE,
    OVCCASEEVE,
    OVCCASEEVE,
    OVCCASEEVE,
    OVCCASEEVE,
    OVCREMINDE,
    OVCDOCUMEN,
    OVCPLACEME,
    OVCEDUCATI,
    OVCEDUCATI,
    OVCDISCHAR,
    OVCADVERSE,
    OVCADVERSE,
    OVCADVERSE,
    OVCFAMILYC,
    OVCCAREEVE,
    OVCCAREASS,
    OVCCAREPRI,
    OVCCARESER,
    OVCCAREEAV,
    OVCCAREF1B,
    # ListBanksS
    OVCGOKBURS,
    OVCCAREFOR,
    OVCCAREBEN,
    OVCCAREWEL,
    OVCCARECAS,
    OVCHOUSEHO,
    OVCEXPLANA,
    OVCGOALSSE,
    OVCREFERRA,
    OVCMONITOR,
    OVCMONITOR,
    OVCHIVSTAT,
    OVCHIVRISK,
    OVCHIVMANA,
    OVCDREAMSS,
    OVCBASICCR,
    OVCBASICPE,
    OVCBASICCA,
    OvcCasePer,
    OvcCaseInf,
    OVCCASELOC,
    OVCCAREQUE,
    OVCCARECPA,
    OVCSUBPOPU,
    OVCCAREIND,
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
    class Meta:
        model = OVCBursary
        fields = "__all__"
class OVCCaseRecordSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCaseRec
        fields = "__all__"
class OVCCaseGeoSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCaseGeo
        fields = "__all__"
class OVCEconomicStatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCEconomi
        fields = "__all__"
class OVCFamilyStatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCFamilyS
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
        model = OVCMedical
        fields = "__all__"
class OVCCaseCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCaseCat
        fields = "__all__"
class OVCCaseSubCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCaseSub
        fields = "__all__"
class OVCInterventionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCInterve
        fields = "__all__"
class OVCReferralSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCReferra
        fields = "__all__"
class OVCNeedsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCNeedsSe
        fields = "__all__"
class FormsLogSerializers(serializers.ModelSerializer):
    class Meta:
        model = FormsLogSe
        fields = "__all__"
class FormsAuditTrailSerializers(serializers.ModelSerializer):
    class Meta:
        model = FormsAudit
        fields = "__all__"
class OVCPlacementSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCPlaceme
        fields = "__all__"
class OVCCaseEventsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCaseEve
        fields = "__all__"
class OVCCaseEventServicesSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCaseEve
        fields = "__all__"
class OVCCaseEventCourtSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCaseEve
        fields = "__all__"
class OVCCaseEventSummonSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCaseEve
        fields = "__all__"
class OVCCaseEventClosureSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCaseEve
        fields = "__all__"
class OVCRemindersSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCReminde
        fields = "__all__"
class OVCDocumentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCDocumen
        fields = "__all__"
class OVCPlacementFollowUpSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCPlaceme
        fields = "__all__"
class OVCEducationFollowUpSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCEducati
        fields = "__all__"
class OVCEducationLevelFollowUpSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCEducati
        fields = "__all__"
class OVCDischargeFollowUpSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCDischar
        fields = "__all__"
class OVCAdverseEventsFollowUpSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCAdverse
        fields = "__all__"
class OVCAdverseEventsOtherFollowUpSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCAdverse
        fields = "__all__"
class OVCAdverseMedicalEventsFollowUpSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCAdverse
        fields = "__all__"
class OVCFamilyCareSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCFamilyC
        fields = "__all__"
class OVCCareEventsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCareEve
        fields = "__all__"
class OVCCareAssessmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCareAss
        fields = "__all__"
class OVCCarePrioritySerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCarePri
        fields = "__all__"
class OVCCareServicesSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCareSer
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
        model = ListBanksS
        fields = "__all__"
class OVCGokBursarySerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCGokBurs
        fields = "__all__"
class OVCCareFormsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCareFor
        fields = "__all__"
class OVCCareBenchmarkScoreSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCareBen
        fields = "__all__"
class OVCCareWellbeingSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCareWel
        fields = "__all__"
class OVCCareCasePlanSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCareCas
        fields = "__all__"
class OVCHouseholdDemographicsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCHouseho
        fields = "__all__"
class OVCExplanationsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCExplana
        fields = "__all__"
class OVCGoalsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCGoalsSe
        fields = "__all__"
class OVCReferralsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCReferra
        fields = "__all__"
class OVCMonitoringSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCMonitor
        fields = "__all__"
class OVCMonitoring11Serializers(serializers.ModelSerializer):
    class Meta:
        model = OVCMonitor
        fields = "__all__"
class OVCHivStatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCHivStat
        fields = "__all__"
class OVCHIVRiskScreeningSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCHIVRisk
        fields = "__all__"
class OVCHIVManagementSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCHIVMana
        fields = "__all__"
class OVCDreamsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCDreamsS
        fields = "__all__"
class OVCBasicCRSSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCBasicCR
        fields = "__all__"
class OVCBasicPersonSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCBasicPe
        fields = "__all__"
class OVCBasicCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCBasicCa
        fields = "__all__"
class OvcCasePersonsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OvcCasePer
        fields = "__all__"
class OvcCaseInformationSerializers(serializers.ModelSerializer):
    class Meta:
        model = OvcCaseInf
        fields = "__all__"
class OVCCaseLocationSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCaseLoc
        fields = "__all__"
class OVCCareQuestionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCareQue
        fields = "__all__"
class OVCCareCpara_upgradeSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCareCpa
        fields = "__all__"
class OVCSubPopulationSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCSubPopu
        fields = "__all__"
class OVCCareIndividaulCparaSerializers(serializers.ModelSerializer):
    class Meta:
        model = OVCCareInd
        fields = "__all__"
