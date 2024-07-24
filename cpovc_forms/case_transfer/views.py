from django.shortcuts import render
from cpovc_registry.models import (
    RegPerson, RegPersonsSiblings, RegPersonsOrgUnits)
from cpovc_ovc.models import (
    OVCRegistration, OVCHouseHold, OVCHHMembers, OVCCareEvents)
from .models import OVCCareTransfer


def case_transfer(request, id):
    try:
        init_data = RegPerson.objects.filter(pk=id)
        child = RegPerson.objects.get(id=id)
        care_giver = RegPerson.objects.get(
            id=OVCRegistration.objects.get(person=child).caretaker_id)
        house_hold = OVCHouseHold.objects.get(
            id=OVCHHMembers.objects.get(person_id=id).house_hold_id)
        siblings = RegPersonsSiblings.objects.select_related().filter(
            child_person=id, is_void=False, date_delinked=None)
        hhold = OVCHHMembers.objects.get(
            is_void=False, person_id=id)
        # Get HH members
        hhid = hhold.house_hold_id
        hhmembers = OVCHHMembers.objects.filter(
            is_void=False, house_hold_id=hhid)

        if request.method == 'POST':
            print(request.POST)
            event_id = 'FCSI'
            person_id = int(id)
            date_of_transfer = request.POST.get("TRANSFER_DATE")
            hhmembers_check = request.POST.getlist('member_id_check')
            hhmembers = request.POST.getlist('member_id')

            event_counter = OVCCareEvents.objects.filter(
                event_type_id=event_id, person=id, is_void=False).count()

            ovccareevent = OVCCareEvents(
                event_type_id=event_id,
                event_counter=event_counter,
                event_score=0,
                date_of_event=date_of_transfer,
                created_by=request.user.id,
                person_id=person_id,
                # date_of_previous_event=date_of_transfer,
                house_hold=house_hold
            )
            ovccareevent.save()
            event_id = ovccareevent.pk

            # Get organization
            organization_id = request.POST.get("ORG_UNIT")

            org_unit_id = organization_id

            for hhmember in hhmembers:
                print("hhmember", hhmember)
                index = hhmembers_check.index(hhmember)
                reason = str(request.POST.getlist("REASON")[index]),
                date_follow_up = str(
                    request.POST.getlist("FOLLOW_UP_DATE")[index])
                print(index, id, event_id, house_hold, date_of_transfer,
                      reason, date_follow_up, '^()^')

                OVCCareTransfer(
                    person_id=hhmember,
                    event_id=event_id,
                    household=house_hold,
                    rec_organization_id=org_unit_id,
                    date_of_event=date_of_transfer,
                    reason=reason,
                    date_follow_up=date_follow_up,
                    # date_of_transfer=date_of_transfer
                ).save()

                # Update child_CBO on OVCReg  &  reg-person-org-unit table
                OVCRegistration.objects.filter(person_id=id).update(
                    child_cbo=organization_id, is_void=True)
                RegPersonsOrgUnits.objects.filter(person_id=id).update(
                    org_unit_id=organization_id, is_void=True)

                msg = 'Transfer initiated successful'
                messages.add_message(request, messages.INFO, msg)
            return redirect('forms/case_transfer.html')

        else:
            caseTransferForm = CaseTransferForm()
            organization_id = OVCCareTransfer.objects.filter(person=id)

            transferedMembers = OVCCareTransfer.objects.all()
            # pdb.set_trace()
            transferedMembers_new = []

            for i in range(0, len(transferedMembers)):
                if not transferedMembers[i].is_void:
                    transferedMembers_new.append(transferedMembers[i])

            return render(
                request,
                template_name='forms/case_transfer.html',
                context={
                    'case_transfer_form': caseTransferForm,
                    'init_data': init_data,
                    'siblings': siblings,
                    'care_giver': care_giver,
                    'child': child,
                    'house_hold': house_hold,
                    'hhid': hhid,
                    'hhmembers': hhmembers,
                    'transferedMembers': transferedMembers_new,
                }
            )
    except Exception as e:
        raise e
    else:
        pass


def edit_transfer(request, id):
    case_transfers = OVCCareTransfer.objects.filter(event_id=id)
    caseTransferForm = CaseTransferForm()

    for transferedCase in case_transfers:
        reason = transferedCase.reason
        follow_up = transferedCase.date_follow_up
        person = transferedCase.person_id
        household = transferedCase.household_id
        date_of_transfer = transferedCase.date_of_event

        # pdb.set_trace()
        if request.method == 'POST':
            print(request.POST)

            OVCCareTransfer.objects.filter(event_id=id).update(
                rec_organization_id=request.POST.get("ORG_UNIT"),
                person_id=person,
                household_id=household,
                date_of_event=date_of_transfer,
                reason=reason,
                date_follow_up=follow_up,
            )

            msg = 'Transfer initiated successful'
            messages.add_message(request, messages.INFO, msg)
            return render(request, 'forms/case_transfer.html')
        else:
            return render(
                request,
                template_name='forms/edit_transfer.html',
                context={
                    'case_transfers': case_transfers,
                    'case_transfer_form': caseTransferForm,
                    'reason': reason.strip(")(,'"),
                    'follow_up': follow_up
                }
            )


def delete_transfer(request):
    transfer_id = request.GET.get('transfer_id')
    case_transfer = OVCCareTransfer.objects.filter(
        transfer_id=transfer_id).update(is_void=True)
    # currentOrg = object.rec_organization_id
    # previousOrg = OVCCareTransfer.objects.get(rec_organization_id=id)

    case_transfer = OVCCareTransfer.objects.get(transfer_id=transfer_id)
    deleted = case_transfer.is_void
    if deleted:
        # OVCCareTransfer.objects.filter(transfer_id=transfer_id).update(rec_organization_id=previousOrg)
        data = {
            'deleted': True
        }

        return JsonResponse(data)
    data = {
        'deleted': False
    }
    return JsonResponse(data)
