import uuid
from django.db import models
from django.utils import timezone
from cpovc_forms.models import RegPerson, RegOrgUnit

# Create your models here from existing SQL.
'''
 intervention_id         | uuid                     |           | not null | 
 dreams_id               | character varying(15)    |           | not null | 
 cpims_id                | integer                  |           |          | 
 nemis_no                | character varying(15)    |           |          | 
 bcert_no                | character varying(25)    |           |          | 
 county_code             | integer                  |           |          | 
 county_name             | character varying(50)    |           |          | 
 sub_county_code         | integer                  |           |          | 
 sub_county_name         | character varying(70)    |           |          | 
 ward_code               | integer                  |           |          | 
 ward_name               | character varying(70)    |           |          | 
 intervention_date       | date                     |           |          | 
 intervention_type_code  | character varying(70)    |           |          | 
 intervention_type_name  | character varying(100)   |           |          | 
 hts_result              | character varying(100)   |           |          | 
 no_of_sessions_attended | character varying(10)    |           |          | 
 pregnancy_test_result   | character varying(15)    |           |          | 
 timestamp_created       | timestamp with time zone |           | not null | 
'''


class DREAMSServices(models.Model):
    """DREAMS Services"""

    intervention_id = models.UUIDField(
        primary_key=True, default=uuid.uuid1, editable=False)
    dreams_id = models.CharField(max_length=15)
    person = models.ForeignKey(RegPerson, on_delete=models.CASCADE, null=True)
    date_of_birth = models.DateField()
    birth_certificate_no = models.CharField(max_length=15)
    org_unit = models.ForeignKey(
        RegOrgUnit, on_delete=models.CASCADE, null=True)
    nemis_no = models.CharField(max_length=15, null=True)
    bcert_no = models.CharField(max_length=25, null=True)
    county_code = models.IntegerField()
    county_name = models.CharField(max_length=50)
    sub_county_code = models.IntegerField(null=True)
    sub_county_name = models.CharField(max_length=70)
    ward_code = models.IntegerField()
    ward_name = models.CharField(max_length=70)
    intervention_date = models.DateField()
    intervention_type_code = models.CharField(max_length=10)
    intervention_type_name = models.CharField(max_length=200)
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
