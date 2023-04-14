"""OVC common methods."""
import datetime
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.db.models import Q
from django.db import connection
from .models import (
    OVCRegistration, OVCHouseHold, OVCHHMembers, OVCHealth, OVCEligibility,
    OVCFacility, OVCSchool, OVCEducation, OVCExit, OVCViralload)
from cpovc_registry.models import (
    RegPerson, RegOrgUnit, RegPersonsTypes, OVCCheckin,
    RegPersonsExternalIds, RegPersonsOrgUnits)
from cpovc_main.functions import convert_date, get_days_difference
from cpovc_registry.functions import (
    extract_post_params, save_person_extids, get_attached_ous,
    get_orgs_child, get_specific_orgs)
from cpovc_main.models import SetupList

from django.contrib import messages


def get_checkins(user_id):
    """Method to get all checkins."""
    try:
        chs, cnt = '', 0
        checkins = OVCCheckin.objects.filter(
            user_id=user_id).order_by("-timestamp_created")
        cins = []
        for checkin in checkins:
            cnt += 1
            time_diff = get_timediff(checkin.timestamp_created)
            t_diff = '%s ago' % (time_diff)
            chs = '<a href="/ovcare/ovc/view/%s/">' % (checkin.person_id)
            chs += '<button type="button" class="btn btn-primary">'
            chs += ' View OVC</button></a>'
            chs += ' <button type="button" class="btn btn-danger'
            chs += ' removecheckin" id="%s">' % (checkin.person_id)
            chs += ' Remove</button></a>'
            chd = {'ovc_id': checkin.person_id, 'ctime': t_diff,
                   'ovc_name': checkin.person.full_name, 'caction': chs}
            cins.append(chd)
    except Exception as e:
        print('error getting checkins - %s' % (str(e)))
        return "", 0
    else:
        return cins, cnt


def get_school(ovc_id):
    """Method to get school details."""
    try:
        school = OVCEducation.objects.get(person_id=ovc_id, is_void=False)
    except Exception as e:
        print('No school details - %s' % (str(e)))
        return None
    else:
        return school


def get_health(ovc_id):
    """Method to get health details."""
    try:
        health = OVCHealth.objects.get(person_id=ovc_id)
    except Exception as e:
        print('No health details - %s' % (str(e)))
        return None
    else:
        return health


