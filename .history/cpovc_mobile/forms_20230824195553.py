"""Forms for Registry sections of CPIMS."""
from django import forms
from django.utils.translation import gettext_lazy as _
from cpovc_main.functions import get_list

person_type_list = ()
sex_id_list = get_list('sex_id', 'Select')


class NOTTForm(forms.Form):
    """Search registry form."""

    person_type = forms.ChoiceField(
        choices=person_type_list,
        initial='0',
        required=False,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'person_type',
                   'data-parsley-required': 'true'}))