QUERIES = {}

QUERIES['1A'] = '''
SELECT count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id
from vw_cpims_registration_fy22 where not (exit_status = 'EXITED' and exit_reason = 'Duplicated') {cbos}
group by gender
'''
# {odate}
# {fdate}

QUERIES['1B'] = '''
SELECT count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id,
CASE exit_status WHEN 'ACTIVE' THEN 'Current case load'
ELSE 'Exited(Left Program)' END AS active_status
from vw_cpims_registration_fy22 where not (exit_status = 'EXITED' and exit_reason = 'Duplicated') {cbos}
group by active_status
UNION
SELECT count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'Ever Registered' AS active_status
from vw_cpims_registration_fy22 where not (exit_status = 'EXITED' and exit_reason = 'Duplicated') {cbos}
'''

QUERIES['1C'] = '''
SELECT count(cpims_ovc_id) as dcount,
'SMAL' as sex_id, eligibility
from vw_cpims_registration_fy22 where not (exit_status = 'EXITED' and exit_reason = 'Duplicated') {cbos}
group by eligibility order by dcount desc
'''

QUERIES['1G'] = '''
SELECT count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, exit_reason
from vw_cpims_registration_fy22 where exit_status = 'EXITED' {cbos}
group by exit_reason order by dcount desc
'''

QUERIES['1D'] = '''
SELECT count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'Current case load' as services
from vw_cpims_registration_fy22 where exit_status='ACTIVE' {cbos} {areas}
UNION
SELECT count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'Has Birth Certificate' as services
from vw_cpims_registration_fy22 where exit_status='ACTIVE'
and birthcert = 'HAS BIRTHCERT' {cbos} {areas}
UNION
SELECT count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'Has Disability' as services
from vw_cpims_registration_fy22 where exit_status='ACTIVE'
and ovcdisability = 'HAS DISABILITY' {cbos} {areas}
UNION
SELECT count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'School Going' as services
from vw_cpims_registration_fy22 where exit_status='ACTIVE'
and schoollevel != 'Not in School' {cbos} {areas}
'''

QUERIES['1E'] = '''
select sum(counts) as dcount, agency, 'SMAL' as sex_id
from vw_cpims_dash_caseload {ocbos} {oareas}
group by agency
'''

QUERIES['1F'] = '''
Select count(distinct(cpims_ovc_id)) AS dcount,
gender as sex_id,
CASE
when ovchivstatus='POSITIVE' THEN 'HIV Status +Ve'
when ovchivstatus='NEGATIVE' THEN 'HIV Status -Ve'
when ovchivstatus='NOT KNOWN' THEN 'HIV Status Unknown'
when ovchivstatus='HIV Test Not Required' THEN 'HIV Test not Required'
when ovchivstatus='HIV Referred For Testing' THEN 'HIV Referred For Testing'
ELSE 'Others' END AS hivstat
from vw_cpims_registration_fy22 where exit_status='ACTIVE' {cbos} {areas}
group by gender, ovchivstatus order by dcount DESC
'''

# ================= Section 2 =====================

QUERIES['2A'] = '''
select * from (
select count(distinct(cpims_ovc_id)) as dcount,
'Case load' as services, 'SMAL' as sex_id
from vw_cpims_dash_caseload {ocbos}
UNION
select count(distinct(cpims_ovc_id)) as dcount,
'Active' as services, 'SMAL' as sex_id
from vw_cpims_dash_caseload where exit_status='ACTIVE' {cbos}
UNION
select count(distinct(cpims_ovc_id)) as dcount,
'Transfers' as services, 'SMAL' as sex_id
from vw_cpims_dash_caseload
WHERE (vw_cpims_dash_caseload.exit_reason = 'Transferred to PEPFAR partner' AND exit_status='EXITED'
OR vw_cpims_dash_caseload.exit_reason = 'Transferred to Non-PEPFAR partner'  AND exit_status='EXITED')
{cbos}
UNION
select count(distinct(cpims_ovc_id)) as dcount, 'Exits' as services, 'SMAL' as sex_id
from vw_cpims_dash_caseload
WHERE exit_status='EXITED' AND (
vw_cpims_dash_caseload.exit_reason = ' Adoption'
OR vw_cpims_dash_caseload.exit_reason = 'Death'
OR vw_cpims_dash_caseload.exit_reason = 'Drop Out'
OR vw_cpims_dash_caseload.exit_reason = ' Family reconciliation'
OR vw_cpims_dash_caseload.exit_reason = 'Family reintegration'
OR vw_cpims_dash_caseload.exit_reason = 'Fostering'
OR vw_cpims_dash_caseload.exit_reason = 'Ineligible'
OR vw_cpims_dash_caseload.exit_reason = 'Left at will'
OR vw_cpims_dash_caseload.exit_reason = 'Married'
OR vw_cpims_dash_caseload.exit_reason = 'Not Traceable'
OR vw_cpims_dash_caseload.exit_reason = 'Over 18'
OR vw_cpims_dash_caseload.exit_reason = 'Over 18 yrs and out of School'
OR vw_cpims_dash_caseload.exit_reason = 'Relocation'
OR vw_cpims_dash_caseload.exit_reason = 'Self Employed'
OR vw_cpims_dash_caseload.exit_reason = ''
OR vw_cpims_dash_caseload.exit_reason = 'Transfered to GOK - DCS'
OR vw_cpims_dash_caseload.exit_reason = 'Transition' )
{cbos}
UNION
select count(distinct(person_id)) as dcount, 'Graduated' as services,
'SMAL' as sex_id from vw_cpims_dash_graduated {ocbos}
) x
order by dcount desc
'''

QUERIES['2B'] = '''
select count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id, agerange
from vw_cpims_dash_caseload {ocbos} {oareas}
group by gender, agerange
'''

QUERIES['2C'] = '''
SELECT count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, eligibility
from vw_cpims_dash_caseload
WHERE eligibility <> 'None' {cbos} {areas}
group by eligibility
having count(distinct(cpims_ovc_id)) > 0
order by dcount desc
'''

QUERIES['2D'] = '''
select count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id, schoollevel as school_level
from vw_cpims_dash_caseload {ocbos} {oareas}
group by gender, schoollevel
'''

QUERIES['2E'] = '''
Select count(distinct(cpims_ovc_id)) AS dcount,
gender as sex_id,
CASE
when ovchivstatus='POSITIVE' THEN 'HIV Status +Ve'
when ovchivstatus='NEGATIVE' THEN 'HIV Status -Ve'
when ovchivstatus='NOT KNOWN' THEN 'HIV Status Unknown'
when ovchivstatus='HIV Test Not Required' THEN 'HIV Test not Required'
when ovchivstatus='HIV Referred For Testing' THEN 'HIV Status Unknown'
when ovchivstatus='HEI NOT KNOWN' THEN 'HEI Not Known'
ELSE 'Not Known' END AS hivstat
from vw_cpims_dash_caseload {ocbos} {oareas}
group by gender, ovchivstatus order by dcount DESC
'''

QUERIES['2F'] = '''
SELECT count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'Current case load' as services
from vw_cpims_dash_caseload where exit_status='ACTIVE' {cbos} {areas}
UNION
SELECT count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'Has Birth Certificate' as services
from vw_cpims_dash_caseload where exit_status='ACTIVE'
and birthcert = 'HAS BIRTHCERT' {cbos} {areas}
UNION
SELECT count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'Has Disability' as services
from vw_cpims_dash_caseload where exit_status='ACTIVE'
and ovcdisability = 'HAS DISABILITY' {cbos} {areas}
UNION
SELECT count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'School Going' as services
from vw_cpims_dash_caseload where exit_status='ACTIVE'
and schoollevel != 'Not in School' {cbos} {areas}
'''

QUERIES['2G'] = '''
select count(distinct(cpims_ovc_id)) as dcount, gender as sex_id
from vw_cpims_registration where registration_date >'2021-09-30' {cbos}
group by gender
'''
'''
select count(distinct(cpims_ovc_id)) as dcount,eligibility
from vw_cpims_registration where registration_date_fy22 >'2021-09-30' and registration_date < '2022-10-01' and exit_reason !='Duplicated'
group by eligibility
'''

