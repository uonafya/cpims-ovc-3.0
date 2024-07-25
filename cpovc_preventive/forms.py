from django import forms
from django.utils.translation import gettext_lazy as _

from cpovc_main.functions import get_list

person_type_list = get_list('person_type_id', 'Please Select Type')
school_level_list = get_list('school_level_id', 'Please Select Level')
eligibility_list = get_list('eligibility_criteria_id', '')
exit_list = get_list('exit_reason_id', 'Please Select one')
admission_list = get_list('school_type_id', 'Please Select one')
intervention_list = get_list('pfs_intervention_id', 'Please Select one')
yesno_list = get_list('yesno_id', 'Please Select')

# registers
INTERVENTION_CHOICES = get_list('attendance_reg_domains', 'Please Select')
OVC_REFFERAL_SERVICES = get_list('attendance_reg_services', 'Please Select')
ATTENDANCE_CHOICES = get_list('session_id', 'Please Select')
ATTENDANCE_CLIENT = get_list('attendance_reg_client', 'Please Select')


class OVCPreventiveRegistrationForm(forms.Form):
    """OVC registration form."""

    def __init__(self, guids, *args, **kwargs):
        """Override methods."""
        super(OVCPreventiveRegistrationForm, self).__init__(*args, **kwargs)

    registration_date = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'id': 'registration_date',
                   'data-parsley-required': "true"}))

    exit_date = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'id': 'exit_date'}))

    is_exited = forms.CharField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={'class': 'form-control',
                   'id': 'is_exited'}))

    cbo_uid = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'initial': '00001', 'id': 'cbo_uid',
                   'data-parsley-required': "true"}))

    cbo_uid_check = forms.CharField(
        required=False,
        widget=forms.HiddenInput(
            attrs={'class': 'form-control',
                   'initial': '00001',
                   'id': 'cbo_uid_check'}))

    cbo_id = forms.CharField(
        required=False,
        widget=forms.HiddenInput(
            attrs={'class': 'form-control',
                   'id': 'cbo_id'}))

    cbo = forms.ChoiceField(
        choices=(),
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'cbo'}))

    intervention = forms.ChoiceField(
        choices=intervention_list,
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'data-parsley-required': "true",
                   'id': 'intervention'}))

    exit_reason = forms.ChoiceField(
        choices=exit_list,
        required=False,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'exit_reason'}))

    school_level = forms.ChoiceField(
        choices=school_level_list,
        required=False,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'school_level'}))

    school_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Start typing then select',
                   'id': 'school_name'}))

    school_id = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'readonly': 'readonly',
                   'id': 'school_id'}))

    admission_type = forms.ChoiceField(
        choices=admission_list,
        required=False,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'admission_type'}))

    school_class = forms.ChoiceField(
        choices=(),
        required=False,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'school_class'}))