def search_ovc(request):
    """Method to search OVC as per USG."""
    try:
        ous = []
        name = request.POST.get('search_name')
        criteria = request.POST.get('search_criteria')
        exited = request.POST.get('person_exited')
        is_exited = True if exited else False
        # Limit permissions
        aous = get_attached_ous(request)
        ous = get_orgs_child(aous, 1)
        cid = int(criteria)
        cbos, pids, chvs = [], [], []
        designs = ['COVC', 'CGOC']
        if cid in [2, 3, 4]:
            queryset = None
        else:
            queryset = RegPerson.objects.filter(
                is_void=False, designation__in=designs)
        field_names = ['surname', 'first_name', 'other_names']
        q_filter = Q()
        # 1: Names, 2: HH, 3: CHV, 4: CBO
        names = name.split()
        cids = []
        if cid == 0:
            for nm in names:
                for field in field_names:
                    q_filter |= Q(**{"%s__icontains" % field: name})
                pids = queryset.filter(q_filter).values_list(
                    'id', flat=True)
        elif cid == 1:
            pids = []
            query = ("SELECT id FROM reg_person WHERE to_tsvector"
                     "(first_name || ' ' || surname || ' '"
                     " || COALESCE(other_names,''))"
                     " @@ to_tsquery('english', '%s') AND is_void=False"
                     " ORDER BY date_of_birth DESC")
            # " OFFSET 10 LIMIT 10")
            vals = ' & '.join(names)
            sql = query % (vals)
            print(sql)
            with connection.cursor() as cursor:
                cursor.execute(sql)
                row = cursor.fetchall()
                pids = [r[0] for r in row]
            # print 'cids', pids
        elif cid == 2:
            pids = OVCHHMembers.objects.filter(
                is_void=False,
                house_hold__head_identifier__iexact=name).values_list(
                'person_id', flat=True)
        elif cid == 3:
            chv_ids = RegPersonsTypes.objects.filter(
                is_void=False, person_type_id='TWVL').values_list(
                'person_id', flat=True)
            queryset = RegPerson.objects.filter(
                is_void=False, id__in=chv_ids)
            for nm in names:
                for field in field_names:
                    q_filter |= Q(**{"%s__icontains" % field: nm})
            chvs = queryset.filter(q_filter).values_list(
                'id', flat=True)
        elif cid == 4:
            cbos = RegOrgUnit.objects.filter(
                is_void=False, org_unit_name__icontains=name).values_list(
                'id', flat=True)
        elif cid == 5:
            query = ("SELECT id FROM reg_person WHERE to_tsvector"
                     "(first_name || ' ' || surname || ' ' || other_names)"
                     " @@ to_tsquery('english', '%s') AND designation = 'CCGV'"
                     " ORDER BY date_of_birth DESC")
            vals = ' & '.join(names)
            sql = query % (vals)
            with connection.cursor() as cursor:
                cursor.execute(sql)
                row = cursor.fetchall()
                cids = [r[0] for r in row]
        elif cid == 6:
            pids = RegPerson.objects.filter(
                id=name, is_void=False).values_list('id', flat=True)

        else:
            for nm in names:
                for field in field_names:
                    q_filter |= Q(**{"%s__icontains" % field: name})
                pids = queryset.filter(q_filter).values_list(
                    'id', flat=True)
        # Query ovc table
        if is_exited:
            qs = OVCRegistration.objects.filter(is_void=False)
        else:
            qs = OVCRegistration.objects.filter(
                is_void=False, is_active=True)
        if not request.user.is_superuser:
            qs = qs.filter(child_cbo_id__in=ous)
        pst, plen = 0, 1000
        if cbos:
            ovcs = qs.filter(child_cbo_id__in=cbos)[pst:plen]
        elif chvs:
            ovcs = qs.filter(child_chv_id__in=chvs)[pst:plen]
        elif cids:
            ovcs = qs.filter(caretaker_id__in=cids)[pst:plen]
        else:
            ovcs = qs.filter(person_id__in=pids)[pst:plen]
    except Exception as e:
        print('Error searching for OVC - %s' % (str(e)))
        return {}
    else:
        return ovcs


def search_master(request):
    """Method to query existing customers."""
    try:
        results = []
        query_id = int(request.GET.get('id'))
        query = request.GET.get('q')
        school_level = request.GET.get('level')
        # Filters for external ids
        if query_id == 1:
            agents = OVCFacility.objects.filter(
                facility_name__icontains=query, is_void=False)
            for agent in agents:
                name = agent.facility_name
                agent_id = agent.id
                val = {'id': agent_id, 'label': name,
                       'value': name}
                results.append(val)
        elif query_id == 2:
            agents = OVCSchool.objects.filter(
                school_name__icontains=query,
                school_level=school_level, is_void=False)
            for agent in agents:
                name = agent.school_name
                agent_id = agent.id
                val = {'id': agent_id, 'label': name,
                       'value': name}
                results.append(val)
        elif query_id == 3:
            agents = RegOrgUnit.objects.filter(
                org_unit_name__icontains=query, is_void=False)
            for agent in agents:
                name = agent.org_unit_name
                agent_id = agent.id
                val = {'id': agent_id, 'label': name,
                       'value': name}
                results.append(val)
        elif query_id == 4:
            setup_lists = SetupList.objects.filter(item_id=query)
            if setup_lists:
                sub_cat_id = setup_lists[0].item_sub_category
                print('Sub cat', sub_cat_id)
                agents = SetupList.objects.filter(
                    field_name=sub_cat_id, is_void=False)
                for agent in agents:
                    name = agent.item_description
                    sub_cat = agent.item_sub_category
                    agent_id = agent.item_id
                    val = {'id': agent_id, 'label': name,
                           'value': name, 'sub_category': sub_cat}
                    results.append(val)
    except Exception as e:
        print('error searching master list - %s' % (str(e)))
        return []
    else:
        return results


def get_hh_members(ovc_id, hh_id=None):
    """Method to get child chv details."""
    try:
        if hh_id:
            ovc_detail = get_list_or_404(
                OVCHHMembers, person_id=ovc_id,
                house_hold_id=hh_id, is_void=False)
        else:
            ovc_detail = get_list_or_404(
                OVCHHMembers, person_id=ovc_id, is_void=False)
    except Exception as e:
        print('error getting ovc hh members - %s' % (str(e)))
        return []
    else:
        return ovc_detail


