from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from cpovc_main.functions import convert_date
from cpovc_forms.forms import OVCSearchForm
from cpovc_registry.models import RegPerson
from cpovc_forms.functions import get_person_ids

from .forms import HesForm
from .models import CPOVC_HES


def hes_home(request):

    try:
        form = OVCSearchForm(data=request.GET)

        search_string = request.GET.get('search_name')
        pids = get_person_ids(request, search_string)

        ctip_ids, case_ids = {}, {}
        cases = RegPerson.objects.filter(is_void=False, id__in=pids)

        # Get HES details
        crss = CPOVC_HES.objects.filter(is_void=False, person_id__in=pids)
        for crs in crss:
            case_ids[crs.person_id] = {
                'clv': 1, 'cs': crs.case_serial, 'cid': crs.case_id}

        for case in cases:
            pid = case.id
            cid = ctip_ids[pid]['cid'] if pid in ctip_ids else 'N/A'
            cdt = ctip_ids[pid]['cdt'] if pid in ctip_ids else 'N/A'
            clvf = case_ids[pid]['clv'] if pid in case_ids else 0
            clv = ctip_ids[pid]['clv'] if pid in ctip_ids else clvf
            csn = case_ids[pid]['cs'] if pid in case_ids else 'N/A'
            ccid = case_ids[pid]['cid'] if pid in case_ids else 'N/A'

            setattr(case, 'case_t', str(cid))
            setattr(case, 'case_date', cdt)
            setattr(case, 'case_level', clv)
            setattr(case, 'case_id', cid)
            setattr(case, 'case_cid', str(ccid))
            setattr(case, 'case_serial', csn)
        context = {
            'status': 200,
            'cases': cases,
            'form': form
        }

        return render(request, 'hes/home.html', context)

    except Exception as e:
        raise e


def new_hes(request, id):

    form = HesForm()
    try:
        if(request.method == "POST"):
            data = request.POST
            print(data)
            CPOVC_HES(
                employment_status=data.get('employment_status'),
                type_of_employment=data.get('type_of_employment'),
                health_scheme=data.get('health_scheme'),
                health_scheme_type=data.get('health_scheme_type'),
                kitchen_garden=data.get('kitchen_garden'),
                social_safety_nets=data.get('social_safety_nets'),
                social_safety_nets_type=data.get('social_safety_nets_type'),
                linkage_to_vsls=data.get('linkage_to_vsls'),
                vsla=data.get('vsla'),
                date_of_linkage_to_vsla=convert_date(data.get('date_linkage')),
                monthly_saving_average=data.get('monthly_saving'),
                average_cumulative_saving=data.get(
                    'average_cumulative_saving'),
                loan_taken=data.get('loan_taken'),
                loan_taken_amount=data.get('loan_taken_amount'),
                date_loan_taken=convert_date(data.get('date_loan_taken')),
                loan_utilization=data.get('loan_utilization'),
                startup=data.get('startup'),
                type_of_startup=data.get('type_of_startup'),
                date_startup_received=convert_date(
                    data.get('date_startup_received')),
                emergency_cash_transfer=data.get('emergency_cash_transfer'),
                amount_received_ect=data.get('amount_received_ect'),
                use_of_ect=data.get('use_of_ect'),
                received_startup_kit=data.get('received_startup_kit'),
                type_of_asset=data.get(' type_of_asset'),
                average_monthly_income_generated=data.get(
                    'average_monthly_income_generated'),
                received_business_grant=data.get('received_business_grant'),
                amount_of_money_received=data.get('amount_of_money_received'),
                business_type_started=data.get('business_type_started'),
                linked_to_value_chain_activities_asset_growth=data.get(
                    'linked_to_value_chain_activities_asset_growth'),
                sector_of_asset_growth=data.get('sector_of_asset_growth'),
                linked_to_source_finance=data.get('linked_to_source_finance'),
                type_of_financial_institution=data.get(
                    ' type_of_financial_institution'),
                loan_taken_income_growth=data.get('loan_taken_asset_growth'),
                date_loan_taken_income_growth=data.get(
                    'date_loan_taken_asset_growth'),
                linked_to_value_chain_activities_income_growth=data.get(
                    'linked_to_value_chain_activities_income_growth'),
                sector_of_income_growth=data.get('sector_of_income_growth'),
            ).save()

            HttpResponseRedirect(reverse(new_hes))
        context = {
            'form': form,

        }
        return render(request, 'hes/new_enrollment.html', context)

    except Exception as e:
        raise e


def view_hes(request, id):

    form = HesForm()
    try:
        case = CPOVC_HES.objects.filter(is_void=False)
        if(request.method == "POST"):
            data = request.POST
            print(data)
            CPOVC_HES(
                employment_status=data.get('employment_status'),
                type_of_employment=data.get('type_of_employment'),
                health_scheme=data.get('health_scheme'),
                health_scheme_type=data.get('health_scheme_type'),
                kitchen_garden=data.get('kitchen_garden'),
                social_safety_nets=data.get('social_safety_nets'),
                social_safety_nets_type=data.get('social_safety_nets_type'),
                linkage_to_vsls=data.get('linkage_to_vsls'),
                vsla=data.get('vsla'),
                date_of_linkage_to_vsla=convert_date(data.get('date_linkage')),
                monthly_saving_average=data.get('monthly_saving'),
                average_cumulative_saving=data.get(
                    'average_cumulative_saving'),
                loan_taken=data.get('loan_taken'),
                loan_taken_amount=data.get('loan_taken_amount'),
                date_loan_taken=convert_date(data.get('date_loan_taken')),
                loan_utilization=data.get('loan_utilization'),
                startup=data.get('startup'),
                type_of_startup=data.get('type_of_startup'),
                date_startup_received=convert_date(
                    data.get('date_startup_received')),
                emergency_cash_transfer=data.get('emergency_cash_transfer'),
                amount_received_ect=data.get('amount_received_ect'),
                use_of_ect=data.get('use_of_ect'),
                received_startup_kit=data.get('received_startup_kit'),
                type_of_asset=data.get(' type_of_asset'),
                average_monthly_income_generated=data.get(
                    'average_monthly_income_generated'),
                received_business_grant=data.get('received_business_grant'),
                amount_of_money_received=data.get('amount_of_money_received'),
                business_type_started=data.get('business_type_started'),
                linked_to_value_chain_activities_asset_growth=data.get(
                    'linked_to_value_chain_activities_asset_growth'),
                sector_of_asset_growth=data.get('sector_of_asset_growth'),
                linked_to_source_finance=data.get('linked_to_source_finance'),
                type_of_financial_institution=data.get(
                    ' type_of_financial_institution'),
                loan_taken_income_growth=data.get('loan_taken_asset_growth'),
                date_loan_taken_income_growth=data.get(
                    'date_loan_taken_asset_growth'),
                linked_to_value_chain_activities_income_growth=data.get(
                    'linked_to_value_chain_activities_income_growth'),
                sector_of_income_growth=data.get('sector_of_income_growth'),
            ).save()

            HttpResponseRedirect(reverse(new_hes))
        context = {'form': form, 'case': case}
        return render(request, 'hes/sta_es.html', context)

    except Exception as e:
        raise e
