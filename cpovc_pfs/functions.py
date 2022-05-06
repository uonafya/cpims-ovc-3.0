from cpovc_ovc.models import OVCEducation


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
