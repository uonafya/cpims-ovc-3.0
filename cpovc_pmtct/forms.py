from django import forms
from django.utils.translation import gettext_lazy as _

from cpovc_main.functions import get_list
from cpovc_forms.functions import get_facility_list

person_type_list = get_list('person_type_id', 'Please Select Type')
school_level_list = get_list('school_level_id', 'Please Select Level')
eligibility_list = get_list('eligibility_criteria_id', '')
exit_list = get_list('exit_reason_id', 'Please Select one')
admission_list = get_list('school_type_id', 'Please Select one')
art_status_list = get_list('art_status_id', 'Please Select Status')
hiv_status_list = get_list('hiv_status_id', 'Please Select HIV Status')

# hei_tracker
yes_no = get_list('yesno_id', 'Please Select')


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


# Pregnant Women_Adolescent
class PREGNANT_WOMEN_ADOLESCENT(forms.Form):
    org_units_list = get_facility_list()
    # HIV_STATUS_CHOICES=(('1', 'Skilled'), ('0', 'Unskilled'))
    trimester_list = (
        ('contact', '1st Contact'), ('tri', '1st Trimester'),
        ('3rd', '3rd Trimester'), ('4th', 'Labour/Delivery'),)
    PWA_WA1_01 = forms.ChoiceField(
        choices=trimester_list,
        widget=forms.RadioSelect(
            # renderer=RadioCustomRenderer,
            attrs={
                # 'data-parsley-errors-container': "#errorfield"
            }))

    PMTCT_PWA6q = forms.DateField(
        required=False,
        widget=forms.widgets.DateInput(
            # format="%m/%d/%Y",
            attrs={'placeholder': _('Date'),
                   'class': 'form-control',
                   'name': 'PMTCT_PWA6q',
                   'id': 'PMTCT_PWA6q',
                   'autocomplete': "off",
                   #    'data-parsley-required': "true",
                   #    'data-parsley-group': 'group0'
                   }))

    PMTCT_PWA7q = forms.ChoiceField(
        required=False,
        choices=(('1', 'HIV_Positive'), ('0', 'HIV_Negative'),),
        widget=forms.RadioSelect(
            # renderer=RadioCustomRenderer,
            attrs={
                # 'data-parsley-required': 'true',
                # 'data-parsley-errors-container': "#errorfield"
            }))

    PMTCT_PWA8q = forms.DateField(
        required=False,
        widget=forms.widgets.DateInput(
            # format="%Y/%m/%d",
            attrs={'placeholder': _('Date'),
                   'class': 'form-control',
                   'name': 'PMTCT_PWA8q',
                   'id': 'PMTCT_PWA8q',
                   'autocomplete': "off",
                   #    'data-parsley-required': "true",
                   #    'data-parsley-group': 'group0'
                   }))

    PMTCT_PWA9q = forms.ChoiceField(
        required=False,
        choices=(('1', 'HIV_Positive'), ('0', 'HIV_Negative'),),
        widget=forms.RadioSelect(
            # renderer=RadioCustomRenderer,
            attrs={
                # 'data-parsley-required': 'true',
                # 'data-parsley-errors-container': "#errorfield"
            }))

    PMTCT_PWA10q = forms.DateField(
        required=False,
        widget=forms.widgets.DateInput(
            # format="%Y/%m/%d",
            attrs={'placeholder': _('Date'),
                   'class': 'form-control',
                   'name': 'PMTCT_PWA10q',
                   'id': 'PMTCT_PWA10q',
                   'autocomplete': "off",
                   #    'data-parsley-required': "true",
                   #    'data-parsley-group': 'group0'
                   }))

    PMTCT_PWA11q = forms.ChoiceField(
        required=False,
        choices=(('1', 'HIV_Positive'), ('0', 'HIV_Negative'),),
        widget=forms.RadioSelect(
            # renderer=RadioCustomRenderer,
            attrs={
                # 'data-parsley-required': 'true',
                # 'data-parsley-errors-container': "#errorfield"
            }))

    PMTCT_PWA12q = forms.DateField(
        required=False,
        widget=forms.widgets.DateInput(
            # format="%Y/%m/%d",
            attrs={'placeholder': _('Date'),
                   'class': 'form-control',
                   'name': 'PMTCT_PWA12q',
                   'id': 'PMTCT_PWA12q',
                   'autocomplete': "off",
                   #    'data-parsley-required': "true",
                   #    'data-parsley-group': 'group0'
                   }))

    PMTCT_PWA13q = forms.ChoiceField(
        required=False,
        choices=(('1', 'HIV_Positive'), ('0', 'HIV_Negative'),),
        widget=forms.RadioSelect(
            # renderer=RadioCustomRenderer,
            attrs={
                # 'data-parsley-required': 'true',
                # 'data-parsley-errors-container': "#errorfield"
            }))

    PMTCT_PWA1q = forms.DateField(
        widget=forms.widgets.DateInput(
            # format="%Y/%m/%d",
            attrs={'placeholder': _('Date'),
                   'class': 'form-control',
                   'name': 'PMTCT_PWA1q',
                   'id': 'PMTCT_PWA1q',
                   'autocomplete': "off",
                   #    'data-parsley-required': "true",
                   #    'data-parsley-group': 'group0'
                   }))

    PMTCT_PWA2q = forms.DateField(
        widget=forms.widgets.DateInput(
            # format="%Y/%m/%d",
            attrs={'placeholder': _('Date'),
                   'class': 'form-control',
                   'name': 'PMTCT_PWA2q',
                   'id': 'PMTCT_PWA2q',
                   'autocomplete': "off",
                   #    'data-parsley-required': "true",
                   #    'data-parsley-group': 'group0'
                   }))

    PMTCT_PWA3q = forms.DateField(
        widget=forms.widgets.DateInput(
            # format="%Y/%m/%d",
            attrs={'placeholder': _('Date'),
                   'class': 'form-control',
                   'name': 'PMTCT_PWA3q',
                   'id': 'PMTCT_PWA3q',
                   'autocomplete': "off",
                   #    'data-parsley-required': "true",
                   #    'data-parsley-group': 'group0'
                   }))

    PMTCT_PWA4q = forms.DateField(
        widget=forms.widgets.DateInput(
            # format="%Y/%m/%d",
            attrs={'placeholder': _('Date'),
                   'class': 'form-control',
                   'name': 'PMTCT_PWA4q',
                   'id': 'PMTCT_PWA4q',
                   'autocomplete': "off",
                   #    'data-parsley-required': "true",
                   #    'data-parsley-group': 'group0'
                   }))

    PMTCT_PWA5q = forms.ChoiceField(
        choices=(('1', 'Skilled'), ('0', 'Unskilled'),),
        widget=forms.RadioSelect(
            # renderer=RadioCustomRenderer,
            attrs={
                # 'data-parsley-errors-container': "#errorfield"
            }))

    PMTCT_PWA14q = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _('Facility Name'),
               'class': 'form-control',
               'id': 'PMTCT_PWA14q',
               'readonly': 'True',
               #    'data-parsley-group': 'group0'
               }))

    PMTCT_PWA15q = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _('CCC NO'),
               'class': 'form-control',
               #    'data-parsley-required': "False",
               'data-parsley-type': "number",
               #    'data-parsley-required': "False"
               }))

    PMTCT_PWA16q = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _('VL result'),
               'class': 'form-control',
               #    'data-parsley-required': "False",
               'data-parsley-type': "number",
               #    'data-parsley-required': "False"
               }))

    PMTCT_PWA17q = forms.DateField(
        widget=forms.widgets.DateInput(
            # format="%Y/%m/%d",
            attrs={'placeholder': _('Date'),
                   'class': 'form-control',
                   'name': 'PMTCT_PWA17q',
                   'id': 'PMTCT_PWA17q',
                   'autocomplete': "off",
                   #    'data-parsley-required': "true",
                   #    'data-parsley-group': 'group0'
                   }))

    # PWA_WA1_15 = forms.ChoiceField(
    #     choices=YESNO_CHOICES,
    #     widget=forms.RadioSelect(
    #         # renderer=RadioCustomRenderer,
    #         attrs={
    #             # 'data-parsley-errors-container': "#errorfield"
    #         }))
    PMTCT_PWA18q = forms.ChoiceField(
        choices=(('1', 'YES'), ('0', 'NO')),
        widget=forms.RadioSelect(
            # renderer=RadioCustomRenderer,
            attrs={
                # 'data-parsley-required': 'true',
                # 'data-parsley-errors-container': "#errorfield"
            }))

    PMTCT_PWA19q = forms.DateField(
        widget=forms.widgets.DateInput(
            attrs={'placeholder': _('Date'),
                   'class': 'form-control',
                   'name': 'PMTCT_PWA19q',
                   'id': 'PMTCT_PWA19q',
                   'autocomplete': "off",
                   # 'data-parsley-required': "true",
                   #    'data-parsley-group': 'group0'
                   }))