QUERIES['2H'] = '''
SELECT count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, exit_reason
from vw_cpims_dash_caseload
WHERE (exit_reason <> 'None' or exit_reason <> 'Duplicated') {cbos} {areas}
group by exit_reason
having count(distinct(cpims_ovc_id)) > 0
order by dcount desc
'''

QUERIES['2I'] = '''
select count(distinct(cpims_ovc_id)) as dcount, eligibility, 'SMAL' as sex_id
from vw_cpims_dash_caseload {ocbos} {oareas}
group by eligibility
order by dcount desc
'''

QUERIES['2J'] = '''
select count(distinct(cpims_ovc_id)) as dcount, agency, 'SMAL' as sex_id
from vw_cpims_dash_caseload {ocbos} {oareas}
group by agency
'''

QUERIES['2K'] = '''
select count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, schoollevel from
vw_cpims_dash_caseload where schoollevel <> 'Not in School' {cbos} {areas}
group by schoollevel
'''

QUERIES['2L'] = '''
select count(distinct(cpims_ovc_id)) as dcount, agency, schoollevel
from vw_cpims_dash_caseload where schoollevel <> 'Not in School' {cbos} {areas}
group by schoollevel, agency
'''

QUERIES['2M'] = '''
select count(distinct(cpims_ovc_id)) as dcount, gender as sex_id from
vw_cpims_dash_caseload where schoollevel <> 'Not in School' {cbos} {areas}
group by gender
'''

QUERIES['2N'] = '''
select count(distinct(cpims_ovc_id)) as dcount, gender as sex_id, schoollevel
from vw_cpims_dash_caseload where schoollevel <> 'Not in School' {cbos} {areas}
group by gender, schoollevel
'''

QUERIES['2P'] = '''
select count(distinct(cpims_ovc_id)) as dcount, schoollevel, mechanism, agency
from vw_cpims_dash_caseload where schoollevel <> 'Not in School' {cbos}
group by schoollevel, mechanism, agency
order by agency, mechanism
'''

QUERIES['2Q'] = '''
select count(distinct(cpims_ovc_id)) as dcount, agerange, gender as sex_id
from vw_cpims_dash_caseload where schoollevel='Not in School' {cbos} {areas}
group by agerange, gender
'''

QUERIES['2R'] = '''
select count(distinct(cpims_ovc_id)) as dcount, agerange,
CASE schoollevel WHEN 'Not in School' THEN 'a.Not in School'
ELSE schoollevel END AS schoollevel
from vw_cpims_dash_caseload {ocbos} {oareas}
group by agerange, schoollevel
order by agerange desc, schoollevel asc
'''

# =============== Section 3 ===========================

QUERIES['3A'] = '''
select * from (
select count(distinct(cpims_ovc_id)) as dcount,
'Case load' as agency, 'Case load' as services
from vw_cpims_dash_caseload {ocbos}
UNION
select count(distinct(cpims_ovc_id)) as dcount,
'Active' as agency, 'Program status' as services
from vw_cpims_dash_caseload where exit_status='ACTIVE' {cbos}
UNION
select count(distinct(cpims_ovc_id)) as dcount,
'Transfers' as agency, 'Program status' as services
from vw_cpims_dash_caseload
WHERE (vw_cpims_dash_caseload.exit_reason = 'Transferred to PEPFAR partner' AND exit_status='EXITED'
OR vw_cpims_dash_caseload.exit_reason = 'Transferred to Non-PEPFAR partner'  AND exit_status='EXITED')
{cbos}
UNION
select count(distinct(cpims_ovc_id)) as dcount, 'Exits' as agency, 'Program status' as services
from vw_cpims_dash_caseload
WHERE exit_status='EXITED' AND (
vw_cpims_dash_caseload.exit_reason = ' Adoption'
OR vw_cpims_dash_caseload.exit_reason = 'Death'
OR vw_cpims_dash_caseload.exit_reason = 'Drop Out'
OR vw_cpims_dash_caseload.exit_reason = ' Family reconciliation'
OR vw_cpims_dash_caseload.exit_reason = 'Family reintegration'
OR vw_cpims_dash_caseload.exit_reason = 'Fostering'
OR vw_cpims_dash_caseload.exit_reason = 'Ineligible'
OR vw_cpims_dash_caseload.exit_reason = 'Left at will'
OR vw_cpims_dash_caseload.exit_reason = 'Married'
OR vw_cpims_dash_caseload.exit_reason = 'Not Traceable'
OR vw_cpims_dash_caseload.exit_reason = 'Over 18'
OR vw_cpims_dash_caseload.exit_reason = 'Over 18 yrs and out of School'
OR vw_cpims_dash_caseload.exit_reason = 'Relocation'
OR vw_cpims_dash_caseload.exit_reason = 'Self Employed'
OR vw_cpims_dash_caseload.exit_reason = ''
OR vw_cpims_dash_caseload.exit_reason = 'Transfered to GOK - DCS'
OR vw_cpims_dash_caseload.exit_reason = 'Transition' )
{cbos}
) x order by services asc
'''

'''
select sum(count) as dcount, 'OVC_SERV' AS mechanism,
'OVC_SERV_FY' AS agency FROM (
select sum(served) as count, mechanism, agency
from vw_Active_Beneficiary_APR22 {ocbos} group by mechanism, agency
UNION
select sum(graduated) as count, mechanism, agency
from vw_cpims_dash_graduated {ocbos} group by mechanism, agency
) srv
UNION ALL
'''

QUERIES['3B'] = '''
select sum(count) as dcount, 'OVC_SERV' AS mechanism,
'OVC_SERV_FY' AS agency FROM (
select sum(served) as count, mechanism, agency
from vw_Active_Beneficiary_APR22 {ocbos} group by mechanism, agency
UNION
select sum(graduated) as count, mechanism, agency
from vw_cpims_dash_graduated {ocbos} group by mechanism, agency
) srv
UNION ALL
select sum(count) as dcount, 'OVC_SERV - >18' AS mechanism,
'OVC_SERV - >18 & <18' AS agency FROM (
select count(distinct(person_id)) as count
from vw_Active_Beneficiary_APR22 where agerange = 'f.[18-20yrs]' {cbos}
UNION
select sum(graduated) as count
from vw_cpims_dash_graduated where agerange = 'f.[18-20yrs]' {cbos}
) srv
UNION ALL
select sum(count) as dcount, 'OVC_SERV - <18' AS mechanism,
'OVC_SERV - >18 & <18' AS agency FROM (
select count(distinct(person_id)) as count
from vw_Active_Beneficiary_APR22 where agerange <> 'f.[18-20yrs]' {cbos}
UNION
select count(distinct(person_id)) as count
from vw_cpims_dash_graduated where agerange <> 'f.[18-20yrs]' {cbos}
) srv
UNION ALL
select count(distinct(person_id)) as dcount,
hivinfo AS mechanism, 'HIV Info' as agency
from vw_cpims_dash_hivstat {ocbos} group by hivinfo
UNION ALL
select count(distinct(person_id)) as dcount, ovchivstatus as mechanism,
'HIV Status' as agency
from vw_cpims_dash_hivstat where hivinfo ='KNOWN HIV Info' {cbos}
group by ovchivstatus
UNION ALL
select count(distinct(person_id)) as dcount,
artstatus as mechanism, 'ART Status' as agency
from vw_cpims_dash_hivstat where hivinfo ='KNOWN HIV Info'
and ovchivstatus='POSITIVE' {cbos} group by artstatus
'''

QUERIES['3C'] = '''
select sum(x.cnt) as dcount, 'SMAL' as sex_id,
'OVC_SERV' as hivstat from
(
Select count(distinct(person_id)) as cnt
from vw_active_beneficiary_apr22 {ocbos}
UNION ALL
Select count(distinct(person_id)) as cnt
from vw_cpims_dash_graduated {ocbos}
) x
UNION
Select count(distinct(cpims_ovc_id)) AS dcount,
'SMAL' as sex_id,
CASE
when ovchivstatus='POSITIVE' THEN 'HIV Status +Ve'
when ovchivstatus='NEGATIVE' THEN 'HIV Status -Ve'
when ovchivstatus='NOT KNOWN' THEN 'HIV Status Unknown'
when ovchivstatus='HIV Test Not Required' THEN 'HIV Test not Required'
when ovchivstatus='HIV Referred For Testing' THEN 'HIV Status Unknown'
ELSE 'Others' END AS hivstat
from vw_cpims_dash_caseload where cpims_ovc_id IN
(select distinct(x.person_id) from
(
Select distinct(person_id)
from vw_active_beneficiary_apr22 {ocbos}
UNION ALL
Select distinct(person_id)
from vw_cpims_dash_graduated {ocbos}
) x )
group by ovchivstatus
'''

