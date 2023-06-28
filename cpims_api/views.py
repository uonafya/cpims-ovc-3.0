from datetime import datetime, date

from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render

from rest_framework import viewsets,status,mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response
from django.db.models import Count

from cpovc_auth.models import *
from cpovc_ovc.models import  *
from cpovc_main.functions import *
from cpovc_ovc.functions import (
    ovc_registration, get_hh_members, get_ovcdetails, gen_cbo_id, search_ovc,
    search_master, get_school, get_health, manage_checkins, ovc_management,
    get_exit_org)
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

from cpovc_main.models  import  *

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

# Create your views here.
from cpims_api.serializers import *
from notifications.views import JsonResponse


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
    queryset = OVCHouseHold.objects.filter(is_void=False)
    serializer_class = OVCHouseHoldSerializers

    def destroy(self, request, *args, **kwargs):
        OVCHouseHold.soft_delete()
        return "Ok"

    # def list(self, request):
    #     raise MethodNotAllowed('GET', detail='Method "GET" not allowed without lookup')

    # def create(self, request):
    #     raise MethodNotAllowed(method='POST')

class PersonsMasterViewSets(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = PersonsMaster.objects.all()
    serializer_class = PersonsMasterSerializers

class OVCBursaryViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCBursary.objects.all()
    serializer_class = OVCBursarySerializers
class OVCCaseRecordViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCaseRecord.objects.all()
    serializer_class = OVCCaseRecordSerializers
class OVCCaseGeoViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCaseGeo.objects.all()
    serializer_class = OVCCaseGeoSerializers
class OVCEconomicStatusViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCEconomicStatus.objects.all()
    serializer_class = OVCEconomicStatusSerializers
class OVCFamilyStatusViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCFamilyStatus.objects.all()
    serializer_class = OVCFamilyStatusSerializers
class OVCHobbiesViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCHobbies.objects.all()
    serializer_class = OVCHobbiesSerializers
class OVCFriendsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCFriends.objects.all()
    serializer_class = OVCFriendsSerializers
class OVCMedicalViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCMedical.objects.all()
    serializer_class = OVCMedicalSerializers
class OVCMedicalSubconditionsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCMedicalSubconditions.objects.all()
    serializer_class = OVCMedicalSubconditionsSerializers
class OVCCaseCategoryViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCaseCategory.objects.all()
    serializer_class = OVCCaseCategorySerializers
class OVCCaseSubCategoryViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCaseSubCategory.objects.all()
    serializer_class = OVCCaseSubCategorySerializers
class OVCReferralViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCReferral.objects.all()
    serializer_class = OVCReferralSerializers
class OVCNeedsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCNeeds.objects.all()
    serializer_class = OVCNeedsSerializers
# FormsLog,
# FormsAuditTrail,
class OVCPlacementViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCPlacement.objects.all()
    serializer_class = OVCPlacementSerializers
class OVCCaseEventsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCaseEvents.objects.all()
    serializer_class = OVCCaseEventsSerializers
class OVCCaseEventServicesViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCaseEventServices.objects.all()
    serializer_class = OVCCaseEventServicesSerializers
class OVCCaseEventCourtViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCaseEventCourt.objects.all()
    serializer_class = OVCCaseEventCourtSerializers
class OVCCaseEventSummonViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCaseEventSummon.objects.all()
    serializer_class = OVCCaseEventSummonSerializers
class OVCCaseEventClosureViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCaseEventClosure.objects.all()
    serializer_class = OVCCaseEventClosureSerializers
class OVCRemindersViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCReminders.objects.all()
    serializer_class = OVCRemindersSerializers
class OVCDocumentsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCDocuments.objects.all()
    serializer_class = OVCDocumentsSerializers
class OVCPlacementFollowUpViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCPlacementFollowUp.objects.all()
    serializer_class = OVCPlacementFollowUpSerializers
class OVCDischargeFollowUpViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCDischargeFollowUp.objects.all()
    serializer_class = OVCDischargeFollowUpSerializers
class OVCAdverseEventsFollowUpViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCAdverseEventsFollowUp.objects.all()
    serializer_class = OVCAdverseEventsFollowUpSerializers
class OVCAdverseEventsOtherFollowUpViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCAdverseEventsOtherFollowUp.objects.all()
    serializer_class = OVCAdverseEventsOtherFollowUpSerializers
class OVCFamilyCareViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCFamilyCare.objects.all()
    serializer_class = OVCFamilyCareSerializers
class OVCCareEventsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCareEvents.objects.all()
    serializer_class = OVCCareEventsSerializers
class OVCCareAssessmentViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCareAssessment.objects.all()
    serializer_class = OVCCareAssessmentSerializers
class OVCCareEAVViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCareEAV.objects.all()
    serializer_class = OVCCareEAVSerializers
class OVCCareF1BViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCareF1B.objects.all()
    serializer_class = OVCCareF1BSerializers
# ListBanks,
class OVCGokBursaryViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCGokBursary.objects.all()
    serializer_class = OVCGokBursarySerializers
class OVCCareFormsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCareForms.objects.all()
    serializer_class = OVCCareFormsSerializers
class OVCCareBenchmarkScoreViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCareBenchmarkScore.objects.all()
    serializer_class = OVCCareBenchmarkScoreSerializers
class OVCCareWellbeingViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCareWellbeing.objects.all()
    serializer_class = OVCCareWellbeingSerializers
class OVCCareCasePlanViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCareCasePlan.objects.all()
    serializer_class = OVCCareCasePlanSerializers
class OVCHouseholdDemographicsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCHouseholdDemographics.objects.all()
    serializer_class = OVCHouseholdDemographicsSerializers
class OVCExplanationsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCExplanations.objects.all()
    serializer_class = OVCExplanationsSerializers
class OVCGoalsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCGoals.objects.all()
    serializer_class = OVCGoalsSerializers
class OVCReferralsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCReferrals.objects.all()
    serializer_class = OVCReferralsSerializers
class OVCMonitoringViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCMonitoring.objects.all()
    serializer_class = OVCMonitoringSerializers
class OVCMonitoring11ViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCMonitoring11.objects.all()
    serializer_class = OVCMonitoring11Serializers
class OVCHivStatusViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCHivStatus.objects.all()
    serializer_class = OVCHivStatusSerializers
class OVCHIVRiskScreeningViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCHIVRiskScreening.objects.all()
    serializer_class = OVCHIVRiskScreeningSerializers
class OVCHIVManagementViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCHIVManagement.objects.all()
    serializer_class = OVCHIVManagementSerializers
class OVCDreamsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCDreams.objects.all()
    serializer_class = OVCDreamsSerializers
class OVCBasicCRSViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCBasicCRS.objects.all()
    serializer_class = OVCBasicCRSSerializers
class OVCBasicPersonViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCBasicPerson.objects.all()
    serializer_class = OVCBasicPersonSerializers
class OVCBasicCategoryViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCBasicCategory.objects.all()
    serializer_class = OVCBasicCategorySerializers
class OvcCasePersonsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OvcCasePersons.objects.all()
    serializer_class = OvcCasePersonsSerializers
class OvcCaseInformationViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OvcCaseInformation.objects.all()
    serializer_class = OvcCaseInformationSerializers
class OVCCaseLocationViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCaseLocation.objects.all()
    serializer_class = OVCCaseLocationSerializers
class OVCCareQuestionsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCareQuestions.objects.all()
    serializer_class = OVCCareQuestionsSerializers
class OVCCareCpara_upgradeViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCareCpara_upgrade.objects.all()
    serializer_class = OVCCareCpara_upgradeSerializers
class OVCSubPopulationViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCSubPopulation.objects.all()
    serializer_class = OVCSubPopulationSerializers
class OVCCareIndividaulCparaViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = OVCCareIndividaulCpara.objects.all()
    serializer_class = OVCCareIndividaulCparaSerializers

class FormsLogViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = FormsLog.objects.all()
    serializer_class = FormsLogSerializers

class FormsAuditTrailViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = FormsAuditTrail.objects.all()
    serializer_class = FormsAuditTrailSerializers


class ListBanksViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = ListBanks.objects.all()
    serializer_class = ListBanksSerializers
class SchoolListViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    queryset = SchoolList.objects.all()
    serializer_class = SchoolistSeriallizers
class SetupGeographyViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    queryset = SetupGeography.objects.all()
    serializer_class = SetupGeographySerializers
class SetupLocationViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    queryset = SetupLocation.objects.all()
    serializer_class = SetupLocationSerializers
class SetupListViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    queryset = SetupList.objects.all()
    serializer_class = SetupListSerializers
class FormsViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    queryset = Forms.objects.all()
    serializer_class = FormsSerializers
class ListQuestionsViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    queryset = ListQuestions.objects.all()
    serializer_class = ListQuestionsSerializers
class ListAnswersViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    queryset = ListAnswers.objects.all()
    serializer_class = ListAnswersSerializers
class FormGenAnswersViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    queryset = FormGenAnswers.objects.all()
    serializer_class = FormGenAnswersSerializers
class FormGenTextViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    queryset = FormGenText.objects.all()
    serializer_class = FormGenTextSerializers
class FormGenDatesViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    queryset = FormGenDates.objects.all()
    serializer_class = FormGenDatesSerializers
class FormGenNumericViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    queryset = FormGenNumeric.objects.all()
    serializer_class = FormGenNumericSerializers
class AdminUploadFormsViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    queryset = AdminUploadForms.objects.all()
    serializer_class = AdminUploadFormsSerializers
class FormPersonParticipationViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    queryset = FormPersonParticipation.objects.all()
    serializer_class = FormPersonParticipationSerializers
class FormOrgUnitContributionsViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    queryset = FormOrgUnitContributions.objects.all()
    serializer_class = FormOrgUnitContributionsSerializers
class FormResChildrenViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    queryset = FormResChildren.objects.all()
    serializer_class = FormResChildrenSerializers
class FormResWorkforceViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    queryset = FormResWorkforce.objects.all()
    serializer_class = FormResWorkforceSerializers
class AdminPreferencesViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    queryset = AdminPreferences.objects.all()
    serializer_class = AdminPreferencesSerializers
class CoreAdverseConditionsViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    queryset = CoreAdverseConditions.objects.all()
    serializer_class = CoreAdverseConditionsSerializers
class CoreServicesViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    queryset = CoreServices.objects.all()
    serializer_class = CoreServicesSerializers
class CoreEncountersViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    queryset = CoreEncounters.objects.all()
    serializer_class = CoreEncountersSerializers
class CoreEncountersNotesViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    queryset = CoreEncountersNotes.objects.all()
    serializer_class = CoreEncountersNotesSerializers
class AdminCaptureSitesViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    queryset = AdminCaptureSites.objects.all()
    serializer_class = AdminCaptureSitesSerializers
class AdminDownloadViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    queryset = AdminDownload.objects.all()
    serializer_class = AdminDownloadSerializers
class CaptureTaskTrackerViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    queryset = CaptureTaskTracker.objects.all()
    serializer_class = CaptureTaskTrackerSerializers
class ListReportsViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    queryset = ListReports.objects.all()
    serializer_class = ListReportsSerializers
class ListReportsParametersViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    queryset = ListReportsParameters.objects.all()
    serializer_class = ListReportsParametersSerializers
class ReportsSetsViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    queryset = ReportsSets.objects.all()
    serializer_class = ReportsSetsSerializers
class ReportsSetsOrgUnitsViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    queryset = ReportsSetsOrgUnits.objects.all()
    serializer_class = ReportsSetsOrgUnitsSerializers
class RegTempViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    queryset = RegTemp.objects.all()
    serializer_class = RegTempSerializers

class MobileDashboardViewSet(viewsets.ViewSet):
    """Viewset to return the mobile dashboard data."""

    queryset = OVCCaseRecord.objects.filter(is_void=False)

    def get_queryset(self):
        return self.queryset

    def list(self, request):
        try:
            dash = {}
            vals = {'TBVC': 0, 'TBGR': 0, 'TWGE': 0, 'TWNE': 0}
            person_types = RegPersonsTypes.objects.filter(
                is_void=False, date_ended=None).values(
                'person_type_id').annotate(dc=Count('person_type_id'))
            for person_type in person_types:
                vals[person_type['person_type_id']] = person_type['dc']
            dash['children'] = vals['TBVC']
            dash['guardian'] = vals['TBGR']
            dash['government'] = vals['TWGE']
            dash['ngo'] = vals['TWNE']
            # Get org units
            org_units = RegOrgUnit.objects.filter(is_void=False).count()
            dash['org_units'] = org_units
            # Case records counts
            case_records = self.get_queryset()
            case_counts = case_records.count()
            dash['case_records'] = case_counts
            # Workforce members
            workforce_members = RegPersonsExternalIds.objects.filter(
                identifier_type_id='IWKF', is_void=False).count()
            dash['workforce_members'] = workforce_members
            # Case categories to find pending cases
            pending_cases = OVCCaseCategory.objects.filter(
                is_void=False)
            pending_count = pending_cases.exclude(
                case_id__summon_status=True).count()
            dash['pending_cases'] = pending_count
            # Child registrations
            case_regs = {}
            # Case Records
            ovc_regs = case_records.values(
                'date_case_opened').annotate(unit_count=Count('date_case_opened'))
            for ovc_reg in ovc_regs:
                the_date = ovc_reg['date_case_opened']
                cdate = datetime.strftime(the_date, '%d-%b-%y')
                case_regs[str(cdate)] = ovc_reg['unit_count']
            # Case categories Top 5
            case_categories = pending_cases.values(
                'case_category').annotate(unit_count=Count(
                'case_category')).order_by('-unit_count')
            dash['case_regs'] = case_regs
            dash['case_cats'] = case_categories
        except Exception as e:
            print('error with dash - {}'.format(str(e)))
            dash = {}
            dash['children'] = 0
            dash['guardian'] = 0
            dash['government'] = 0
            dash['ngo'] = 0
            dash['org_units'] = 0
            dash['case_records'] = 0
            dash['workforce_members'] = 0
            dash['pending_cases'] = 0
            dash['case_regs'] = []
            dash['case_categories'] = 0
            serializer = DashboardSerializer(dash)
            return Response(serializer.data)
        else:
            serializer = DashboardSerializer(dash)
            return Response(serializer.data)



class OVCViewSet(viewsets.ViewSet):
    queryset = OVCRegistration.objects.filter(is_void=False)

    def list(self, request, id=None):
        try:
            if id is not None:
                ovc_id = int(id)
                print(ovc_id)
                try:
                    child = RegPerson.objects.get(is_void=False, id=ovc_id)
                except RegPerson.DoesNotExist:
                    child=None
                try:
                    creg = OVCRegistration.objects.get(is_void=False, person=ovc_id)
                    print(creg)
                    days = 0
                    if not creg.is_active and creg.exit_date:
                        edate = creg.exit_date
                        tdate = date.today()
                        days = (tdate - edate).days
                    print('exit days', days)
                    allow_edit = False if days > 90 else True
                    params = {}
                    gparams = {}
                except OVCRegistration.DoesNotExist:
                    creg=None
                    params=None
                    gparams=None
                # Get guardians
                try:
                    guardians = RegPersonsGuardians.objects.filter(
                        is_void=False, child_person=child.id)
                    guids = [guardian.guardian_person_id for guardian in guardians]
                    guids.append(child.id)
                except RegPersonsGuardians.DoesNotExist:
                    guardians=None
                    guids=None

                try:
                    extids = RegPersonsExternalIds.objects.filter(person__in=guids)
                    for extid in extids:
                        if extid.person_id == child.id:
                            params[extid.identifier_type_id] = extid.identifier
                        else:
                            gkey = f"{extid.person_id}_{extid.identifier_type_id}"
                            gparams[gkey] = extid.identifier
                    # Health details
                    health = {}
                    if creg.hiv_status == 'HSTP':
                        health = get_health(ovc_id)
                    # School details
                    school = {}
                    if creg.school_level != 'SLNS':
                        school = get_school(ovc_id)
                except RegPersonsExternalIds.DoesNotExist:
                    extid=None
                    health=None
                    school=None
                # Get household
                try:
                    hhold = OVCHHMembers.objects.get(is_void=False, person=child.id)
                    # Get HH members
                    hhid = hhold.house_hold
                    hhmqs = OVCHHMembers.objects.filter(is_void=False, house_hold=hhid).order_by("-hh_head")
                    hhmembers = list(hhmqs.exclude(person=child.id))
                except OVCHHMembers.DoesNotExist:
                    hhold = None
                    hhmqs = None
                    hhmembers = None
                # Viral load
                vload = OVCViralload.objects.filter(is_void=False, person=ovc_id).order_by("-viral_date")[:1]
                vl_sup, v_val, v_dt = 'Missing', None, None
                if vload:
                    for vl in vload:
                        v_val = vl.viral_load
                        v_dt = vl.viral_date
                    vl_sup = 'YES' if not v_val or v_val < 1000 else 'NO'
                # Get siblings
                siblings = RegPersonsSiblings.objects.filter(is_void=False, child_person=child.id)
                # Get services
                servs = {
                    'FSAM': 'f1a',
                    'FCSI': 'fcsi',
                    'FHSA': 'fhva',
                    'cpr': 'cpr',
                    'wba': 'wba',
                    'CPAR': 'CPAR',
                    'WBG': 'WBG'
                }
                services = {key: 0 for key in servs.values()}
                sqs = OVCCareEvents.objects.filter(Q(person=child.id) | Q(house_hold=hhid))
                sqs = sqs.filter(is_void=False).values('event_type_id').annotate(total=Count('event_type_id')).order_by(
                    'total')
                for serv in sqs:
                    item = serv['event_type_id']
                    item_count = serv['total']
                    if item in servs:
                        item_key = servs[item]
                        services[item_key] = item_count
                # Re-usable values
                check_fields = [
                    'relationship_type_id',
                    'school_level_id',
                    'hiv_status_id',
                    'immunization_status_id',
                    'art_status_id',
                    'school_type_id',
                    'class_level_id'
                ]
                vals = get_dict(field_name=check_fields)
                wellbeing_services = {
                    'wba': services['wba'],
                    'WBG': services['WBG']
                }
                child_hiv_status = OVCRegistration.objects.get(person=id).hiv_status
                try:
                    care_giver = RegPerson.objects.get(id=OVCRegistration.objects.get(person=child).caretaker_id)
                except RegPerson.DoesNotExist:
                    care_giver = None
                    print('Caregiver does not exist for child: %s' % child.id)

                # Rest of the code...

                dataset = {
                    'status': 200,
                    'child': child,
                    'params': params,
                    'child_hiv_status': child_hiv_status,
                    'guardians': guardians,
                    'siblings': siblings,
                    'hhold': hhold,
                    'creg': creg,
                    'extids': gparams,
                    'health': health,
                    'hhmembers': hhmembers,
                    'school': school,
                    'care_giver': care_giver,
                    'services': services,
                    'allow_edit': allow_edit,
                    'suppression': vl_sup,
                    'well_being_count': wellbeing_services
                }
                # print(f"{dataset} child")

                serializer = OVCSerializer(dataset)
                print(dataset)
                return Response(serializer.data)
            else:
                covc_ids = RegPerson.objects.filter(is_void=False, designation="COVC").values_list("id", flat=True)
                dataset_list = []
                print(covc_ids)

                for covc_id in covc_ids:

                    child = RegPerson.objects.get(is_void=False, id=covc_id)
                    try:
                        creg = OVCRegistration.objects.get(is_void=False, person_id=covc_id)
                        days = 0
                        if not creg.is_active and creg.exit_date:
                            edate = creg.exit_date
                            tdate = date.today()
                            days = (tdate - edate).days
                        print('exit days', days)
                        allow_edit = False if days > 90 else True
                        params = {}
                        gparams = {}
                        # Health details
                        health = {}
                        if creg.hiv_status == 'HSTP':
                            health = get_health(covc_id)
                        # School details
                        school = {}
                        if creg.school_level != 'SLNS':
                            school = get_school(covc_id)
                    except OVCRegistration.DoesNotExist:
                        creg=None
                        params=None
                        gparams=None
                        health=None
                        school=None


                    # Get guardians
                    try:
                        guardians = RegPersonsGuardians.objects.filter(
                            is_void=False, child_person_id=child.id)
                        guids = [guardian.guardian_person_id for guardian in guardians]
                        guids.append(child.id)
                    except RegPersonsGuardians.DoesNotExist:
                        guardians=None
                        guids=None
                    try:
                        extids = RegPersonsExternalIds.objects.filter(person_id__in=guids)
                        for extid in extids:
                            if extid.person_id == child.id:
                                params[extid.identifier_type_id] = extid.identifier
                            else:
                                gkey = f"{extid.person_id}_{extid.identifier_type_id}"
                                gparams[gkey] = extid.identifier
                    except RegPersonsExternalIds.DoesNotExist:
                        extidS=None
                        gparams[gkey]=None

                    # Get household
                    try:
                        hhold = OVCHHMembers.objects.get(is_void=False, person=child.id)
                        # Get HH members
                        hhid = hhold.house_hold
                        hhmqs = OVCHHMembers.objects.filter(is_void=False, house_hold=hhid).order_by("-hh_head")
                        hhmembers = list(hhmqs.exclude(person=child.id))
                    except OVCHHMembers.DoesNotExist:
                        hhold=None
                        hhmqs = None
                        hhmembers = None
                        hhid=None

                    # Viral load
                    try:
                        vload = OVCViralload.objects.filter(is_void=False, person_id=covc_id).order_by("-viral_date")[
                                :1]
                        vl_sup, v_val, v_dt = 'Missing', None, None
                        if vload:
                            for vl in vload:
                                v_val = vl.viral_load
                                v_dt = vl.viral_date
                            vl_sup = 'YES' if not v_val or v_val < 1000 else 'NO'
                    except OVCViralload.DoesNotExist:
                        vl_sup=None
                    # Get siblings
                    try:
                        siblings = RegPersonsSiblings.objects.filter(is_void=False, child_person_id=child.id)
                    except RegPersonsSiblings.DoesNotExist:
                        siblings=None
                    # Get services

                try:
                    servs = {
                        'FSAM': 'f1a',
                        'FCSI': 'fcsi',
                        'FHSA': 'fhva',
                        'cpr': 'cpr',
                        'wba': 'wba',
                        'CPAR': 'CPAR',
                        'WBG': 'WBG'
                    }
                    services = {key: 0 for key in servs.values()}
                    sqs = OVCCareEvents.objects.filter(Q(person=child.id) | Q(house_hold=hhid))
                    sqs = sqs.filter(is_void=False).values('event_type_id').annotate(
                        total=Count('event_type_id')).order_by(
                        'total')
                    for serv in sqs:
                        item = serv['event_type_id']
                        item_count = serv['total']
                        if item in servs:
                            item_key = servs[item]
                            services[item_key] = item_count

                except OVCCareEvents.DoesNotExist:
                    services=None

                    # Re-usable values

                try:

                    check_fields = [
                        'relationship_type_id',
                        'school_level_id',
                        'hiv_status_id',
                        'immunization_status_id',
                        'art_status_id',
                        'school_type_id',
                        'class_level_id'
                    ]
                    vals = get_dict(field_name=check_fields)
                    wellbeing_services = {
                        'wba': services['wba'],
                        'WBG': services['WBG']
                    }

                except OVCCareEvents.DoesNotExist:
                    wellbeing_services=None


                try:
                    child_hiv_status = OVCRegistration.objects.get(person=id).hiv_status
                except OVCRegistration.DoesNotExist:
                    child_hiv_status=None


                try:

                    care_giver = RegPerson.objects.get(id=OVCRegistration.objects.get(person=child).caretaker_id)
                except RegPerson.DoesNotExist:
                    care_giver = None
                    print('Caregiver does not exist for child: %s' % child.id)

                # Rest of the code...

                dataset = {
                    'status': 200,
                    'child': child,
                    'params': params,
                    'child_hiv_status': child_hiv_status,
                    'guardians': guardians,
                    'siblings': siblings,
                    'hhold': hhold,
                    'creg': creg,
                    'extids': gparams,
                    'health': health,
                    'hhmembers': hhmembers,
                    'school': school,
                    'care_giver': care_giver,
                    'services': services,
                    'allow_edit': allow_edit,
                    'suppression': vl_sup,
                    'well_being_count': wellbeing_services
                }
                # print(dataset + "child")
                dataset_list.append(dataset)

            serializer = OVCSerializer(dataset_list, many=True)
            print(dataset_list)
            return Response(serializer.data)

        except Exception as e:
            print("Error retrieving OVC data - %s" % (str(e)))
            msg = "An error occurred when retrieving OVC data"
            return Response({'error': msg})
    def play(self,request,id=None):
        if id is not None:
            ovc_id = int(id)
            print(ovc_id)
            try:
                child = RegPerson.objects.get(is_void=False, id=ovc_id)
            except RegPerson.DoesNotExist:
                child = None

            creg = OVCRegistration.objects.get(is_void=False, person=ovc_id)

            # Get guardians

            guardians = RegPersonsGuardians.objects.filter(
                    is_void=False, child_person=child.id)



            extids = RegPersonsExternalIds.objects.all()
                for extid in extids:
                # Health details
                health = {}
                if creg.hiv_status == 'HSTP':
                    health = get_health(ovc_id)
                # School details
                school = {}
                if creg.school_level != 'SLNS':
                    school = get_school(ovc_id)
            except RegPersonsExternalIds.DoesNotExist:
                extid = None
                health = None
                school = None
            # Get household
            try:
                hhold = OVCHHMembers.objects.get(is_void=False, person=child.id)
                # Get HH members
                hhid = hhold.house_hold
                hhmqs = OVCHHMembers.objects.filter(is_void=False, house_hold=hhid).order_by("-hh_head")
                hhmembers = list(hhmqs.exclude(person=child.id))
            except OVCHHMembers.DoesNotExist:
                hhold = None
                hhmqs = None
                hhmembers = None
            # Viral load
            vload = OVCViralload.objects.filter(is_void=False, person=ovc_id).order_by("-viral_date")[:1]
            vl_sup, v_val, v_dt = 'Missing', None, None
            if vload:
                for vl in vload:
                    v_val = vl.viral_load
                    v_dt = vl.viral_date
                vl_sup = 'YES' if not v_val or v_val < 1000 else 'NO'
            # Get siblings
            siblings = RegPersonsSiblings.objects.filter(is_void=False, child_person=child.id)
            # Get services
            servs = {
                'FSAM': 'f1a',
                'FCSI': 'fcsi',
                'FHSA': 'fhva',
                'cpr': 'cpr',
                'wba': 'wba',
                'CPAR': 'CPAR',
                'WBG': 'WBG'
            }
            services = {key: 0 for key in servs.values()}
            sqs = OVCCareEvents.objects.filter(Q(person=child.id) | Q(house_hold=hhid))
            sqs = sqs.filter(is_void=False).values('event_type_id').annotate(total=Count('event_type_id')).order_by(
                'total')
            for serv in sqs:
                item = serv['event_type_id']
                item_count = serv['total']
                if item in servs:
                    item_key = servs[item]
                    services[item_key] = item_count
            # Re-usable values
            check_fields = [
                'relationship_type_id',
                'school_level_id',
                'hiv_status_id',
                'immunization_status_id',
                'art_status_id',
                'school_type_id',
                'class_level_id'
            ]
            vals = get_dict(field_name=check_fields)
            wellbeing_services = {
                'wba': services['wba'],
                'WBG': services['WBG']
            }
            child_hiv_status = OVCRegistration.objects.get(person=id).hiv_status
            try:
                care_giver = RegPerson.objects.get(id=OVCRegistration.objects.get(person=child).caretaker_id)
            except RegPerson.DoesNotExist:
                care_giver = None
                print('Caregiver does not exist for child: %s' % child.id)

            # Rest of the code...

            dataset = {
                'status': 200,
                'child': child,
                'params': params,
                'child_hiv_status': child_hiv_status,
                'guardians': guardians,
                'siblings': siblings,
                'hhold': hhold,
                'creg': creg,
                'extids': gparams,
                'health': health,
                'hhmembers': hhmembers,
                'school': school,
                'care_giver': care_giver,
                'services': services,
                'allow_edit': allow_edit,
                'suppression': vl_sup,
                'well_being_count': wellbeing_services
            }
            # print(f"{dataset} child")

            serializer = OVCSerializer(dataset)
            print(dataset)
            return Response(serializer.data)







