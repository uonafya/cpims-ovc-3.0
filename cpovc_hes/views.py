from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from cpovc_auth.models import AppUser
from cpovc_main.functions import convert_date
from cpovc_forms.forms import OVCSearchForm
from cpovc_preventive.functions import get_person_org_unit
from cpovc_registry.models import RegPerson, RegOrgUnit
from cpovc_forms.functions import get_person_ids
from datetime import datetime


from .forms import HesForm
from .models import CPOVC_HES
from decimal import Decimal


def hes_home(request):
    try:
        form = OVCSearchForm(data=request.GET)
        search_string = request.GET.get('search_name')
        pids = get_person_ids(request, search_string)

        person_records = RegPerson.objects.filter(is_void=False, id__in=pids, designation='CCGV')  # Filter by designation

        hes_data = {}
        hes_records = CPOVC_HES.objects.filter(is_void=False, person_id__in=pids)
        for hes_record in hes_records:
            hes_data[hes_record.person_id] = {
                'id': hes_record.id,
                'cbo_id': hes_record.cbo_id
            }

        combined_data = []  # List to hold combined records
        for person_record in person_records:
            combined_record = {
                'person_record': person_record,
                'hes_data': hes_data.get(person_record.id, {})  # Retrieve HES data for the person
            }
            combined_data.append(combined_record)

        context = {
            'status': 200,
            'combined_data': combined_data,  # Pass combined data to the template
            'form': form
        }

        return render(request, 'hes/home.html', context)

    except Exception as e:
        raise e


def new_hes(request, id):
    form = HesForm()
    reg_person_id = int(id)
    org_unit_id = get_person_org_unit(request, reg_person_id)
    cbo_id = org_unit_id if org_unit_id else None
    user_id = request.user.id
    created_by_user = AppUser.objects.get(id=user_id)

    try:
        if request.method == "POST":
            data = request.POST

            def get_date(key):
                date_str = data.get(key)
                return convert_date(date_str) if date_str else None

            def get_decimal(key):
                decimal_str = data.get(key)
                return Decimal(decimal_str) if decimal_str else None

            new_hes_instance = CPOVC_HES(
                person_id=RegPerson.objects.filter(is_void=False, id=reg_person_id).values_list('id', flat=True).first(),
                cbo_id=cbo_id,
                employment_status=data.get('employment_status'),
                type_of_employment=data.get('type_of_employment'),
                health_scheme=data.get('have_health_scheme'),
                health_scheme_type=data.get('health_scheme'),
                kitchen_garden=data.get('kitchen_garden'),
                social_safety_nets=data.get('social_safety_nets'),
                social_safety_nets_type=data.get('social_safety_nets_type'),
                linkage_to_vsls=data.get('linkage_to_vsls'),
                vsla=data.get('vsla_name'),
                date_of_linkage_to_vsla=get_date('date_linkage'),
                monthly_saving_average=get_decimal('monthly_saving'),
                average_cumulative_saving=get_decimal('average_cumulative_saving'),
                loan_taken=data.get('loan_taken'),
                loan_taken_amount=get_decimal('loan_taken_amount'),
                date_loan_taken=get_date('date_loan_taken'),
                loan_utilization=data.get('loan_utilization'),
                startup=data.get('startup'),
                type_of_startup=data.get('type_of_startup'),
                date_startup_received=get_date('date_startup_received'),
                emergency_cash_transfer=data.get('emergency_cash_transfer'),
                amount_received_ect=get_decimal('amount_received_ect'),
                use_of_ect=data.get('use_of_ect'),
                received_startup_kit=data.get('received_startup_kit'),
                type_of_asset=data.get('type_of_asset'),
                average_monthly_income_generated=get_decimal('average_monthly_income_generated'),
                received_business_grant=data.get('received_business_grant'),
                amount_of_money_received=get_decimal('amount_of_money_received'),
                business_type_started=data.get('business_type_started'),
                linked_to_value_chain_activities_asset_growth=data.get('linked_to_value_chain_activities_asset_growth'),
                sector_of_asset_growth=data.get('sector_of_asset_growth'),
                linked_to_source_finance=data.get('linked_to_source_finance'),
                type_of_financial_institution=data.get('type_of_financial_institution'),
                loan_taken_income_growth=data.get('loan_taken_income_growth'),
                date_loan_taken_income_growth=get_date('date_loan_taken_income_growth'),
                linked_to_value_chain_activities_income_growth=data.get('linked_to_value_chain_activities_income_growth'),
                sector_of_income_growth=data.get('sector_of_income_growth'),
                created_by=created_by_user
            )
            new_hes_instance.save()

            hes_instance_id = new_hes_instance.id

            return redirect('view_hes', id=hes_instance_id)

        context = {
            'form': form,
        }
        return render(request, 'hes/new_enrollment.html', context)

    except Exception as e:
        raise e

