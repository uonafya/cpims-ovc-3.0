import uuid
from django.db import models
from django.utils import timezone
from cpovc_registry.models import RegPerson, RegOrgUnit
from cpovc_ovc.models import OVCSchool
from cpovc_auth.models import AppUser


class OVCDREAMSRegistration(models.Model):
    dreams_reg_id = models.UUIDField(
        primary_key=True, default=uuid.uuid1, editable=False)
    person = models.ForeignKey(RegPerson, on_delete=models.CASCADE)
    registration_date = models.DateField(default=timezone.now)
    intervention = models.CharField(max_length=10)
    school = models.ForeignKey(
        OVCSchool, on_delete=models.CASCADE, null=True)
    child_cbo = models.ForeignKey(RegOrgUnit, on_delete=models.CASCADE)
    caregiver = models.ForeignKey(
        RegPerson, on_delete=models.CASCADE, null=True,
        related_name='dreams_caregiver')
    is_active = models.BooleanField(default=True)
    exit_reason = models.CharField(max_length=4, null=True)
    exit_date = models.DateField(default=timezone.now, null=True)
    created_by = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    timestamp_created = models.DateTimeField(default=timezone.now)
    timestamp_updated = models.DateTimeField(default=timezone.now)
    is_void = models.BooleanField(default=False)
    sync_id = models.UUIDField(default=uuid.uuid1, editable=False)

    class Meta:
        db_table = 'ovc_dreams_registration'

    def __unicode__(self):
        return str(self.preventive_reg_id)
