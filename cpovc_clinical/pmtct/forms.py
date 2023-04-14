from django import forms
from cpovc_main.functions import get_list

person_type_list = get_list('person_type_id', 'Please Select Type')
school_level_list = get_list('school_level_id', 'Please Select Level')
eligibility_list = get_list('eligibility_criteria_id', '')
exit_list = get_list('exit_reason_id', 'Please Select one')
admission_list = get_list('school_type_id', 'Please Select one')
art_status_list = get_list('art_status_id', 'Please Select Status')
hiv_status_list = get_list('hiv_status_id', 'Please Select HIV Status')


class OVCPMTCTRegistrationForm(forms.Form):
    """OVC registration form."""

    def __init__(self, guids, *args, **kwargs):
        """Override methods."""
        super(OVCPMTCTRegistrationForm, self).__init__(*args, **kwargs)

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

    exit_reason = forms.ChoiceField(
        choices=exit_list,
        required=False,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'exit_reason'}))

    school_level = forms.ChoiceField(
        choices=school_level_list,
        initial='0',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'data-parsley-required': "true",
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

    facility = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'data-parsley-required': "true",
                   'placeholder': 'Start typing then select',
                   'id': 'facility'}))

    art_status = forms.ChoiceField(
        choices=art_status_list,
        required=False,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'data-parsley-required': "true",
                   'id': 'art_status'}))

    link_date = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'id': 'link_date'}))

    ccc_number = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': '99999-99999',
                   'id': 'ccc_number'}))

    facility_id = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'readonly': 'readonly',
                   'id': 'facility_id'}))

    hiv_status = forms.ChoiceField(
        choices=hiv_status_list,
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'data-parsley-required': "true",
                   'id': 'hiv_status'}))

    caregiver_contact = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': '07XXXXXXXX',
                   'id': 'caregiver_contact'}))
