from django.utils import timezone

from cpovc_registry.models import RegPersonsOrgUnits
from cpovc_ovc.models import (
    OVCEducation, OVCHealth, OVCHHMembers, OVCHouseHold)

from cpovc_main.functions import convert_date
from cpovc_ovc.functions import get_first_household


def save_school(request, person_id, school_level='SLNS'):
    # Update School details
    try:
        created = None
        if school_level != 'SLNS':
            school_id = request.POST.get('school_id')
            school_class = request.POST.get('school_class')
            school_adm = request.POST.get('admission_type')
            if school_id and school_class and school_adm:
                OVCEducation.objects.filter(
                    person_id=person_id).update(is_void=True)
                obj, created = OVCEducation.objects.update_or_create(
                    person_id=person_id, school_level=school_level,
                    defaults={'school_id': school_id,
                              'school_class': school_class,
                              'admission_type': school_adm, 'is_void': False})
    except Exception as e:
        raise e
    else:
        return created


def get_person_org_unit(request, person_id):
    """ Method to get attached org unit."""
    try:
        ou_id = 0
        person = RegPersonsOrgUnits.objects.filter(
            person_id=person_id, is_void=False).first()
        if person:
            ou_id = person.org_unit_id
    except Exception as e:
        print('Error getting person org unit - %s' % (e))
        return 0
    else:
        return ou_id


def save_health(request, person_id):
    """Method to save health details."""
    try:
        facility_id = request.POST.get('facility_id')
        art_status = request.POST.get('art_status')
        link_date = request.POST.get('link_date')
        date_linked = convert_date(link_date)
        ccc_no = request.POST.get('ccc_number')
        health, created = OVCHealth.objects.update_or_create(
            person_id=person_id,
            defaults={'facility_id': facility_id, 'art_status': art_status,
                      'date_linked': date_linked, 'ccc_number': ccc_no,
                      'is_void': False},)
    except Exception as e:
        raise e
    else:
        pass


def save_household(request, caregiver_id, ovc_id, hh_members=[]):
    """Method to create Households."""
    try:
        todate = timezone.now()
        oid = int(ovc_id)
        caretaker_id = int(caregiver_id)
        hhid = get_first_household(caretaker_id)
        if not hhid:
            new_hh = OVCHouseHold(
                head_person_id=caretaker_id,
                head_identifier=caretaker_id
            )
            new_hh.save()
            hh_id = new_hh.pk
        else:
            print("I do have household ID.")
            hh_id = hhid.id
        # Add members to HH
        hh_members.append(ovc_id)
        for hh_m in hh_members:
            hh_head = True if int(hh_m) == caretaker_id else False
            member_type = 'TOVC' if oid == int(hh_m) else 'TBVC'
            hiv_status, member_alive, death_cause = None, 'AYES', None

            membership, created = OVCHHMembers.objects.update_or_create(
                house_hold_id=hh_id, person_id=hh_m,
                defaults={'hh_head': hh_head, 'member_type': member_type,
                          'death_cause': death_cause,
                          'member_alive': member_alive,
                          'hiv_status': hiv_status, 'date_linked': todate,
                          'is_void': False},)
    except Exception as e:
        raise e
    else:
        pass


def get_house_hold(request, person_id):
    """Method to get a house hold."""
    try:
        member = OVCHHMembers.objects.get(person_id=person_id, is_void=False)
        hh = OVCHouseHold.objects.get(id=member.house_hold_id)
    except Exception as e:
        print('Error getting HH based on a member - %s' % (str(e)))
        return None
    else:
        return hh
