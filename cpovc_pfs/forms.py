from django import forms
from django.utils.translation import gettext_lazy as _

from cpovc_main.functions import get_list

person_type_list = get_list('person_type_id', 'Please Select Type')
school_level_list = get_list('school_level_id', 'Please Select Level')
eligibility_list = get_list('eligibility_criteria_id', '')
exit_list = get_list('exit_reason_id', 'Please Select one')
admission_list = get_list('school_type_id', 'Please Select one')
intervention_list = get_list('pfs_intervention_id', 'Please Select one')

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
