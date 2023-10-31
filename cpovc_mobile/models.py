from django.db import models
from enum import Enum, auto
import uuid


class ApprovalStatus(Enum):
    NEUTRAL = auto()  # stored as 1 in the DB
    TRUE = auto()  # stored as 2 in the DB
    FALSE = auto()  # stored as 3 in the DB

# use for CPARA


class OVCMobileEvent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.IntegerField()
    ovc_cpims_id = models.CharField(max_length=255)
    date_of_event = models.DateField()
    is_accepted = models.IntegerField(
        choices=[(status.value, status.name) for status in ApprovalStatus],
        default=ApprovalStatus.NEUTRAL.value
    )
    message = models.TextField(null=True)

    class Meta:
        db_table = 'cpara_mobile_event'


class OVCMobileEventAttribute(models.Model):
    event = models.ForeignKey(OVCMobileEvent, on_delete=models.CASCADE)
    ovc_cpims_id_individual = models.CharField(max_length=255)
    question_name = models.CharField(max_length=255)
    answer_value = models.CharField(max_length=255)

    class Meta:
        db_table = 'cpara_mobile_attributes'


# Store rejected CPARA
# use for CPARA
class OVCMobileEventRejected(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.IntegerField()
    ovc_cpims_id = models.CharField(max_length=255)
    date_of_event = models.DateField()
    is_accepted = models.IntegerField(
        choices=[(status.value, status.name) for status in ApprovalStatus],
        default=ApprovalStatus.NEUTRAL.value
    )
    message = models.TextField(null=True)

    class Meta:
        db_table = 'cpara_mobile_event_rejected'

 # use for CPARA data


class OVCMobileEventAttributeRejected(models.Model):
    event = models.ForeignKey(OVCMobileEventRejected,
                              on_delete=models.CASCADE, to_field='id')
    ovc_cpims_id_individual = models.CharField(max_length=255)
    question_name = models.CharField(max_length=255)
    answer_value = models.CharField(max_length=255)

    class Meta:
        db_table = 'cpara_mobile_attributes_rejected'


# use for form 1 A and B
class OVCEvent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.IntegerField()
    ovc_cpims_id = models.CharField(max_length=255)
    date_of_event = models.DateField()
    form_type = models.CharField(max_length=255)

    class Meta:
        db_table = 'f1ab_mobile_event'

# use for Form1A and B


class OVCServices(models.Model):
    event = models.ForeignKey(
        OVCEvent, on_delete=models.CASCADE, to_field='id')
    id = models.UUIDField(editable=False, primary_key=True)
    domain_id = models.CharField(max_length=255)
    service_id = models.CharField(max_length=255)
    message = models.TextField(null=True)
    is_accepted = models.IntegerField(
        choices=[(status.value, status.name) for status in ApprovalStatus],
        default=ApprovalStatus.NEUTRAL.value
    )

    class Meta:
        db_table = 'f1ab_mobile_attributes'

# Store rejectedform 1A nd 1B
# use for form 1 A and B


class OVCEventRejected(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.IntegerField()
    ovc_cpims_id = models.CharField(max_length=255)
    date_of_event = models.DateField()
    form_type = models.CharField(max_length=255)

    class Meta:
        db_table = 'f1ab_mobile_event_rejected'

# use for Form1A and B


class OVCServicesRejected(models.Model):
    event = models.ForeignKey(
        OVCEventRejected, on_delete=models.CASCADE, to_field='id')
    id = models.UUIDField(editable=False, primary_key=True)
    domain_id = models.CharField(max_length=255)
    service_id = models.CharField(max_length=255)
    message = models.TextField(null=True)
    is_accepted = models.IntegerField(
        choices=[(status.value, status.name) for status in ApprovalStatus],
        default=ApprovalStatus.NEUTRAL.value
    )

    class Meta:
        db_table = 'f1ab_mobile_attributes_rejected'


# use for case plan template
class CasePlanTemplateEvent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ovc_cpims_id = models.CharField(max_length=255)
    date_of_event = models.DateField()
    user_id = models.IntegerField()

    class Meta:
        db_table = 'case_plan_mobile_event'


class CasePlanTemplateService(models.Model):
    unique_service_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    message = models.TextField(null=True)
    event = models.ForeignKey(CasePlanTemplateEvent, on_delete=models.CASCADE)
    domain_id = models.CharField(max_length=255)
    service_id = models.CharField(max_length=255)
    goal_id = models.CharField(max_length=255)
    gap_id = models.CharField(max_length=255)
    priority_id = models.CharField(max_length=255)
    responsible_id = models.JSONField()
    results_id = models.CharField(max_length=255)
    reason_id = models.CharField(max_length=255)
    completion_date = models.DateField()
    is_accepted = models.IntegerField(
        choices=[(status.value, status.name) for status in ApprovalStatus],
        default=ApprovalStatus.NEUTRAL.value
    )

    class Meta:
        db_table = 'case_plan_mobile_attributes'


# Store rejected case plan templates
# use for case plan template
class CasePlanTemplateEventRejected(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ovc_cpims_id = models.CharField(max_length=255)
    date_of_event = models.DateField()
    user_id = models.IntegerField()

    class Meta:
        db_table = 'case_plan_mobile_event_rejected'


class CasePlanTemplateServiceRejected(models.Model):
    unique_service_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
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
    reason_id = models.CharField(max_length=255)
    completion_date = models.DateField()
    is_accepted = models.IntegerField(
        choices=[(status.value, status.name) for status in ApprovalStatus],
        default=ApprovalStatus.NEUTRAL.value
    )

    class Meta:
        db_table = 'case_plan_mobile_attributes_rejected'
