from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse

from cpovc_settings.forms import SettingsForm

from .forms import mobile_approve
from cpovc_forms.models import OVCCareF1B, OVCCareEAV


@login_required
def mobile_home(request):
    """Method to do pivot reports."""

    form1b = OVCCareEAV.objects.filter(event = '')
    print(f'form 1 b data{form1b}')
    try:
        form = mobile_approve()
        return render(
            request, 'mobile/home.html',
            {
                'form': form,
                'formdata': form1b
             
            }
             )
    except Exception as e:
        raise e
    else:
        pass