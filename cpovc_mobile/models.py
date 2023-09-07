from django.db import models

from enum import Enum, auto
import uuid

from cpovc_registry.models import RegPersonsOrgUnits, RegOrgUnit, RegPerson

from cpovc_forms.models import OVCCareQuestions

class ApprovalStatus(Enum):
    NEUTRAL = auto() # stored as 1 in the DB
    TRUE = auto() # stored as 2 in the DB
    FALSE = auto() # stored as 3 in the DB

# use for CPARA
class OVCMobileEvent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ovc_cpims = models.ForeignKey(RegPerson,  on_delete=models.CASCADE)
    date_of_event = models.DateField()
    is_accepted = models.IntegerField(
        choices=[(status.value, status.name) for status in ApprovalStatus],
        default=ApprovalStatus.NEUTRAL.value
    )
    message = models.TextField(null=True)
    class Meta:
        db_table = 'ovc_mobile_event'
        
 # use for CPARA data       

class OVCMobileEventAttribute(models.Model):
    event = models.ForeignKey(OVCMobileEvent, on_delete=models.CASCADE, to_field='id')
    ovc_cpims_individual = models.ForeignKey(RegPerson,  on_delete=models.CASCADE)
    question_name = models.CharField(max_length=255)
    answer_value = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'cpara_mobile_attributes'


# use for form 1 A and B
class OVCEvent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ovc_cpims = models.ForeignKey(RegPerson,  on_delete=models.CASCADE)
    date_of_event = models.DateField()

    class Meta:
        db_table = 'f1ab_mobile_event'

# use for Form1A and B
class OVCServices(models.Model):
    event = models.ForeignKey(OVCEvent, on_delete=models.CASCADE, to_field='id')
    domain_id = models.CharField(max_length=10)
    service_id = models.CharField(max_length=10)
    message = models.TextField(null=True)
    form = models.CharField(null=False, max_length=50)
    is_accepted = models.IntegerField(
        choices=[(status.value, status.name) for status in ApprovalStatus],
        default=ApprovalStatus.NEUTRAL.value
    )

    class Meta:
        db_table = 'f1ab_mobile_attributes'


# use for case plan template
class CasePlanTemplateEvent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ovc_cpims = models.ForeignKey(RegPerson,  on_delete=models.CASCADE)
    date_of_event = models.DateField()
    
    class Meta:
        db_table = 'case_plan_mobile_event'

class CasePlanTemplateService(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    message = models.TextField(null=True)
    event = models.ForeignKey(CasePlanTemplateEvent, on_delete=models.CASCADE)
    domain_id = models.CharField(max_length=255)
    service_id = models.CharField(max_length=255)
    goal_id = models.CharField(max_length=255)
    gap_id = models.CharField(max_length=255)
    priority_id = models.CharField(max_length=255)
    responsible_id = models.CharField()
    results_id = models.CharField(max_length=255)
    reason_id = models.CharField(max_length=255)
    completion_date = models.DateField()
    is_accepted = models.IntegerField(
        choices=[(status.value, status.name) for status in ApprovalStatus],
        default=ApprovalStatus.NEUTRAL.value
    )

    class Meta:
        db_table = 'case_plan_mobile_attributes'

