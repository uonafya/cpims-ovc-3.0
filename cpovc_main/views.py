import memcache
from datetime import datetime, timedelta
from django.shortcuts import render
from django.http import JsonResponse
from cpovc_registry.functions import dashboard, ovc_dashboard, get_public_dash_ovc_hiv_status, \
    get_ovc_hiv_status, fetch_locality_data, fetch_total_ovc_ever, fetch_total_ovc_ever_exited, \
    fetch_total_wout_bcert_at_enrol, get_cbo_list, get_ever_tested_for_HIV, _get_ovc_active_hiv_status, \
    _get_ovc_served_stats, fetch_total_w_bcert_2date, fetch_total_s_bcert_aft_enrol, fetch_new_ovcregs_by_period, \
    fetch_exited_hsehlds_by_period, fetch_exited_ovcs_by_period, fetch_served_bcert_by_period, \
    fetch_u5_served_bcert_by_period
from cpovc_main.functions import get_dict
from django.contrib.auth.decorators import login_required

mc = memcache.Client(['127.0.0.1:11211'], debug=0)


def public_dash(request):
    """Some default page for the home page / Dashboard."""
    try:
        print("we are here")
        # vals = get_dashboard(request)
        return render(request, 'public_dash.html')
    except Exception as e:
        print(('dashboard error - %s' % (str(e))))
        raise e


# #################### Dash
def public_dashboard_reg(request):
    try:
        print("we are here")
        # vals = get_dashboard(request)
        # return render(request, 'public_dash_' + p_dash + '.html')
        return render(request, 'public_dash/reg.html')
    except Exception as e:
        print(('dashboard error - %s' % (str(e))))
        raise e


def public_dashboard_hivstat(request):
    try:
        print("we are here")
        # vals = get_dashboard(request)
        # return render(request, 'public_dash_' + p_dash + '.html')
        return render(request, 'public_dash/hivstat.html')
    except Exception as e:
        print('dashboard error - %s' % (str(e)))
        raise e


def public_dashboard_served(request):
    try:
        print("we are here")
        # vals = get_dashboard(request)
        # return render(request, 'public_dash_' + p_dash + '.html')
        return render(request, 'public_dash/served.html')
    except Exception as e:
        print('dashboard error - %s' % (str(e)))
        raise e


# #################### endDash

def get_pub_data(request, org_level, area_id):
    print(org_level)
    print(area_id)
    main_dash_data = get_public_dash_ovc_hiv_status(org_level, area_id)
    return JsonResponse(main_dash_data, content_type='application/json',
                        safe=False)


def get_ovc_active_hiv_status(request, org_level, area_id):
    print(org_level)
    print(area_id)
    main_dash_data = _get_ovc_active_hiv_status(org_level, area_id)
    return JsonResponse(main_dash_data, content_type='application/json',
                        safe=False)


def get_ovc_served_stats(request, org_level, area_id, funding_partner, funding_part_id, period_type):
    main_dash_data = _get_ovc_served_stats(
        org_level, area_id, funding_partner, funding_part_id, period_type)
    return JsonResponse(main_dash_data, content_type='application/json',
                        safe=False)


def fetch_cbo_list(request):
    return JsonResponse(get_cbo_list(), content_type='application/json',
                        safe=False)


def get_locality_data(request):
    print("locality data")
    locality_data = fetch_locality_data()
    return JsonResponse(locality_data, content_type='application/json',
                        safe=False)


# ################### dash
def get_total_ovc_ever(request, org_level, area_id):
    print("total ovc ever")
    total_ovc_ever = fetch_total_ovc_ever(request, None, org_level, area_id)
    return JsonResponse(total_ovc_ever, content_type='application/json', safe=False)


def get_total_ovc_ever_exited(request, org_level, area_id):
    print("total ovc ever exited")
    total_ovc_ever_exited = fetch_total_ovc_ever_exited(
        request, None, org_level, area_id)
    return JsonResponse(total_ovc_ever_exited, content_type='application/json', safe=False)