QUERIES['3D'] = '''
select sum(x.cnt) as dcount, 'SMAL' as sex_id,
'OVC_SERV' as hivstat from
(
Select count(distinct(cpims_ovc_id)) as cnt
from vw_cpims_active_beneficiary
WHERE age < 18 {cbos}
UNION ALL
Select count(distinct(cpims_ovc_id)) as cnt
from vw_cpims_benchmark_achieved_v1 where age < 18 AND (current_date - date_of_event) <= 400
AND cpara_score = 17 {cbos}
) x
UNION
Select count(distinct(cpims_ovc_id)) AS dcount,
'SMAL' as sex_id,
CASE
when ovchivstatus='POSITIVE' THEN 'HIV Status +Ve'
when ovchivstatus='NEGATIVE' THEN 'HIV Status -Ve'
when ovchivstatus='NOT KNOWN' THEN 'HIV Status Unknown'
when ovchivstatus='HIV Test Not Required' THEN 'HIV Test not Required'
when ovchivstatus='HIV Referred For Testing' THEN 'HIV Referred For Testing'
ELSE 'Others' END AS hivstat
from vw_cpims_registration where age < 18 AND cpims_ovc_id in
(select distinct(x.cpims_ovc_id) from
(
Select distinct(cpims_ovc_id)
from vw_cpims_active_beneficiary {ocbos}
UNION ALL
Select distinct(cpims_ovc_id)
from vw_cpims_benchmark_achieved_v1 where (current_date - date_of_event) <= 400
AND cpara_score = 17 {cbos}
) x)
and exit_status='ACTIVE'
group by ovchivstatus
'''

QUERIES['3E'] = '''
select * from (
Select count(distinct(cpims_ovc_id)) AS dcount,
'SMAL' as sex_id, 'Positive' as hivstat
from vw_cpims_dash_caseload where
ovchivstatus='POSITIVE' {cbos}
UNION
Select count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'On ART' as hivstat
from vw_cpims_dash_caseload
where ovchivstatus='POSITIVE' AND artstatus='ART' {cbos}
UNION
Select count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'VL Accessed' as hivstat
from vw_cpims_dash_viral_load {ocbos}
UNION
Select count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'Valid VL' as hivstat
from vw_cpims_dash_viral_load where vl_period_validity='Valid' {cbos}
UNION
Select count(distinct(cpims_ovc_id)) AS dcount,
'SMAL' as sex_id, 'Suppressed' as hivstat
from vw_cpims_dash_viral_load WHERE viral_load < 1000 {cbos}
UNION
Select count(distinct(cpims_ovc_id)) AS dcount,
'SMAL' as sex_id, 'Not Suppressed' as hivstat
from vw_cpims_dash_viral_load WHERE viral_load > 999 {cbos}
) x
order by dcount desc
'''

QUERIES['3F'] = '''
SELECT count(distinct(cpims_ovc_id)) as dcount,
'Male' as sex_id, 'Known HIV Status' as hivstat
from vw_cpims_registration where exit_status='ACTIVE' {cbos}
UNION
Select count(distinct(cpims_ovc_id)) AS dcount,
'Male' as sex_id, 'On ART' as hivstat
from vw_cpims_registration where exit_status='ACTIVE'
and ovchivstatus='POSITIVE' {cbos}
UNION
Select count(distinct(v.cpims_ovc_id)) as dcount,
'Male' as sex_id, 'Suppression' as hivstat
from vw_cpims_viral_load v
inner join (
select cpims_ovc_id, max(date_of_event) as most_current_vl_date
from vw_cpims_viral_load
group by cpims_ovc_id ) vl on v.cpims_ovc_id = vl.cpims_ovc_id
and v.date_of_event=vl.most_current_vl_date
where current_date - vl.most_current_vl_date <= 400 {vcbos}
UNION
Select count(distinct(cpims_ovc_id)) AS dcount,
'Female' as sex_id, 'Known HIV Status' as hivstat
from vw_cpims_registration where exit_status='ACTIVE'
and (ovchivstatus='POSITIVE' or ovchivstatus='NEGATIVE'
or ovchivstatus='NOT KNOWN' or ovchivstatus='HIV Test Not Required'
or ovchivstatus='HIV Referred For Testing') {cbos}
UNION
Select count(distinct(cpims_ovc_id)) as dcount,
'Female' as sex_id, 'On ART' as hivstat
from vw_cpims_registration where exit_status='ACTIVE'
and ovchivstatus='POSITIVE' AND artstatus='ART' {cbos}
UNION
Select count(distinct(v.cpims_ovc_id)) AS dcount,
'Female' as sex_id, 'Suppression' as hivstat
from vw_cpims_viral_load v
inner join (
select cpims_ovc_id, max(date_of_event) as most_current_vl_date
from vw_cpims_viral_load
group by cpims_ovc_id ) vl on v.cpims_ovc_id = vl.cpims_ovc_id
and v.date_of_event=vl.most_current_vl_date
where current_date - vl.most_current_vl_date <= 400
and v.viral_load < 1001 {vcbos}
'''

QUERIES['3G'] = '''
Select count(distinct(cpims_ovc_id)) as dcount, gender as sex_id, agerange
from vw_cpims_viral_load where (current_date - date_of_event) < 401
and viral_load > 1000 {cbos} group by gender, agerange
'''

QUERIES['3H'] = '''
select count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id, agerange
from vw_cpims_dash_caseload where ovchivstatus='POSITIVE' {cbos}
group by gender, agerange
'''

# ========= Section 4 ===============================

QUERIES['4A'] = '''
select count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'Case Load' as services
from vw_cpims_dash_caseload {ocbos}
UNION
SELECT count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'Received Services' as services
from vw_cpims_dash_list_served {ocbos}
UNION
Select count(distinct(person_id)) AS dcount,
'SMAL' as sex_id, 'Served Two Quarters' as services
from vw_cpims_two_quarters where ('2022-09-30' - date_of_event) <=200
AND date_of_event < '2022-09-30' {cbos}
UNION
Select count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'Case Plans' as services
from vw_cpims_case_plan where ('2022-09-30' - date_of_event) <= 400
AND date_of_event < '2022-09-30' {cbos}
UNION
select count(distinct(person_id)) as dcount,  'SMAL' as sex_id,
'Graduated' as services from vw_cpims_dash_graduated {ocbos}
UNION
Select count(distinct(person_id)) as dcount,
'SMAL' as sex_id, 'Active Beneficiary' as services
from vw_active_beneficiary_apr22 {ocbos}
UNION
select sum(x.cnt) as dcount, 'SMAL' as sex_id,
'OVC_SERV' as hivstat from
(
Select count(distinct(person_id)) as cnt,
'SMAL' as sex_id from vw_active_beneficiary_apr22 {ocbos}
group by gender
UNION ALL
Select count(distinct(cpims_ovc_id)), 'SMAL' as sex_id
from vw_cpims_benchmark_achieved_v1 where
('2022-09-30' - date_of_event) <= 400 AND date_of_event < '2022-09-30'
AND cpara_score = 17 {cbos} group by gender
) x
UNION
Select count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'Exit without Graduation' as services
from vw_cpims_dash_caseload where exit_status='ACTIVE'
AND cpims_ovc_id NOT IN
(select distinct(vw_cpims_dash_caseload.cpims_ovc_id)
from vw_cpims_two_quarters) {cbos}
'''

