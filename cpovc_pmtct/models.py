import uuid
from django.db import models
from django.utils import timezone
from cpovc_registry.models import RegPerson, RegOrgUnit
from cpovc_ovc.models import OVCSchool, OVCHouseHold
from cpovc_auth.models import AppUser
from cpovc_forms.models import OVCCareForms


class OVCPMTCTRegistration(models.Model):
    pmtct_id = models.UUIDField(
        primary_key=True, default=uuid.uuid1, editable=False)
    person = models.ForeignKey(RegPerson, on_delete=models.CASCADE)
    registration_date = models.DateField(default=timezone.now)

    school = models.ForeignKey(
        OVCSchool, on_delete=models.CASCADE, null=True)
    child_cbo = models.ForeignKey(
        RegOrgUnit, on_delete=models.CASCADE, related_name='pmtct_cbo')
    caregiver = models.ForeignKey(
        RegPerson, on_delete=models.CASCADE, null=True,
        related_name='pmtct_caregiver')
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


# Pregnant Women/Adolesctent Monthly Tracker

class PMTCTEvents(models.Model):
    event = models.UUIDField(
        primary_key=True, default=uuid.uuid1, editable=False)
    event_type_id = models.CharField(max_length=10)
    event_counter = models.IntegerField(default=0)
    event_score = models.IntegerField(null=True, default=0)
    date_of_event = models.DateField(default=timezone.now)
    created_by = models.IntegerField(null=True, default=404)
    timestamp_created = models.DateTimeField(default=timezone.now)
    is_void = models.BooleanField(default=False)
    sync_id = models.UUIDField(default=uuid.uuid1, editable=False)
    app_user = models.ForeignKey(
        AppUser, related_name='pmtct_user', on_delete=models.CASCADE)
    person = models.ForeignKey(
        RegPerson, related_name='pmtct_person', null=True,
        on_delete=models.CASCADE)

    class Meta:
        db_table = 'pmtct_events_pm'


class OVCPregnantWomen(models.Model):
    preg_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey(RegPerson, on_delete=models.CASCADE)
    date_of_contact = models.DateField(
        default=timezone.now, blank=True, null=True)
    date_test_done2a = models.DateField(blank=True, null=True)
    test_result2b = models.BooleanField(null=True)
    date_test_done3a = models.DateField(blank=True, null=True)
    test_result3b = models.BooleanField(null=True)
    date_test_done4a = models.DateField(blank=True, null=True)
    test_result4b = models.BooleanField(null=True)
    date_test_done5a = models.DateField(blank=True, null=True)
    test_result5b = models.BooleanField(null=True)
    anc_date1 = models.DateField(default=timezone.now, blank=True, null=True)
    anc_date2 = models.DateField(default=timezone.now, blank=True, null=True)
    anc_date3 = models.DateField(default=timezone.now, blank=True, null=True)
    anc_date4 = models.DateField(default=timezone.now, blank=True, null=True)
    mode_of_delivery = models.BooleanField(null=True)
    facility_code = models.CharField(max_length=10, null=True)
    ccc_no = models.IntegerField(null=True)
    vl_result = models.IntegerField(null=True)
    vl_test_date = models.DateField(
        default=timezone.now, blank=True, null=True)  # date new 1
    disclosure_done = models.BooleanField(null=True)
    event = models.ForeignKey(PMTCTEvents, on_delete=models.CASCADE)
    is_void = models.BooleanField(default=False)
    date_of_event = models.DateField(
        default=timezone.now, blank=True, null=True)  # date
    timestamp_created = models.DateTimeField(auto_now_add=True)
    timestamp_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ovc_pregnant_women'

    def __str__(self):
        return str(self.tracker_id)


class PMTCTQuestions(models.Model):
    question_id = models.UUIDField(
        primary_key=True, default=uuid.uuid1, editable=False)
    code = models.CharField(max_length=20)
    question = models.CharField(max_length=55)
    domain = models.CharField(max_length=10)
    question_text = models.CharField(max_length=255)
    question_type = models.CharField(max_length=20, null=False)
    form = models.ForeignKey(
        OVCCareForms, related_name='pmtct_form', on_delete=models.CASCADE)
    is_void = models.BooleanField(default=False)
    timestamp_created = models.DateTimeField(auto_now_add=True)
    timestamp_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code

    class Meta:
        db_table = 'pmtct_questions_pmtct'


class PMTCTPregnantWA(models.Model):
    pmtct_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey(RegPerson, on_delete=models.CASCADE)
    caregiver = models.ForeignKey(
        RegPerson, on_delete=models.CASCADE, related_name='pregwa_caregiver')
    question_code = models.CharField(max_length=10, null=False, blank=True)
    question = models.ForeignKey(PMTCTQuestions, on_delete=models.CASCADE)
    answer = models.CharField(max_length=15)
    event = models.ForeignKey(PMTCTEvents, on_delete=models.CASCADE)

    timestamp_created = models.DateTimeField(default=timezone.now)
    is_void = models.BooleanField(default=False)
    timestamp_updated = models.DateTimeField(auto_now=True)

    def save(
            self, force_insert=False, force_update=False,
            using=None, update_fields=None):
        self.question_code = self.question.code
        super(PMTCTPregnantWA, self).save(
            force_insert, force_update, using, update_fields)

    class Meta:
        db_table = 'pmtct_pregnant_wa'

    def __str__(self):
        return str(self.pmtct_id)


