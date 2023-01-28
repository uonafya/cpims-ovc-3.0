class CaseTransferForm(forms.Form):
    CHOICES = (('', 'Please select'),
        ('Child ages out of the program prior to achieving their case plan',
            'Child ages out of the program prior to achieving their case plan'),
        ('Child and or family plans to relocate prior to achieving their case plan',
            'Child and or family plans to relocate prior to achieving their case plan'),
        ('Program relocates or closes before recommended interventions have been completed',
            'Program relocates or closes before recommended interventions have been completed'),
        ('Interventions outlining case plan have been achieved',
            'Interventions outlining case plan have been achieved'),
        ('Service required not available', 'Service required not available')
    )

    TRANSFER_DATE = forms.DateField(
        widget=forms.widgets.DateInput(
            format='%m/%d/%Y',
            attrs={'class': 'datepicker',
                   'placeholder': 'Date of follow up',
                   'class': 'form-control',
                   'autocomplete': "off",
                   'data-parsley-required': "True",
                   'type': 'date'
                   }
        ),
        input_formats=('%m/%d/%Y', ),
        # required=True
    )

    REASON = forms.ChoiceField(
        choices=CHOICES, widget=forms.Select(
            attrs={
                'id': 'transfer_reason',
                'class': 'form-control',
                'data-parsley-required': "false",
                'data-parsley-group': 'group0'
            }),
    )

    FOLLOW_UP_DATE =forms.DateField(
        widget=forms.TextInput(
        attrs={'placeholder': _('Follow up Date'),
               'class': 'form-control',
               'id': 'follow_up_date',
               'data-parsley-required': "false",
               'data-parsley-group': 'group0',
               'type': 'date'
            },
        ),
        
    )
    COMMENT = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Comment'),
               'class': 'form-control',
               'id': 'comment',
               'data-parsley-required': "false",
               'data-parsley-group': 'group0',
               'rows': '3'
               }
    ),
    required=False
    )
    CHECKBOX = forms.BooleanField(
        widget=forms.widgets.CheckboxInput(
            attrs={'class': 'checkbox-inline',
                   'data-parsley-required': "false",
                   'data-parsley-group': 'group0',
                   'id':'checkboxform'
                   }
        ),
    ),
    CPIMSID = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'id': 'cpims_id',
               'type': 'hidden',
               'data-parsley-required': "False"
               }
        )
    ),
    ORG_UNIT =  forms.ChoiceField(
        choices=org_units_list, widget=forms.Select(
            attrs={
                'id': 'transfer_org',
                'class': 'form-control',
                'data-parsley-required': "false",
                'data-parsley-group': 'group0'
            }),
    )
    EDIT_REASON = forms.ChoiceField(
        choices=CHOICES, widget=forms.Select(
            attrs={
                'id': 'transfer_reason',
                'class': 'form-control',
                'data-parsley-required': "false",
                'data-parsley-group': 'group0'
            }),
    )
    EDIT_ORG =  forms.ChoiceField(
        choices=org_units_list, widget=forms.Select(
            attrs={
                'id': 'transfer_org',
                'class': 'form-control',
                'data-parsley-required': "false",
                'data-parsley-group': 'group0'
            }),
    )