class PREVENTIVE_ATTENDANCE_REGISTER_FORM(forms.Form):
    INTERVENTION = forms.CharField(widget=forms.Select(
        choices=INTERVENTION_CHOICES,
        attrs={'placeholder': _('Select Date'),
               'class': 'form-control',
               'name': 'prevention_register',
               'id': 'intervention_prevention_register'}
    ))

    SESSION_ATTENDED_DAYS = forms.CharField(widget=forms.Select(
        choices=ATTENDANCE_CHOICES,
        attrs={'placeholder': _('Select Date'),
               'class': 'form-control',
               'name': 'SESSION_ATTENDED_DAYS',
               'id': 'session_attended_days'}))

    REFFERAL_SERVICES = forms.CharField(widget=forms.Select(
        choices=OVC_REFFERAL_SERVICES,
        attrs={'placeholder': _('Select Date'),
               'class': 'form-control',
               'name': 'REFFERAL_SERVICES',
               'id': 'refferal_services_id'}))

    REFERAL_MADE = forms.ChoiceField(
        choices=((1, 'Y'), ('0', 'N')),
        widget=forms.RadioSelect(
            attrs={'placeholder': _('Select Date'),
                   'class': 'form-control',
                   'name': 'REFERAL_MADE',
                   'id': 'refferal_made_id',
                   }))
    ATTENDANCE_CLIENT = forms.CharField(widget=forms.Select(
        choices=ATTENDANCE_CLIENT,
        attrs={'placeholder': _('Select Date'),
               'class': 'form-control',
               'name': 'ATTENDANCE_CLIENT',
               'id': 'client_name'}
    ))

    OTHER_SERVICES_SPECIFY = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _('Other Services Specify'),
               'class': 'form-control',
               'id': 'other_preventive_services_specified',
               'data-parsley-required': "true",
               #    'readonly': "true",
               'name': 'OTHER_SERVICES_SPECIFY',
               'data-parsley-group': 'group0'
               }))

    DATE_OF_SERVICE_ENCOUNTER = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date of service encounter'),
               'class': 'form-control',
               'name': 'date of makeup',
               'id': 'date_of_service_encounter'
               }))

    COMPLETED_ALL_SESSIONS = forms.ChoiceField(
        choices=(('Yes', 'Yes'), ('No', 'No')),
        required=False,
        widget=forms.RadioSelect(
            attrs={'placeholder': _('Select Date'),
                   # 'class': 'form-control',
                   'name': 'COMPLETED_ALL_SESSIONS',
                   'id': 'completed_all_sessions',

                   }))

    OVC_REFFEREDFOR_SERVICES = forms.ChoiceField(
        choices=(('Yes', 'Yes'), ('No', 'No')),
        widget=forms.RadioSelect(
            attrs={
                # 'class': 'form-control',
                'name': 'OVC_REFFEREDFOR_SERVICES',
                'id': 'reffered_for_service',

            }))

    OVC_REFFERAL_COMPLETED = forms.ChoiceField(
        choices=(('Yes', 'Yes'), ('No', 'No')),
        widget=forms.RadioSelect(
            attrs={'placeholder': _('Select Date'),
                   # 'class': 'form-control',
                   'name': 'OVC_REFFERAL_COMPLETED',
                   'id': 'ovc_refferal_completed'}
        ))

    SESSION_DATE = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date of Event'),
               'class': 'form-control',
               'name': 'date of makeup',
               'id': 'session_date_id'
               }))

    COMMENTS = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Attendance Comments'),
               'class': 'form-control',
               'id': 'attendance_comments',
               'rows': '2'}))

    person = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'id': 'person',
               'type': 'hidden'
               }))
    caretaker_id = forms.CharField(widget=forms.HiddenInput(
        attrs={'id': 'caretaker_id'}))

    service_provided_list = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'hidden',
               'id': 'service_provided_list'}))

    preventive_assessment_provided_list = forms.CharField(
        widget=forms.TextInput(
            attrs={'type': 'hidden',
                   'id': 'preventive_assessment_provided_list'}))

    assessment_provided_list = forms.CharField(
        widget=forms.TextInput(
            attrs={'type': 'hidden',
                   'id': 'assessment_provided_list'}))


