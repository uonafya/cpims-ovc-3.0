from django.urls import path, include, re_path
from . import views

# This should contain paths related to registry ONLY
urlpatterns = [
    # Forms Registry
    # 'cpovc_forms.views',
    path('', views.forms_home, name='forms'),
    path('followups/', views.forms_registry, name='forms_registry'),
    # Documents Manager
    path('documents_manager/', views.documents_manager, name='documents_manager'),
    path('documents_manager_search/', views.documents_manager_search, name='documents_manager_search'),

    # Case Record Sheet paths
    path('crs/', views.case_record_sheet, name='case_record_sheet'),
    re_path('crs/new/(?P<id>\d+)/', views.new_case_record_sheet, name='new_case_record_sheet'),
    re_path('crs/view/(?P<id>\w+)/', views.view_case_record_sheet, name='view_case_record_sheet'),
    re_path('crs/edit/(?P<id>\w+)/', views.edit_case_record_sheet, name='edit_case_record_sheet'),
    re_path('crs/delete/(?P<id>\w+)/', views.delete_case_record_sheet, name='delete_case_record_sheet'),

    # Alternative Family Care paths
    path('afc/', views.alternative_family_care, name='alternative_family_care'),
    re_path('afc/new/(?P<id>\d+)/', views.new_alternative_family_care, name='new_alternative_family_care'),
    # path('afc/edit/(?P<id>\w+)/', views.edit_alternative_family_care, name='edit_alternative_family_care'),
    re_path(r'^afc/edit/(?P<id>\w+)/$', views.edit_alternative_family_care, name='edit_alternative_family_care'),
    re_path('afc/view/(?P<id>\w+)/', views.view_alternative_family_care, name='view_alternative_family_care'),

    # Residential Placement
    path('placement/save/', views.save_placement, name='save_placement'),
    re_path('placement/view/(?P<id>\w+)/', views.view_placement, name='view_placement'),
    re_path('placement/edit/(?P<id>\w+)/', views.edit_placement, name='edit_placement'),
    path('placement/delete/', views.delete_placement, name='delete_placement'),
    path('placement/', views.residential_placement, name='residential_placement'),
    re_path('placement/(?P<id>\d+)/', views.placement, name='placement'),

    # Residential Placement FollowUp
    re_path('placement_followup/(?P<id>\d+)/', views.placement_followup, name='placement_followup'),
    path('save_placementfollowup/', views.save_placementfollowup, name='save_placementfollowup'),
    path('view_placementfollowup/', views.view_placementfollowup, name='view_placementfollowup'),
    path('edit_placementfollowup/', views.edit_placementfollowup, name='edit_placementfollowup'),
    path('delete_placementfollowup/', views.delete_placementfollowup, name='delete_placementfollowup'),

    # Case Events (Encounters/Court Sessions/Referrals/Case
    # Closure/Summons)
    re_path('case_events/(?P<id>\w+)/', views.case_events, name='case_events'),
    # ---------------------------------------------------------
    path('save_encounter/', views.save_encounter, name='save_encounter'),
    path('view_encounter/', views.view_encounter, name='view_encounter'),
    path('edit_encounter/', views.edit_encounter, name='edit_encounter'),
    path('delete_encounter/', views.delete_encounter, name='delete_encounter'),
    # ----------------------------------------------------------
    path('save_court/', views.save_court, name='save_court'),
    path('view_court/', views.view_court, name='view_court'),
    path('edit_court/', views.edit_court, name='edit_court'),
    path('delete_court/', views.delete_court, name='delete_court'),
    # ----------------------------------------------------------
    path('save_summon/', views.save_summon, name='save_summon'),
    path('edit_summon/', views.edit_summon, name='edit_summon'),
    path('view_summon/', views.view_summon, name='view_summon'),
    path('delete_summon/', views.delete_summon, name='delete_summon'),
    # ----------------------------------------------------------
    path('save_closure/', views.save_closure, name='save_closure'),
    path('edit_closure/', views.edit_closure, name='edit_closure'),
    path('view_closure/', views.view_closure, name='view_closure'),
    path('delete_closure/', views.delete_closure, name='delete_closure'),

    # Referrals
    path('delete_referral/', views.delete_referral, name='delete_referral'),

    # Management paths
    path('manage_refferal/', views.manage_refferal, name='manage_refferal'),
    path('manage_refferal001/', views.manage_refferal001, name='manage_refferal001'),
    path('manage_refferal002/', views.manage_refferal002, name='manage_refferal002'),
    path('manage_refferal003/', views.manage_refferal003, name='manage_refferal003'),
    path('manage_casecategory001/', views.manage_casecategory001, name='manage_casecategory001'),
    path('manage_casecategory002/', views.manage_casecategory002, name='manage_casecategory002'),
    path('manage_casecategory003/', views.manage_casecategory003, name='manage_casecategory003'),
    path('manage_casecategory004/', views.manage_casecategory004, name='manage_casecategory004'),
    path('manage_encounters001/', views.manage_encounters001, name='manage_encounters001'),
    path('manage_encounters004/', views.manage_encounters004, name='manage_encounters004'),
    path('manage_case_events/', views.manage_case_events, name='manage_case_events'),
    path('manage_placementfollowup/', views.manage_placementfollowup, name='manage_placementfollowup'),
    path('manage_schools/', views.manage_schools, name='manage_schools'),
    path('manage_countries/', views.manage_countries, name='manage_countries'),
    path('manage_casehistory/', views.manage_casehistory, name='manage_casehistory'),
    path('manage_service_category/', views.manage_service_category, name='manage_service_category'),
    path('manage_form_type/', views.manage_form_type, name='manage_form_type'),
    # ---------------------------------------------------------------
    path('userorgunits_lookup/', views.userorgunits_lookup, name='userorgunits_lookup'),
    path('usersubcounty_lookup/', views.usersubcounty_lookup, name='usersubcounty_lookup'),
    path('userward_lookup/', views.userward_lookup, name='userward_lookup'),
    path('generate_serialnumber/', views.generate_serialnumber, name='generate_serialnumber'),
    path('getJsonObject001/', views.getJsonObject001, name='getJsonObject001'),

    # Search paths
    path('ovc_search/', views.ovc_search, name='ovc_search'),

    # School & Bursary paths
    path('education/', views.background_details, name='background_details'),
    re_path('education/new/(?P<id>\d+)/', views.new_education_info, name='new_education_info'),
    re_path('education/edit/(?P<id>\w+)/', views.edit_education_info, name='edit_education_info'),
    re_path('education/view/(?P<id>\w+)/', views.view_education_info, name='view_education_info'),
    re_path('education/delete/(?P<id>\w+)/', views.delete_education_info, name='delete_education_info'),
    # -----------------------------------------------------------------
    path('school/', views.new_school, name='new_school'),
    # ------------------------------------------------------------------
    path('bursary/new/', views.new_bursary_info, name='new_bursary_info'),
    path('bursary/edit/', views.edit_bursary_info, name='edit_bursary_info'),
    path('bursary/view/', views.view_bursary_info, name='view_bursary_info'),
    path('bursary/delete/', views.delete_bursary_info, name='delete_bursary_info'),
    re_path('bursary/followup/(?P<id>\d+)/', views.bursary_followup, name='bursary_followup'),
    path('bursary/manage/', views.manage_bursary, name='manage_bursary'),
    # OVC Care - CSI
    path('csi/', views.csi, name='csi'),
    re_path('csi/new/(?P<id>\d+)/', views.new_csi, name='new_csi'),
    re_path('csi/edit/(?P<id>\w+)/', views.edit_csi, name='edit_csi'),
    re_path('csi/view/(?P<id>\w+)/', views.view_csi, name='view_csi'),
    re_path('csi/delete/(?P<id>\w+)/', views.delete_csi, name='delete_csi'),

    # OVC Care - Form1A
    re_path('form1a/new/(?P<id>\d+)/', views.form1a_events, name='form1a_events'),
    path('form1a/save/', views.save_form1a, name='save_form1a'),
    path('form1a/update/', views.update_form1a, name='update_form1a'),
    re_path('form1a/edit/(?P<id>\d+)/(?P<btn_event_type>\w+)/(?P<btn_event_pk>.+)/', views.edit_form1a,
            name='edit_form1a'),
    path('form1a/view/', views.view_form1a, name='view_form1a'),
    re_path('form1a/delete/(?P<id>\d+)/(?P<btn_event_type>\w+)/(?P<btn_event_pk>.+)/', views.delete_form1a,
            name='delete_form1a'),
    re_path('form1a/delete_previous_event_entry/(?P<btn_event_type>\w+)/(?P<entry_id>.+)/',
            views.delete_previous_event_entry, name='delete_previous_event_entry'),
    path('form1a/manage/', views.manage_form1a_events, name='manage_form1a_events'),
    # end OVC Care - Form1A

    # OVC Care - Form1B
    re_path('form1b/new/(?P<id>\d+)/', views.new_form1b, name='new_form1b'),
    re_path('form1b/delete/(?P<id>\d+)/(?P<btn_event_pk>.+)/', views.delete_form1b, name='delete_form1b'),
    path('form1b/manage/', views.manage_form1b_events, name='manage_form1b_events'),
    # OVC Care - Form1B

    # OVC Care - HHVA
    re_path('hhva/new/(?P<id>\d+)/', views.new_hhva, name='new_hhva'),
    re_path('hhva/edit/(?P<id>\w+)/', views.edit_hhva, name='edit_hhva'),
    re_path('hhva/view/(?P<id>\w+)/', views.view_hhva, name='view_hhva'),
    re_path('hhva/delete/(?P<id>\w+)/', views.delete_hhva, name='delete_hhva'),
    # Presidential Bursary
    re_path('bursary/list/(?P<id>\d+)/', views.list_bursary, name='list_bursary'),
    re_path(r'^bursary/view/(?P<id>[0-9A-Za-z_\-{32}\\Z]+)/', views.view_bursary, name='view_bursary'),
    re_path('bursary/new/(?P<id>\d+)/', views.new_bursary, name='new_bursary'),
    re_path(r'^bursary/edit/(?P<id>[0-9A-Za-z_\-{32}\\Z]+)/', views.edit_bursary, name='edit_bursary'),
    re_path(r'^bursary/form/(?P<id>[0-9A-Za-z_\-{32}\\Z]+)/', views.form_bursary, name='form_bursary'),
    # OVC Care - CPARA Form
    re_path('cpara/new/(?P<id>\d+)/', views.new_cpara, name='new_cpara'),
    re_path('cpara/delete/(?P<id>\d+)/(?P<btn_event_pk>.+)/', views.delete_cpara, name='delete_cpara'),

    # OVC Care - Case Plan Template
    re_path('caseplan/new/(?P<id>\d+)/', views.case_plan_template, name='new_caseplan'),
    re_path('caseplan/update/(?P<ovcid>\d+)/(?P<event_id>.+)/', views.update_caseplan, name='update_caseplan'),
    re_path('caseplan-monitoring/new/(?P<id>\d+)/', views.new_case_plan_monitoring, name='new_caseplan_monitoring'),

    # wellbeing Adult and Child
    re_path(r'^wellbeing/new/(?P<id>\d+)/$', views.new_wellbeing, name='new_wellbeing'),

    # wellbeing Adolescent
    re_path(r'^wellbeingadolescent/new/(?P<id>\d+)/$', views.new_wellbeingadolescent, name='new_wellbeingadolescent'),
    # hiv_status
    path('HIVstatus/', views.hiv_status, name='hiv_status'),

    # HIV Risk Assessment Form
    re_path('hivscreeningtool/new/(?P<id>\d+)/', views.new_hivscreeningtool, name='new_hivscreeningtool'),

    # HIV Risk Management Form
    re_path('hivmanagementform/new/(?P<id>\d+)/', views.new_hivmanagementform, name='new_hivmanagementform'),

    # Dreams SerivceUptake Form
    re_path('dreamsform/new/(?P<id>\d+)/', views.new_dreamsform, name='new_dreamsform'),

]