def view_hes(request, id):
    try:
        hes_id = int(id)
        hes_instance = CPOVC_HES.objects.filter(id=hes_id, is_void=False).first()
        person_instance = RegPerson.objects.filter(id=hes_instance.person_id, is_void=False).first()

        if hes_instance:

            data = {
                'person_id': person_instance.id,
                'cbo_id': hes_instance.cbo_id,
                'employment_status': hes_instance.employment_status,
                'type_of_employment': hes_instance.type_of_employment,
                'have_health_scheme': hes_instance.health_scheme,
                'health_scheme': hes_instance.health_scheme_type,
                'kitchen_garden': hes_instance.kitchen_garden,
                'social_safety_nets': hes_instance.social_safety_nets,
                'social_safety_nets_type': hes_instance.social_safety_nets_type,
                'linkage_to_vsls': hes_instance.linkage_to_vsls,
                'vsla': hes_instance.vsla,
                'date_of_linkage_to_vsla': hes_instance.date_of_linkage_to_vsla,
                'monthly_saving': hes_instance.monthly_saving_average,
                'average_cumulative_saving': hes_instance.average_cumulative_saving,
                'loan_taken': hes_instance.loan_taken,
                'loan_taken_amount': hes_instance.loan_taken_amount,
                'date_loan_taken': hes_instance.date_loan_taken,
                'loan_utilization': hes_instance.loan_utilization,
                'startup': hes_instance.startup,
                'type_of_startup': hes_instance.type_of_startup,
                'date_startup_received': hes_instance.date_startup_received,
                'emergency_cash_transfer': hes_instance.emergency_cash_transfer,
                'amount_received_ect': hes_instance.amount_received_ect,
                'use_of_ect': hes_instance.use_of_ect,
                'received_startup_kit': hes_instance.received_startup_kit,
                'type_of_asset': hes_instance.type_of_asset,
                'average_monthly_income_generated': hes_instance.average_monthly_income_generated,
                'received_business_grant': hes_instance.received_business_grant,
                'amount_of_money_received': hes_instance.amount_of_money_received,
                'business_type_started': hes_instance.business_type_started,
                'linked_to_value_chain_activities_asset_growth': hes_instance.linked_to_value_chain_activities_asset_growth,
                'sector_of_asset_growth': hes_instance.sector_of_asset_growth,
                'linked_to_source_finance': hes_instance.linked_to_source_finance,
                'type_of_financial_institution': hes_instance.type_of_financial_institution,
                'loan_taken_income_growth': hes_instance.loan_taken_income_growth,
                'date_loan_taken_income_growth': hes_instance.date_loan_taken_income_growth,
                'linked_to_value_chain_activities_income_growth': hes_instance.linked_to_value_chain_activities_income_growth,
                'sector_of_income_growth': hes_instance.sector_of_income_growth,
                'created_by': hes_instance.created_by,
            }

            form = HesForm(initial=data)

            # Retrieve person details and org_unit_name
            person_details = {
                'first_name': person_instance.first_name,
                'last_name': person_instance.surname,
                'dob': person_instance.date_of_birth,
                # ... (other details)
            }

            org_unit_id = hes_instance.cbo_id
            org_unit = RegOrgUnit.objects.filter(id=org_unit_id).first()
            org_unit_name = org_unit.org_unit_name if org_unit else ""

            context = {
                'form': form,
                'person_details': person_details,
                'hes_details': hes_instance,
                'org_unit_name': org_unit_name,
                'allow_edit': True
            }
            return render(request, 'hes/view_hes.html', context)
        else:
            raise Http404("HES record does not exist")

    except Exception as e:
        raise e



