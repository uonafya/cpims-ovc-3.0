import uuid
from django.db import models
from django.utils import timezone
from cpovc_registry.models import RegPerson, RegOrgUnit
from cpovc_ovc.models import OVCHouseHold
from cpovc_forms.models import OVCCareEvents


class OVCCareTransfer(models.Model):
    transfer_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey(RegPerson, on_delete=models.CASCADE)
    household = models.ForeignKey(OVCHouseHold, on_delete=models.CASCADE)
    reason = models.CharField(max_length=254, null=True)
    rec_organization = models.ForeignKey(
        RegOrgUnit, on_delete=models.CASCADE,
        related_name="receiving_organization", default=0)
    organization_from = models.ForeignKey(
        RegOrgUnit, on_delete=models.CASCADE, default=56)
    date_of_event = models.DateField()
    date_follow_up = models.DateField()
    is_void = models.BooleanField(default=False)
    event = models.ForeignKey(
        OVCCareEvents, on_delete=models.CASCADE)
    timestamp_created = models.DateTimeField(default=timezone.now)
    timestamp_updated = models.DateTimeField(auto_now=True)

    class Meta:
        """Override table details."""

        db_table = 'ovc_care_transfer'
        verbose_name = 'OVC Transfer'
        verbose_name_plural = 'OVC Transfers'

    def __str__(self):
        """To be returned on default."""
        return str(self.transfer_id)
