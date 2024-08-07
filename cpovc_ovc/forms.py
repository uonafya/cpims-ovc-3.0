"""OVC Registration forms."""
from django import forms
from django.utils.translation import gettext_lazy as _
from cpovc_main.functions import get_list, get_org_units_list

search_criteria_list = (('', 'Select Criteria'), ('1', 'Names'),
                        ('2', 'HouseHold'), ('3', 'CHV'), ('4', 'CBO'),
                        ('5', 'Caregiver'), ('6', 'CPIMS ID'))

immunization_list = get_list('immunization_status_id', 'Please Select')

person_type_list = get_list('person_type_id', 'Please Select Type')
school_level_list = get_list('school_level_id', 'Please Select Level')
hiv_status_list = get_list('hiv_status_id', 'Please Select HIV Status')
alive_status_list = get_list('yesno_id', '')
art_status_list = get_list('art_status_id', 'Please Select Status')
ovc_form_type_list = get_list('ovc_form_type_id', 'Please Select')
ovc_form_type_list += [('CPR', 'Case Plan'), ('CPT', 'Case Plan Template'),
                       ('WB', 'Well Being'),
                       ('WBA', 'Well Being Adolescent'),
                       ('HVSRN', 'HIV Risk Assessment'),
                       ('HVMGT', 'HIV Management Form'),
                       ('DREAMS', 'DREAMS Service Uptake Form')]
eligibility_list = get_list('eligibility_criteria_id', '')
death_cause_list = get_list('death_cause_id', 'Please Select Cause of Death')
exit_list = get_list('exit_reason_id', 'Please Select one')
admission_list = get_list('school_type_id', 'Please Select one')
health_unit_list = get_org_units_list(
    default_txt='Select Unit', org_types=['HFGU'])

# -------------additions

point_of_entry_choices = (('', 'Select Criteria'),
                          ('1', 'Health facility'), ('2', 'Community'))
initial_enrolment_choices = (
    ('', 'Select Criteria'), ('1', 'Yes'), ('2', 'No'))

# -------------additions
education_level_list = get_list('education_level_id', 'Please Select')


class OVCSearchForm(forms.Form):
    """Search registry form."""

    search_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _('Search . . .'),
               'class': 'form-control',
               'id': 'search_name',
               'data-parsley-minlength': '3',
               'data-parsley-required': 'true'}))

    search_criteria = forms.ChoiceField(
        choices=search_criteria_list,
        initial='0',
        required=False,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'data-parsley-required': "true",
                   'id': 'search_criteria'}))

    person_exited = forms.CharField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={'id': 'person_exited'}))

    form_type = forms.ChoiceField(
        choices=ovc_form_type_list,
        initial='0',
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'form_type'}))