def get_ovcdetails(ovc_id):
    """Method to get child chv details."""
    try:
        ovc_detail = get_object_or_404(
            OVCRegistration, person_id=ovc_id, is_void=False)
    except Exception as e:
        print('error getting ovc details - %s' % (str(e)))
        return {}
    else:
        return ovc_detail


def ovc_registration(request, ovc_id, edit=0):
    """Method to complete ovc registration."""
    try:
        status_id = 0
        msg = "OVC Registration completed successfully"
        min_date = convert_date('01-Jan-1900')
        reg_date = request.POST.get('reg_date')
        reg_date = convert_date(reg_date)
        if reg_date < min_date:
            reg_date = min_date
        bcert = request.POST.get('has_bcert')
        disabled = request.POST.get('disb')
        hh_members = request.POST.getlist('hh_member')
        cbo_id = request.POST.get('cbo_id')
        has_bcert = True if bcert else False
        is_disabled = True if disabled else False

        bcert_no = request.POST.get('bcert_no')
        ncpwd_no = request.POST.get('ncpwd_no')
        dreams_id = request.POST.get('dreams_id')
        ext_ids = {}
        if bcert_no:
            ext_ids['ISOV'] = bcert_no
        if ncpwd_no:
            ext_ids['IPWD'] = ncpwd_no
        if dreams_id:
            ext_ids['IDRM'] = dreams_id
        if ext_ids:
            save_person_extids(ext_ids, ovc_id)

        hiv_status = request.POST.get('hiv_status')
        immmune = request.POST.get('immunization')
        org_uid = request.POST.get('cbo_uid')
        org_uid_check = request.POST.get('cbo_uid_check')
        caretaker = request.POST.get('caretaker')
        school_level = request.POST.get('school_level')
        is_exited = request.POST.get('is_exited')
        exit_reason = request.POST.get('exit_reason')
        criterias = request.POST.getlist('eligibility')
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        exit_date = request.POST.get('exit_date')
        ovc_detail = get_object_or_404(OVCRegistration, person_id=ovc_id)
        # HIV status update only if unknown
        ovc_dob = ovc_detail.person.date_of_birth
        if edit == 0:
            edit_hiv = True
            cbo_uid = gen_cbo_id(cbo_id, ovc_id)
            org_cid = cbo_uid if org_uid == org_uid_check else org_uid
            ovc_detail.hiv_status = str(hiv_status)
            nhiv_status = str(hiv_status)
            ohiv_status = str(hiv_status)
        else:
            org_cid = org_uid
            nhiv_status = str(hiv_status)
            ohiv_status = ovc_detail.hiv_status
            edit_hiv = True
            if ohiv_status == 'HSTP' and nhiv_status != 'HSTP':
                edit_hiv = False
            elif nhiv_status == 'HHEI' and ohiv_status != 'HHEI':
                edit_hiv = True
                if nhiv_status == 'HSTP':
                    edit_hiv = False
            elif ohiv_status == 'HHEI' and nhiv_status != 'HHEI':
                edit_hiv = True
                if nhiv_status == 'HSKN':
                    edit_hiv = False
        if request.user.is_staff:
            edit_hiv = True
        if edit_hiv:
            ovc_detail.hiv_status = nhiv_status
        is_active = False if is_exited else True
        ovc_detail.has_bcert = has_bcert
        ovc_detail.is_disabled = is_disabled
        ovc_detail.immunization_status = str(immmune)
        ovc_detail.org_unique_id = org_cid
        ovc_detail.caretaker_id = caretaker
        ovc_detail.school_level = school_level
        ovc_detail.is_active = is_active
        ovc_detail.exit_reason = exit_reason
        # Validate changes in Registration/Exit dates
        create_date = ovc_detail.created_at
        reg_year = reg_date.year
        days_diff = get_days_difference(reg_date)
        days_diff2 = dates_difference(create_date, reg_date)
        days_diff3 = dates_difference(ovc_dob, reg_date)
        # Diff dates checks
        ui_reg_date_str = str(reg_date.date())
        db_reg_date_str = str(ovc_detail.registration_date)
        reg_check = True if ui_reg_date_str != db_reg_date_str else False
        print('REG CHECK', reg_date, ovc_detail.registration_date, reg_check)
        allowed_reg = True
        if days_diff < 0:
            allowed_reg = False
            msg = 'Future date (%s) of registration not allowed' % (reg_date)
        elif days_diff2 > 28 and reg_year > 1900 and reg_check:
            allowed_reg = False
            msg = 'Registration date (%s) is ' % (reg_date)
            msg += 'more than 28 days from system date and is NOT allowed'
        elif days_diff3 > 0:
            allowed_reg = False
            msg = 'Registration date (%s) is before OVC DOB.' % (reg_date)
        if allowed_reg:
            ovc_detail.registration_date = reg_date
        else:
            status_id = 1
        if exit_reason:
            ovc_detail.exit_date = exit_date
        ovc_detail.save(
            update_fields=["registration_date", "has_bcert", "is_disabled",
                           "immunization_status", "org_unique_id",
                           "caretaker_id", "school_level", "hiv_status",
                           "is_active", "exit_reason", "exit_date"])
        # Update eligibility
        OVCEligibility.objects.filter(person_id=ovc_id).update(is_void=True)
        for criteria_id in criterias:
            eligibility, created = OVCEligibility.objects.update_or_create(
                person_id=ovc_id, criteria=criteria_id, is_void=False,
                defaults={'person_id': ovc_id, 'criteria': criteria_id},)
        # Update Health status
        if hiv_status in ['HSTP', 'HHEI'] and edit_hiv:
            facility = request.POST.get('facility_id')
            art_status = request.POST.get('art_status')
            link_date = request.POST.get('link_date')
            date_linked = convert_date(link_date)
            ccc_no = request.POST.get('ccc_number')
            if facility and art_status and date_linked and ccc_no:
                health, created = OVCHealth.objects.update_or_create(
                    person_id=ovc_id,
                    defaults={'facility_id': facility,
                              'art_status': art_status,
                              'date_linked': date_linked, 'ccc_number': ccc_no,
                              'is_void': False},)
        # Delete linkage details
        hiv_stats = ['HSTP', 'HHEI']
        if ohiv_status in hiv_stats and nhiv_status not in hiv_stats:
            try:
                hhealth = get_object_or_404(OVCHealth, person_id=ovc_id)
                hhealth.is_void = True
                hhealth.save(update_fields=["is_void"])
            except Exception:
                print('No existing linkage details')
            # Delete viral load - Feb 2023
            try:
                vls = get_object_or_404(OVCViralload, person_id=ovc_id)
                vls.is_void = True
                vls.save(update_fields=["is_void"])
            except Exception:
                print('No Viral load data available')
        # Update School details
        if school_level != 'SLNS':
            school_id = request.POST.get('school_id')
            school_class = request.POST.get('school_class')
            school_adm = request.POST.get('admission_type')
            if school_id and school_class and school_adm:
                OVCEducation.objects.filter(
                    person_id=ovc_id).update(is_void=True)
                health, created = OVCEducation.objects.update_or_create(
                    person_id=ovc_id, school_class=school_class,
                    defaults={'person_id': ovc_id,
                              'school_id': school_id,
                              'school_level': school_level,
                              'school_class': school_class,
                              'admission_type': school_adm,
                              'is_void': False},)
        # cgs = extract_post_params(request, naming='cg_')
        hhrs = extract_post_params(request, naming='hhr_')
        # Alive status, HIV status and Death cause for Guardian
        ast = extract_post_params(request, naming='astatus_')
        hst = extract_post_params(request, naming='gstatus_')
        cst = extract_post_params(request, naming='cstatus_')
        # Alive status, HIV status and Death cause for Sibling
        sast = extract_post_params(request, naming='sastatus_')
        shst = extract_post_params(request, naming='sgstatus_')
        todate = timezone.now()
        if edit == 0:
            # Create House Hold and populate members

            # caretaker_id = int(cgs[caretaker][0])
            # hhid=get_house_hold(caretaker_id)
            caretaker_id = int(caretaker)
            hhid = get_first_household(caretaker_id)

            print(("CareTaker ID--->", caretaker_id))
            print(("HouseHold ID-->", hhid))
            if not hhid:
                print("I don't have household ID.")
                new_hh = OVCHouseHold(
                    head_person_id=caretaker,
                    head_identifier=caretaker_id
                )
                new_hh.save()
                hh_id = new_hh.pk
                # Duplicate Fix
                # new_hh = OVCHouseHold(
                # head_person_id=caretaker,
                # head_identifier=caretaker_id),
                # new_hh.save()
                # hh_id = new_hh.pk

            else:
                print("I do have household ID.")
                hh_id = hhid.id
                print(hh_id)
            # Add members to HH
            hh_members.append(ovc_id)
            for hh_m in hh_members:
                oid = int(ovc_id)
                hh_head = True if int(hh_m) == caretaker_id else False
                m_type = hhrs[hh_m][0] if hh_m in hhrs else 'TBVC'
                member_type = 'TOVC' if oid == int(hh_m) else m_type
                if member_type == 'TBVC' or member_type == 'TOVC':
                    hh_hiv = shst[hh_m][0] if hh_m in shst else None
                    hh_alive = sast[hh_m][0] if hh_m in sast else 'AYES'
                    hh_death = None
                else:
                    hh_hiv = hst[hh_m][0] if hh_m in hst else None
                    hh_alive = ast[hh_m][0] if hh_m in ast else 'AYES'
                    hh_death = cst[hh_m][0] if hh_m in cst else None
                if oid == hh_m:
                    hh_hiv, hh_alive, hh_death = hiv_status, 'AYES', None

                membership = get_hh_members(hh_m, hh_id)
                print('membership', membership)
                if not membership:
                    OVCHHMembers(
                        house_hold_id=hh_id, person_id=hh_m,
                        hh_head=hh_head, member_type=member_type,
                        death_cause=hh_death, member_alive=hh_alive,
                        hiv_status=hh_hiv, date_linked=todate).save()
        else:
            # Update HH details
            hhid = request.POST.get('hh_id')
            # caretaker_id = cgs[caretaker][0]
            caretaker_id = int(caretaker)  # Fix
            hh_detail = get_object_or_404(OVCHouseHold, id=hhid)
            hh_detail.head_person_id = caretaker
            hh_detail.head_identifier = caretaker_id
            hh_detail.save(update_fields=["head_identifier", "head_person"])
            # Update HH Members
            for hh_m in hhrs:
                oid = int(ovc_id)
                hh_head = True if hh_m == caretaker else False
                member_type = hhrs[hh_m][0]
                if member_type == 'TBVC' or member_type == 'TOVC':
                    hh_hiv = shst[hh_m][0] if hh_m in shst else None
                    hh_alive = sast[hh_m][0] if hh_m in sast else 'AYES'
                    hh_death = None
                else:
                    hh_hiv = hst[hh_m][0] if hh_m in hst else None
                    hh_alive = ast[hh_m][0] if hh_m in ast else 'AYES'
                    hh_death = cst[hh_m][0] if hh_m in cst else None
                if oid == hh_m:
                    hh_hiv, hh_alive, hh_death = hiv_status, 'AYES', None
                hhm, created = OVCHHMembers.objects.update_or_create(
                    person_id=hh_m, house_hold_id=hhid, is_void=False,
                    defaults={'person_id': hh_m, 'hh_head': hh_head,
                              'member_type': member_type,
                              'death_cause': hh_death,
                              'member_alive': hh_alive,
                              'date_linked': todate, 'hiv_status': hh_hiv},)
    except Exception as e:
        msg = 'Error updating OVC ID: %s - %s' % (ovc_id, str(e))
        return {'status_id': 9, 'status_msg': msg}
    else:
        return {'status_id': status_id, 'status_msg': msg}