def get_total_wout_bcert_at_enrol(request, org_level, area_id):
    print("without birthcert at enrolment")
    total_wout_bcert_at_enrol = fetch_total_wout_bcert_at_enrol(
        request, None, org_level, area_id)
    return JsonResponse(total_wout_bcert_at_enrol, content_type='application/json', safe=False)


def get_total_w_bcert_2date(request, org_level, area_id):
    print("all with birthcert to date")
    total_w_bcert_2date = fetch_total_w_bcert_2date(
        request, None, org_level, area_id)
    return JsonResponse(total_w_bcert_2date, content_type='application/json', safe=False)


def get_total_s_bcert_aft_enrol(request, org_level, area_id):
    print("all served birthcert after enrolment")
    total_s_bcert_aft_enrol = fetch_total_s_bcert_aft_enrol(
        request, None, org_level, area_id)
    return JsonResponse(total_s_bcert_aft_enrol, content_type='application/json', safe=False)

    # --------graphs-byperiod-------#


def get_new_ovcregs_by_period(request, org_level, area_id, funding_partner, funding_part_id, period_type):
    # print "new ovcregs by period with month_year="+month_year
    new_ovcregs_by_period = fetch_new_ovcregs_by_period(request, org_level, area_id, funding_partner, funding_part_id,
                                                        period_type)
    return JsonResponse(new_ovcregs_by_period, content_type='application/json', safe=False)


def get_active_ovcs_by_period(request, org_level, area_id, funding_partner, funding_part_id, period_type):
    pass
    # print "active ovcregs by period with month_year="+month_year
    # active_ovcs_by_period=fetch_active_ovcs_by_period(request, org_level,area_id,funding_partner,funding_part_id,period_type)
    # return JsonResponse(active_ovcs_by_period, content_type='application/json', safe=False)


def get_exited_ovcs_by_period(request, org_level, area_id, funding_partner, funding_part_id, period_type):
    # print "exited ovcregs by period with month_year="+month_year
    exited_ovcs_by_period = fetch_exited_ovcs_by_period(request, org_level, area_id, funding_partner, funding_part_id,
                                                        period_type)
    return JsonResponse(exited_ovcs_by_period, content_type='application/json', safe=False)


def get_exited_hsehlds_by_period(request, org_level, area_id, funding_partner, funding_part_id, period_type):
    # print "exited hsehlds by period with month_year="+month_year
    exited_hsehlds_by_period = fetch_exited_hsehlds_by_period(request, org_level, area_id, funding_partner,
                                                              funding_part_id, period_type)
    return JsonResponse(exited_hsehlds_by_period, content_type='application/json', safe=False)


def get_served_bcert_by_period(request, org_level, area_id, month_year):
    # print "served bcert by period with month_year="+month_year
    served_bcert_by_period = fetch_served_bcert_by_period(
        request, None, org_level, area_id, month_year)
    return JsonResponse(served_bcert_by_period, content_type='application/json', safe=False)


def get_u5_served_bcert_by_period(request, org_level, area_id, month_year):
    # print "u5 served bcert by period with month_year="+month_year
    u5_served_bcert_by_period = fetch_u5_served_bcert_by_period(
        request, None, org_level, area_id, month_year)
    return JsonResponse(u5_served_bcert_by_period, content_type='application/json', safe=False)
    # --------graphs-byperiod-------#


# ################### endDash

def get_hiv_suppression_data(request, org_level, area_id):
    hiv_suppression_data = get_ovc_hiv_status(
        request, None, org_level, area_id)
    return JsonResponse(hiv_suppression_data, content_type='application/json',
                        safe=False)


def get_ever_tested_hiv(request, org_level, area_id):
    ever_tested = get_ever_tested_for_HIV(request, None, org_level, area_id)
    return JsonResponse(ever_tested, content_type='application/json',
                        safe=False)
