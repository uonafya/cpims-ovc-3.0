from django import forms
from cpovc_main.functions import get_list

EMPLOYMENT_STATUS = (('Employed', 'Employed'), ('Unemployed', 'Unemployed'),
                     )
EMPLOYMENT_TYPE = (('Casual', 'Casual'), ('Business', 'Business'))

HEALTH_SCHEME = (('County Health Scheme', 'County Health Scheme'), ('NHIF', 'NHIF'),
                 ('Universal Health Coverage', 'Universal Health Coverage'))

SAFETY_NETS = (('None', 'None'), ('CT OVC', 'CT OVC'),
               ('CT Elderly', 'CT Elderly'), ('CT Disability', 'CT Disability'))
SECTOR = (('Agriculture', 'Agriculture'),
          (' Non Agriculture', 'Non Agriculture'))

FINANCIAL_INSTITUTION_TYPE = (
    ('Bank ', 'Bank'), (' MFI', 'MFI'), (' SACCO', 'SACCO'), (' VSLA', 'VSLA'))
TYPE_OF_ASSETS = (('Business Asset', 'Business Asset'),
                  ('Agriculture assets ', 'Agriculture assets '))
USE_OF_ECT = (('Transport to facility', 'Transport to facility'), (' Food', 'Food'), (' Medication',
                                                                                      'Medication'), (' Setting up a business', 'Setting up a business'), (' NHIF ', 'NHIF '))
LOAN_UTILIZATION = (('Business ', 'Business'), (' School Fees',
                                                'School Fees'), ('Food', 'Food'), (' None', 'None'))
YESNO_CHOICES = get_list('yesno_id')


