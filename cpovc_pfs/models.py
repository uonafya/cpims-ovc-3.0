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
    chv = models.ForeignKey(RegPerson, related_name='preventive_chv', null=True, on_delete=models.CASCADE)
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
    place_of_ebi = models.ForeignKey('cpovc_main.SetupGeography', related_name='ebi_place', on_delete=models.CASCADE)  # geo
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
    """ This table will hold Service and referral Data """
    ebi_service_id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    person_id = models.ForeignKey(RegPerson, on_delete=models.CASCADE)
    domain = models.CharField(max_length=10, null=True)  # sinovuyo or fmp or hcbf
    ebi_service_provided = models.CharField(max_length=25)
    ebi_provider = models.ForeignKey(RegOrgUnit, on_delete=models.CASCADE, related_name='ebi_provider_fk')  # cbo
    ebi_service_client = models.CharField(max_length=4, null=True)  # cg or ovc
    ebi_service_referred = models.CharField(max_length=4,
                                            null=True)  # service referred. Add ebi services to list general
    ebi_service_completed = models.CharField(max_length=4, null=True)  # yesno
    place_of_ebi_service = models.ForeignKey('cpovc_main.SetupGeography', related_name='ebi_service_place', on_delete=models.CASCADE)  # geo
    date_of_encounter_event = models.DateField(default=timezone.now, null=True)
    event = models.ForeignKey(OVCPreventiveEvents, on_delete=models.CASCADE)
    ebi_grouping_id = models.UUIDField(default=uuid.uuid1, editable=False)
    is_void = models.BooleanField(default=False)
    sync_id = models.UUIDField(default=uuid.uuid1, editable=False)

    class Meta:
        db_table = 'ovc_preventive_service'

        def __unicode__(self):
            return '%s %s' % str(self.ebi_service_id)


class OVCPrevEvaluation(models.Model):
    evaluation_id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    person = models.ForeignKey(RegPerson, on_delete=models.CASCADE)
    ref_caregiver = models.ForeignKey(RegPerson, on_delete=models.CASCADE, related_name='preval_caregiver')
    know_where = models.CharField(max_length=10)
    know_what = models.CharField(max_length=10)
    know_who = models.CharField(max_length=10)
    often_watch_tv = models.CharField(max_length=10)
    know_what_watching_tv = models.CharField(max_length=10)
    not_watch_programs_tv = models.CharField(max_length=10)
    talk_sex_on_tv = models.CharField(max_length=10)
    watch_tv_with_child = models.CharField(max_length=10)
    what_sex_is = models.CharField(max_length=10)
    talk_hiv = models.CharField(max_length=10)
    talk_sti = models.CharField(max_length=10)
    talk_sex_issues = models.CharField(max_length=10)
    talk_sex_issue_what = models.CharField(max_length=10)
    ask_sex_issue = models.CharField(max_length=10)
    ask_sex_issue_respond = models.CharField(max_length=10)
    question_about_sex_issue = models.CharField(max_length=10)
    know_how_talk_sex_issue = models.CharField(max_length=10)
    information_sex_issues = models.CharField(max_length=10)
    bad_things_from_sex = models.CharField(max_length=10)
    talk_sex_child_opinion = models.CharField(max_length=10)
    ready_learn_sex_issues = models.CharField(max_length=10)
    encourage_have_sex = models.CharField(max_length=10)
    young_learn_sex_issues = models.CharField(max_length=10)
    someone_talk_sex_issues = models.CharField(max_length=10)
    parent_responsibility_talk_sex = models.CharField(max_length=10)
    happy_with_child = models.CharField(max_length=10)
    event = models.ForeignKey(OVCPreventiveEvents, on_delete=models.CASCADE)
    fmp_pre_grouping_id = models.UUIDField(default=uuid.uuid1, editable=False)
    timestamp_created = models.DateTimeField(default=timezone.now)
    timestamp_updated = models.DateTimeField(default=timezone.now)
    is_void = models.BooleanField(default=False)
    sync_id = models.UUIDField(default=uuid.uuid1, editable=False)

    class Meta:
        db_table = 'ovc_prev_fmp_evaluation'

        def __unicode__(self):
            return '%s %s' % str(self.evaluation_id)