class OVCSinovuyoCaregiverAssessmentForm(forms.Form):
    """
    Sinovuyo Care-giver Preventive Pre and Post Program Assessment Form
    """
    CHOICES_TYPE_ASSESSMENT = get_list("evaluation_type_id")
    CHOICES_READ = get_list('literacy_lvl_id', "Please select")
    CHOICES_EDUCATION = get_list("school_level_id")
    YES_NO_CHOICES = get_list('yesno_id')
    CHOICES_INCOME = get_list("employed_id", "Please select")
    CHOICES_RELATIONSHIP = get_list(
        'relationship_caregiver_id', "Please select")
    CHOICES_BEHAVIOR = get_list("my_behaviour_id", "Please select")
    CHOICES_DISCIPLINE = get_list("dsp_times_id", "Please select")
    CHOICES_BIOLOGICAL_FATHER = get_list(
        "father_mortality_id", "Please select")
    CHOICES_BIOLOGICAL_MOTHER = get_list(
        "mother_mortality_id", "Please select")
    CHOICES_HIV = get_list("under_care_id", "Please select")
    CHOICES_FEELING = get_list("agree_level_id", "Please select")
    CHOICES_SAD = get_list("feeling_sad_id", "Please select")
    CHOICES_FINANCE = get_list("often_id", "Please select")

    type_of_assessment = forms.ChoiceField(
        choices=CHOICES_TYPE_ASSESSMENT,
        widget=forms.RadioSelect())

    date_of_assessment = forms.DateField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'date_of_assessment'
        }))

    # SECTION 1: BACKGROUND DETAILS
    SINO_CGQ03 = forms.ChoiceField(
        choices=CHOICES_READ,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control',
            'id': 'bd_read',
        }))

    SINO_CGQ04 = forms.ChoiceField(
        choices=CHOICES_EDUCATION,
        widget=forms.RadioSelect(
            # renderer=RadioCustomRenderer,
        ))

    SINO_CGQ05 = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control'}))

    SINO_CGQ06 = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control'}))

    SINO_CGQ07 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect(
            # renderer=RadioCustomRenderer,
        ))

    SINO_CGQ08 = forms.ChoiceField(
        choices=CHOICES_INCOME,
        widget=forms.Select(attrs={
                            'intial': 'Please select',
                            'class': 'form-control',
                            'id': 'bd_source_income',
                            }))

    SINO_CGQ09 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect(
            # renderer=RadioCustomRenderer,
        ))

    SINO_CGQ10 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect(
            # renderer=RadioCustomRenderer,
        ))

    SINO_CGQ11 = forms.ChoiceField(
        choices=yesno_list,
        widget=forms.Select(attrs={
                            'initial': 'Please select',
                            'id': 'bd_biologocal_mother',
                            'class': 'form-control',
                            }
                            ))

    SINO_CGQ12 = forms.ChoiceField(
        choices=CHOICES_BIOLOGICAL_MOTHER, required=False,
        widget=forms.Select(attrs={
                            'intial': 'Please select',
                            'class': 'form-control',
                            'id': 'bd_bm_live_hh',
                            }))

    SINO_CGQ13 = forms.ChoiceField(
        choices=yesno_list,
        widget=forms.Select(attrs={
                            'initial': 'Please select',
                            'id': 'bd_biologocal_father',
                            'class': 'form-control',

                            }
                            ))

    SINO_CGQ14 = forms.ChoiceField(
        choices=CHOICES_BIOLOGICAL_FATHER, required=False,
        widget=forms.Select(attrs={
                            'intial': 'Please select',
                            'class': 'form-control',
                            'id': 'bd_bf_live_hh',
                            }))

    SINO_CGQ15 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect(
            # renderer=RadioCustomRenderer,
        ))

    SINO_CGQ16 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect(

            # renderer=RadioCustomRenderer,
        ))

    SINO_CGQ17 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect(

            # renderer=RadioCustomRenderer,
        ))

    SINO_CGQ18 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect(
            # renderer=RadioCustomRenderer,
        ))

    SINO_CGQ19 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect(

            # renderer=RadioCustomRenderer,
        ))

    SINO_CGQ20 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect(

            # renderer=RadioCustomRenderer,
        ))

    SINO_CGQ21 = forms.ChoiceField(
        choices=CHOICES_HIV,
        widget=forms.Select(attrs={
                            'intial': 'Please select',
                            'class': 'form-control',
                            'id': 'bd_children_hiv_status',
                            }
                            ))

    SINO_CGQ22 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect(

            # renderer=RadioCustomRenderer,
        ))

    SINO_CGQ23 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect(

            # renderer=RadioCustomRenderer,
        ))

    SINO_CGQ24 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect(

            # renderer=RadioCustomRenderer,
        ))

    # SECTION 2: MY RELATIONSHIP WITH MY CHILD
    SINO_CGQ25 = forms.ChoiceField(
        choices=CHOICES_RELATIONSHIP,
        widget=forms.Select(attrs={
                            'intial': 'Please select',
                            'class': 'form-control',
                            'id': 'rc_discuss_child_needs',
                            }))

    SINO_CGQ26 = forms.ChoiceField(
        choices=CHOICES_RELATIONSHIP,
        widget=forms.Select(attrs={
                            'intial': 'Please select',
                            'class': 'form-control',
                            'id': 'rc_discipline',
                            }))

    SINO_CGQ27 = forms.ChoiceField(
        choices=CHOICES_RELATIONSHIP,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control',
            'id': 'rc_tells_bothering',
        }))

    SINO_CGQ28 = forms.ChoiceField(
        choices=CHOICES_RELATIONSHIP,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control',
            'id': 'rc_involve_decisions',
        }))

    # SECTION 3: MY CHILD’S BEHAVIOUR
    SINO_CGQ29 = forms.ChoiceField(
        choices=CHOICES_BEHAVIOR,
        widget=forms.Select(attrs={
                            'intial': 'Please select',
                            'class': 'form-control',
                            'id': 'cb_child_obedient',
                            }))

    SINO_CGQ30 = forms.ChoiceField(
        choices=CHOICES_BEHAVIOR,
        widget=forms.Select(attrs={
                            'intial': 'Please select',
                            'class': 'form-control',
                            'id': 'cb_figths_children',
                            }))

    # SECTION 4: DISCIPLINING MY CHILD
    SINO_CGQ31 = forms.ChoiceField(
        choices=CHOICES_DISCIPLINE,
        widget=forms.Select(attrs={
                            'intial': 'Please select',
                            'class': 'form-control',
                            'id': 'dc_often_discipline',
                            }))
    SINO_CGQ32 = forms.ChoiceField(
        choices=CHOICES_DISCIPLINE,
        widget=forms.Select(attrs={
                            'intial': 'Please select',
                            'class': 'form-control',
                            'id': 'dc_physical_discipline',
                            }))

    SINO_CGQ33 = forms.ChoiceField(
        choices=CHOICES_DISCIPLINE,
        widget=forms.Select(attrs={
                            'intial': 'Please select',
                            'class': 'form-control',
                            'id': 'dc_upset_child',
                            }))

    # SECTION 5: DEALING WITH STRESSFUL LIVES AS PARENTS
    SINO_CGQ34 = forms.ChoiceField(
        choices=CHOICES_FEELING,
        widget=forms.Select(attrs={
                            'intial': 'Please select',
                            'class': 'form-control',
                            'id': 'sp_caring_energy',
                            }))
    SINO_CGQ35 = forms.ChoiceField(
        choices=CHOICES_FEELING,
        widget=forms.Select(attrs={
                            'intial': 'Please select',
                            'class': 'form-control',
                            'id': 'sp_source_stress',
                            }))

    SINO_CGQ36 = forms.ChoiceField(
        choices=CHOICES_FEELING,
        widget=forms.Select(attrs={
                            'intial': 'Please select',
                            'class': 'form-control',
                            'id': 'sp_physical_punish',
                            }))

    # SECTION 6: FEELING SAD
    SINO_CGQ37 = forms.ChoiceField(
        choices=CHOICES_SAD,
        widget=forms.Select(attrs={
                            'intial': 'Please select',
                            'class': 'form-control',
                            'id': 'fs_depressed',
                            }))

    SINO_CGQ38 = forms.ChoiceField(
        choices=CHOICES_SAD,
        widget=forms.Select(attrs={
                            'intial': 'Please select',
                            'class': 'form-control',
                            'id': 'fs_depressed',
                            }))

    SINO_CGQ39 = forms.ChoiceField(
        choices=CHOICES_SAD,
        widget=forms.Select(attrs={
                            'intial': 'Please select',
                            'class': 'form-control',
                            'id': 'fs_depressed',
                            }))

    # SECTION 7: FINANCES
    SINO_CGQ40 = forms.ChoiceField(
        choices=CHOICES_FINANCE,
        widget=forms.Select(attrs={
                            'intial': 'Please select',
                            'class': 'form-control',
                            'id': 'fi_money_important_items',
                            }))

    SINO_CGQ41 = forms.ChoiceField(
        choices=CHOICES_FINANCE,
        widget=forms.Select(attrs={
                            'intial': 'Please select',
                            'class': 'form-control',
                            'id': 'fi_worried_money',
                            }))


