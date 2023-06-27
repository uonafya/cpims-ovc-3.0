from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse

from .forms import CaseLoad
from .functions import get_geo, get_lips, get_chart_data, get_ips, get_data
from .parameters import colors as dcolors
from .parameters import CHART
from .params import CHART as GCHART

from cpovc_settings.forms import SettingsForm


@login_required
def ovc_dashboard(request):
    """Method to do pivot reports."""
    try:
        form = CaseLoad()
        return render(
            request, 'dashboards/ovc_dashboard.html',
            {'form': form, 'colors': dcolors})
    except Exception as e:
        raise e
    else:
        pass


@login_required
def ovc_dashboard_hivstat(request):
    """Method to do pivot reports."""
    try:
        form = CaseLoad()
        return render(
            request, 'dashboards/ovc_dashboard_hivstat.html',
            {'form': form, 'colors': dcolors})
    except Exception as e:
        raise e
    else:
        pass


@login_required
def ovc_dashboard_services(request):
    """Method to do pivot reports."""
    try:
        form = CaseLoad()
        return render(
            request, 'dashboards/ovc_dashboard_services.html',
            {'form': form, 'colors': dcolors})
    except Exception as e:
        raise e
    else:
        pass


@login_required
def ovc_dashboard_cm(request):
    """Method to do pivot reports."""
    try:
        form = CaseLoad()
        return render(
            request, 'dashboards/ovc_dashboard_cm.html',
            {'form': form, 'colors': dcolors})
    except Exception as e:
        raise e
    else:
        pass


@login_required
def ovc_dashboard_perform(request):
    """Method to do pivot reports."""
    try:
        form = CaseLoad()
        return render(
            request, 'dashboards/ovc_dashboard_perform.html',
            {'form': form, 'colors': dcolors})
    except Exception as e:
        raise e
    else:
        pass


@login_required
def ovc_dashboard_registration(request):
    """Method to do pivot reports."""
    try:
        form = CaseLoad()
        return render(
            request, 'dashboards/ovc_dashboard_registration.html',
            {'form': form, 'colors': dcolors})
    except Exception as e:
        raise e
    else:
        pass


@login_required
def ovc_dashboard_MER(request):
    """Method to do pivot reports."""
    try:
        form = CaseLoad()
        return render(
            request, 'dashboards/ovc_dashboard_mer.html',
            {'form': form, 'colors': dcolors})
    except Exception as e:
        raise e
    else:
        pass


@login_required
def ovc_dashboard_epc(request):
    """Method to do pivot reports."""
    try:
        form = CaseLoad()
        return render(
            request, 'dashboards/ovc_dashboard_epc.html',
            {'form': form, 'colors': dcolors})
    except Exception as e:
        raise e
    else:
        pass


@login_required
def raw_dashboard(request, did=1):
    """Method to do pivot reports."""
    try:
        # form = CaseLoad()
        dcols = ['ID', 'OVC CPIMS ID', 'OVC Names', 'CBO ID', 'CBO',
                 'CHV CPIMS ID', 'CHV Names', 'Caregiver CPIMS ID',
                 'Caregiver Names', 'Registration Date', 'Exit status',
                 'Exit Date']
        if did == 4:
            dcols = dcols + ['Domain', 'Service', 'Event date']
        cols = dcols + ['User', 'Timestamp']
        today = datetime.now()
        primary_org_unt = request.session.get('ou_primary')
        todate = str(today.strftime("%d-%b-%Y"))
        sdata = {'report_from_date': '01-Jan-2000', 'report_to_date': todate,
                 'org_unit': primary_org_unt}
        form = SettingsForm(request.user, sdata)
        data, params = [], {'did': did}
        org_unit = request.GET.get('org_unit', 0)
        from_date = request.GET.get('from_date')
        to_date = request.GET.get('to_date')
        cluster = request.GET.get('cluster')
        print(org_unit, from_date, to_date)
        if org_unit and from_date and to_date:
            params['cluster'] = cluster
            params['org_unit'] = org_unit
            params['from_date'] = from_date
            params['to_date'] = to_date
            data = get_data(request, params)
            return JsonResponse({'data': data}, safe=False)
        return render(
            request, 'dashboards/ovc_dashboard_rawdata.html',
            {'form': form, 'colors': dcolors, 'cols': cols, 'did': did})
    except Exception as e:
        raise e
    else:
        pass


