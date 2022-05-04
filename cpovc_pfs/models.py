import uuid
from django.db import models
from django.utils import timezone
from cpovc_registry.models import RegPerson, RegOrgUnit
from cpovc_ovc.models import OVCSchool
from cpovc_auth.models import AppUser


class OVCPreventiveGroup(models.Model):
    gid = models.UUIDField(
        primary_key=True, default=uuid.uuid1, editable=False)
    org_unit = models.ForeignKey(RegOrgUnit, on_delete=models.CASCADE)
    group_id = models.CharField(max_length=5)
    group_name = models.CharField(max_length=50)
    group_date = models.DateField(default=timezone.now, null=True)
    timestamp_created = models.DateTimeField(default=timezone.now)
    timestamp_updated = models.DateTimeField(default=timezone.now)
    is_void = models.BooleanField(default=False)

    class Meta:
        db_table = 'ovc_preventive_group'

    def __unicode__(self):
        return '%s %s' % str(self.group_id, self.group_name)


class OVCPreventiveRegistration(models.Model):
    preventive_reg_id = models.UUIDField(
        primary_key=True, default=uuid.uuid1, editable=False)
    person = models.ForeignKey(RegPerson, on_delete=models.CASCADE)
    registration_date = models.DateField(default=timezone.now)
    intervention = models.CharField(max_length=10)
    group = models.ForeignKey(
        OVCPreventiveGroup, on_delete=models.CASCADE, null=True)
    school = models.ForeignKey(
        OVCSchool, on_delete=models.CASCADE, null=True)
    child_cbo = models.ForeignKey(RegOrgUnit, on_delete=models.CASCADE)
    caregiver = models.ForeignKey(
        RegPerson, on_delete=models.CASCADE, null=True,
        related_name='caregiver')
    is_active = models.BooleanField(default=True)
    exit_reason = models.CharField(max_length=4, null=True)
    exit_date = models.DateField(default=timezone.now, null=True)
    created_by = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    timestamp_created = models.DateTimeField(default=timezone.now)
    timestamp_updated = models.DateTimeField(default=timezone.now)
    is_void = models.BooleanField(default=False)
    sync_id = models.UUIDField(default=uuid.uuid1, editable=False)

    class Meta:
        db_table = 'ovc_preventive_registration'

    def __unicode__(self):
        return str(self.preventive_reg_id)
