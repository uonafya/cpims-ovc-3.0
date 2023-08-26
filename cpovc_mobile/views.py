from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse

from cpovc_settings.forms import SettingsForm

from .forms import mobile_approve
from cpovc_forms.models import OVCCareF1B, OVCCareEAV

from cpovc_registry.models import RegPersonsOrgUnits, RegOrgUnit, RegPerson

from cpovc_ovc.models import OVCRegistration


@login_required
def mobile_home(request):
    """Method to do pivot reports."""

    form1b = OVCCareEAV.objects.filter(event = 'b4e0d636-34e8-11e9-9e13-e4a471adc5eb')
    currentUser = request.user.reg_person_id
    try:
        form = mobile_approve()
        lip_name = request.session.get('ou_primary_name')
        lip_id = request.session.get('ou_primary')

        chvss = OVCRegistration.objects.filter(is_void=False, child_cbo_id=lip_id).distinct('child_chv_id')
        chvs = []
        for chv in chvss:
            chvs.append({
                'cpims_chv_id': chv.child_chv.pk,
                'name': f"{chv.child_chv.full_name}"
            })

        return render(
            request, 'mobile/home.html',
            {
                'form': form,
                'formdata': form1b,
                'chvs': chvs,
                'lip_name': lip_name
             
            }
             )
    except Exception as e:
        raise e
    else:
        pass

def mobiledataapproval(request):
    if request.method == "POST":
        data = request.POST
        print(f">>>>>approval data{data.getlist('data[]')} {data.get('type')}")
        # Do something with the data, e.g., save to a database

        approval_type = data.get('type')
        approval_data = data.getlist('data[]')
        response_data = {
            "status": "success",
            "message": "Data received and processed successfully."
            }
        return JsonResponse(response_data, safe=False)
    else:
        return JsonResponse({"error": "Invalid request method."}, safe=False)
    
def fetchChildren(request):
    children = []
    if request.method == "POST":
        data = request.POST.getlist('data[]')
        childrens = OVCRegistration.objects.filter(is_void=False, child_chv_id__in = data).distinct('person')
        for child in childrens:
            children.append({
                'cpims_ovc_id': child.person.pk,
                'name': child.person.full_name
            })

        print(f"----- {data} >- {children} -  {childrens}")
        # Do something with the data, e.g., save to a database
        response_data = {"message": "Data received and processed successfully."}
        return JsonResponse(children, safe=False)
    else:
        return JsonResponse({"error": "Invalid request method."}, safe=False)
    
def fetchData(request):
    if request.method == "POST":
        data = request.POST
        # Do something with the data, e.g., save to a database

        form_sel = request.POST.get('form')
        chv_sel = request.POST.getlist('chvs[]')
        child_sel = request.POST.getlist('child[]')
        print(f"{form_sel} - {chv_sel} - {child_sel}")
   
        response_data = {
            "status": "success",
            "message": "Data received and processed successfully."
            }
        return JsonResponse(response_data, safe=False)
    else:
        return JsonResponse({"error": "Invalid request method."}, safe=False)
    