QUERIES['4B'] = '''
Select count(distinct(household_id)) as dcount,
 'Case Plans' as services, 'SMAL' as sex_id
from vw_cpims_case_plan where (current_date - date_of_event) <= 400 {cbos}
UNION
Select sum(dcount) as dcount, services, sex_id from (
Select count(distinct(household)) as dcount,
'CPARA' as services, 'SMAL' as sex_id
from vw_cpims_cpara_v1 where (current_date - date_of_event) <= 400 {cbos}
UNION
Select count(distinct(household)) as dcount,
'CPARA' as services, 'SMAL' as sex_id
from vw_cpims_cpara where (current_date - date_of_event) <= 400 {cbos}
)cp
group by cp.services, cp.sex_id
'''

QUERIES['4C'] = '''
Select count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, domain as services
from vw_cpims_dash_list_served {ocbos} group by domain
order by dcount desc
'''

QUERIES['4D'] = '''
SELECT count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'OVC Comprehensive' as services
from vw_cpims_dash_caseload where exit_status='ACTIVE' {cbos}
'''

QUERIES['4E'] = '''
Select count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, service as services
from vw_cpims_dash_list_served
where date_of_service > '2022-03-31' {cbos}
group by service
order by dcount desc limit 35
'''

QUERIES['4F'] = '''
Select count(distinct(cpims_ovc_id)) as dcount,
domain, gender as sex_id from vw_cpims_dash_list_served {ocbos}
group by domain, gender
order by dcount desc
'''

QUERIES['4G'] = '''
select count(distinct(household)) as dcount, domain,
'SMAL' as sex_id from vw_cpims_dash_list_served {ocbos} group by domain
'''

QUERIES['4H'] = '''
select count(distinct(cpims_ovc_id)) as dcount,
domain, agency from vw_cpims_dash_list_served {ocbos}
group by agency, domain
'''

QUERIES['4I'] = '''
select dcount, domain as agency, service as mechanism,
'Service' as schoollevel from (
(select count(distinct(cpims_ovc_id)) as dcount,
domain, service from vw_cpims_dash_list_served
Where domain='Healthy' {cbos}
group by domain, service
order by dcount DESC limit 5)
UNION
(select count(distinct(cpims_ovc_id)) as dcount,
domain, service from vw_cpims_dash_list_served
Where domain='Stable' {cbos}
group by domain, service
order by dcount DESC limit 5)
Union
(select count(distinct(cpims_ovc_id)) as dcount,
domain, service from vw_cpims_dash_list_served
Where domain='Safe' {cbos}
group by domain, service
order by dcount DESC limit 5)
union
(select count(distinct(cpims_ovc_id)) as dcount,
domain, service from vw_cpims_dash_list_served
Where domain='Schooled' {cbos}
group by domain, service
order by dcount DESC limit 5)
) x
order by domain asc, dcount desc
'''

# ============= Section 5 ===========================

QUERIES['5A'] = '''
SELECT count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'Active' as services
from vw_cpims_registration_fy22 where exit_status='ACTIVE' {cbos}
UNION
Select count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'Current Case Plan' as services
from vw_cpims_case_plan where ('2022-09-30' - date_of_event) <= 400 {cbos}
'''

QUERIES['5B'] = '''
Select count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, graduationpath as services
from vw_cpims_benchmark_achieved_v1
where (current_date - date_of_event) <= 400 {cbos}
group by graduationpath
'''

QUERIES['5C'] = '''
select count(distinct(household_id)) as dcount,
graduation_pathway, 'SMAL' as sex_id
from vw_cpims_benchmark where date_of_event > '2022-03-31' {cbos}
group by graduation_pathway
'''

QUERIES['5D'] = '''
Select count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'Current CPARA' as services
from vw_cpims_cpara_final where (current_date - date_of_event) <= 400 {cbos}
'''

QUERIES['5E'] = '''
select count(distinct(household)) as dcount, agency, 'SMAL' as sex_id
from vw_cpims_dash_caseload {ocbos} group by agency
'''

QUERIES['5F'] = '''
select * from (
select count(distinct(household)) as dcount, agency,
'All Households' as services from vw_cpims_dash_caseload
where agency is not null and not exists
(select household_id from vw_cpims_dash_case_plan where
vw_cpims_dash_caseload.household = vw_cpims_dash_case_plan.household_id) {cbos}
group by agency
UNION
select count(distinct(household_id)) as dcount, agency,
'HH with case plans' as services
from vw_cpims_dash_case_plan where agency is not null {cbos} group by agency
) y order by dcount asc
'''

QUERIES['5G'] = '''
select count(distinct(household_id)) as dcount, mechanism, agency
from vw_cpims_dash_case_plan where agency is not null {cbos}
group by mechanism, agency
'''

QUERIES['5H'] = '''
Select count(distinct(cpims_ovc_id)) as dcount,
graduationpath as services, agency
from vw_cpims_benchmark_achieved_v1
where (current_date - date_of_event) <= 400 {cbos}
group by agency, graduationpath
'''

QUERIES['5I'] = '''
select * from (
select count(distinct(household)) as dcount, 'SMAL' as sex_id,
'BM01: HIV Risk assessment done and HIV testing referrals completed' as benchmark
from vw_cpims_benchmark_achieved_v1 where bench1 = 1
and date_of_event < '2022-04-01' {cbos} group by bench1
UNION
select count(distinct(household)) as dcount, 'SMAL' as sex_id,
'BM02: Caregivers know the HIV+ status of the children they care as well as their own' as benchmark
from vw_cpims_benchmark_achieved_v1 where bench2 = 1
and date_of_event < '2022-04-01' {cbos} group by bench2
UNION
select count(distinct(household)) as dcount, 'SMAL' as sex_id,
'BM03: HIV+ persons in the household have been on ART for last 12 months' as benchmark
from vw_cpims_benchmark_achieved_v1 where bench3 = 1
and date_of_event < '2022-04-01' {cbos} group by bench3
UNION
select count(distinct(household)) as dcount, 'SMAL' as sex_id,
'BM04: Enrolled women/ adolescent girls who are/become pregnant receive HIV testing' as benchmark
from vw_cpims_benchmark_achieved_v1 where bench4 = 1
and date_of_event < '2022-04-01' {cbos} group by bench4
UNION
select count(distinct(household)) as dcount, 'SMAL' as sex_id,
'BM05: Adolescents and their caregivers have knowledge to decrease their HIV risk' as benchmark
from vw_cpims_benchmark_achieved_v1 where bench5 = 1
and date_of_event < '2022-04-01' {cbos} group by bench5
UNION
select count(distinct(household)) as dcount, 'SMAL' as sex_id,
'BM06: Children living with chronic illness/disability receive treatment' as benchmark
from vw_cpims_benchmark_achieved_v1 where bench6 = 1
and date_of_event < '2022-04-01' {cbos} group by bench6
UNION
select count(distinct(household)) as dcount, 'SMAL' as sex_id,
'BM07: HH able to provide a minimum of two meals/day' as benchmark
from vw_cpims_benchmark_achieved_v1 where bench7 = 1
and date_of_event < '2022-04-01' {cbos} group by bench7
UNION
select count(distinct(household)) as dcount, 'SMAL' as sex_id,
'BM08: HH able to pay for child(ren)’s basic needs' as benchmark
from vw_cpims_benchmark_achieved_v1 where bench8 = 1
and date_of_event < '2022-04-01' {cbos} group by bench8
UNION
select count(distinct(household)) as dcount, 'SMAL' as sex_id,
'BM09: HH able to pay for emergency expenses' as benchmark
from vw_cpims_benchmark_achieved_v1 where bench9 = 1
and date_of_event < '2022-04-01' {cbos} group by bench9
UNION
select count(distinct(household)) as dcount, 'SMAL' as sex_id,
'BM10:The caregiver has demonstrated knowledge on access to critical services' as benchmark
from vw_cpims_benchmark_achieved_v1 where bench10 = 1
and date_of_event < '2022-04-01' {cbos} group by bench10
UNION
select count(distinct(household)) as dcount, 'SMAL' as sex_id,
'BM11: Child-headed HHs have received child and social protection services' as benchmark
from vw_cpims_benchmark_achieved_v1 where bench11 = 1
and date_of_event < '2022-04-01' {cbos} group by bench11
UNION
select count(distinct(household)) as dcount, 'SMAL' as sex_id,
'BM12: All children in the HH able to participate in daily activities and engage with others' as benchmark
from vw_cpims_benchmark_achieved_v1 where bench12 = 1
and date_of_event < '2022-04-01' {cbos} group by bench12
UNION
select count(distinct(household)) as dcount, 'SMAL' as sex_id,
'BM13: Children at risk of abuse have been referred to and are receiving appropriate services' as benchmark
from vw_cpims_benchmark_achieved_v1 where bench13 = 1
and date_of_event < '2022-04-01' {cbos} group by bench13
UNION
select count(distinct(household)) as dcount, 'SMAL' as sex_id,
'BM14: Caregivers can identify individual or group providing social or emotional support' as benchmark
from vw_cpims_benchmark_achieved_v1 where bench14 = 1
and date_of_event < '2022-04-01' {cbos} group by bench14
UNION
select count(distinct(household)) as dcount, 'SMAL' as sex_id,
'BM15: Caregivers have completed a parenting skills or able to clearly articulate positive parenting' as benchmark
from vw_cpims_benchmark_achieved_v1 where bench15 = 1
and date_of_event < '2022-04-01' {cbos} group by bench15
UNION
select count(distinct(household)) as dcount, 'SMAL' as sex_id,
'BM16: All 6-17 children enrolled and attend school regularly' as benchmark
from vw_cpims_benchmark_achieved_v1 where bench16 = 1
and date_of_event < '2022-04-01' {cbos} group by bench16
UNION
select count(distinct(household)) as dcount, 'SMAL' as sex_id,
'BM17: Adolescents enrolled in vocational attend regularly' as benchmark
from vw_cpims_benchmark_achieved_v1 where bench17 = 1
and date_of_event < '2022-04-01' {cbos} group by bench17
) x order by benchmark asc
'''

