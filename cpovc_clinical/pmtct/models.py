import uuid
from django.db import models
from django.utils import timezone
from cpovc_registry.models import RegPerson, RegOrgUnit
from cpovc_ovc.models import OVCSchool, OVCFacility
from cpovc_auth.models import AppUser


class OVCPMTCTRegistration(models.Model):
    pmtct_id = models.UUIDField(
        primary_key=True, default=uuid.uuid1, editable=False)
    person = models.ForeignKey(RegPerson, on_delete=models.CASCADE)
    registration_date = models.DateField(default=timezone.now)

    school = models.ForeignKey(
        OVCSchool, on_delete=models.CASCADE, null=True)
    child_cbo = models.ForeignKey(RegOrgUnit, on_delete=models.CASCADE)
    caregiver = models.ForeignKey(
        RegPerson, on_delete=models.CASCADE, null=True,
        related_name='care_taker')
    caregiver_contact = models.CharField(max_length=15)
    hiv_status = models.CharField(max_length=4, null=True)
    chv = models.ForeignKey(RegPerson, related_name='pmtct_chv',
                            on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)
    exit_reason = models.CharField(max_length=4, null=True)
    exit_date = models.DateField(default=timezone.now, null=True)
    created_by = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    timestamp_created = models.DateTimeField(default=timezone.now)
    timestamp_updated = models.DateTimeField(default=timezone.now)
    is_void = models.BooleanField(default=False)
    sync_id = models.UUIDField(default=uuid.uuid1, editable=False)

    class Meta:
        db_table = 'ovc_pmtct_registration'

    def __str__(self):
        return '%s : %s' % (self.pmtct_id, self.person)