class OVCHEITracker(models.Model):
    hei_id = models.UUIDField(
        primary_key=True, default=uuid.uuid1, editable=False)
    person = models.ForeignKey(RegPerson, on_delete=models.CASCADE, related_name="person_ovcheitracker")
    hivstatus = models.CharField(max_length=20)
    hivpositive = models.CharField(max_length=20, blank=True, null=True)
    facility = models.CharField(max_length=20, blank=True, null=True)
    ccc = models.CharField(max_length=20, blank=True, null=True)
    vl = models.CharField(max_length=20, blank=True, null=True)
    vldate = models.DateField(default=timezone.now, null=True)

    f1date = models.DateField(default=timezone.now, null=True)
    f1hivtest = models.CharField(max_length=20, null=True)
    f1testresults = models.CharField(max_length=20)
    f1vlresults = models.CharField(max_length=20)
    f1prophylaxis = models.CharField(max_length=20)
    f1mode = models.CharField(max_length=20)

    f2date = models.DateField(default=timezone.now, null=True)
    f2hivtest = models.CharField(max_length=20, blank=True, null=True)
    f2testresults = models.CharField(max_length=20, blank=True, null=True)
    f2vlresults = models.CharField(max_length=20, blank=True, null=True)
    f2prophylaxis = models.CharField(max_length=20, blank=True, null=True)
    f2immunization = models.CharField(max_length=20, blank=True, null=True)
    f2mode = models.CharField(max_length=20, blank=True, null=True)

    f3date = models.DateField(default=timezone.now, null=True)
    f3hivtest = models.CharField(max_length=20, blank=True, null=True)
    f3testresults = models.CharField(max_length=20, blank=True, null=True)
    f3vlresults = models.CharField(max_length=20, blank=True, null=True)
    f3prophylaxis = models.CharField(max_length=20, blank=True, null=True)
    f3immunization = models.CharField(max_length=20, blank=True, null=True)
    f3mode = models.CharField(max_length=20, blank=True, null=True)

    f4date = models.DateField(default=timezone.now, null=True)
    f4hivtest = models.CharField(max_length=20, blank=True, null=True)
    f4testresults = models.CharField(max_length=20, blank=True, null=True)
    f4vlresults = models.CharField(max_length=20, blank=True, null=True)
    f4prophylaxis = models.CharField(max_length=20, blank=True, null=True)
    f4immunization = models.CharField(max_length=20, blank=True, null=True)
    f4mode = models.CharField(max_length=20, blank=True, null=True)

    f5date = models.DateField(default=timezone.now, null=True)
    f5hivtest = models.CharField(max_length=20, blank=True, null=True)
    f5testresults = models.CharField(max_length=20, blank=True, null=True)
    f5vlresults = models.CharField(max_length=20, blank=True, null=True)
    f5prophylaxis = models.CharField(max_length=20, blank=True, null=True)
    f5immunization = models.CharField(max_length=20, blank=True, null=True)
    f5mode = models.CharField(max_length=20, blank=True, null=True)
    reason = models.CharField(max_length=20, blank=True, null=True)
    comments = models.CharField(max_length=20, blank=True, null=True)

    event = models.ForeignKey(PMTCTEvents, on_delete=models.CASCADE)
    date_of_event = models.DateField(default=timezone.now, null=True)
    timestamp_created = models.DateTimeField(default=timezone.now)
    timestamp_updated = models.DateTimeField(default=timezone.now)
    is_void = models.BooleanField(default=False)
    sync_id = models.UUIDField(default=uuid.uuid1, editable=False)

    class Meta:
        db_table = 'ovc_hei_tracker_pmtct'


class PMTCTHEI(models.Model):
    pmtct_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey(RegPerson, on_delete=models.CASCADE, related_name="person_pmtcthei")
    caregiver = models.ForeignKey(
        RegPerson, on_delete=models.CASCADE, related_name='caregiver_pmtct_hei')
    question_code = models.CharField(max_length=10, null=False, blank=True)
    question = models.ForeignKey(PMTCTQuestions, on_delete=models.CASCADE, )
    answer = models.CharField(max_length=100)
    event = models.ForeignKey(PMTCTEvents, on_delete=models.CASCADE)

    timestamp_created = models.DateTimeField(default=timezone.now)
    is_void = models.BooleanField(default=False)
    timestamp_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.answer

    def save(
            self, force_insert=False, force_update=False,
            using=None, update_fields=None):
        self.question_code = self.question.code
        super(PMTCTHEI, self).save(force_insert,
                                   force_update, using, update_fields)

    class Meta:
        db_table = 'pmtct_hei_pmtct'

    def __str__(self):
        return str(self.pmtct_id)
