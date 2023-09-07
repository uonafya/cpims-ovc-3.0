from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse

from cpovc_settings.forms import SettingsForm

from .forms import mobile_approve


@login_required
def ovc_dashboard(request):
    """Method to do pivot reports."""
    try:
        form = mobile_approve()
        return render(
            request, 'dashboards/ovc_dashboard.html',
            {'form': form})
    except Exception as e:
        raise e
    else:
        pass