class OVCSinovuyoTeenAssessmentForm(forms.Form):
    """
    Sinovuyo Care-giver Preventive Pre and Post Program Assessment Form
    """
    CHOICES_TYPE_ASSESSMENT = get_list("evaluation_type_id")
    CHOICES_READ = get_list('literacy_lvl_id', "Please select")
    CHOICES_EDUCATION = get_list("school_level_id")
    CHOICES_SCHOOL_TYPE = get_list("school_type_id", "Please Select")
    YES_NO_CHOICES = get_list('yesno_id')
    CHOICES_INCOME = get_list("employed_id", "Please select")
    CHOICES_RELATIONSHIP = get_list(
        'relationship_caregiver_id', "Please select")
    CHOICES_BEHAVIOR = get_list("my_behaviour_id", "Please select")
    CHOICES_DISCIPLINE = get_list("dsp_times_id", "Please select")
    CHOICES_BIOLOGICAL_FATHER = get_list(
        "father_mortality_id", "Please select")
    CHOICES_BIOLOGICAL_MOTHER = get_list(
        "mother_mortality_id", "Please select")
    CHOICES_HIV = get_list("under_care_id", "Please select")
    CHOICES_FEELING = get_list("agree_level_id", "Please select")
    CHOICES_SAD = get_list("feeling_sad_id", "Please select")
    CHOICES_FINANCE = get_list("often_id", "Please select")

    type_of_assessment = forms.ChoiceField(
        choices=CHOICES_TYPE_ASSESSMENT,
        widget=forms.RadioSelect())

    date_of_assessment = forms.DateField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'date_of_assessment'
        }))

    # SECTION 1: BACKGROUND DETAILS
    SINO_TNQ03 = forms.ChoiceField(
        choices=CHOICES_READ,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control',
            'id': 'bd_read',
        }))

    SINO_TNQ05 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect(
        ))

    SINO_TNQ04A = forms.ChoiceField(
        choices=CHOICES_EDUCATION,
        widget=forms.RadioSelect(
        ))

    SINO_TNQ04B = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        }))

    SINO_TNQ04C = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        }))

    SINO_TNQ04D = forms.ChoiceField(
        required=False,
        choices=CHOICES_SCHOOL_TYPE,
        widget=forms.Select(
            attrs={
                'intial': 'Please select',
                'class': 'form-control'
            }))

    SINO_TNQ06 = forms.ChoiceField(
        choices=CHOICES_BIOLOGICAL_MOTHER,
        widget=forms.Select(
            attrs={
                'intial': 'Please select',
                'class': 'form-control',
                'id': 'bd_bm_live_hh',
            }))

    SINO_TNQ07 = forms.ChoiceField(
        choices=CHOICES_BIOLOGICAL_FATHER,
        widget=forms.Select(
            attrs={
                'intial': 'Please select',
                'class': 'form-control',
                'id': 'bd_bf_live_hh',
            }))

    SINO_TNQ08 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect())

    SINO_TNQ09 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect())

    SINO_TNQ10 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect())

    SINO_TNQ11 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect())

    SINO_TNQ12 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect())

    SINO_TNQ13 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect())

    SINO_TNQ14 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect())

    SINO_TNQ15 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect())

    SINO_TNQ16 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect())

    SINO_TNQ17 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect())

    # SECTION 2: MY RELATIONSHIP WITH MY CHILD
    SINO_TNQ18 = forms.ChoiceField(
        choices=CHOICES_RELATIONSHIP,
        widget=forms.Select(
            attrs={
                'intial': 'Please select',
                'class': 'form-control'
            }))

    SINO_TNQ19 = forms.ChoiceField(
        choices=CHOICES_RELATIONSHIP,
        widget=forms.Select(
            attrs={
                'intial': 'Please select',
                'class': 'form-control'
            }))

    SINO_TNQ20 = forms.ChoiceField(
        choices=CHOICES_RELATIONSHIP,
        widget=forms.Select(
            attrs={
                'intial': 'Please select',
                'class': 'form-control'
            }))

    SINO_TNQ21 = forms.ChoiceField(
        choices=CHOICES_RELATIONSHIP,
        widget=forms.Select(
            attrs={
                'intial': 'Please select',
                'class': 'form-control'
            }))

    # SECTION 3: MY BEHAVIOUR
    SINO_TNQ22 = forms.ChoiceField(
        choices=CHOICES_BEHAVIOR,
        widget=forms.Select(
            attrs={
                'intial': 'Please select',
                'class': 'form-control'
            }))

    SINO_TNQ23 = forms.ChoiceField(
        choices=CHOICES_BEHAVIOR,
        widget=forms.Select(
            attrs={
                'intial': 'Please select',
                'class': 'form-control'
            }))

    # SECTION 4: DISCIPLINING MY CHILD
    SINO_TNQ24 = forms.ChoiceField(
        choices=CHOICES_DISCIPLINE,
        widget=forms.Select(
            attrs={
                'intial': 'Please select',
                'class': 'form-control'
            }))

    SINO_TNQ25 = forms.ChoiceField(
        choices=CHOICES_DISCIPLINE,
        widget=forms.Select(
            attrs={
                'intial': 'Please select',
                'class': 'form-control'
            }))

    SINO_TNQ26 = forms.ChoiceField(
        choices=CHOICES_DISCIPLINE,
        widget=forms.Select(
            attrs={
                'intial': 'Please select',
                'class': 'form-control'
            }))

    SINO_TNQ27 = forms.ChoiceField(
        choices=CHOICES_DISCIPLINE,
        widget=forms.Select(
            attrs={
                'intial': 'Please select',
                'class': 'form-control'
            }))

    # SECTION 5: FEELING SAD
    SINO_TNQ28 = forms.ChoiceField(
        choices=CHOICES_SAD,
        widget=forms.Select(attrs={
                            'intial': 'Please select',
                            'class': 'form-control'
                            }))

    SINO_TNQ29 = forms.ChoiceField(
        choices=CHOICES_SAD,
        widget=forms.Select(attrs={
                            'intial': 'Please select',
                            'class': 'form-control'
                            }))

    SINO_TNQ30 = forms.ChoiceField(
        choices=CHOICES_SAD,
        widget=forms.Select(attrs={
                            'intial': 'Please select',
                            'class': 'form-control'
                            }))