@login_required
def get_constituency(request, area_id):
    """Method to do pivot reports."""
    try:
        values = []
        geos = get_geo(area_id)
        for geo in geos:
            vls = {'id': geo.area_id, 'name': geo.area_name}
            values.append(vls)
    except Exception:
        return JsonResponse([], safe=False)
    else:
        return JsonResponse(values, safe=False)


@login_required
def get_ward(request, area_id):
    """Method to do pivot reports."""
    try:
        values = []
        geos = get_geo(area_id, 'GWRD')
        for geo in geos:
            vls = {'id': geo.area_id, 'name': geo.area_name}
            values.append(vls)
    except Exception:
        return JsonResponse([], safe=False)
    else:
        return JsonResponse(values, safe=False)


@login_required
def get_ip(request, fund_id):
    """Method to do pivot reports."""
    try:
        values = []
        ips = get_ips(fund_id)
        for ip in ips:
            vls = {'id': ip.org_unit.id, 'name': ip.org_unit.org_unit_name}
            values.append(vls)
    except Exception:
        return JsonResponse([], safe=False)
    else:
        return JsonResponse(values, safe=False)


@login_required
def get_lip(request, ip_id):
    """Method to do pivot reports."""
    try:
        values = []
        lips = get_lips(ip_id)
        for lip in lips:
            vls = {'id': lip.org_unit.id, 'name': lip.org_unit.org_unit_name}
            values.append(vls)
    except Exception:
        return JsonResponse([], safe=False)
    else:
        return JsonResponse(values, safe=False)


@login_required
def get_chart(request, rid, county_id, const_id, ward_id=0, mech_id=0,
              ip_id=0, lip_id=0, prd=0, yr=0):
    """Method to do pivot reports."""
    try:
        html = get_chart_data(request, rid, county_id, const_id, ward_id,
                              mech_id, ip_id, lip_id, prd, yr)
    except Exception as e:
        print('Chart view error - %s' % (str(e)))
        msg = 'Please change the Filters and try again.'
        return HttpResponse('<p>Error Generating Chart. %s</p>' % (msg))
    else:
        return HttpResponse(html)


@login_required
def settings(request):
    """Method to do pivot reports."""
    try:
        if request.method == 'POST':
            msg = {'status': 0, 'message': 'Settings saved successfully'}
            sel_color = int(request.POST.get('sel_color', 0))
            if sel_color:
                request.session['sel_color'] = sel_color
        else:
            msg = {'status': 1, 'message': 'Request not allowed'}
    except Exception:
        msg = {'status': 9, 'message': 'Error saving settings'}
        return JsonResponse(msg, safe=False)
    else:
        return JsonResponse(msg, safe=False)


@login_required
def ovc_dashboard_help(request):
    """Method to do pivot reports."""
    try:
        form = CaseLoad()
        charts = {}
        cats = [1, 2, 3, 4, 5, 6, 7, 8]
        for cat in cats:
            charts[cat] = []
            for cts in CHART:
                if cts.startswith(str(cat)):
                    CHART[cts]['number'] = cts
                    if cts in GCHART:
                        icts = GCHART[cts]
                        idesc = icts['desc'] if 'desc' in icts else ''
                        icalc = icts['calc'] if 'calc' in icts else ''
                        CHART[cts]['desc'] = idesc
                        CHART[cts]['calc'] = icalc
                    charts[cat].append(CHART[cts])
        return render(
            request, 'dashboards/ovc_dashboard_help.html',
            {'form': form, 'colors': dcolors, 'chart': CHART,
             'charts': charts})
    except Exception as e:
        raise e
    else:
        pass
