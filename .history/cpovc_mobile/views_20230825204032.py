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
    try:
        form = mobile_approve()

        chvs = [
            {
                'cpimsid': 456,
                'name': 'Wafula Chebukati'
             },
            {
                'cpimsid': 4566,
                'name': 'Tim Wanyonyi'
            },
            {
                'cpimsid': 566,
                'name': 'Bukusu Kachmega'
            }
        ]
        return render(
            request, 'mobile/home.html',
            {
                'form': form,
                'formdata': form1b,
                'chvs': chvs,
             
            }
             )
    except Exception as e:
        raise e
    else:
        pass

def mobiledataapproval(request):
    if request.method == "POST":
        data = request.POST.get("data")
        print(data) 
        # Do something with the data, e.g., save to a database
        response_data = {
            "message": "Data received and processed successfully."}
        return JsonResponse(response_data, safe=False)
    else:
        return JsonResponse({"error": "Invalid request method."}, safe=False)
    
def fetchChildren(request):
    if request.method == "POST":
        data = request.POST.get("data")
        print(data)
        # Do something with the data, e.g., save to a database
        response_data = {"message": "Data received and processed successfully."}
        return JsonResponse(response_data, safe=False)
    else:
        return JsonResponse({"error": "Invalid request method."}, safe=False)