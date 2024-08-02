import uuid
from django.db import models
from django.utils import timezone

from cpovc_auth.models import AppUser
from cpovc_registry.models import RegPerson


class DeviceManagement(models.Model):
    """Device Management Service for Mobile App"""

    dm_id = models.UUIDField(
        primary_key=True, default=uuid.uuid1, editable=False)
    device_id = models.CharField(db_index=True, max_length=25)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    timestamp_created = models.DateTimeField(default=timezone.now)
    timestamp_updated = models.DateTimeField(auto_now=True)
    is_blocked = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_void = models.BooleanField(default=False)

    class Meta:
        """Override Params."""

        unique_together = ('device_id', 'user')

        db_table = 'api_device_management'
        verbose_name = 'API Device Management'
        verbose_name_plural = 'API Device Managements'

    def __str__(self):
        """To be returned by admin actions."""
        return str(self.dm_id)


class MetadataManagement(models.Model):
    """Metadata Management Service for Mobile App"""

    meta_id = models.UUIDField(
        primary_key=True, default=uuid.uuid1, editable=False)
    person = models.ForeignKey(RegPerson, on_delete=models.CASCADE)
    device_id = models.CharField(db_index=True, max_length=25, null=True)
    form_id = models.CharField(max_length=25, null=True)
    form_unique_id = models.UUIDField(default=uuid.uuid4, null=True)
    house_hold_id = models.UUIDField(default=uuid.uuid4, null=True)
    # Device
    device_user = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='device_user')
    device_event_id = models.UUIDField(default=uuid.uuid4)
    date_of_event = models.DateField()
    device_timestamp_created = models.DateTimeField(default=timezone.now)
    location_lat = models.DecimalField(max_digits=22, decimal_places=10, blank=True, null=True)
    location_lon = models.DecimalField(max_digits=22, decimal_places=10, blank=True, null=True)
    device_start_timestamp = models.DateTimeField(null=True)
    device_end_timestamp = models.DateTimeField(null=True)
    # Approval
    approve_user = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='approve_user')
    approve_event_id = models.UUIDField(default=uuid.uuid4)
    approve_timestamp_created = models.DateTimeField(auto_now_add=True)
    is_void = models.BooleanField(default=False)


    class Meta:
        """Override Params."""

        db_table = 'api_metadata_management'
        verbose_name = 'API Metadata Management'
        verbose_name_plural = 'API Metadata Managements'

    def __str__(self):
        """To be returned by admin actions."""
        return str(self.meta_id)