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

    form1b = OVCCareEAV.objects.filter(event = 'b4e0d636-34e8-11e9-9e13-e4a471adc5eb')
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

def my_django_endpoint(request):
    if request.method == "POST":
        data = request.POST.get("data")
        # Do something with the data, e.g., save to a database
        response_data = {"message": "Data received and processed successfully."}
        return JsonResponse(response_data)
    else:
        return JsonResponse({"error": "Invalid request method."})