from django import forms
from cpovc_main.functions import get_list

EMPLOYMENT_STATUS = get_list('employment_id','Please Select')

EMPLOYMENT_TYPE = get_list('employment_type_id','Please Select')

HEALTH_SCHEME = get_list('health_scheme_id','Please Select')

SAFETY_NETS =get_list ( 'safety_net_id','Please Select')
SECTOR = get_list('sector_id','Please Select')

FINANCIAL_INSTITUTION_TYPE = get_list('financial_institution_id','Please Select')
TYPE_OF_ASSETS = get_list('asset_type_id','Please Select')
USE_OF_ECT = get_list('use_of_ect_id','Please Select')
LOAN_UTILIZATION = get_list('loan_utilization_id','Please Select')

YESNO_CHOICES = get_list('yesno_id')


class HesForm(forms.Form):
    employment_status = forms.ChoiceField(label="Employment Status",
                                          choices=EMPLOYMENT_STATUS,
                                          required=True,
                                          widget=forms.Select(
                                              attrs={
                                                  "placeholder": ("Employment status"),
                                                  "class": "form-control",
                                                  "data_parsley_required": "true",

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

                                           required=True,
                                           choices=YESNO_CHOICES,
                                           widget=forms.RadioSelect(
                                               attrs={
                                                   "data_parsley_required": "true",

                                               }
                                           ))
=

    health_scheme = forms.ChoiceField(label="Health Scheme",
                                      required=False,
                                      choices=HEALTH_SCHEME,
                                      widget=forms.Select(
                                          attrs={
                                              "class": "form-control",
                                              "class": "form-control",

                                          }
                                      ))
    kitchen_garden = forms.ChoiceField(label="Kitchen Garden",

                                       required=True,
                                       choices=YESNO_CHOICES,
                                       widget=forms.RadioSelect(
                                               attrs={
                                                   "data_parsley_required": "true",

                                               }
                                           ))
    social_safety_nets = forms.ChoiceField(label="Social Safety Nets",
                                           required=True,
                                           choices=YESNO_CHOICES,
                                           widget=forms.RadioSelect(
                                               attrs={
                                                   "data_parsley_required": "true",

                                               }
                                           ))
    social_safety_nets_type = forms.ChoiceField(label="Social Safety Nets",
                                                required=False,
                                                choices=SAFETY_NETS,
                                                widget=forms.Select(
                                                    attrs={
                                                        "placeholder": ("Health scheme"),
                                                        "class": "form-control",


                                                    }
                                                ))

    linkage_to_vsls = forms.ChoiceField(label="Linkage to VSLS",
                                        required=True,
                                        choices=YESNO_CHOICES,

                                        widget=forms.RadioSelect(
                                               attrs={
                                                   "data_parsley_required": "true",

                                               }
                                           ))
    vsla_name = forms.CharField(label="VSLA",
                                required=False,

                                widget=forms.TextInput(
                                    attrs={'placeholder': ('VSLA'),
                                           'class': 'form-control',
                                           }))

    date_linkage = forms.DateField(label='Date of Linkage to VSLA',
                                   required=False,
                                   widget=forms.TextInput(
                                       attrs={
                                           "placeholder": ("Date Start Up Received"),
                                           "class": "form-control",
                                           "id": "admission_date",
                                           "data_parsley_group": "group0",
                                       }
                                   )
                                   )
    monthly_saving = forms.DecimalField(label='Monthly Saving',
                                        required=False,
                                        widget=forms.TextInput(
                                            attrs={'placeholder': ('Amount(Ksh)'),
                                                   'class': 'form-control',


                                                   }))
    average_cumulative_saving = forms.DecimalField(label='Average Cumulative Saving',
                                                   required=False,
                                                   widget=forms.TextInput(
                                                       attrs={'placeholder': ('Amount(Ksh)'),
                                                              'class': 'form-control',


                                                              }))
    loan_taken = forms.ChoiceField(label='Loan Taken',
                                   required=True,
                                   choices=YESNO_CHOICES,

                                   widget=forms.RadioSelect(
                                               attrs={
                                                   "data_parsley_required": "true",
                                               }
                                           ))

    loan_taken_amount = forms.DecimalField(label='Loan Taken Amount',
                                           required=False,
                                           widget=forms.TextInput(
                                               attrs={'placeholder': ('Amount(Ksh)'),
                                                      'class': 'form-control',

                                                      }))
    date_loan_taken = forms.DateField(label='Date Loan Taken',
                                      required=False,
                                      widget=forms.TextInput(
                                          attrs={
                                              "placeholder": ("Date Start Up Received"),
                                              "class": "form-control",
                                              "id": "admission_date",
                                              "data_parsley_group": "group0",
                                          }
                                      )
                                      )
    loan_utilization = forms.ChoiceField(label='Loan Utilization',
                                         required=False,
                                         choices=LOAN_UTILIZATION,
                                         widget=forms.Select(
                                             attrs={'class': 'form-control',


                                                    }))
    startup = forms.ChoiceField(label='Start Up',

                                required=True,
                                choices=YESNO_CHOICES,
                                widget=forms.RadioSelect(
                                               attrs={
                                                   "data_parsley_required": "true",
                                               }
                                           ))


    type_of_startup = forms.ChoiceField(label='Type of Startup',
                                        required=False,
                                        choices=SECTOR,
                                        widget=forms.Select(
                                            attrs={'class': 'form-control',

                                                   }))
    date_startup_received = forms.DateField(label='Date Startup Received',
                                            required=False,
                                            widget=forms.TextInput(
                                                attrs={
                                                    "placeholder": ("Date Start Up Received"),
                                                    "class": "form-control",
                                                    "id": "admission_date",
                                                    "data_parsley_group": "group0",
                                                }
                                            )
                                            )
    emergency_cash_transfer = forms.ChoiceField(label='Emergency Cash Transfer (ECT)',
                                                required=True,
                                                choices=YESNO_CHOICES,

                                                widget=forms.RadioSelect
                                                    (
                                                    attrs={
                                                        "data_parsley_required": "true",
                                                    }
                                                )
                                                )

    amount_received_ect = forms.DecimalField(label='Amount received ECT',
                                             required=False,
                                             widget=forms.TextInput(
                                                 attrs={'placeholder': ('Amount(Ksh)'),
                                                        'class': 'form-control'}))
    use_of_ect = forms.ChoiceField(label='Use of ECT',

                                   required=False,

                                   choices=USE_OF_ECT,
                                   widget=forms.Select(
                                       attrs={'class': 'form-control',

                                              }))

    received_startup_kit = forms.ChoiceField(label='Received Start-up Kit',
                                             required=True,
                                             choices=YESNO_CHOICES,

                                             widget=forms.RadioSelect(
                                               attrs={
                                                   "data_parsley_required": "true",
                                               }
                                           ))

    type_of_asset = forms.ChoiceField(label='Type of Asset',
                                      required=False,
                                      choices=TYPE_OF_ASSETS,
                                      widget=forms.Select(
                                          attrs={'class': 'form-control',

                                                 }))
    average_monthly_income_generated = forms.DecimalField(label='Average Monthly Income Generated',
                                                          required=False,
                                                          widget=forms.TextInput(
                                                              attrs={'class': 'form-control',

                                                                     }))
    received_business_grant = forms.ChoiceField(label='Received Business Grant',
                                                required=True,
                                                choices=YESNO_CHOICES,

                                                widget=forms.RadioSelect(
                                               attrs={
                                                   "data_parsley_required": "true",
                                               }
                                           ))

    amount_of_money_received = forms.DecimalField(label='Amount of Money Received',
                                                  required=False,
                                                  widget=forms.TextInput(
                                                      attrs={'class': 'form-control',

                                                             }))
    business_type_started = forms.CharField(label='Business Type Started',
                                            required=False,
                                            widget=forms.TextInput(
                                                attrs={'placeholder': ('business type'),
                                                       'class': 'form-control',
                                                       }))
    linked_to_value_chain_activities_asset_growth = forms.ChoiceField(label='Linked to',

                                                                      required=True,
                                                                      choices=YESNO_CHOICES,
                                                                      widget=forms.RadioSelect(
                                               attrs={
                                                   "data_parsley_required": "true",
                                               }
                                           ))

    sector_of_asset_growth = forms.ChoiceField(label='Sector',
                                               required=False,
                                               choices=SECTOR,
                                               widget=forms.Select(
                                                   attrs={'class': 'form-control',

                                                          }))
    linked_to_source_finance = forms.ChoiceField(label='Linked to Source of Finance',
                                                 required=True,
                                                 choices=YESNO_CHOICES,

                                                 widget=forms.RadioSelect(
                                               attrs={
                                                   "data_parsley_required": "true",
                                               }
                                           ))

    type_of_financial_institution = forms.ChoiceField(label='Type of Financial Institution',
                                                      required=False,

                                                      choices=FINANCIAL_INSTITUTION_TYPE,
                                                      widget=forms.Select(
                                                          attrs={'class': 'form-control',

                                                                 }))
    loan_taken_income_growth = forms.ChoiceField(label='Loan Taken',
                                                 required=True,
                                                 choices=YESNO_CHOICES,
                                                 widget=forms.RadioSelect(
                                               attrs={
                                                   "data_parsley_required": "true",
                                               }
                                           ))
    date_loan_taken_income_growth = forms.DateField(label='Date of Loan Taken',

                                                    required=False,
                                   widget=forms.TextInput(
                                                        attrs={
                                                            "placeholder": ("Date Start Up Received"),
                                                            "class": "form-control",
                                                            "id": "admission_date",

                                                            "data_parsley_group": "group0",
                                                        }
                                                    )
                                                    )
    linked_to_value_chain_activities_income_growth = forms.ChoiceField(label='Linked to',
                                                                       required=True,
                                                                       choices=YESNO_CHOICES,
                                                                       widget=forms.RadioSelect(
                                               attrs={
                                                   "data_parsley_required": "true",
                                               }
                                           ))
    sector_of_income_growth = forms.ChoiceField(label='Sector',
                                                required=False,
                                                choices=SECTOR,
                                                widget=forms.Select(
                                                    attrs={'class': 'form-control',

                                                           }))