def get_timediff(create_time):
    """Get time differences."""
    tnow = timezone.now()

    td = tnow - create_time
    days = td.days
    hours = td.seconds // 3600
    minutes = (td.seconds // 60) % 60
    if days > 0:
        return '%s days' % (days)
    elif hours > 0:
        return '%s hours' % (hours)
    else:
        return '%s minutes' % (minutes)


def gen_cbo_id(cbo_id, ovc_id):
    """Invoice validations."""
    try:
        last_id = OVCRegistration.objects.filter(
            child_cbo_id=cbo_id).exclude(org_unique_id__isnull=True).order_by(
            'org_unique_id').last()
        if not last_id:
            return '00001'
        lid = last_id.org_unique_id
        if lid and lid.isnumeric():
            new_id = str(int(lid) + 1).zfill(5)
        else:
            if lid:
                new_id = '%sX' % (lid[:-1])
            else:
                '0000X'
        return new_id
    except Exception as e:
        raise e
    else:
        pass


def get_house_hold(person_id):
    """Method to get household id."""
    try:
        hh_detail = get_object_or_404(
            OVCHouseHold, head_person_id=person_id)
        print(("Get HouseHold Function Detail->", hh_detail))
    except Exception as e:
        print('error getting hh - %s' % (str(e)))
        return None
    else:
        print(("Return GetHouseHold Func", hh_detail))
        return hh_detail


def get_first_household(person_id):
    """A fix for duplication-Method to get household
       list and return just one """
    try:
        hh_details = get_list_or_404(
            OVCHouseHold, head_person_id=person_id)
        # Gets the last item in the list  (First household)
        hh_detail = hh_details[-1]
    except Exception as e:
        print('error getting hh - %s' % (str(e)))
        return None
    else:
        return hh_detail  # Return only one household


def get_hh_membership(person_id):
    try:
        member = get_object_or_404(OVCHHMembers, person_id=person_id)

    except Exception:
        return None

    else:
        return member


def manage_checkins(request, gid=0):
    """Method to handle checkins."""
    try:
        chs, ovc_ids = '', []
        org_unit_id = None
        ovcid = request.POST.get('ovc_id')
        aid = request.POST.get('id')
        ovcids = request.POST.getlist('ovc_id[]')
        act_id = int(aid) if aid else 0
        action_id = gid if gid else act_id
        user_id = request.user.id
        if ovcid:
            ovc_ids = [ovcid]
        elif ovcids:
            ovc_ids = ovcids
        if action_id == 1:
            if 'ou_primary' in request.session:
                ou_id = request.session['ou_primary']
                org_unit_id = int(ou_id) if ou_id else None
            cnt = 0
            for ovc_id in ovc_ids:
                cnt += 1
                checkin, created = OVCCheckin.objects.update_or_create(
                    person_id=ovc_id, user_id=user_id,
                    defaults={'person_id': ovc_id, 'user_id': user_id,
                              'org_unit_id': org_unit_id},)
            msg = 'OVC (%s) checked in successfully.' % (str(cnt))
        elif action_id == 2:
            chs, cnt = get_checkins(user_id)
            msg = 'OVC checked in returned %s results.' % (cnt)
        elif action_id == 3:
            ovcid = request.POST.get('ovc_out_id')
            # chs, cnt = get_checkins(user_id)
            ovcs = OVCCheckin.objects.filter(person_id=ovcid)
            for ovc in ovcs:
                ovc.delete()
            msg = 'OVC checked out successfully.'
    except Exception as e:
        print('error handling checkins - %s' % (str(e)))
        return msg, 0
    else:
        return msg, chs


def ovc_management(request):
    try:
        msg = 'Successful'
        action_id = int(request.POST.get('action'))
        if action_id == 2:
            msg = perform_exit(request)
        elif action_id == 3:
            msg = save_viral_load(request)
        messages.add_message(request, messages.INFO, msg)
    except Exception as e:
        msg = 'Error - %s' % str(e)
        return msg
    else:
        return msg


def perform_exit(request):
    try:
        msg = 'Exit saved successfully'
        ovcid = request.POST.get('ovc_id')
        exit_date = convert_date(request.POST.get('exit_date'))
        exit_reason = request.POST.get('exit_reason')
        exit_org_name = request.POST.get('exit_org_name')
        # Today's date
        days_diff = get_days_difference(exit_date)
        month_exit = exit_date.month
        ovc_details = OVCRegistration.objects.get(person_id=ovcid)
        db_exit_date = ovc_details.exit_date
        ui_exit_date_str = str(exit_date.date())
        db_exit_date_str = str(db_exit_date) if db_exit_date else ''
        exit_check = True if ui_exit_date_str != db_exit_date_str else False
        print('Days diff, month', days_diff, month_exit)
        allow_exit = True
        if days_diff > 90:
            allow_exit = False
            msg = 'Exit not allowed after 90 days'
        elif days_diff < 0:
            allow_exit = False
            msg = 'Exit not allowed in future dates'
        elif exit_check and db_exit_date_str:
            allow_exit = False
            msg = 'Change of exit dates not allowed'
        if allow_exit or request.user.is_superuser:
            ovc_details.exit_date = exit_date
            ovc_details.exit_reason = exit_reason
            if exit_org_name:
                # ovc_details.exit_org_name = exit_org_name
                org, created = OVCExit.objects.update_or_create(
                    person_id=ovcid,
                    defaults={'person_id': ovcid,
                              'org_unit_name': exit_org_name},)
            ovc_details.is_active = False
            ovc_details.save(
                update_fields=["exit_date", "exit_reason", "is_active"])
    except Exception as e:
        msg = 'error exiting - %s' % (str(e))
        print(msg)
        return msg
    else:
        return msg


def get_exit_org(ovc_id):
    """Method to get exit organization."""
    try:
        org = OVCExit.objects.get(is_void=False, person_id=ovc_id)
    except Exception as e:
        print('No org details - %s' % (str(e)))
        return ''
    else:
        return org.org_unit_name


def save_viral_load(request):
    try:
        msg = ' Viral load saved successful'
        ovcid = request.POST.get('ovc_id')
        viral_date = convert_date(request.POST.get('viral_date'))
        ldl = request.POST.get('ldl')
        viral_value = request.POST.get('viral_value')
        viral_load = None if ldl == 'true' else viral_value
        # OVC Viral load
        org, created = OVCViralload.objects.update_or_create(
            person_id=ovcid, viral_date=viral_date,
            defaults={'person_id': ovcid, 'viral_load': viral_load},)
    except Exception as e:
        print('error exiting - %s' % (str(e)))
        return 'error'
    else:
        return msg


def method_once(method):
    "A decorator that runs a method only once."
    attrname = "_%s_once_result" % id(method)

    def decorated(self, *args, **kwargs):
        try:
            return getattr(self, attrname)
        except AttributeError:
            setattr(self, attrname, method(self, *args, **kwargs))
            return getattr(self, attrname)
    return decorated


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


def save_hh_info(request, person_id):
    """Method to save HH additional info."""
    try:
        dob = request.POST.get('date_of_birth')
        date_of_birth = convert_date(dob)
        phone_number = request.POST.get('mobile_number')[-9:]
        person = RegPerson.objects.get(id=person_id)
        person.date_of_birth = date_of_birth
        person.des_phone_number = phone_number
        person.save()
        # Other additional information
        national_id = request.POST.get('id_number')
        education_level = request.POST.get('education_level')
        id_types = {}
        id_types['INTL'] = national_id
        id_types['IHLE'] = education_level
        save_person_extids(id_types, person_id)
    except Exception as e:
        raise e
    else:
        pass


def get_extra_info(person_id):
    """Method to get extra info."""
    try:
        person = PersonObj()
        extras = RegPersonsExternalIds.objects.filter(
            person_id=person_id, is_void=False)
        person.education_level = 'N/A'
        for extid in extras:
            id_type = extid.identifier_type_id
            id_detail = extid.identifier
            setattr(person, id_type, id_detail)
    except Exception:
        return {}
    else:
        return person


def limit_person_ids_orgs(request, pids):
    """Method to limit searched ID to org units and CBOs."""
    try:
        ous = []
        user_person_id = request.user.reg_person_id
        if not request.user.is_superuser:
            org_units = get_specific_orgs(user_person_id)
            for org_unit in org_units:
                ou_id, ou_name = org_unit
                if ou_id:
                    ous.append(ou_id)
            pids = RegPersonsOrgUnits.objects.filter(
                person_id__in=pids, is_void=False,
                org_unit_id__in=ous).values_list('person_id')
    except Exception as e:
        print('Person filter error - %s' % (str(e)))
        return []
    else:
        return pids


def dates_difference(event_date, from_date=None):
    """method to get days difference."""
    try:
        fmt = '%d-%b-%Y'
        if not from_date:
            from_date = datetime.datetime.now()
        # ev_date = convert_date(event_date)
        if isinstance(event_date, datetime.datetime):
            ev_date = event_date.date()
        elif isinstance(event_date, datetime.date):
            ev_date = event_date
        else:
            edate = datetime.datetime.strptime(event_date, fmt)
            ev_date = edate.date()
        ev_diff = ev_date - from_date.date()
        diff_days = ev_diff.days
    except Exception as e:
        print('Error - %s' % str(e))
        return 0
    else:
        return diff_days


class PersonObj(object):
    pass

