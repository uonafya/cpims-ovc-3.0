import uuid
from django.db import models
from django.utils import timezone

from cpovc_auth.models import AppUser


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

'''
class MetadataManagement(models.Model):
    """Metadata Management"""

    meta_id = models.UUIDField(
        primary_key=True, default=uuid.uuid1, editable=False)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    app_device_id = models.CharField(
        db_index=True, max_length=25, blank=True, null=True)
    app_lon = models.DecimalField(
        max_digits=15, decimal_places=10, blank=True, null=True)
    app_lat = models.DecimalField(
        max_digits=15, decimal_places=10, blank=True, null=True)
    app_start_datetime = models.DateTimeField(
        default=timezone.now, blank=True, null=True)
    app_end_datetime = models.DateTimeField(
        default=timezone.now, blank=True, null=True)
    approver_user = models.ForeignKey(
        AppUser, on_delete=models.CASCADE, blank=True, null=True)
    approval_datetime = models.DateTimeField(
        default=timezone.now, blank=True, null=True)
    other_params = models.Textarea(blank=True, null=True)
    timestamp_created = models.DateTimeField(default=timezone.now)
    timestamp_updated = models.DateTimeField(auto_now=True)
    is_void = models.BooleanField(default=False)

    class Meta:
        """Override Params."""

        db_table = 'metadata_management'
        verbose_name = 'Metadata Management'
        verbose_name_plural = 'Metadata Managements'

    def __str__(self):
        """To be returned by admin actions."""
        return str(self.meta_id)
'''