QUERIES['5J'] = '''
select * from (
select count(distinct(household_id)) as dcount,
'SMAL' as sex_id, 'BM1: All children, adolescents, and caregivers in the household have known HIV status or a test is not required based on risk assessment' as benchmark from vw_cpims_benchmark
where benchmark_1 = 1 and date_of_event > '2022-03-31' {cbos}
group by benchmark_1
UNION
select count(distinct(household_id)) as dcount,
'SMAL' as sex_id, 'BM2: All HIV+ children, adolescents, and caregivers in the household with a viral load result documented in the medical record and/or laboratory information systems (LIS) have been virally suppressed for the last 12 months' as benchmark from vw_cpims_benchmark
where benchmark_2 = 1 and date_of_event > '2022-03-31' {cbos}
group by benchmark_2
UNION
select count(distinct(household_id)) as dcount,
'SMAL' as sex_id, 'BM3: All adolescents 10-17 years of age in the household have key knowledge about preventing HIV infection' as benchmark from vw_cpims_benchmark
where benchmark_3 = 1 and date_of_event > '2022-03-31' {cbos}
group by benchmark_3
UNION
select count(distinct(household_id)) as dcount,
'SMAL' as sex_id, 'BM4: No children < 5 years in the household are undernourished' as benchmark from vw_cpims_benchmark
where benchmark_4 = 1 and date_of_event > '2022-03-31' {cbos}
group by benchmark_4
UNION
select count(distinct(household_id)) as dcount,
'SMAL' as sex_id, 'BM5: Caregivers are able to access money (without selling productive assets) to pay for school fees, medical costs (buy medicine, transport to facility etc), legal and other administrative fees (related to guardianship, civil registration, or inheritance) for children 0-17 years' as benchmark from vw_cpims_benchmark
where benchmark_5 = 1 and date_of_event > '2022-03-31' {cbos}
group by benchmark_5
UNION
select count(distinct(household_id)) as dcount,
'SMAL' as sex_id, 'BM6: No children, adolescents, and caregivers in the household report experiences of violence (including physical violence, emotional violence, sexual violence, gender-based violence, and neglect) in the last six months' as benchmark from vw_cpims_benchmark
where benchmark_6 = 1 and date_of_event > '2022-03-31' {cbos}
group by benchmark_6
UNION
select count(distinct(household_id)) as dcount,
'SMAL' as sex_id, 'BM7: All children and adolescents in the household are under the care of a stable adult caregiver' as benchmark from vw_cpims_benchmark
where benchmark_7 = 1 and date_of_event > '2022-03-31' {cbos}
group by benchmark_7
UNION
select count(distinct(household_id)) as dcount,
'SMAL' as sex_id, 'BM8: All children <18 years have legal proof of identity' as benchmark from vw_cpims_benchmark
where benchmark_8 = 1 and date_of_event > '2022-03-31' {cbos}
group by benchmark_8
UNION
select count(distinct(household_id)) as dcount,
'SMAL' as sex_id, 'BM9: All school-aged children (4-17) and adolescents aged 18-20 enrolled in secondary school in the household regularly attended school and progressed during the last year.' as benchmark from vw_cpims_benchmark
where benchmark_9 = 1 and date_of_event > '2022-03-31' {cbos}
group by benchmark_9
) x order by benchmark asc
'''

QUERIES['5K'] = '''
Select count(distinct(cpims_ovc_id)) as dcount,
 cpara_score as services, 'SMAL' as sex_id
from vw_cpims_benchmark
where (current_date - date_of_event) <= 400 {cbos}
group by cpara_score order by cpara_score asc
'''

QUERIES['5L'] = '''
Select count(distinct(cpims_ovc_id)) as dcount,
 cpara_score as benchmark_total_scores, 'SMAL' as sex_id
from vw_cpims_benchmark_achieved_v1
where (current_date - date_of_event) <= 400 {cbos}
group by cpara_score order by cpara_score asc
'''

# ==== Section 6 ===============================

QUERIES['6A'] = '''
select count(distinct(cpims_ovc_id)) as dcount,
'Case load' as agency, 'Case load' as services
from vw_cpims_dash_caseload {ocbos}
UNION
select count(distinct(cpims_ovc_id)) as dcount,
'Active' as agency, 'Program status' as services
from vw_cpims_dash_caseload where exit_status='ACTIVE' {cbos}
UNION
select count(distinct(cpims_ovc_id)) as dcount,
'Transfers' as agency, 'Program status' as services
from vw_cpims_dash_caseload
WHERE (vw_cpims_dash_caseload.exit_reason = 'Transferred to PEPFAR partner' AND exit_status='EXITED'
OR vw_cpims_dash_caseload.exit_reason = 'Transferred to Non-PEPFAR partner' AND exit_status='EXITED') {cbos}
UNION
select count(distinct(cpims_ovc_id)) as dcount, 'Exits' as agency, 'Program status' as services
from vw_cpims_dash_caseload
WHERE (vw_cpims_dash_caseload.exit_reason <> 'Transferred to PEPFAR partner' AND exit_status='EXITED'
OR vw_cpims_dash_caseload.exit_reason <> 'Transferred to Non-PEPFAR partner' AND exit_status='EXITED') {cbos}
'''

QUERIES['6B'] = '''
select sum(count) as dcount, 'OVC_SERV' AS mechanism,
'OVC_SERV_FY' AS agency FROM (
select sum(served) as count, mechanism, agency
from vw_Active_Beneficiary_APR22 {ocbos}
group by mechanism, agency
UNION
select sum(graduated) as count, mechanism, agency
from vw_cpims_dash_graduated {ocbos} group by mechanism, agency
) srv
UNION ALL
select sum(count) as dcount, 'OVC_SERV - >18' AS mechanism,
'OVC_SERV - >18 & <18' AS agency FROM (
select sum(served) as count
from vw_Active_Beneficiary_APR22 where agerange = 'f.[18-20yrs]' {cbos}
UNION
select sum(graduated) as count
from vw_cpims_dash_graduated where agerange = 'f.[18-20yrs]' {cbos}
) srv
UNION ALL
select sum(count) as dcount, 'OVC_SERV - <18' AS mechanism,
'OVC_SERV - >18 & <18' AS agency FROM (
select sum(served) as count
from vw_Active_Beneficiary_APR22 where agerange <> 'f.[18-20yrs]' {cbos}
UNION
select sum(graduated) as count
from vw_cpims_dash_graduated where agerange <> 'f.[18-20yrs]' {cbos}
) srv
UNION ALL
select count(hivinfo) as dcount, hivinfo AS mechanism, 'HIV Info' as agency
from vw_cpims_dash_hivstat {ocbos} group by hivinfo
UNION ALL
select sum(hivstat) as dcount, ovchivstatus as mechanism,
'HIV Status' as agency
from vw_cpims_dash_hivstat where hivinfo ='KNOWN HIV Info' {cbos}
group by ovchivstatus
UNION ALL
select sum(hivstat) as dcount, artstatus as mechanism, 'ART Status' as agency
from vw_cpims_dash_hivstat where hivinfo ='KNOWN HIV Info'
and ovchivstatus='POSITIVE' {cbos} group by artstatus
'''