class OVCHCBFAssessmentForm(forms.Form):
    """
    HCBF Preventive Pre and Post Program Assessment Form
    """
    CHOICES_TYPE_ASSESSMENT = get_list("evaluation_type_id")
    YES_NO_CHOICES = get_list('yesno_id')
    RATE_CHOICES = get_list('rate_times_id', 'Please Select')
    COUNT_CHOICES = get_list('count_times_id', 'Please Select')

    type_of_assessment = forms.ChoiceField(
        choices=CHOICES_TYPE_ASSESSMENT,
        widget=forms.RadioSelect())

    date_of_assessment = forms.DateField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'date_of_assessment'
        }))

    # SECTION 1: BACKGROUND DETAILS
    HCBF_TNQ01 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect())

    HCBF_TNQ02 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect())

    HCBF_TNQ03 = forms.ChoiceField(
        choices=COUNT_CHOICES,
        widget=forms.Select(
            attrs={
                'intial': 'Please select',
                'class': 'form-control'
            }))

    HCBF_TNQ04 = forms.ChoiceField(
        choices=COUNT_CHOICES,
        widget=forms.Select(
            attrs={
                'intial': 'Please select',
                'class': 'form-control'
            }))

    HCBF_TNQ05 = forms.ChoiceField(
        choices=COUNT_CHOICES,
        widget=forms.Select(
            attrs={
                'intial': 'Please select',
                'class': 'form-control'
            }))

    HCBF_TNQ06 = forms.ChoiceField(
        choices=COUNT_CHOICES,
        widget=forms.Select(
            attrs={
                'intial': 'Please select',
                'class': 'form-control'
            }))

    HCBF_TNQ07 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect())

    HCBF_TNQ08 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect())

    HCBF_TNQ09 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect())

    HCBF_TNQ10 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect())

    HCBF_TNQ11 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect())

    HCBF_TNQ12 = forms.ChoiceField(
        choices=COUNT_CHOICES,
        widget=forms.Select(
            attrs={
                'intial': 'Please select',
                'class': 'form-control'
            }))

    HCBF_TNQ13 = forms.ChoiceField(
        choices=RATE_CHOICES,
        widget=forms.Select(
            attrs={
                'intial': 'Please select',
                'class': 'form-control'
            }))

    HCBF_TNQ14 = forms.ChoiceField(
        choices=RATE_CHOICES,
        widget=forms.Select(
            attrs={
                'intial': 'Please select',
                'class': 'form-control'
            }))