def edit_hes(request, id):
    hes_id = int(id)
    try:
        hes_instance = CPOVC_HES.objects.filter(id=hes_id, is_void=False).first()
        person_instance = RegPerson.objects.filter(id=hes_instance.person_id, is_void=False).first()

        if hes_instance:
            data = {
                'employment_status': hes_instance.employment_status,
                'type_of_employment': hes_instance.type_of_employment,
                'have_health_scheme': hes_instance.health_scheme,
                'health_scheme': hes_instance.health_scheme_type,
                'kitchen_garden': hes_instance.kitchen_garden,
                'social_safety_nets': hes_instance.social_safety_nets,
                'social_safety_nets_type': hes_instance.social_safety_nets_type,
                'linkage_to_vsls': hes_instance.linkage_to_vsls,
                'vsla': hes_instance.vsla,
                'date_linkage': hes_instance.date_of_linkage_to_vsla.strftime(
                    '%Y-%m-%d') if hes_instance.date_of_linkage_to_vsla else None,
                'monthly_saving': hes_instance.monthly_saving_average,
                'average_cumulative_saving': hes_instance.average_cumulative_saving,
                'loan_taken': hes_instance.loan_taken,
                'loan_taken_amount': hes_instance.loan_taken_amount,
                'date_loan_taken': hes_instance.date_loan_taken.strftime(
                    '%Y-%m-%d') if hes_instance.date_loan_taken else None,
                'loan_utilization': hes_instance.loan_utilization,
                'startup': hes_instance.startup,
                'type_of_startup': hes_instance.type_of_startup,
                'date_startup_received': hes_instance.date_startup_received.strftime(
                    '%Y-%m-%d') if hes_instance.date_startup_received else None,
                'emergency_cash_transfer': hes_instance.emergency_cash_transfer,
                'amount_received_ect': hes_instance.amount_received_ect,
                'use_of_ect': hes_instance.use_of_ect,
                'received_startup_kit': hes_instance.received_startup_kit,
                'type_of_asset': hes_instance.type_of_asset,
                'average_monthly_income_generated': hes_instance.average_monthly_income_generated,
                'received_business_grant': hes_instance.received_business_grant,
                'amount_of_money_received': hes_instance.amount_of_money_received,
                'business_type_started': hes_instance.business_type_started,
                'linked_to_value_chain_activities_asset_growth': hes_instance.linked_to_value_chain_activities_asset_growth,
                'sector_of_asset_growth': hes_instance.sector_of_asset_growth,
                'linked_to_source_finance': hes_instance.linked_to_source_finance,
                'type_of_financial_institution': hes_instance.type_of_financial_institution,
                'loan_taken_income_growth': hes_instance.loan_taken_income_growth,
                'date_loan_taken_income_growth': hes_instance.date_loan_taken_income_growth.strftime(
                    '%Y-%m-%d') if hes_instance.date_loan_taken_income_growth else None,
                'linked_to_value_chain_activities_income_growth': hes_instance.linked_to_value_chain_activities_income_growth,
                'sector_of_income_growth': hes_instance.sector_of_income_growth,
            }
            form = HesForm(initial=data)
        else:
            form = HesForm()

        person_details = {
            'first_name': person_instance.first_name,
            'last_name': person_instance.surname,
            'dob': person_instance.date_of_birth,

            # ... (other details)
        }

        org_unit_id = hes_instance.cbo_id if hes_instance else None
        org_unit = RegOrgUnit.objects.filter(id=org_unit_id).first()
        org_unit_name = org_unit.org_unit_name if org_unit else ""

        context = {
            'form': form,
            'person_details': person_details,
            'org_unit_name': org_unit_name,
            'allow_edit': True,
        }

        if request.method == "POST":
            form = HesForm(request.POST)

            if form.is_valid():
                updated_hes_data = form.cleaned_data

                # Convert decimal fields
                decimal_fields = ['monthly_saving', 'average_cumulative_saving', 'loan_taken_amount',
                                  'amount_received_ect', 'average_monthly_income_generated', 'amount_of_money_received']
                for field_name in decimal_fields:
                    if updated_hes_data[field_name] is None:
                        updated_hes_data[field_name] = Decimal('0')

                # Convert date fields manually
                date_fields = ['date_linkage', 'date_loan_taken', 'date_startup_received',
                               'date_loan_taken_income_growth']
                for field_name in date_fields:
                    date_value = updated_hes_data[field_name]
                    if isinstance(date_value, str):
                        updated_hes_data[field_name] = datetime.strptime(date_value,
                                                                         '%Y-%m-%d').date() if date_value else None
                    # Else, it's already a date object, so keep it as it is

                # Update hes_instance fields
                for field_name, value in updated_hes_data.items():
                    setattr(hes_instance, field_name, value)

                hes_instance.save()  # Save the updated instance

                return redirect('view_hes', id=hes_instance.id)
            else:
                print("Form is not valid:", form.errors)

        return render(request, 'hes/edit_hes.html', context)


    except Exception as e:
        raise e


def delete_hes(request, id):
    hes_instance = get_object_or_404(CPOVC_HES, id=id, is_void=False)


    hes_instance.is_void = True
    hes_instance.save()
    url = reverse('hes_home')
    msg = "Data deleted successfully"
    messages.add_message(request, messages.INFO, msg)

    return HttpResponseRedirect(url)




