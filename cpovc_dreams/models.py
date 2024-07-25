import uuid
from django.db import models
from django.utils import timezone
from cpovc_forms.models import RegPerson, RegOrgUnit


class DREAMSServices(models.Model):
    """DREAMS Services"""

    intervention_id = models.UUIDField(
        primary_key=True, default=uuid.uuid1, editable=False)
    dreams_id = models.CharField(max_length=15)
    person = models.ForeignKey(RegPerson, on_delete=models.CASCADE, null=True)
    date_of_birth = models.DateField()
    birth_certificate_no = models.CharField(max_length=20, null=True)
    org_unit = models.ForeignKey(
        RegOrgUnit, on_delete=models.CASCADE, null=True)
    nemis_no = models.CharField(max_length=15, null=True)
    bcert_no = models.CharField(max_length=25, null=True)
    county_code = models.IntegerField(null=True)
    county_name = models.CharField(max_length=50, null=True)
    sub_county_code = models.CharField(max_length=50, null=True)
    sub_county_name = models.CharField(max_length=70, null=True)
    ward_code = models.IntegerField()
    ward_name = models.CharField(max_length=70)
    intervention_date = models.DateField()
    intervention_type_code = models.CharField(max_length=10, null=True)
    intervention_type_name = models.CharField(max_length=200, null=True)
    hts_result = models.CharField(max_length=100, null=True)
    no_of_sessions_attended = models.IntegerField(null=True)
    pregnancy_test_result = models.CharField(max_length=15, null=True)
    timestamp_created = models.DateTimeField(default=timezone.now)
    is_void = models.BooleanField(default=False)

    class Meta:
        """Override some params."""

        db_table = 'dreams_interventions'
        verbose_name = 'DREAMS Intervention'
        verbose_name_plural = 'DREAMS Interventions'

    def __str__(self):
        """To be returned by admin actions."""
        return self.dreams_id

