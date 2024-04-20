import uuid
from enum import Enum, auto
from django.db import models
from django.utils import timezone
from cpovc_registry.models import RegPerson
from cpovc_auth.models import AppUser
from cpovc_registry.models import RegOrgUnit


class ApprovalStatus(Enum):
    NEUTRAL = auto()  # stored as 1 in the DB
    TRUE = auto()  # stored as 2 in the DB
    FALSE = auto()  # stored as 3 in the DB


# use for CPARA
class OVCMobileEvent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    date_of_event = models.DateField()
    is_accepted = models.IntegerField(
        choices=[(status.value, status.name) for status in ApprovalStatus],
        default=ApprovalStatus.NEUTRAL.value
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    message = models.TextField(null=True)
    app_form_metadata = models.CharField(max_length=500, default="{}")
    # approved_initiated = models.BooleanField(default=False, null=True, blank=True)
    signature = models.BinaryField(max_length=500, null=True)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    ovc_cpims = models.ForeignKey(RegPerson, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cpara_mobile_event'


class OVCMobileEventAttribute(models.Model):
    event = models.ForeignKey(OVCMobileEvent, on_delete=models.CASCADE)
    question_name = models.CharField(max_length=255)
    answer_value = models.CharField(max_length=255)
    ovc_cpims = models.ForeignKey(RegPerson, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cpara_mobile_attributes'


# Store rejected CPARA
# use for CPARA
class OVCMobileEventRejected(models.Model):
    id = models.UUIDField(primary_key=True, editable=True)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    # ovc_cpims = models.ForeignKey(RegPerson, on_delete=models.CASCADE)
    date_of_event = models.DateField()
    is_accepted = models.IntegerField(
        choices=[(status.value, status.name) for status in ApprovalStatus],
        default=ApprovalStatus.NEUTRAL.value
    )
    message = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    app_form_metadata = models.CharField(max_length=500, default="{}")
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    ovc_cpims = models.ForeignKey(RegPerson, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cpara_mobile_event_rejected'

# use for CPARA data


class OVCMobileEventAttributeRejected(models.Model):
    event = models.ForeignKey(OVCMobileEventRejected,
                              on_delete=models.CASCADE, to_field='id')
    question_name = models.CharField(max_length=255)
    answer_value = models.CharField(max_length=255)
    ovc_cpims = models.ForeignKey(RegPerson, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cpara_mobile_attributes_rejected'


# use for form 1 A and B
class OVCEvent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    date_of_event = models.DateField()
    form_type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    app_form_metadata = models.CharField(max_length=500)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    ovc_cpims = models.ForeignKey(RegPerson, on_delete=models.CASCADE)

    class Meta:
        db_table = 'f1ab_mobile_event'

# use for Form1A and B


class OVCServices(models.Model):
    event = models.ForeignKey(
        OVCEvent, on_delete=models.CASCADE, to_field='id')
    id = models.UUIDField(editable=True, primary_key=True)
    domain_id = models.CharField(max_length=255)
    service_id = models.CharField(max_length=255)
    message = models.TextField(null=True)
    is_accepted = models.IntegerField(
        choices=[(status.value, status.name) for status in ApprovalStatus],
        default=ApprovalStatus.NEUTRAL.value
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'f1ab_mobile_attributes'

# Store rejectedform 1A nd 1B
# use for form 1 A and B


class OVCEventRejected(models.Model):
    id = models.UUIDField(primary_key=True, editable=True)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    # ovc_cpims = models.ForeignKey(RegPerson, on_delete=models.CASCADE)

    date_of_event = models.DateField()
    form_type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    app_form_metadata = models.CharField(max_length=500, default="{}")
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    ovc_cpims = models.ForeignKey(RegPerson, on_delete=models.CASCADE)

    class Meta:
        db_table = 'f1ab_mobile_event_rejected'

# use for Form1A and B


class OVCServicesRejected(models.Model):
    event = models.ForeignKey(
        OVCEventRejected, on_delete=models.CASCADE, to_field='id')
    id = models.UUIDField(editable=True, primary_key=True)
    domain_id = models.CharField(max_length=255)
    service_id = models.CharField(max_length=255)
    message = models.TextField(null=True)
    is_accepted = models.IntegerField(
        choices=[(status.value, status.name) for status in ApprovalStatus],
        default=ApprovalStatus.NEUTRAL.value
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'f1ab_mobile_attributes_rejected'


# use for case plan template
class CasePlanTemplateEvent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    date_of_event = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    app_form_metadata = models.CharField(max_length=500, default="{}")
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    ovc_cpims = models.ForeignKey(RegPerson, on_delete=models.CASCADE)

    class Meta:
        db_table = 'case_plan_mobile_event'


class CasePlanTemplateService(models.Model):
    unique_service_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=True)
    message = models.TextField(null=True)
    event = models.ForeignKey(CasePlanTemplateEvent, on_delete=models.CASCADE)
    domain_id = models.CharField(max_length=255)
    service_id = models.CharField(max_length=255)
    goal_id = models.CharField(max_length=255)
    gap_id = models.CharField(max_length=255)
    priority_id = models.CharField(max_length=255)
    responsible_id = models.JSONField()
    results_id = models.CharField(max_length=255)
    reason_id = models.CharField(max_length=255, null=True)
    completion_date = models.DateField(null=True)
    is_accepted = models.IntegerField(
        choices=[(status.value, status.name) for status in ApprovalStatus],
        default=ApprovalStatus.NEUTRAL.value
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'case_plan_mobile_attributes'


# Store rejected case plan templates
# use for case plan template
class CasePlanTemplateEventRejected(models.Model):
    id = models.UUIDField(primary_key=True, editable=True)
    # ovc_cpims = models.ForeignKey(RegPerson, on_delete=models.CASCADE)
    date_of_event = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    app_form_metadata = models.CharField(max_length=500, default="{}")
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    ovc_cpims = models.ForeignKey(RegPerson, on_delete=models.CASCADE)

    class Meta:
        db_table = 'case_plan_mobile_event_rejected'


class CasePlanTemplateServiceRejected(models.Model):
    unique_service_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=True)
    message = models.TextField(null=True)
    event = models.ForeignKey(
        CasePlanTemplateEventRejected, on_delete=models.CASCADE)
    domain_id = models.CharField(max_length=255)
    service_id = models.CharField(max_length=255)
    goal_id = models.CharField(max_length=255)
    gap_id = models.CharField(max_length=255)
    priority_id = models.CharField(max_length=255)
    responsible_id = models.JSONField()
    results_id = models.CharField(max_length=255)
    reason_id = models.CharField(max_length=255, null=True)
    completion_date = models.DateField(null=True)
    is_accepted = models.IntegerField(
        choices=[(status.value, status.name) for status in ApprovalStatus],
        default=ApprovalStatus.NEUTRAL.value
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'case_plan_mobile_attributes_rejected'


# OVC HIV MANAGEMENT
class HIVManagementStaging(models.Model):
    adherence_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=True)
    hiv_confirmed_date = models.DateTimeField(null=False)
    treatment_initiated_date = models.DateTimeField(null=False)
    baseline_hei = models.CharField(max_length=100, null=False)
    firstline_start_date = models.DateTimeField(null=False)
    substitution_firstline_arv = models.BooleanField(default=False)
    substitution_firstline_date = models.DateTimeField(null=True, blank=True)
    switch_secondline_arv = models.BooleanField(default=False)
    switch_secondline_date = models.DateTimeField(null=True)
    switch_thirdline_arv = models.BooleanField(default=False)
    switch_thirdline_date = models.DateTimeField(null=True)
    visit_date = models.DateTimeField(null=False)
    duration_art = models.CharField(max_length=3, null=True)
    height = models.CharField(max_length=3, null=True)
    weight = models.CharField(max_length=3, null=True)
    muac = models.CharField(max_length=20, null=True)
    currentregimen = models.CharField(max_length=20, null=True)
    enoughdrugs = models.CharField(max_length=20, null=True)
    attendingsuppportgroup = models.CharField(max_length=20, null=True)
    pamacare = models.CharField(max_length=20, null=True)
    enrolledotz = models.CharField(max_length=20, null=True)
    adherence = models.CharField(max_length=20, null=False)
    adherence_drugs_duration = models.CharField(max_length=3, null=True)
    adherence_counselling = models.CharField(max_length=30, null=True)
    treatment_supporter = models.CharField(max_length=100, null=True)
    treatment_supporter_relationship = models.CharField(
        max_length=20, null=True)
    treatment_supporter_gender = models.CharField(max_length=11, null=True)
    treatment_supporter_age = models.CharField(max_length=11, null=True)
    treatment_supporter_hiv = models.CharField(max_length=100, null=True)
    viral_load_results = models.CharField(max_length=7, null=True)
    viral_load_date = models.DateTimeField(null=False)
    detectable_viralload_interventions = models.CharField(
        max_length=50, null=True)
    disclosure = models.CharField(max_length=20, null=True)
    muac_score = models.CharField(max_length=20, null=True)
    bmi = models.CharField(max_length=20, null=True)
    nutritional_support = models.CharField(max_length=255, null=True)
    support_group_status = models.CharField(max_length=20, null=True)
    nhif_enrollment = models.BooleanField(default=False)
    support_group_enrollment = models.BooleanField(default=False)
    nhif_status = models.CharField(max_length=11, null=True)
    referral_services = models.CharField(max_length=100, null=True)
    nextappointment_date = models.DateField(null=True)
    peer_educator_name = models.CharField(max_length=100, null=True)
    peer_educator_contact = models.CharField(max_length=20, null=True)
    # event = models.ForeignKey(OVCCareEvents, on_delete=models.CASCADE)
    is_void = models.BooleanField(default=False)
    date_of_event = models.DateField()
    timestamp_created = models.DateTimeField(auto_now_add=True)
    timestamp_updated = models.DateTimeField(auto_now=True)
    is_accepted = models.IntegerField(
        choices=[(status.value, status.name) for status in ApprovalStatus],
        default=ApprovalStatus.NEUTRAL.value
    )
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    app_form_metadata = models.CharField(max_length=500, default="{}")
    # approved_initiated = models.BooleanField(default=False, null=True, blank=True)
    ovc_cpims = models.ForeignKey(RegPerson, on_delete=models.CASCADE)

    class Meta:
        db_table = 'hiv_management_staging'

    def __unicode__(self):
        return str(self.adherence_id)


# HIV SCREENING
class RiskScreeningStaging(models.Model):
    risk_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=True)
    test_done_when = models.BooleanField(null=True)
    test_donewhen_result = models.BooleanField(null=True)
    caregiver_know_status = models.BooleanField(null=True)
    caregiver_knowledge_yes = models.CharField(max_length=50, null=True)
    parent_PLWH = models.BooleanField(null=True)
    child_sick_malnourished = models.BooleanField(null=True)
    child_sexual_abuse = models.BooleanField(null=True)
    traditional_procedure = models.BooleanField(null=True)
    adol_sick = models.BooleanField(null=True)
    adol_had_tb = models.BooleanField(null=True)
    adol_sexual_abuse = models.BooleanField(null=True)
    sex = models.BooleanField(null=True)
    sti = models.BooleanField(null=True)
    sharing_needles = models.BooleanField(null=True)
    hiv_test_required = models.BooleanField(null=True)
    parent_consent_testing = models.BooleanField(null=True)
    parent_consent_date = models.DateField(
        default=timezone.now, null=True)  # date new 1
    referral_made = models.BooleanField(null=True)
    referral_made_date = models.DateField(default=timezone.now, null=True)
    referral_completed = models.BooleanField(null=True)
    referral_completed_date = models.DateField(
        default=timezone.now, null=True)  # date new 2
    not_completed = models.CharField(max_length=50, null=True)
    test_result = models.CharField(max_length=20, null=True)
    art_referral = models.BooleanField(null=True)
    art_referral_date = models.DateField(
        default=timezone.now, null=True)  # date
    art_referral_completed = models.BooleanField(null=True)
    art_referral_completed_date = models.DateField(
        default=timezone.now, null=True)  # date
    facility_code = models.CharField(max_length=10, null=True)
    # event = models.ForeignKey(OVCCareEvents, on_delete=models.CASCADE)
    date_of_event = models.DateField(default=timezone.now, null=True)  # date
    is_void = models.BooleanField(null=True)
    timestamp_created = models.DateTimeField(auto_now_add=True)
    timestamp_updated = models.DateTimeField(auto_now=True)
    is_accepted = models.IntegerField(
        choices=[(status.value, status.name) for status in ApprovalStatus],
        default=ApprovalStatus.NEUTRAL.value
    )
    app_form_metadata = models.CharField(max_length=500, default="{}")
    # approved_initiated = models.BooleanField(default=False, null=True, blank=True)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    ovc_cpims = models.ForeignKey(RegPerson, on_delete=models.CASCADE)

    class Meta:
        db_table = 'risk_screening_staging'

    def __unicode__(self):
        return str(self.risk_id)


# Rejected models for HIV Management and Risk Screening
# OVC HIV MANAGEMENT
class HIVManagementStagingRejected(models.Model):
    adherence_id = models.UUIDField(primary_key=True, editable=True)
    # person = models.ForeignKey(RegPerson, on_delete=models.CASCADE)
    # ovc_cpims = models.ForeignKey(RegPerson, on_delete=models.CASCADE)
    hiv_confirmed_date = models.DateTimeField(null=False)
    treatment_initiated_date = models.DateTimeField(null=False)
    baseline_hei = models.CharField(max_length=100, null=False)
    firstline_start_date = models.DateTimeField(null=False)
    substitution_firstline_arv = models.BooleanField(default=False)
    substitution_firstline_date = models.DateTimeField(default=timezone.now)
    switch_secondline_arv = models.BooleanField(default=False)
    switch_secondline_date = models.DateTimeField(null=True)
    switch_thirdline_arv = models.BooleanField(default=False)
    switch_thirdline_date = models.DateTimeField(null=True)
    visit_date = models.DateTimeField(null=False)
    duration_art = models.CharField(max_length=3, null=True)
    height = models.CharField(max_length=3, null=True)
    weight = models.CharField(max_length=3, null=True)
    muac = models.CharField(max_length=20, null=True)
    currentregimen = models.CharField(max_length=20, null=True)
    enoughdrugs = models.CharField(max_length=20, null=True)
    attendingsuppportgroup = models.CharField(max_length=20, null=True)
    pamacare = models.CharField(max_length=20, null=True)
    enrolledotz = models.CharField(max_length=20, null=True)
    adherence = models.CharField(max_length=20, null=False)
    adherence_drugs_duration = models.CharField(max_length=3, null=True)
    adherence_counselling = models.CharField(max_length=30, null=True)
    treatment_supporter = models.CharField(max_length=100, null=True)
    treatment_supporter_relationship = models.CharField(
        max_length=20, null=True)
    treatment_supporter_gender = models.CharField(max_length=11, null=True)
    treatment_supporter_age = models.CharField(max_length=11, null=True)
    treatment_supporter_hiv = models.CharField(max_length=100, null=True)
    viral_load_results = models.CharField(max_length=7, null=True)
    viral_load_date = models.DateTimeField(null=False)
    detectable_viralload_interventions = models.CharField(
        max_length=50, null=True)
    disclosure = models.CharField(max_length=20, null=True)
    muac_score = models.CharField(max_length=20, null=True)
    bmi = models.CharField(max_length=20, null=True)
    nutritional_support = models.CharField(max_length=255, null=True)
    support_group_status = models.CharField(max_length=20, null=True)
    nhif_enrollment = models.BooleanField(default=False)
    support_group_enrollment = models.BooleanField(default=False)
    nhif_status = models.CharField(max_length=11, null=True)
    referral_services = models.CharField(max_length=100, null=True)
    nextappointment_date = models.DateField(null=True)
    peer_educator_name = models.CharField(max_length=100, null=True)
    peer_educator_contact = models.CharField(max_length=20, null=True)
    # event = models.ForeignKey(OVCCareEvents, on_delete=models.CASCADE)
    is_void = models.BooleanField(default=False)
    date_of_event = models.DateField()
    timestamp_created = models.DateTimeField(auto_now_add=True)
    timestamp_updated = models.DateTimeField(auto_now=True)
    is_accepted = models.IntegerField(
        choices=[(status.value, status.name) for status in ApprovalStatus],
        default=ApprovalStatus.NEUTRAL.value
    )
    message = models.TextField(null=True)
    app_form_metadata = models.CharField(max_length=500, default="{}")
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    ovc_cpims = models.ForeignKey(RegPerson, on_delete=models.CASCADE)

    class Meta:
        db_table = 'hiv_management_staging_rejected'

    def __unicode__(self):
        return str(self.adherence_id)


# HIV SCREENING
class RiskScreeningStagingRejected(models.Model):
    # person = models.ForeignKey(RegPerson, on_delete=models.CASCADE)
    # ovc_cpims = models.ForeignKey(RegPerson, on_delete=models.CASCADE)
    risk_id = models.UUIDField(primary_key=True, editable=True)
    test_done_when = models.BooleanField(null=True)
    test_donewhen_result = models.BooleanField(null=True)
    caregiver_know_status = models.BooleanField(null=True)
    caregiver_knowledge_yes = models.CharField(max_length=50, null=True)
    parent_PLWH = models.BooleanField(null=True)
    child_sick_malnourished = models.BooleanField(null=True)
    child_sexual_abuse = models.BooleanField(null=True)
    traditional_procedure = models.BooleanField(null=True)
    adol_sick = models.BooleanField(null=True)
    adol_had_tb = models.BooleanField(null=True)
    adol_sexual_abuse = models.BooleanField(null=True)
    sex = models.BooleanField(null=True)
    sti = models.BooleanField(null=True)
    sharing_needles = models.BooleanField(null=True)
    hiv_test_required = models.BooleanField(null=True)
    parent_consent_testing = models.BooleanField(null=True)
    parent_consent_date = models.DateField(
        default=timezone.now, null=True)  # date new 1
    referral_made = models.BooleanField(null=True)
    referral_made_date = models.DateField(default=timezone.now, null=True)
    referral_completed = models.BooleanField(null=True)
    referral_completed_date = models.DateField(
        default=timezone.now, null=True)  # date new 2
    not_completed = models.CharField(max_length=50, null=True)
    test_result = models.CharField(max_length=20, null=True)
    art_referral = models.BooleanField(null=True)
    art_referral_date = models.DateField(
        default=timezone.now, null=True)  # date
    art_referral_completed = models.BooleanField(null=True)
    art_referral_completed_date = models.DateField(
        default=timezone.now, null=True)  # date
    facility_code = models.CharField(max_length=10, null=True)
    # event = models.ForeignKey(OVCCareEvents, on_delete=models.CASCADE)
    date_of_event = models.DateField(default=timezone.now, null=True)  # date
    is_void = models.BooleanField(null=True)
    timestamp_created = models.DateTimeField(auto_now_add=True)
    timestamp_updated = models.DateTimeField(auto_now=True)
    is_accepted = models.IntegerField(
        choices=[(status.value, status.name) for status in ApprovalStatus],
        default=ApprovalStatus.NEUTRAL.value
    )
    message = models.TextField(null=True)
    app_form_metadata = models.CharField(max_length=500, default="{}")
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    ovc_cpims = models.ForeignKey(RegPerson, on_delete=models.CASCADE)

    class Meta:
        db_table = 'risk_screening_staging_rejected'

    # def __unicode__(self):
    #     return str(self.risk_id)
    

# Track the data flow from submission to approval / rejection
    
class MobileAppDataTrack(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    event_id=models.UUIDField(null=False, blank=False, unique=True)
    date_of_event = models.DateField(null=True)
    service_id=models.UUIDField(null=True, blank=True, unique=True)
    form_type=models.CharField(max_length=100,blank=False)
    timestamp_created=models.DateTimeField()
    action=models.IntegerField(
        choices=[(status.value, status.name) for status in ApprovalStatus],
        default=ApprovalStatus.NEUTRAL.value
    )
    timestamp_actioned=models.DateTimeField(auto_now_add=True)
    user_submitting=models.ForeignKey(AppUser,related_name='user_submitting', on_delete=models.CASCADE)
    user_actioning=models.ForeignKey(AppUser,related_name='user_actioning', on_delete=models.CASCADE)
    ovc_cpims = models.ForeignKey(RegPerson, on_delete=models.CASCADE)
    CBO=models.ForeignKey(RegOrgUnit, on_delete=models.CASCADE)

    class Meta:
        db_table = 'mobile_app_data_track'

