from django.db.models import Count, IntegerField
from django.db.models.functions import Cast

from cpovc_api.models import DeviceManagement
from cpovc_ovc.models import OVCRegistration

from cpovc_registry.models import RegPersonsOrgUnits
from cpovc_registry.functions import get_attached_ous, get_orgs_child
from .models import (
    OVCMobileEvent, OVCEvent, CasePlanTemplateEvent,
    CasePlanTemplateService, OVCServices)

def get_events(request):
    """Method to get events"""
    try:
        form_id = request.GET.get('form_id')
        params = {}
        evs, evs_list = {}, []
        sts = {1: 'pending', 2: 'approved', 3: 'rejected'}
        stsb = {'pending': 0, 'approved': 0, 'rejected': 0}
        all_events = 0
        all_forms = {}
        all_forms['CPR'] = {'pending': 0, 'approved': 0, 'rejected': 0}
        all_forms['CPT'] = {'pending': 0, 'approved': 0, 'rejected': 0}
        all_forms['F1A'] = {'pending': 0, 'approved': 0, 'rejected': 0}
        all_forms['F1B'] = {'pending': 0, 'approved': 0, 'rejected': 0}
        all_statuses = {'pending': 0, 'approved': 0, 'rejected': 0}
        # Limit the results to Organization Units
        admin = False
        aous = get_attached_ous(request)
        ous = get_orgs_child(aous, 1)
        if not ous:
            ous = [2]
        if request.user.is_superuser and 2 in ous:
            admin = True
        # My caseload
        caseload = OVCRegistration.objects.filter(
            child_cbo_id__in=ous, is_active=True).values('person_id')
        # CPARA
        cpara_events = OVCMobileEvent.objects.exclude(ovc_cpims_id='')
        '''
        if not admin:
            cpara_events = cpara_events.filter(ovc_cpims_id__in=caseload)
        '''
        all_cpara = cpara_events.count()
        cpara_statuses = cpara_events.values(
            'is_accepted').annotate(dc=Count('is_accepted'))
        for status in cpara_statuses:
            stid = status['is_accepted']
            stid_label = sts[stid]
            stid_label_perc = '%s_perc' % (stid_label)
            all_forms['CPR'][stid_label] = status['dc']
            all_forms['CPR'][stid_label_perc] = round((status['dc'] / all_cpara) * 100, 2)
        fss = cpara_events.filter(is_accepted=1).values(
                'date_of_event').annotate(dc=Count('date_of_event'))
        for fs in fss:
            devt = fs['date_of_event'].strftime('%Y-%m-%d')
            sevt = fs['dc']
            if devt not in evs:
                evs[devt] = {'a': 0, 'b': 0, 'c': 0, 'y': sevt, 'z': 0}
            else:
                evs[devt]['y'] = sevt
        # CPT
        cpt_events = CasePlanTemplateService.objects.all()
        all_cpt = cpt_events.count()
        cpt_statuses = cpt_events.values(
            'is_accepted').annotate(dc=Count('is_accepted'))
        for status in cpt_statuses:
            stid = status['is_accepted']
            stid_label = sts[stid]
            stid_label_perc = '%s_perc' % (stid_label)
            all_forms['CPT'][stid_label] = status['dc']
            all_forms['CPT'][stid_label_perc] = round((status['dc'] / all_cpt) * 100, 2)
        cpt_fss = cpt_events.filter(is_accepted=1).values(
                'event__date_of_event').annotate(dc=Count('event__date_of_event'))
        for fs in cpt_fss:
            devt = fs['event__date_of_event'].strftime('%Y-%m-%d')
            sevt = fs['dc']
            if devt not in evs:
                evs[devt] = {'a': 0, 'b': 0, 'c': 0, 'y': 0, 'z': sevt}
            else:
                evs[devt]['z'] = sevt
        # Services
        services = OVCServices.objects.all()
        f1a_events =  services.filter(event__form_type='F1A')
        f1b_events =  services.filter(event__form_type='F1B')
        all_f1a = f1a_events.count()
        all_f1b = f1b_events.count()

        ovc_list, ovc_alist, ovc_blist = [], [], []
        # 1A
        f1a_statuses = f1a_events.values(
            'is_accepted').annotate(dc=Count('is_accepted'))
        for status in f1a_statuses:
            stid = status['is_accepted']
            stid_label = sts[stid]
            stid_label_perc = '%s_perc' % (stid_label)
            all_forms['F1A'][stid_label] = status['dc']
            all_forms['F1A'][stid_label_perc] = round((status['dc'] / all_f1a) * 100, 2)
        f1a_fss = f1a_events.filter(is_accepted=1).values(
                'event__date_of_event').annotate(dc=Count('event__date_of_event'))
        for fs in f1a_fss:
            devt = fs['event__date_of_event'].strftime('%Y-%m-%d')
            sevt = fs['dc']
            if devt not in evs:
                evs[devt] = {'a': sevt, 'b': 0, 'c': 0, 'y': 0, 'z': 0}
            else:
                evs[devt]['a'] = sevt
        # 1B
        f1b_statuses = f1b_events.values(
            'is_accepted').annotate(dc=Count('is_accepted'))
        for status in f1b_statuses:
            stid = status['is_accepted']
            stid_label = sts[stid]
            stid_label_perc = '%s_perc' % (stid_label)
            all_forms['F1B'][stid_label] = status['dc']
            all_forms['F1B'][stid_label_perc] = round((status['dc'] / all_f1b) * 100, 2)
        f1b_fss = f1b_events.filter(is_accepted=1).values(
                'event__date_of_event').annotate(dc=Count('event__date_of_event'))
        for fs in f1b_fss:
            devt = fs['event__date_of_event'].strftime('%Y-%m-%d')
            sevt = fs['dc']
            if devt not in evs:
                evs[devt] = {'a': 0, 'b': sevt, 'c': 0, 'y': 0, 'z': 0}
            else:
                evs[devt]['b'] = sevt

        if form_id == 'CPR':
            all_events = all_cpara
            for cpara_sum in all_forms['CPR']:
                params[cpara_sum] = all_forms['CPR'][cpara_sum]
                all_statuses[cpara_sum] = all_forms['CPR'][cpara_sum]
            ovc_ids = cpara_events.exclude(ovc_cpims_id='').values(
                'is_accepted',
                cpims_id=Cast('ovc_cpims_id', IntegerField()))
            for ovc_id in ovc_ids:
                accept_id = ovc_id['is_accepted']
                if accept_id == 1:
                    ovc_list.append(ovc_id['cpims_id'])
                elif accept_id == 2:
                    ovc_alist.append(ovc_id['cpims_id'])
                elif accept_id == 3:
                    ovc_blist.append(ovc_id['cpims_id'])
        elif form_id == 'CPT':
            all_events = all_cpt
            for cpara_sum in all_forms['CPT']:
                params[cpara_sum] = all_forms['CPT'][cpara_sum]
                all_statuses[cpara_sum] = all_forms['CPT'][cpara_sum]
            ovc_ids = cpt_events.exclude(event__ovc_cpims_id='').values(
                'is_accepted',
                cpims_id=Cast('event__ovc_cpims_id', IntegerField()))
            for ovc_id in ovc_ids:
                accept_id = ovc_id['is_accepted']
                if accept_id == 1:
                    ovc_list.append(ovc_id['cpims_id'])
                elif accept_id == 2:
                    ovc_alist.append(ovc_id['cpims_id'])
                elif accept_id == 3:
                    ovc_blist.append(ovc_id['cpims_id'])
        elif form_id == 'F1A':
            all_events = all_f1a
            for cpara_sum in all_forms['F1A']:
                params[cpara_sum] = all_forms['F1A'][cpara_sum]
                all_statuses[cpara_sum] = all_forms['F1A'][cpara_sum]
            ovc_ids = f1a_events.exclude(event__ovc_cpims_id='').values(
                'is_accepted',
                cpims_id=Cast('event__ovc_cpims_id', IntegerField()))
            for ovc_id in ovc_ids:
                accept_id = ovc_id['is_accepted']
                if accept_id == 1:
                    ovc_list.append(ovc_id['cpims_id'])
                elif accept_id == 2:
                    ovc_alist.append(ovc_id['cpims_id'])
                elif accept_id == 3:
                    ovc_blist.append(ovc_id['cpims_id'])
        elif form_id == 'F1B':
            all_events = all_f1b
            for cpara_sum in all_forms['F1B']:
                params[cpara_sum] = all_forms['F1B'][cpara_sum]
                all_statuses[cpara_sum] = all_forms['F1B'][cpara_sum]
            ovc_ids = f1b_events.exclude(event__ovc_cpims_id='').values(
                'is_accepted',
                cpims_id=Cast('event__ovc_cpims_id', IntegerField()))
            for ovc_id in ovc_ids:
                accept_id = ovc_id['is_accepted']
                if accept_id == 1:
                    ovc_list.append(ovc_id['cpims_id'])
                elif accept_id == 2:
                    ovc_alist.append(ovc_id['cpims_id'])
                elif accept_id == 3:
                    ovc_blist.append(ovc_id['cpims_id'])
        else:
            # All combined
            all_events = all_cpara + all_cpt + all_f1a + all_f1b
            params['approved'] = 0
            params['pending'] = 0
            params['rejected'] = 0
            for a_form in all_forms:
                params['approved'] += all_forms[a_form]['approved']
                params['pending'] += all_forms[a_form]['pending']
                params['rejected'] += all_forms[a_form]['rejected']
            # Percentages
            params['approved_perc'] = round((params['approved'] / all_events) * 100, 2)
            params['pending_perc'] = round((params['pending'] / all_events) * 100, 2)
            params['rejected_perc'] = round((params['rejected'] / all_events) * 100, 2)

        total_events = all_cpara + all_cpt + all_f1a + all_f1b
        for ev in evs:
            if form_id == 'CPR' and evs[ev]['y'] > 0:
                evs_list.append({'x': ev, 'a': evs[ev]['a'], 'b': evs[ev]['b'],
                                 'c': evs[ev]['c'], 'y': evs[ev]['y'],
                                 'z': evs[ev]['z']})
            if form_id == 'CPT' and evs[ev]['z'] > 0:
                evs_list.append({'x': ev, 'a': evs[ev]['a'], 'b': evs[ev]['b'],
                                 'c': evs[ev]['c'], 'y': evs[ev]['y'],
                                 'z': evs[ev]['z']})
            if form_id == 'F1A' and evs[ev]['a'] > 0:
                evs_list.append({'x': ev, 'a': evs[ev]['a'], 'b': evs[ev]['b'],
                                 'c': evs[ev]['c'], 'y': evs[ev]['y'],
                                 'z': evs[ev]['z']})
            if form_id == 'F1B' and evs[ev]['b'] > 0:
                evs_list.append({'x': ev, 'a': evs[ev]['a'], 'b': evs[ev]['b'],
                                 'c': evs[ev]['c'], 'y': evs[ev]['y'],
                                 'z': evs[ev]['z']})
            else:
                evs_list.append({'x': ev, 'a': evs[ev]['a'], 'b': evs[ev]['b'],
                                 'c': evs[ev]['c'], 'y': evs[ev]['y'],
                                 'z': evs[ev]['z']})
        params['cm'] = evs_list
        # OVC LIPs
        ovcs = OVCRegistration.objects.filter(person_id__in=ovc_list)
        aovcs = OVCRegistration.objects.filter(person_id__in=ovc_blist)
        devices = DeviceManagement.objects.all()
        # By person orgs mapping and must be registration assistants
        person_ids = RegPersonsOrgUnits.objects.filter(
            org_unit_id__in=ous, reg_assistant=True,
            is_void=False).values('person_id')
        if not admin:
            ovcs = ovcs.filter(child_cbo_id__in=ous)
            devices = devices.filter(user__reg_person_id__in=person_ids)
        ovc_cbos = ovcs.filter(is_void=False).values(
                'child_cbo__org_unit_name').annotate(
                dc=Count('person_id')).order_by('-dc')
        # Devices
        
        params['dev_pending'] = devices.filter(
            is_active=False, is_blocked=False, is_void=False).count()
        params['dev_active'] = devices.filter(is_active=True).count()
        params['dev_blocked'] = devices.filter(is_blocked=True).count()
        params['dev_retired'] = devices.filter(is_void=True).count()
        # Forms - F1A / F1B
        params['cl_F1A'] = all_f1a
        params['cl_F1B'] = all_f1b
        params['cl_CPT'] = all_cpt
        params['cl_CPR'] = all_cpara
        params['events'] = all_events
        params['total_events'] = total_events
        params['cbos'] = ovc_cbos
        params['ovcs'] = ovcs
        params['aovcs'] = aovcs
        params['devices'] = devices

        # print(params)

    except Exception as e:
        raise e
    else:
    	return params