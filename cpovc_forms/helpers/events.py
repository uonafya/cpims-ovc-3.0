from ..models import OVCHouseHold, OVCCareEvents, RegPerson
from cpovc_ovc.models import OVCHHMembers, OVCHouseHold


def save_event(request, person_id, event_name, date_of_event):
    """
    Function to save events details
    Args:
        params: person_id(int)
            event_name(str)

        Return: Primary keoy


    """
    child = RegPerson.objects.get(id=person_id)
    house_hold = OVCHouseHold.objects.get(id=OVCHHMembers.objects.get(person=child).house_hold_id)
    event_type_id = 'FCSI'
    event_counter = OVCCareEvents.objects.filter(
    event_type_id=event_type_id, person=person_id, is_void=False).count()

    ovccareevent = OVCCareEvents(
    event_type_id= event_name,
    event_counter=1,
    event_score=0,
    date_of_event= date_of_event,
    created_by=request.user.id,
    person_id = person_id,
    house_hold=house_hold
    )
    ovccareevent.save()

    return ovccareevent