QUERIES['6C'] = '''
select sum(count) as dcount, gender as sex_id, agerange FROM (
select sum(served) as count, gender, agerange
from vw_Active_Beneficiary_APR22 where agerange <> 'f.[18-20yrs]' {cbos}
group by gender, agerange
UNION
select sum(graduated) as count, gender, agerange
from vw_cpims_dash_graduated where agerange <> 'f.[18-20yrs]' {cbos}
group by gender, agerange
) srv
group by gender, agerange
'''

QUERIES['6D'] = '''
select sum(not_served) as dcount, agency, 'SMAL' as sex_id
from vw_cpims_dash_not_served {ocbos} group by agency
order by dcount desc
'''

QUERIES['6E'] = '''
select sum(dcount) as dcount, agency, 'SMAL' as sex_id from (
select sum(not_served) as dcount, agency
from vw_cpims_dash_not_served {ocbos} group by agency
UNION ALL
select sum(attrition) as dcount, agency
from vw_cpims_dash_attrition {ocbos} group by agency
) x
group by agency
order by dcount desc
'''

QUERIES['6F'] = '''
select sum(attrition) as dcount, exit_reason, agency, 'SMAL' as sex_id
from vw_cpims_dash_attrition {ocbos} group by exit_reason, agency
order by dcount desc
'''

QUERIES['6G'] = '''
select sum(not_served) as dcount, mechanism, agency
from vw_cpims_dash_not_served {ocbos} group by mechanism, agency
'''

QUERIES['6H'] = '''
select sum(dct) as dcount, agency, 'Female' as sex_id from (
select sum(not_served) as dct, agency
from vw_cpims_dash_not_served {ocbos} group by agency
UNION ALL
select sum(attrition) as dct, agency
from vw_cpims_dash_attrition {ocbos} group by agency
) srv
group by agency
UNION ALL
select count(distinct(cpims_ovc_id)) as dcount, agency, 'Male' as sex_id
from vw_cpims_dash_caseload {ocbos} group by agency
'''

QUERIES['6I'] = '''
select agency, sum(ovc_serv) as dcount
from report_cop_targets where is_void = False group by agency
'''

QUERIES['6J'] = '''
select agency, sum(ovc_serv) as dcount
from report_cop_targets where is_void = False
and agency is null group by agency
'''

QUERIES['6K'] = '''
select agency, sum(ovc_serv) as dcount
from report_cop_targets where is_void = False
and agency is null group by agency
'''

QUERIES['6L'] = '''
select agency, sum(ovc_serv) as dcount
from report_cop_targets where is_void = False
and agency is null group by agency
'''

QUERIES['6M'] = '''
select agency, sum(ovc_serv) as dcount
from report_cop_targets where is_void = False
and agency is null group by agency
'''

QUERIES['6N'] = '''
select agency, sum(ovc_serv) as dcount
from report_cop_targets where is_void = False
and agency is null group by agency
'''

QUERIES['6P'] = '''
select agency, sum(ovc_serv) as dcount
from report_cop_targets where is_void = False
and agency is null group by agency
'''

QUERIES['6Q'] = '''
select agency, sum(ovc_serv) as dcount
from report_cop_targets where is_void = False
and agency is null group by agency
'''

QUERIES['6R'] = '''
select agency, sum(ovc_serv) as dcount
from report_cop_targets where is_void = False
and agency is null group by agency
'''

QUERIES['6S'] = '''
select agency, sum(ovc_serv) as dcount
from report_cop_targets where is_void = False
and agency is null group by agency
'''

QUERIES['6T'] = '''
select agency, sum(ovc_serv) as dcount
from report_cop_targets where is_void = False
and agency is null group by agency
'''

# ================== MER Reporting ========================

QUERIES['7A'] = '''
select * from (
select count(distinct(cpims_ovc_id)) as dcount,
'Case load' as agency, 'Case load' as services
from vw_cpims_dash_caseload {ocbos}
UNION
select count(distinct(cpims_ovc_id)) as dcount,
'Active' as agency, 'Program status' as services
from vw_cpims_dash_caseload where exit_status='ACTIVE' {cbos}
UNION
select count(distinct(cpims_ovc_id)) as dcount,
'Transfers' as agency, 'Program status' as services
from vw_cpims_dash_caseload
WHERE (vw_cpims_dash_caseload.exit_reason = 'Transferred to PEPFAR partner' AND exit_status='EXITED'
OR vw_cpims_dash_caseload.exit_reason = 'Transferred to Non-PEPFAR partner'  AND exit_status='EXITED')
{cbos}
UNION
select count(distinct(cpims_ovc_id)) as dcount, 'Exits' as agency, 'Program status' as services
from vw_cpims_dash_caseload
WHERE (vw_cpims_dash_caseload.exit_reason <> 'Transferred to PEPFAR partner' AND exit_status='EXITED'
OR vw_cpims_dash_caseload.exit_reason <> 'Transferred to Non-PEPFAR partner'  AND exit_status='EXITED')
{cbos}
) x order by services asc
'''

QUERIES['7D'] = '''
Select count(distinct(cpims_ovc_id)) AS dcount,
'SMAL' as sex_id, 'Positive' as hivstat
from vw_cpims_registration where exit_status='ACTIVE'
and ovchivstatus='POSITIVE' {cbos}
UNION
Select count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'On ART' as hivstat
from vw_cpims_registration where exit_status='ACTIVE'
and ovchivstatus='POSITIVE' AND artstatus='ART' {cbos}
UNION
Select count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'VL Accessed' as hivstat
from vw_cpims_viral_load {ocbos}
UNION
Select count(distinct(v.cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'Valid VL' as hivstat
from vw_cpims_viral_load v
inner join (
select cpims_ovc_id, max(date_of_event) as most_current_vl_date
from vw_cpims_viral_load
group by cpims_ovc_id ) vl on v.cpims_ovc_id = vl.cpims_ovc_id
and v.date_of_event=vl.most_current_vl_date
where current_date - vl.most_current_vl_date <= 400 {vcbos}
UNION
Select count(distinct(v.cpims_ovc_id)) AS dcount,
'SMAL' as sex_id, 'Suppressed' as hivstat
from vw_cpims_viral_load v
inner join (
select cpims_ovc_id, max(date_of_event) as most_current_vl_date
from vw_cpims_viral_load
group by cpims_ovc_id ) vl on v.cpims_ovc_id = vl.cpims_ovc_id
and v.date_of_event=vl.most_current_vl_date
where current_date - vl.most_current_vl_date <= 400
and v.viral_load < 1001 {vcbos}
UNION
Select count(distinct(v.cpims_ovc_id)) AS dcount,
'SMAL' as sex_id, 'Not Suppressed' as hivstat
from vw_cpims_viral_load v
inner join (
select cpims_ovc_id, max(date_of_event) as most_current_vl_date
from vw_cpims_viral_load
group by cpims_ovc_id ) vl on v.cpims_ovc_id=vl.cpims_ovc_id
and v.date_of_event=vl.most_current_vl_date
where current_date - vl.most_current_vl_date <=400
and v.viral_load > 1000 {vcbos}
'''