class OVCFMPAssessmentForm(forms.Form):
    """
    FMP Preventive Pre and Post Program Assessment Form
    """
    CHOICES_TYPE_ASSESSMENT = get_list("evaluation_type_id")
    YES_NO_CHOICES = get_list('yesno_id')
    YES_NO_UK_CHOICES = get_list('ctip_yesno_otdk')
    COUNT_CHOICES = get_list('count_times_id', 'Please Select')
    TRUTH_CHOICES = get_list('rate_truth_id', 'Please Select')

    type_of_assessment = forms.ChoiceField(
        choices=CHOICES_TYPE_ASSESSMENT,
        widget=forms.RadioSelect())

    date_of_assessment = forms.DateField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'date_of_assessment'
        }))

    # SECTION 1: BACKGROUND DETAILS
    FMP_CGQ01 = forms.ChoiceField(
        choices=COUNT_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    FMP_CGQ02 = forms.ChoiceField(
        choices=COUNT_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    FMP_CGQ03 = forms.ChoiceField(
        choices=COUNT_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    FMP_CGQ04 = forms.ChoiceField(
        choices=COUNT_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    FMP_CGQ05 = forms.ChoiceField(
        choices=COUNT_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    FMP_CGQ06 = forms.ChoiceField(
        choices=COUNT_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    FMP_CGQ07 = forms.ChoiceField(
        choices=COUNT_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    FMP_CGQ08 = forms.ChoiceField(
        choices=COUNT_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    FMP_CGQ09 = forms.ChoiceField(
        choices=COUNT_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    FMP_CGQ10 = forms.ChoiceField(
        choices=COUNT_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    FMP_CGQ11 = forms.ChoiceField(
        choices=COUNT_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    FMP_CGQ12 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect())

    FMP_CGQ13 = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Details"),
                   'class': 'form-control', 'rows': '3'}))

    FMP_CGQ14 = forms.ChoiceField(
        choices=YES_NO_UK_CHOICES,
        widget=forms.RadioSelect())

    FMP_CGQ15 = forms.ChoiceField(
        choices=TRUTH_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    FMP_CGQ16 = forms.ChoiceField(
        choices=TRUTH_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    FMP_CGQ17 = forms.ChoiceField(
        choices=TRUTH_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    FMP_CGQ18 = forms.ChoiceField(
        choices=TRUTH_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    FMP_CGQ19 = forms.ChoiceField(
        choices=TRUTH_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    FMP_CGQ20 = forms.ChoiceField(
        choices=TRUTH_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    FMP_CGQ21 = forms.ChoiceField(
        choices=TRUTH_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    FMP_CGQ22 = forms.ChoiceField(
        choices=TRUTH_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    FMP_CGQ23 = forms.ChoiceField(
        choices=TRUTH_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    FMP_CGQ24 = forms.ChoiceField(
        choices=TRUTH_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    FMP_CGQ25 = forms.ChoiceField(
        choices=TRUTH_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    FMP_CGQ26 = forms.ChoiceField(
        choices=TRUTH_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))


class OVCCBIMAssessmentForm(forms.Form):
    """
    CBIM Preventive Pre and Post Program Assessment Form
    """
    CHOICES_TYPE_ASSESSMENT = get_list("evaluation_type_id")
    YES_NO_CHOICES = get_list('yesno_id')
    AGREE_CHOICES = get_list("agree_level_id", "Please select")
    CBIM_CHOICES = get_list("cbim_coaching_id", "Please select")
    ABUSE_CHOICES = get_list("rate_abuse_id", "Please select")
    LIKELY_CHOICES = get_list("rate_likely_id", "Please select")
    AGE_CHOICES = get_list("age_rate_id", "Please select")
    RACE_CHOICES = get_list("race_id", "Please select")

    type_of_assessment = forms.ChoiceField(
        choices=CHOICES_TYPE_ASSESSMENT,
        widget=forms.RadioSelect())

    date_of_assessment = forms.DateField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'date_of_assessment'
        }))

    # SECTION 1: BACKGROUND DETAILS
    CBIM_TNQ11 = forms.ChoiceField(
        choices=CBIM_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ12 = forms.ChoiceField(
        choices=CBIM_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    # SECTION 2:
    CBIM_TNQ21 = forms.ChoiceField(
        choices=ABUSE_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ22 = forms.ChoiceField(
        choices=ABUSE_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ23 = forms.ChoiceField(
        choices=ABUSE_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ24 = forms.ChoiceField(
        choices=ABUSE_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ25 = forms.ChoiceField(
        choices=ABUSE_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ26 = forms.ChoiceField(
        choices=ABUSE_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ27 = forms.ChoiceField(
        choices=ABUSE_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ28 = forms.ChoiceField(
        choices=ABUSE_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ29 = forms.ChoiceField(
        choices=ABUSE_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ210 = forms.ChoiceField(
        choices=ABUSE_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ211 = forms.ChoiceField(
        choices=ABUSE_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ212 = forms.ChoiceField(
        choices=ABUSE_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ213 = forms.ChoiceField(
        choices=ABUSE_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ214 = forms.ChoiceField(
        choices=ABUSE_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ215 = forms.ChoiceField(
        choices=ABUSE_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ216 = forms.ChoiceField(
        choices=ABUSE_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ217 = forms.ChoiceField(
        choices=ABUSE_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ218 = forms.ChoiceField(
        choices=ABUSE_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    # SECTION 3:
    CBIM_TNQ31 = forms.ChoiceField(
        choices=LIKELY_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ32 = forms.ChoiceField(
        choices=LIKELY_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ33 = forms.ChoiceField(
        choices=LIKELY_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ34 = forms.ChoiceField(
        choices=LIKELY_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ35 = forms.ChoiceField(
        choices=LIKELY_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ36 = forms.ChoiceField(
        choices=LIKELY_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ37 = forms.ChoiceField(
        choices=LIKELY_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ38 = forms.ChoiceField(
        choices=LIKELY_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ39 = forms.ChoiceField(
        choices=LIKELY_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    # SECTION 4: BACKGROUND DETAILS
    CBIM_TNQ41 = forms.ChoiceField(
        choices=AGREE_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ42 = forms.ChoiceField(
        choices=AGREE_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ43 = forms.ChoiceField(
        choices=AGREE_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ44 = forms.ChoiceField(
        choices=AGREE_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ45 = forms.ChoiceField(
        choices=AGREE_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ46 = forms.ChoiceField(
        choices=AGREE_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ47 = forms.ChoiceField(
        choices=AGREE_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ48 = forms.ChoiceField(
        choices=AGREE_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ49 = forms.ChoiceField(
        choices=AGREE_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ410 = forms.ChoiceField(
        choices=AGREE_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    # SECTION 5: BACKGROUND DETAILS
    CBIM_TNQ51 = forms.ChoiceField(
        choices=AGE_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

    CBIM_TNQ52 = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Details"),
                   'class': 'form-control', 'rows': '2'}))

    CBIM_TNQ53 = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect())

    CBIM_TNQ54 = forms.ChoiceField(
        choices=RACE_CHOICES,
        widget=forms.Select(attrs={
            'intial': 'Please select',
            'class': 'form-control'
        }))

