from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from cpovc_auth.models import AppUser
from cpovc_main.functions import convert_date
from cpovc_ovc.forms import OVCSearchForm
from cpovc_preventive.functions import get_person_org_unit
from cpovc_registry.models import RegPerson, RegOrgUnit
from cpovc_forms.functions import get_person_ids
from datetime import datetime


from .models import DREAMSServices
from cpovc_dreams.tasks import get_dreams_services


def dreams_home(request):
    try:
        form = OVCSearchForm(data=request.GET)
        search_string = request.GET.get('search_name')
        pids = get_person_ids(request, search_string)

        person_records = RegPerson.objects.filter(
            is_void=False, id__in=pids, designation='CCGV')

        hes_data = {}
        hes_records = DREAMSServices.objects.filter(
            is_void=False, person_id__in=pids)
        for hes_record in hes_records:
            hes_data[hes_record.person_id] = {
                'id': hes_record.hes_id,
                'cbo_id': hes_record.cbo_id
            }

        combined_data = []  # List to hold combined records
        for person_record in person_records:
            combined_record = {
                'person_record': person_record,
                # Retrieve HES data for the person
                'hes_data': hes_data.get(person_record.id, {})
            }
            combined_data.append(combined_record)

        context = {
            'status': 200,
            'combined_data': combined_data,
            'form': form
        }
        get_dreams_services.delay(1, 2)

        return render(request, 'dreams/home.html', context)

    except Exception as e:
        raise e
