import uuid
from django.db import models
from django.utils import timezone
from cpovc_registry.models import RegPerson, RegOrgUnit
from cpovc_ovc.models import OVCSchool
from cpovc_auth.models import AppUser


class OVCPreventiveGroup(models.Model):
    gid = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
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
    preventive_reg_id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    person = models.ForeignKey(RegPerson, on_delete=models.CASCADE)
    caregiver = models.ForeignKey(RegPerson, on_delete=models.CASCADE, null=True, related_name='caregiver')
    intervention = models.CharField(max_length=10)
    group = models.ForeignKey(OVCPreventiveGroup, on_delete=models.CASCADE, null=True)
    school = models.ForeignKey(OVCSchool, on_delete=models.CASCADE, null=True)
    child_cbo = models.ForeignKey(RegOrgUnit, on_delete=models.CASCADE)
    chv = models.ForeignKey(RegPerson, related_name='preventive_chv', null=true)
    registration_date = models.DateField(default=timezone.now)
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
        return '%s %s' % str(self.preventive_reg_id)


class OVCPreventiveEvents(models.Model):
    event = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    event_type_id = models.CharField(max_length=10)
    event_counter = models.IntegerField(default=0)
    event_score = models.IntegerField(null=True, default=0)
    date_of_event = models.DateField(default=timezone.now)
    date_of_previous_event = models.DateTimeField(null=True)
    created_by = models.IntegerField(null=True, default=404)
    timestamp_created = models.DateTimeField(default=timezone.now)
    is_void = models.BooleanField(default=False)
    sync_id = models.UUIDField(default=uuid.uuid1, editable=False)
    app_user = models.ForeignKey(AppUser, default=1, on_delete=models.CASCADE)
    person = models.ForeignKey(RegPerson, on_delete=models.CASCADE)

    class Meta:
        db_table = 'ovc_preventive_events'

        def __unicode__(self):
            return '%s %s' % str(self.event)


class OVCPreventiveEbi(models.Model):
    """ This table will hold Sessions Data """


ebi_id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
person_id = models.ForeignKey(RegPerson, on_delete=models.CASCADE)
domain = models.CharField(max_length=4, null=True)  # sinovuyo or fmp or hcbf
ebi_provided = models.CharField(max_length=25)
ebi_provider = models.ForeignKey(RegOrgUnit, on_delete=models.CASCADE, related_name='ebi_provide_fk')  # cbo
ebi_session = models.CharField(max_length=4)  ##session e.g s1, s2,
ebi_session_type = models.CharField(max_length=10)  ## general or makeup
place_of_ebi = models.ForeignKey('cpovc_main.SetupGeography', related_name='ebi_place')  # geo
date_of_encounter_event = models.DateField(default=timezone.now, null=True)
event = models.ForeignKey(OVCPreventiveEvents, on_delete=models.CASCADE)
ebi_grouping_id = models.UUIDField(default=uuid.uuid1, editable=False)
is_void = models.BooleanField(default=False)
sync_id = models.UUIDField(default=uuid.uuid1, editable=False)


class Meta:
    db_table = 'ovc_preventive_ebi'

    def __unicode__(self):
        return '%s %s' % str(self.ebi_id)


class OVCPreventiveService(models.Model):
    """ This table will hold Service and refferral Data """
    ebi_service_id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    person_id = models.ForeignKey(RegPerson, on_delete=models.CASCADE)
    domain = models.CharField(max_length=10, null=True)  # sinovuyo or fmp or hcbf
    ebi_service_provided = models.CharField(max_length=25)
    ebi_provider = models.ForeignKey(RegOrgUnit, on_delete=models.CASCADE, related_name='ebi_provider_fk')  # cbo
    ebi_service_client = models.CharField(max_length=4, null=True)  # cg or ovc
    ebi_service_referred = models.CharField(max_length=4,
                                            null=True)  # service referred. Add ebi services to list general
    ebi_service_completed = models.CharField(max_length=4, null=True)  # yesno
    place_of_ebi_service = models.ForeignKey('cpovc_main.SetupGeography', related_name='ebi_service_place')  # geo
    date_of_encounter_event = models.DateField(default=timezone.now, null=True)
    event = models.ForeignKey(OVCPreventiveEvents, on_delete=models.CASCADE)
    ebi_grouping_id = models.UUIDField(default=uuid.uuid1, editable=False)
    is_void = models.BooleanField(default=False)
    sync_id = models.UUIDField(default=uuid.uuid1, editable=False)

    class Meta:
        db_table = 'ovc_preventive_service'

        def __unicode__(self):
            return '%s %s' % str(self.ebi_service_id)