QUERIES['7C'] = '''
select sum(x.cnt) as dcount, 'SMAL' as sex_id,
'OVC_SERV' as hivstat from
(
Select count(distinct(cpims_ovc_id)) as cnt
from vw_cpims_active_beneficiary {ocbos}
UNION ALL
Select count(distinct(cpims_ovc_id)) as cnt
from vw_cpims_benchmark_achieved_v1 where (current_date - date_of_event) <= 400
AND cpara_score = 17 {cbos}
) x
UNION
Select count(distinct(cpims_ovc_id)) AS dcount,
'SMAL' as sex_id,
CASE
when ovchivstatus='POSITIVE' THEN 'HIV Status +Ve'
when ovchivstatus='NEGATIVE' THEN 'HIV Status -Ve'
when ovchivstatus='NOT KNOWN' THEN 'HIV Status Unknown'
when ovchivstatus='HIV Test Not Required' THEN 'HIV Test not Required'
when ovchivstatus='HIV Referred For Testing' THEN 'HIV Referred For Testing'
ELSE 'Others' END AS hivstat
from vw_cpims_registration where cpims_ovc_id in
(select distinct(x.cpims_ovc_id) from
(
Select distinct(cpims_ovc_id)
from vw_cpims_active_beneficiary {ocbos}
UNION ALL
Select distinct(cpims_ovc_id)
from vw_cpims_benchmark_achieved_v1 where (current_date - date_of_event) <= 400
AND cpara_score = 17 {cbos}
) x )
and exit_status='ACTIVE' {cbos}
group by ovchivstatus
'''

QUERIES['7B'] = '''
select sum(count) as dcount, 'OVC_SERV' AS mechanism,
'OVC_SERV_FY' AS agency FROM (
select sum(served) as count, mechanism, agency
from vw_Active_Beneficiary_APR22 {ocbos} group by mechanism, agency
UNION
select sum(graduated) as count, mechanism, agency
from vw_cpims_dash_graduated {ocbos} group by mechanism, agency
) srv
UNION ALL
select sum(count) as dcount, 'OVC_SERV - >18' AS mechanism,
'OVC_SERV - >18 & <18' AS agency FROM (
select sum(served) as count
from vw_Active_Beneficiary_APR22 where agerange = 'f.[18-20yrs]' {cbos}
UNION
select sum(graduated) as count
from vw_cpims_dash_graduated where agerange = 'f.[18-20yrs]' {cbos}
) srv
UNION ALL
select sum(count) as dcount, 'OVC_SERV - <18' AS mechanism,
'OVC_SERV - >18 & <18' AS agency FROM (
select sum(served) as count
from vw_Active_Beneficiary_APR22 where agerange <> 'f.[18-20yrs]' {cbos}
UNION
select sum(graduated) as count
from vw_cpims_dash_graduated where agerange <> 'f.[18-20yrs]' {cbos}
) srv
UNION ALL
select count(hivinfo) as dcount, hivinfo AS mechanism, 'HIV Info' as agency
from vw_cpims_dash_hivstat {ocbos} group by hivinfo

UNION ALL
select sum(hivstat) as dcount, ovchivstatus as mechanism,
'HIV Status' as agency
from vw_cpims_dash_hivstat where hivinfo ='KNOWN HIV Info' {cbos}
group by ovchivstatus

UNION ALL
select sum(hivstat) as dcount, artstatus as mechanism, 'ART Status' as agency
from vw_cpims_dash_hivstat where hivinfo ='KNOWN HIV Info'
and ovchivstatus='POSITIVE' {cbos} group by artstatus
'''

QUERIES['7E'] = '''
SELECT count(distinct(cpims_ovc_id)) as dcount,
'Male' as sex_id, 'Known HIV Status' as hivstat
from vw_cpims_registration where exit_status='ACTIVE' {cbos}
UNION
Select count(distinct(cpims_ovc_id)) AS dcount,
'Male' as sex_id, 'On ART' as hivstat
from vw_cpims_registration where exit_status='ACTIVE'
and ovchivstatus='POSITIVE' {cbos}
UNION
Select count(distinct(v.cpims_ovc_id)) as dcount,
'Male' as sex_id, 'Suppression' as hivstat
from vw_cpims_viral_load v
inner join (
select cpims_ovc_id, max(date_of_event) as most_current_vl_date
from vw_cpims_viral_load
group by cpims_ovc_id ) vl on v.cpims_ovc_id = vl.cpims_ovc_id
and v.date_of_event=vl.most_current_vl_date
where current_date - vl.most_current_vl_date <= 400 {vcbos}
UNION
Select count(distinct(cpims_ovc_id)) AS dcount,
'Female' as sex_id, 'Known HIV Status' as hivstat
from vw_cpims_registration where exit_status='ACTIVE'
and (ovchivstatus='POSITIVE' or ovchivstatus='NEGATIVE'
or ovchivstatus='NOT KNOWN' or ovchivstatus='HIV Test Not Required'
or ovchivstatus='HIV Referred For Testing') {cbos}
UNION
Select count(distinct(cpims_ovc_id)) as dcount,
'Female' as sex_id, 'On ART' as hivstat
from vw_cpims_registration where exit_status='ACTIVE'
and ovchivstatus='POSITIVE' AND artstatus='ART' {cbos}
UNION
Select count(distinct(v.cpims_ovc_id)) AS dcount,
'Female' as sex_id, 'Suppression' as hivstat
from vw_cpims_viral_load v
inner join (
select cpims_ovc_id, max(date_of_event) as most_current_vl_date
from vw_cpims_viral_load
group by cpims_ovc_id ) vl on v.cpims_ovc_id = vl.cpims_ovc_id
and v.date_of_event=vl.most_current_vl_date
where current_date - vl.most_current_vl_date <= 400
and v.viral_load < 1001 {vcbos}
'''


# ======= Section 8 =======================

QUERIES['8A'] = '''
select count(distinct(cpims_ovc_id)) as dcount, agency,
CASE
when ovchivstatus='POSITIVE' THEN 'HIV+'
ELSE 'Case load and not HIV+' END AS services
from vw_cpims_dash_caseload where cbo is not NULL {cbos}
group by agency, services
order by agency asc, services desc, dcount desc
'''

QUERIES['8B'] = '''
select count(distinct(cpims_ovc_id)) as dcount, mechanism as ip,
CASE
when ovchivstatus='POSITIVE' THEN 'HIV+'
ELSE 'Case load and not HIV+' END AS services
from vw_cpims_dash_caseload where cbo is not NULL {cbos}
group by mechanism, services, agency
order by agency asc, services desc, dcount desc
'''

QUERIES['8C'] = '''
select count(distinct(cpims_ovc_id)) as dcount, cbo as lip,
CASE
when ovchivstatus='POSITIVE' THEN 'HIV+'
ELSE 'Case load and not HIV+' END AS services
from vw_cpims_dash_caseload where cbo is not NULL {cbos}
group by cbo, services, agency
order by agency asc, services desc, dcount desc
'''

QUERIES['8D'] = '''
select count(distinct(cpims_ovc_id)) as dcount, county,
CASE
when ovchivstatus='POSITIVE' THEN 'HIV+'
ELSE 'Case load and not HIV+' END AS services
from vw_cpims_dash_caseload where cbo is not NULL and county is not NULL {cbos}
group by county, services, agency
order by agency asc, services desc, dcount desc
'''

QUERIES['8E'] = '''
select count(distinct(cpims_ovc_id)) as dcount, agency,
CASE
when artstatus='ART' THEN 'On ART'
ELSE 'Not on ART' END AS services
from vw_cpims_dash_caseload where ovchivstatus='POSITIVE'
and cbo is not NULL {cbos}
group by agency, services
order by agency asc, services asc, dcount desc
'''

QUERIES['8F'] = '''
select count(distinct(cpims_ovc_id)) as dcount, mechanism as ip,
CASE
when artstatus='ART' THEN 'On ART'
ELSE 'Not on ART' END AS services
from vw_cpims_dash_caseload
where ovchivstatus='POSITIVE' and cbo is not NULL {cbos}
group by mechanism, services, agency
order by agency asc, services asc, dcount desc
'''

QUERIES['8G'] = '''
select count(distinct(cpims_ovc_id)) as dcount, cbo as lip,
CASE
when artstatus='ART' THEN 'On ART'
ELSE 'Not on ART' END AS services
from vw_cpims_dash_caseload
where ovchivstatus='POSITIVE' and cbo is not NULL {cbos}
group by cbo, services, agency
order by agency asc, services asc, dcount desc
'''

