from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse

from .forms import CaseLoad
from .functions import get_geo, get_lips, get_chart_data, get_ips, get_data
from .parameters import colors as dcolors
from .parameters import CHART
from .params import CHART as GCHART

from cpovc_settings.forms import SettingsForm


@login_required
def ovc_dashboard(request):
    """Method to do pivot reports."""
    try:
        form = CaseLoad()
        return render(
            request, 'dashboards/ovc_dashboard.html',
            {'form': form, 'colors': dcolors})
    except Exception as e:
        raise e
    else:
        pass