class OVCHEITrackerForm(forms.Form):

    HIV_STATUS = (('', 'Select Status'), ('Positive', 'Positive'),
                  ('Negative', 'Negative'), ('Unknown', 'Unknown'))
    Test_Results = (('', 'Select Status'),
                    ('Positive', 'Positive'), ('Negative', 'Negative'),)
    Feeding_Mode = (('', 'Select Feeding mode'), ('Exclusive', 'Exclusive'),
                    ('BreastFeeding', 'BreastFeeding'),
                    ('Replacementfeeding', 'Replacement feeding'),
                    ('Mixedfeeding', 'Mixed feeding'),)
    ON_Track = (('', 'Select'), ('OnTrack', 'On Track'),
                ('NotOnTrack', 'Not On Track'),)
    # yes_no = (('', 'Select'), ('Yes', 'Yes'), ('No', 'No'),)
    Follow_Up = forms.ChoiceField(
        choices=(
            ('AtFirstContact', 'At first contact'),
            ('At6wks', 'At 6 weeks'),
            ('At6mths', 'At 6 months'),
            ('At12mths', 'At 12 months'),
            ('At18mths', 'At 18 months')
        ),
        widget=forms.RadioSelect(
            # renderer=RadioCustomRenderer,
            attrs={
                #  'data-parsley-required': 'true',
                # 'data-parsley-errors-container': "#errorfield"
            }))
    Attrition_reasons = (('', 'Select Attrition reason'), ('Died', 'Died'),
                         ('Relocation', 'Relocation'),
                         ('leftAtWill', 'Left at will'))

    # care giver biodata
    PMTCT_HEI5q = forms.ChoiceField(
        choices=HIV_STATUS,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'PMTCT_HEI5q',
                # 'data-parsley-type': "digits",
                # 'data-parsley-required': "true",
                # 'data-parsley-group': 'group0'
            })
    )
    PMTCT_HEI6q = forms.ChoiceField(
        required=False,
        choices=yes_no,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'PMTCT_HEI6q',
                # 'data-parsley-type': "digits",
                # 'data-parsley-required': "true",
                # 'data-parsley-group': 'group0'
            })
    )
    PMTCT_HEI7q = forms.CharField(

        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Enter facility'),
                'class': 'form-control',
                'id': 'PMTCT_HEI7q',
                'readonly': 'true',
                # 'data-parsley-type': "digits",
                # 'data-parsley-required': "true",
                # 'data-parsley-group': 'group0'
            })
    )
    PMTCT_HEI8q = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Enter CCC number'),
                'class': 'form-control',
                'id': 'PMTCT_HEI8q',
                # 'data-parsley-type': "digits",
                # 'data-parsley-required': "true",
                # 'data-parsley-group': 'group0'
            })
    )
    PMTCT_HEI9q = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Enter latest Vl results'),
                'class': 'form-control',
                'id': 'PMTCT_HEI9q',
                # 'data-parsley-type': "digits",
                # 'data-parsley-required': "true",
                # 'data-parsley-group': 'group0'
            })
    )
    PMTCT_HEI10q = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Date of VL test'),
                'class': 'form-control',
                'id': 'PMTCT_HEI10q',
                # 'data-parsley-type': "digits",
                # 'data-parsley-required': "true",
                # 'data-parsley-group': 'group0'
            })
    )
    PMTCT_HEI42q = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Date of follow up'),
                'class': 'form-control',
                'id': 'PMTCT_HEI42q',
                # 'data-parsley-type': "digits",
                # 'data-parsley-required': "true",
                # 'data-parsley-group': 'group0'
            })
    )
    PMTCT_HEI42q = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Date of follow up'),
                'class': 'form-control',
                'id': 'PMTCT_HEI42q',
                # 'data-parsley-type': "date",
                # 'data-parsley-required': "true",
                # 'data-parsley-group': 'group0'
            })
    )
    PMTCT_HEI43q = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Date of follow up'),
                'class': 'form-control',
                'id': 'PMTCT_HEI43q',
                # 'data-parsley-type': "digits",
                # 'data-parsley-required': "true",
                # 'data-parsley-group': 'group0'
            })
    )
    PMTCT_HEI44q = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Date of follow up'),
                'class': 'form-control',
                'id': 'PMTCT_HEI44q',
                # 'data-parsley-type': "digits",
                # 'data-parsley-required': "true",
                # 'data-parsley-group': 'group0'
            })
    )
    PMTCT_HEI45q = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Date of follow up'),
                'class': 'form-control',
                'id': 'PMTCT_HEI45q',
                # 'data-parsley-type': "digits",
                # 'data-parsley-required': "true",
                # 'data-parsley-group': 'group0'
            })
    )
    PMTCT_HEI46q = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Date of follow up'),
                'class': 'form-control',
                'id': 'PMTCT_HEI46q',
                # 'data-parsley-type': "digits",
                # 'data-parsley-required': "true",
                # 'data-parsley-group': 'group0'
            })
    )
    PMTCT_HEI10q = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': _('Date of HEI tracking'),
            'class': 'form-control',
            'id': 'PMTCT_HEI10q',
            # 'data-parsley-type': "digits",
            # 'data-parsley-required': "true",
            # 'data-parsley-group': 'group0'
        })
    )

    # HEI Follow up first contact
    PMTCT_HEI13q = forms.ChoiceField(
        required=False,
        choices=yes_no,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'PMTCT_HEI13q',
                'data-parsley-required': "false",
            })
    )

    PMTCT_HEI14q = forms.ChoiceField(
        required=False,
        choices=Test_Results,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'PMTCT_HEI14q',
                'data-parsley-required': "false",
            })
    )
    PMTCT_HEI15q = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Enter vl results'),
                'class': 'form-control',
                'id': 'PMTCT_HEI15q',
                # 'data-parsley-type': "digits",
                'data-parsley-required': "false",
                # 'data-parsley-group': 'group0'
            })
    )
    PMTCT_HEI16q = forms.ChoiceField(
        required=False,
        choices=yes_no,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'PMTCT_HEI16q',
                'data-parsley-required': "false",
            })
    )
    PMTCT_HEI17q = forms.ChoiceField(
        required=False,
        choices=Feeding_Mode,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'PMTCT_HEI17q',
                'data-parsley-required': "false",
            })
    )

    # HEI Follow up at 6mnths
    PMTCT_HEI24q = forms.ChoiceField(
        required=False,
        choices=yes_no,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'PMTCT_HEI24q',
                'data-parsley-required': "false",
            })
    )

    PMTCT_HEI25q = forms.ChoiceField(
        required=False,
        choices=Test_Results,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'PMTCT_HEI25q',
                'data-parsley-required': "false",
            })
    )
    PMTCT_HEI26q = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Enter vl results'),
                'class': 'form-control',
                'id': 'PMTCT_HEI26q',
                # 'data-parsley-type': "digits",
                'data-parsley-required': "false",
                # 'data-parsley-group': 'group0'
            })
    )
    PMTCT_HEI27q = forms.ChoiceField(
        required=False,
        choices=yes_no,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'PMTCT_HEI27q',
                'data-parsley-required': "false",
            })
    )
    PMTCT_HEI28q = forms.ChoiceField(
        required=False,
        choices=ON_Track,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'PMTCT_HEI28q',
                'data-parsley-required': "false",
            })
    )
    PMTCT_HEI29q = forms.ChoiceField(
        required=False,
        choices=Feeding_Mode,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'PMTCT_HEI29q',
                'data-parsley-required': "false",
            })
    )

    # HEI Follow up at 6wks
    PMTCT_HEI18q = forms.ChoiceField(
        required=False,
        choices=yes_no,
        widget=forms.Select(
            attrs={
                'placeholder': _('Female'),
                'class': 'form-control',
                'id': 'PMTCT_HEI8q',
                'data-parsley-required': "false",
            })
    )

    PMTCT_HEI19q = forms.ChoiceField(
        required=False,
        choices=Test_Results,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'PMTCT_HEI19q',
                'data-parsley-required': "false",
            })
    )
    PMTCT_HEI20q = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Enter vl results'),
                'class': 'form-control',
                'id': 'PMTCT_HEI20q',
                # 'data-parsley-type': "digits",
                'data-parsley-required': "false",
                # 'data-parsley-group': 'group0'
            })
    )
    PMTCT_HEI21q = forms.ChoiceField(
        required=False,
        choices=yes_no,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'PMTCT_HEI21q',
                'data-parsley-required': "false",
            })
    )
    PMTCT_HEI22q = forms.ChoiceField(
        required=False,
        choices=ON_Track,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'PMTCT_HEI22q',
                'data-parsley-required': "false",
            })
    )
    PMTCT_HEI23q = forms.ChoiceField(
        required=False,
        choices=Feeding_Mode,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'PMTCT_HEI23q',
                'data-parsley-required': "false",
            })
    )

    # HEI Follow up at 12mnths
    PMTCT_HEI30q = forms.ChoiceField(
        required=False,
        choices=yes_no,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'PMTCT_HEI30q',
                'data-parsley-required': "false",
            })
    )

    PMTCT_HEI31q = forms.ChoiceField(
        required=False,
        choices=Test_Results,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'PMTCT_HEI31q',
                'data-parsley-required': "false",
            })
    )
    PMTCT_HEI32q = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Enter vl results'),
                'class': 'form-control',
                'id': 'PMTCT_HEI32q',
                # 'data-parsley-type': "digits",
                'data-parsley-required': "false",
                # 'data-parsley-group': 'group0'
            })
    )
    PMTCT_HEI33q = forms.ChoiceField(
        required=False,
        choices=yes_no,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'PMTCT_HEI33q',
                'data-parsley-required': "false",
            })
    )
    PMTCT_HEI34q = forms.ChoiceField(
        required=False,
        choices=ON_Track,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'PMTCT_HEI34q',
                'data-parsley-required': "false",
            })
    )
    PMTCT_HEI35q = forms.ChoiceField(
        required=False,
        choices=Feeding_Mode,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'PMTCT_HEI35q',
                'data-parsley-required': "false",
            })
    )

    # HEI Follow up at 18mnths
    PMTCT_HEI36q = forms.ChoiceField(
        required=False,
        choices=yes_no,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'PMTCT_HEI36q',
                'data-parsley-required': "false",
            })
    )
    PMTCT_HEI37q = forms.ChoiceField(
        required=False,
        choices=Test_Results,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'PMTCT_HEI37q',
                'data-parsley-required': "false",
            })
    )
    PMTCT_HEI38q = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Enter vl results'),
                'class': 'form-control',
                'id': 'PMTCT_HEI38q',
                # 'data-parsley-type': "digits",
                'data-parsley-required': "false",
                # 'data-parsley-group': 'group0'
            })
    )
    PMTCT_HEI39q = forms.ChoiceField(
        required=False,
        choices=yes_no,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'PMTCT_HEI39q',
                'data-parsley-required': "false",
            })
    )
    PMTCT_HEI40q = forms.ChoiceField(
        required=False,
        choices=ON_Track,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'PMTCT_HEI40q',
                'data-parsley-required': "false",
            })
    )
    PMTCT_HEI41q = forms.ChoiceField(
        required=False,
        choices=Feeding_Mode,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'PMTCT_HEI41q',
                'data-parsley-required': "false",
            })
    )

    # Others
    PMTCT_HEI47q = forms.ChoiceField(
        required=False,
        choices=Attrition_reasons,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'PMTCT_HEI47q',
                'data-parsley-required': "false",
            })
    )
    PMTCT_HEI48q = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _('Comments'),
                   'class': 'form-control',
                   'id': 'PMTCT_HEI48q',
                   'data-parsley-required': "false",
                   'rows': '2'}))
