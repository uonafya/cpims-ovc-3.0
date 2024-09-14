from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from cpovc_auth.models import AppUser
from cpovc_main.functions import convert_date
from cpovc_ovc.forms import OVCSearchForm
from cpovc_preventive.functions import get_person_org_unit
from cpovc_registry.models import (
    RegPerson, RegOrgUnit, RegPersonsExternalIds)
from cpovc_forms.functions import get_person_ids
from datetime import datetime


from .models import DREAMSServices
from cpovc_dreams.tasks import get_dreams_services


@login_required
def dreams_home(request):
    try:
        form = OVCSearchForm(data=request.GET)
        search_string = request.GET.get('search_name')
        pids = get_person_ids(request, search_string)

        person_records = RegPerson.objects.filter(
            is_void=False, id__in=pids, designation='CCGV')

        hes_data = {}
        all_records = DREAMSServices.objects.filter(is_void=False)
        dreams_data = all_records.filter(person_id__in=pids).distinct('dreams_id')

        # Get co-enrolled
        co_enrolls = RegPersonsExternalIds.objects.filter(
            identifier_type_id='IDRM', is_void=False)
        stats = {}
        # all_records.filter(person_id__isnull=False).count()
        stats['co_enrolled'] = co_enrolls.count()
        stats['agyw'] = all_records.distinct('dreams_id').count()
        stats['services'] = all_records.count()

        context = {
            'status': 200,
            'combined_data': dreams_data,
            'form': form, 'stats': stats
        }
        get_dreams_services.delay(1, 2)

        return render(request, 'dreams/home.html', context)

    except Exception as e:
        raise e