class OVCPrevSinovuyoCaregiverEvaluation(models.Model):
    evaluation_id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    person = models.ForeignKey(RegPerson, on_delete=models.CASCADE)
    ref_caregiver = models.ForeignKey(RegPerson, on_delete=models.CASCADE, related_name='preval_caregiver_caregiver')
    date_of_event = models.DateField(default=timezone.now)  # date_of-assessment
    bd_age = models.CharField(max_length=10)
    bd_sex = models.CharField(max_length=10)
    bd_read = models.CharField(max_length=10)
    bd_education_level = models.CharField(max_length=10)
    bd_biological_children = models.CharField(max_length=10)
    bd_non_biological_children = models.CharField(max_length=10)
    bd_children_not_in_school = models.CharField(max_length=10)
    watch_tv_with_child = models.CharField(max_length=10)
    bd_source_income = models.CharField(max_length=10)
    bd_adults_contribute_hh_income = models.CharField(max_length=10)
    bd_children_contribute_hh_income = models.CharField(max_length=10)
    bd_biological_mother = models.CharField(max_length=10)
    bd_bm_live_hh = models.CharField(max_length=10, null=True)
    bd_biological_father = models.CharField(max_length=10)
    bd_bf_live_hh = models.CharField(max_length=10, null=True)
    bd_money_basic_expenses = models.CharField(max_length=10)
    bd_violence = models.CharField(max_length=10)
    bd_adult_unwell = models.CharField(max_length=10)
    bad_things_from_sex = models.CharField(max_length=10)
    bd_child_unwell = models.CharField(max_length=10)
    bd_miss_school = models.CharField(max_length=10)
    bd_hiv_status = models.CharField(max_length=10)
    bd_children_hiv_status = models.CharField(max_length=10)
    bd_hiv_prevention = models.CharField(max_length=10)
    bd_two_meals = models.CharField(max_length=10)
    bd_missing_meal = models.CharField(max_length=10)
    rc_discuss_child_needs = models.CharField(max_length=10)
    rc_discipline = models.CharField(max_length=10)
    rc_tells_bothering = models.CharField(max_length=10)
    rc_involve_decisions = models.CharField(max_length=10)
    cb_child_obedient = models.CharField(max_length=10)
    cb_fights_children = models.CharField(max_length=10)
    dc_often_discipline = models.CharField(max_length=10)
    dc_physical_discipline = models.CharField(max_length=10)
    dc_upset_child = models.CharField(max_length=10)
    sp_caring_energy = models.CharField(max_length=10)
    sp_source_stress = models.CharField(max_length=10)
    sp_physical_punish = models.CharField(max_length=10)
    fs_depressed = models.CharField(max_length=10)
    fs_effort = models.CharField(max_length=10)
    fs_hopeful = models.CharField(max_length=10)
    fi_money_important_items = models.CharField(max_length=10)
    fi_worried_money = models.CharField(max_length=10)
    event = models.ForeignKey(OVCPreventiveEvents, on_delete=models.CASCADE)
    fmp_pre_grouping_id = models.UUIDField(default=uuid.uuid1, editable=False)
    timestamp_created = models.DateTimeField(default=timezone.now)
    timestamp_updated = models.DateTimeField(default=timezone.now)
    is_void = models.BooleanField(default=False)
    sync_id = models.UUIDField(default=uuid.uuid1, editable=False)

    class Meta:
        db_table = 'ovc_prev_sinovuyo_caregiver_evaluation'

        def __unicode__(self):
            return '%s %s' % str(self.evaluation_id)


class OVCPrevSinovyoTeenEvaluation(models.Model):
    evaluation_id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    person = models.ForeignKey(RegPerson, on_delete=models.CASCADE)
    ref_caregiver = models.ForeignKey(RegPerson, on_delete=models.CASCADE, related_name='preval_teen_caregiver')
    date_of_event = models.DateField(default=timezone.now)  ## assessment date
    bd_age = models.CharField(max_length=10)
    bd_sex = models.CharField(max_length=10)
    bd_read = models.CharField(max_length=10)
    bd_education_level = models.CharField(max_length=10)
    bd_class = models.CharField(max_length=10)
    bd_bd_boarding_status = models.CharField(max_length=10)
    bd_biological_children = models.CharField(max_length=10)
    bd_live_biological_father = models.CharField(max_length=10)
    bd_live_biological_mother = models.CharField(max_length=10)
    bd_disability = models.CharField(max_length=10)
    bd_money_essentials = models.CharField(max_length=10)
    bd_violence = models.CharField(max_length=10)
    bd_adult_unwell = models.CharField(max_length=10)
    bd_child_unwell = models.CharField(max_length=10)
    bd_miss_school = models.CharField(max_length=10)
    bd_hiv_status = models.CharField(max_length=10)
    bd_hiv_prevention = models.CharField(max_length=10)
    bd_two_meals = models.CharField(max_length=10)
    bd_missing_meal = models.CharField(max_length=10)
    rc_discuss_child_needs = models.CharField(max_length=10)
    rc_discipline = models.CharField(max_length=10)
    rc_tells_bothering = models.CharField(max_length=10)
    rc_involve_decisions = models.CharField(max_length=10)
    cb_child_obedient = models.CharField(max_length=10)
    cb_fights_children = models.CharField(max_length=10)
    dc_often_discipline = models.CharField(max_length=10)
    dc_physical_discipline = models.CharField(max_length=10)
    dc_upset_child = models.CharField(max_length=10)
    sp_physical_punish = models.CharField(max_length=10)
    fs_unhappy = models.CharField(max_length=10)
    fs_too_tired = models.CharField(max_length=10)
    fs_hopeful = models.CharField(max_length=10)
    event = models.ForeignKey(OVCPreventiveEvents, on_delete=models.CASCADE)
    fmp_pre_grouping_id = models.UUIDField(default=uuid.uuid1, editable=False)
    timestamp_created = models.DateTimeField(default=timezone.now)
    timestamp_updated = models.DateTimeField(default=timezone.now)
    is_void = models.BooleanField(default=False)
    sync_id = models.UUIDField(default=uuid.uuid1, editable=False)

    class Meta:
        db_table = 'ovc_prev_sinovuyo_teen_evaluation'

        def __unicode__(self):
            return '%s %s' % str(self.evaluation_id)
