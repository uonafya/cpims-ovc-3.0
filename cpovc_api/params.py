SID = {}
# Default settings

SID['sex_id'] = {'id': 'sex_id', 'name': 'Sex ID'}
SID['yesno_na'] = {'id': 'yesno_na', 'name': 'Yes / No / Not Applicable'}
SID['yesno_id'] = {'id': 'yesno_id', 'name': 'Yes / No'}
SID['ovc_domain_id'] = {'id': 'ovc_domain_id', 'name': 'Domain ID'}
SID['case_plan_goals_health'] = {
    'id': 'case_plan_goals_health', 'name': 'CP Healthy goals'}
SID['case_plan_goals_stable'] = {
    'id': 'case_plan_goals_stable', 'name': 'CP Stable goals'}
SID['case_plan_goals_school'] = {
    'id': 'case_plan_goals_school', 'name': 'CP Schooled goals'}
SID['case_plan_goals_safe'] = {
    'id': 'case_plan_goals_safe', 'name': 'CP Safe goals'}
SID['case_plan_gaps_health'] = {
    'id': 'case_plan_gaps_health', 'name': 'CP Healthy gaps'}
SID['case_plan_gaps_stable'] = {
    'id': 'case_plan_gaps_stable', 'name': 'CP Stable gaps'}
SID['case_plan_gaps_school'] = {
    'id': 'case_plan_gaps_school', 'name': 'CP Schooled gaps'}
SID['case_plan_gaps_safe'] = {
    'id': 'case_plan_gaps_safe', 'name': 'CP Safe gaps'}
SID['case_plan_priorities_health'] = {
    'id': 'case_plan_priorities_health', 'name': 'CP Healthy priorities'}
SID['case_plan_priorities_stable'] = {
    'id': 'case_plan_priorities_stable', 'name': 'CP Stable priorities'}
SID['case_plan_priorities_school'] = {
    'id': 'case_plan_priorities_school', 'name': 'CP Schooled priorities'}
SID['case_plan_priorities_safe'] = {
    'id': 'case_plan_priorities_safe', 'name': 'CP Safe priorities'}
SID['case_plan_services_health'] = {
    'id': 'case_plan_services_health', 'name': 'CP Healthy services'}
SID['case_plan_services_stable'] = {
    'id': 'case_plan_services_stable', 'name': 'CP Stable services'}
SID['case_plan_services_school'] = {
    'id': 'case_plan_services_school', 'name': 'CP Schooled services'}
SID['case_plan_services_safe'] = {
    'id': 'case_plan_services_safe', 'name': 'CP Safe services'}
SID['case_plan_responsible'] = {
    'id': 'case_plan_responsible', 'name': 'Case plan responsible'}
SID['case_plan_result'] = {
    'id': 'case_plan_result', 'name': 'Case plan results'}


# F1A items
SID['f1a_education_service_id'] = {
    'id': 'olmis_education_service_id', 'name': 'Schooled F1A'}
SID['f1a_health_service_id'] = {
    'id': 'olmis_health_service_id', 'name': 'Healthy F1A'}
SID['f1a_hes_service_id'] = {
    'id': 'olmis_hes_service_id', 'name': 'Stable F1A'}
SID['f1a_protection_service_id'] = {
    'id': 'olmis_protection_service_id', 'name': 'Safe F1A'}

# F1B items
SID['form1b_healhty_service_id'] = {'id': 'form1b_items',
                                    'name': 'Healthy F1B',
                                    'filter': 'item_sub_category__1s'}
SID['form1b_safe_service_id'] = {'id': 'form1b_items', 'name': 'Safe F1B',
                                 'filter': 'item_sub_category__3s'}
SID['form1b_stable_service_id'] = {'id': 'form1b_items', 'name': 'Stable F1B',
                                   'filter': 'item_sub_category__6s'}

# Default listing of allowed items - Disable Guess working
SIDS = ['sex_id', 'ovc_domain_id',
        'case_plan_goals_health', 'case_plan_goals_stable',
        'case_plan_goals_school', 'case_plan_goals_safe',
        'case_plan_gaps_health', 'case_plan_gaps_stable',
        'case_plan_gaps_school', 'case_plan_gaps_safe',
        'case_plan_priorities_health', 'case_plan_priorities_stable',
        'case_plan_priorities_school', 'case_plan_priorities_safe',
        'case_plan_services_health', 'case_plan_services_stable',
        'case_plan_services_school', 'case_plan_services_safe',
        'case_plan_responsible', 'case_plan_result',
        'olmis_education_service_id', 'olmis_health_service_id',
        'olmis_hes_service_id', 'olmis_protection_service_id',
        'form1b_items', 'form1b_healhty_service_id', 'yesno_na',
        'form1b_safe_service_id', 'form1b_stable_service_id',
        'f1a_education_service_id', 'f1a_health_service_id',
        'f1a_hes_service_id', 'f1a_protection_service_id']

META_IDS = []
for S_ID in SID:
    META_IDS.append(SID[S_ID]['id'])

# Device management status
STATUSES = {}
STATUSES[1] = 'Device added successfully'
STATUSES[2] = 'New Device has not been activated.'
STATUSES[3] = 'Change of Device'
STATUSES[4] = 'Device is Blocked'
STATUSES[5] = 'Multiple devices set up'
STATUSES[6] = 'Device already set up for a different user'
STATUSES[7] = 'Reserved'
STATUSES[8] = 'Reserved'
STATUSES[9] = 'New Device set up activate first.'