class OVCRegistrationForm(forms.Form):
    """OVC registration form."""

    def __init__(self, guids, *args, **kwargs):
        """Override methods."""
        super(OVCRegistrationForm, self).__init__(*args, **kwargs)
        pids = guids['guids']
        kids = guids['chids']
        # Guardians
        for i in pids:
            gid = 'gstatus_%s' % str(i)
            aid = 'astatus_%s' % str(i)
            cid = 'cstatus_%s' % str(i)
            gstatus = forms.ChoiceField(
                choices=hiv_status_list,
                required=False,
                widget=forms.Select(
                    attrs={'class': 'form-control', 'id': gid,
                           'data-parsley-required': "true"}))
            astatus = forms.ChoiceField(
                choices=alive_status_list,
                initial='AYES',
                required=False,
                widget=forms.Select(
                    attrs={'class': 'form-control alive', 'id': aid,
                           'data-parsley-required': "true"}))
            cstatus = forms.ChoiceField(
                required=False,
                choices=death_cause_list,
                initial='AYES',
                widget=forms.Select(
                    attrs={'class': 'form-control alive', 'id': cid}))
            self.fields[gid] = gstatus
            self.fields[aid] = astatus
            self.fields[cid] = cstatus
        # Siblings
        for i in kids:
            gid = 'sgstatus_%s' % str(i)
            aid = 'sastatus_%s' % str(i)
            sgstatus = forms.ChoiceField(
                choices=hiv_status_list,
                initial='0',
                widget=forms.Select(
                    attrs={'class': 'form-control', 'id': gid,
                           'data-parsley-required': "true"}))
            sastatus = forms.ChoiceField(
                choices=alive_status_list,
                initial='AYES',
                widget=forms.Select(
                    attrs={'class': 'form-control', 'id': aid,
                           'data-parsley-required': "true"}))
            self.fields[gid] = sgstatus
            self.fields[aid] = sastatus

    reg_date = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'id': 'reg_date',
                   'data-parsley-required': "true"}))

    init_enrol = forms.ChoiceField(
        choices=initial_enrolment_choices,
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control', 'id': 'init_enrol',
                   'data-parsley-required': "true"}))

    po_entry = forms.ChoiceField(
        choices=point_of_entry_choices,
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control', 'id': 'po_entry',
                   'data-parsley-required': "true"}))

    exit_date = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'id': 'exit_date'}))

    has_bcert = forms.CharField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={'class': 'form-control',
                   'id': 'has_bcert'}))

    is_exited = forms.CharField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={'class': 'form-control',
                   'id': 'is_exited'}))

    bcert_no = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'id': 'bcert_no'}))

    ncpwd_no = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'id': 'ncpwd_no'}))

    disb = forms.CharField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={'class': 'form-control',
                   'id': 'disb'}))

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

    immunization = forms.ChoiceField(
        choices=immunization_list,
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'data-parsley-required': "true",
                   'id': 'immunization'}))

    eligibility = forms.MultipleChoiceField(
        choices=eligibility_list,
        required=True,
        widget=forms.SelectMultiple(
            attrs={'class': 'form-control',
                   'data-parsley-required': "true",
                   'id': 'eligibility'}))

    exit_reason = forms.ChoiceField(
        choices=exit_list,
        required=False,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'exit_reason'}))

    ovc_exit_reason = forms.ChoiceField(
        choices=exit_list,
        required=False,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'ovc_exit_reason'}))

    hiv_status = forms.ChoiceField(
        choices=hiv_status_list,
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'data-parsley-required': "true",
                   'id': 'hiv_status'}))

    school_level = forms.ChoiceField(
        choices=school_level_list,
        initial='0',
        required=False,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'data-parsley-required': "true",
                   'id': 'school_level'}))

    facility = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'data-parsley-required': "true",
                   'placeholder': 'Start typing then select',
                   'id': 'facility'}))

    school_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Start typing then select',
                   'id': 'school_name'}))

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
                   'id': 'ccc_number'}))

    facility_id = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'readonly': 'readonly',
                   'id': 'facility_id'}))

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

    exit_org_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Organization name exiting to',
                   'id': 'exit_org_name'}))

    date_of_testing = forms.DateField(
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'date of Testing',
                   'class': 'form-control',
                   'autocomplete': 'off',
                   'id': 'date_of_event'}

        )
    )

    hiv_statuss = forms.ChoiceField(
        choices=hiv_status_list,
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'data-parsley-required': "true",
                   'id': 'hiv_statuss'}))

    # July 2023
    birth_not_id = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': _('Birth Notification Number'),
                   'class': 'form-control',
                   'id': 'birth_not_id'}))

    nemis_id = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': _('NEMIS Number'),
                   'class': 'form-control',
                   'id': 'nemis_id'}))

    is_dreams_enrolled = forms.CharField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={'class': 'form-control',
                   'id': 'is_dreams_enrolled'}))

    dreams_id = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': _('DREAMS ID'),
                   'class': 'form-control',
                   'id': 'dreams_id'}))

    nupi_id = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': _('NUPI Number'),
                   'class': 'form-control',
                   'id': 'nupi_id'}))

    exit_org_id = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'readonly': 'readonly',
                   'id': 'exit_org_id'}))


class OVCExtraInfoForm(forms.Form):
    """OVC Extra Information form."""

    date_of_birth = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'id': 'date_of_birth',
                   'data-parsley-required': 'true'}
        )
    )

    id_number = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'ID Number',
                   'class': 'form-control',
                   'id': 'id_number',
                   'data-parsley-required': 'true'}
        )
    )

    mobile_number = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': '07x or 01x',
                   'class': 'form-control',
                   'id': 'mobile_number',
                   'data-parsley-required': 'true'}
        )
    )

    education_level = forms.ChoiceField(
        choices=education_level_list,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'form_type'}
        )
    )

    member_type = forms.CharField(
        required=False,
        widget=forms.HiddenInput(
            attrs={'class': 'form-control',
                   'id': 'member_type'}
        )
    )