class HesForm(forms.Form):
    employment_status = forms.ChoiceField(label="Employment Status",
                                          choices=EMPLOYMENT_STATUS,
                                          required=False,
                                          widget=forms.Select(
                                              attrs={
                                                  "placeholder": ("Employment status"),
                                                  "class": "form-control",

                                              }
                                          ))
    type_of_employment = forms.ChoiceField(label="Employment Status",
                                           choices=EMPLOYMENT_TYPE,
                                           required=False,
                                           widget=forms.Select(
                                               attrs={
                                                   "placeholder": ("Employment status"),
                                                   "class": "form-control",

                                               }
                                           ))

    have_health_scheme = forms.ChoiceField(label='Have health scheme?',
                                           choices=YESNO_CHOICES,
                                           widget=forms.RadioSelect)

    health_scheme = forms.ChoiceField(label="Health Scheme",
                                      choices=HEALTH_SCHEME,
                                      widget=forms.Select(
                                          attrs={
                                              "placeholder": ("Health scheme"),
                                              "class": "form-control",
                                              "id": "institution_type",
                                          }
                                      ))
    kitchen_garden = forms.ChoiceField(label="Kitchen Garden",
                                       choices=YESNO_CHOICES,
                                       widget=forms.RadioSelect)
    social_safety_nets = forms.ChoiceField(label="Social Safety Nets",
                                           choices=YESNO_CHOICES,
                                           widget=forms.RadioSelect)
    social_safety_nets_type = forms.ChoiceField(label="Social Safety Nets",
                                                choices=SAFETY_NETS,
                                                widget=forms.Select(
                                                    attrs={
                                                        "placeholder": ("Health scheme"),
                                                        "class": "form-control",

                                                    }
                                                ))

    linkage_to_vsls = forms.ChoiceField(label="Linkage to VSLS",
                                        choices=YESNO_CHOICES,
                                        widget=forms.RadioSelect)
    vsla_name = forms.CharField(label="VSLA",
                                widget=forms.TextInput(
                                    attrs={'placeholder': ('VSLA'),
                                           'class': 'form-control',
                                           }))

    date_linkage = forms.DateField(label='Date of Linkage to VSLA',
                                   widget=forms.TextInput(
                                       attrs={
                                           "placeholder": ("Date Start Up Received"),
                                           "class": "form-control",
                                           "id": "admission_date",
                                           "data_parsley_required": "true",
                                           "data_parsley_group": "group0",
                                       }
                                   )
                                   )
    monthly_saving = forms.DecimalField(label='Monthly Saving',
                                        widget=forms.TextInput(
                                            attrs={'placeholder': ('Amount(Ksh)'),
                                                   'class': 'form-control',


                                                   }))
    average_cumulative_saving = forms.DecimalField(label='Average Cumulative Saving',
                                                   widget=forms.TextInput(
                                                       attrs={'placeholder': ('Amount(Ksh)'),
                                                              'class': 'form-control',


                                                              }))
    loan_taken = forms.ChoiceField(label='Loan Taken',
                                   choices=YESNO_CHOICES,
                                   widget=forms.RadioSelect)
    loan_taken_amount = forms.DecimalField(label='Loan Taken Amount',
                                           widget=forms.TextInput(
                                               attrs={'placeholder': ('Amount(Ksh)'),
                                                      'class': 'form-control',

                                                      }))
    date_loan_taken = forms.DateField(label='Date Loan Taken',
                                      widget=forms.TextInput(
                                          attrs={
                                              "placeholder": ("Date Start Up Received"),
                                              "class": "form-control",
                                              "id": "admission_date",
                                              "data_parsley_required": "true",
                                              "data_parsley_group": "group0",
                                          }
                                      )
                                      )
    loan_utilization = forms.ChoiceField(label='Loan Utilization',
                                         choices=LOAN_UTILIZATION,
                                         widget=forms.Select(
                                             attrs={'class': 'form-control',


                                                    }))
    startup = forms.ChoiceField(label='Start Up',
                                choices=YESNO_CHOICES,
                                widget=forms.RadioSelect)

    type_of_startup = forms.ChoiceField(label='Type of Startup',
                                        choices=SECTOR,
                                        widget=forms.Select(
                                            attrs={'class': 'form-control',

                                                   }))
    date_startup_received = forms.DateField(label='Date Startup Received',
                                            widget=forms.TextInput(
                                                attrs={
                                                    "placeholder": ("Date Start Up Received"),
                                                    "class": "form-control",
                                                    "id": "admission_date",
                                                    "data_parsley_required": "true",
                                                    "data_parsley_group": "group0",
                                                }
                                            )
                                            )
    emergency_cash_transfer = forms.ChoiceField(label='Emergency Cash Transfer (ECT)',
                                                choices=YESNO_CHOICES,
                                                widget=forms.RadioSelect)
    amount_received_ect = forms.DecimalField(label='Amount received ECT',
                                             widget=forms.TextInput(
                                                 attrs={'placeholder': ('Amount(Ksh)'),
                                                        'class': 'form-control'}))
    use_of_ect = forms.ChoiceField(label='Use of ECT',
                                   choices=USE_OF_ECT,
                                   widget=forms.Select(
                                       attrs={'class': 'form-control',

                                              }))

    received_startup_kit = forms.ChoiceField(label='Received Start-up Kit',
                                             choices=YESNO_CHOICES,
                                             widget=forms.RadioSelect)
    type_of_asset = forms.ChoiceField(label='Type of Asset',
                                      choices=TYPE_OF_ASSETS,
                                      widget=forms.Select(
                                          attrs={'class': 'form-control',

                                                 }))
    average_monthly_income_generated = forms.DecimalField(label='Average Monthly Income Generated',
                                                          widget=forms.TextInput(
                                                              attrs={'class': 'form-control',

                                                                     }))
    received_business_grant = forms.ChoiceField(label='Received Business Grant',
                                                choices=YESNO_CHOICES,
                                                widget=forms.RadioSelect)
    amount_of_money_received = forms.DecimalField(label='Amount of Money Received',
                                                  widget=forms.TextInput(
                                                      attrs={'class': 'form-control',

                                                             }))
    business_type_started = forms.CharField(label='Business Type Started',
                                            widget=forms.TextInput(
                                                attrs={'placeholder': ('business type'),
                                                       'class': 'form-control',
                                                       }))
    linked_to_value_chain_activities_asset_growth = forms.ChoiceField(label='Linked to',
                                                                      choices=YESNO_CHOICES,
                                                                      widget=forms.RadioSelect)
    sector_of_asset_growth = forms.ChoiceField(label='Sector',
                                               choices=SECTOR,
                                               widget=forms.Select(
                                                   attrs={'class': 'form-control',

                                                          }))
    linked_to_source_finance = forms.ChoiceField(label='Linked to Source of Finance',
                                                 choices=YESNO_CHOICES,
                                                 widget=forms.RadioSelect)

    type_of_financial_institution = forms.ChoiceField(label='Type of Financial Institution',
                                                      choices=FINANCIAL_INSTITUTION_TYPE,
                                                      widget=forms.Select(
                                                          attrs={'class': 'form-control',

                                                                 }))
    loan_taken_income_growth = forms.ChoiceField(label='Loan Taken',
                                                 choices=YESNO_CHOICES,
                                                 widget=forms.RadioSelect)
    date_loan_taken_income_growth = forms.DateField(label='Date of Loan Taken',
                                                    widget=forms.TextInput(
                                                        attrs={
                                                            "placeholder": ("Date Start Up Received"),
                                                            "class": "form-control",
                                                            "id": "admission_date",
                                                            "data_parsley_required": "true",
                                                            "data_parsley_group": "group0",
                                                        }
                                                    )
                                                    )
    linked_to_value_chain_activities_income_growth = forms.ChoiceField(label='Linked to',
                                                                       choices=YESNO_CHOICES,
                                                                       widget=forms.RadioSelect)
    sector_of_income_growth = forms.ChoiceField(label='Sector',
                                                choices=SECTOR,
                                                widget=forms.Select(
                                                    attrs={'class': 'form-control',

                                                           }))
