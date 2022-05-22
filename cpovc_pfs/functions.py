from cpovc_ovc.models import OVCEducation, OVCHealth
from cpovc_registry.models import RegPersonsOrgUnits

from cpovc_main.functions import convert_date


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