QUERIES['8H'] = '''
select count(distinct(cpims_ovc_id)) as dcount, county,
CASE
when artstatus='ART' THEN 'On ART'
ELSE 'Not on ART' END AS services
from vw_cpims_dash_caseload
where ovchivstatus='POSITIVE' and county is not NULL {cbos}
group by county, services, agency
order by agency asc, services asc, dcount desc
'''

QUERIES['8I'] = '''
select * from (
select count(distinct(cpims_ovc_id)) as dcount, agency,
'Valid VL' as services
from vw_cpims_dash_viral_load where agency is not null
and vl_period_validity='Valid' {cbos}
group by agency
UNION
select count(distinct(cpims_ovc_id)) as dcount, agency,
'On ART without valid VL' as services
from vw_cpims_dash_caseload where ovchivstatus='POSITIVE' and artstatus='ART'
and cpims_ovc_id not in (
select distinct(cpims_ovc_id) from vw_cpims_dash_viral_load
where agency is not null and vl_period_validity='Valid' {cbos}
) {cbos}
group by agency
) x
order by agency asc, services desc, dcount desc
'''

QUERIES['8J'] = '''
select * from (
select count(distinct(cpims_ovc_id)) as dcount, mechanism as ip,
'Valid VL' as services
from vw_cpims_dash_viral_load where agency is not null
and vl_period_validity='Valid' {cbos}
group by mechanism
UNION
select count(distinct(cpims_ovc_id)) as dcount, mechanism as ip,
'On ART without valid VL' as services
from vw_cpims_dash_caseload where ovchivstatus='POSITIVE'
and artstatus='ART' and agency is not null
and cpims_ovc_id not in (
select distinct(cpims_ovc_id) from vw_cpims_dash_viral_load
where agency is not null and vl_period_validity='Valid' {cbos}
) {cbos}
group by mechanism
) x
order by services desc, dcount desc
'''

QUERIES['8K'] = '''
select * from (
select count(distinct(cpims_ovc_id)) as dcount, cbo as lip,
'Valid VL' as services
from vw_cpims_dash_viral_load where cbo is not null
and vl_period_validity='Valid' {cbos}
group by cbo
UNION
select count(distinct(cpims_ovc_id)) as dcount, cbo as lip,
'On ART without valid VL' as services
from vw_cpims_dash_caseload where ovchivstatus='POSITIVE'
and artstatus='ART' and cbo is not null
and cpims_ovc_id not in (
select distinct(cpims_ovc_id) from vw_cpims_dash_viral_load
where agency is not null and vl_period_validity='Valid' {cbos}
) {cbos}
group by cbo
) x
order by services desc, dcount desc
'''

QUERIES['8L'] = '''
select * from (
select count(distinct(cpims_ovc_id)) as dcount, county,
'Valid VL' as services
from vw_cpims_dash_viral_load where county is not null
and vl_period_validity='Valid' {cbos}
group by county
UNION
select count(distinct(cpims_ovc_id)) as dcount, county,
'On ART without valid VL' as services
from vw_cpims_dash_caseload where ovchivstatus='POSITIVE'
and artstatus='ART' and county is not null
and cpims_ovc_id not in (
select distinct(cpims_ovc_id) from vw_cpims_dash_viral_load
where agency is not null and vl_period_validity='Valid' {cbos}
) {cbos}
group by county
) x
order by services desc, dcount desc
'''

QUERIES['8M'] = '''
select * from (
select count(distinct(cpims_ovc_id)) as dcount, agency,
'Suppressed' as services
from vw_cpims_dash_viral_load where agency is not null
and vl_period_validity='Valid' and (suppression = '0-400'
or suppression = '400 - 999'
or suppression = 'LDL') {cbos}
group by agency
UNION
select count(distinct(cpims_ovc_id)) as dcount, agency,
'On ART and not suppressed' as services
from vw_cpims_dash_caseload where ovchivstatus='POSITIVE' and artstatus='ART'
and cpims_ovc_id in (
select distinct(cpims_ovc_id) from vw_cpims_dash_viral_load
where agency is not null and vl_period_validity='Valid' {cbos}
)
and cpims_ovc_id not in (
select distinct(cpims_ovc_id) from vw_cpims_dash_viral_load
where agency is not null and vl_period_validity='Valid'
and (suppression = '0-400' or suppression = '400 - 999'
or suppression = 'LDL') {cbos}
)
group by agency
) x
order by services desc, dcount desc
'''


QUERIES['8N'] = '''
select * from (
select count(distinct(cpims_ovc_id)) as dcount, mechanism as ip,
'Suppressed' as services
from vw_cpims_dash_viral_load where agency is not null
and vl_period_validity='Valid' and (suppression = '0-400'
or suppression = '400 - 999'
or suppression = 'LDL') {cbos}
group by mechanism
UNION
select count(distinct(cpims_ovc_id)) as dcount, mechanism as ip,
'On ART and not suppressed' as services
from vw_cpims_dash_caseload where ovchivstatus='POSITIVE' and artstatus='ART'
and cpims_ovc_id in (
select distinct(cpims_ovc_id) from vw_cpims_dash_viral_load
where agency is not null and vl_period_validity='Valid' {cbos}
)
and cpims_ovc_id not in (
select distinct(cpims_ovc_id) from vw_cpims_dash_viral_load
where agency is not null and vl_period_validity='Valid'
and (suppression = '0-400' or suppression = '400 - 999'
or suppression = 'LDL') {cbos}
)
group by mechanism
) x
order by services desc, dcount desc
'''

QUERIES['8P'] = '''
select * from (
select count(distinct(cpims_ovc_id)) as dcount, cbo as lip,
'Suppressed' as services
from vw_cpims_dash_viral_load where agency is not null
and vl_period_validity='Valid' and (suppression = '0-400'
or suppression = '400 - 999'
or suppression = 'LDL') {cbos}
group by cbo
UNION
select count(distinct(cpims_ovc_id)) as dcount, cbo as lip,
'On ART and not suppressed' as services
from vw_cpims_dash_caseload where ovchivstatus='POSITIVE' and artstatus='ART'
and cpims_ovc_id in (
select distinct(cpims_ovc_id) from vw_cpims_dash_viral_load
where agency is not null and vl_period_validity='Valid' {cbos}
)
and cpims_ovc_id not in (
select distinct(cpims_ovc_id) from vw_cpims_dash_viral_load
where agency is not null and vl_period_validity='Valid'
and (suppression = '0-400' or suppression = '400 - 999'
or suppression = 'LDL') {cbos}
)
group by cbo
) x
order by services desc, dcount desc
'''

QUERIES['8Q'] = '''
select * from (
select count(distinct(cpims_ovc_id)) as dcount, county,
'Suppressed' as services
from vw_cpims_dash_viral_load where agency is not null and county is not null
and vl_period_validity='Valid' and (suppression = '0-400'
or suppression = '400 - 999'
or suppression = 'LDL') {cbos}
group by county
UNION
select count(distinct(cpims_ovc_id)) as dcount, county,
'On ART and not suppressed' as services
from vw_cpims_dash_caseload where ovchivstatus='POSITIVE' and artstatus='ART'
and cpims_ovc_id in (
select distinct(cpims_ovc_id) from vw_cpims_dash_viral_load
where agency is not null and county is not null
and vl_period_validity='Valid' {cbos}
)
and cpims_ovc_id not in (
select distinct(cpims_ovc_id) from vw_cpims_dash_viral_load
where agency is not null and county is not null and vl_period_validity='Valid'
and (suppression = '0-400' or suppression = '400 - 999'
or suppression = 'LDL') {cbos}
)
group by county
) x
order by services desc, dcount desc
'''

QUERIES['8R'] = '''
select count(distinct(cpims_ovc_id)) as dcount, agency, suppression
from vw_cpims_dash_viral_load where agency is not null
and suppression is not null
and vl_period_validity='Valid' group by agency, suppression
'''

QUERIES['8S'] = '''
select count(distinct(cpims_ovc_id)) as dcount,
CONCAT(agency, ' : ', suppression) as services, duration_on_art
from vw_cpims_dash_viral_load where agency is not null
and suppression is not null and duration_on_art is not null
and vl_period_validity='Valid'
group by agency, suppression, duration_on_art
order by duration_on_art
'''
