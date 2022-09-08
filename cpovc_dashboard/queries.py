QUERIES = {}

QUERIES['1A'] = '''
SELECT count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id
from vw_cpims_registration {ocbos} {oareas} {odate}
group by gender
'''

QUERIES['1B'] = '''
SELECT count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id,
CASE exit_status WHEN 'ACTIVE' THEN 'Current Caseload'
ELSE 'Exited(Left Program)' END AS active_status
from vw_cpims_registration {ocbos} {oareas} {odate}
group by gender, active_status
UNION
SELECT count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id, 'Ever Registered' AS active_status
from vw_cpims_registration {ocbos} {oareas} {odate}
group by gender
'''

QUERIES['1C'] = '''
SELECT count(cpims_ovc_id) as dcount,
'SMAL' as sex_id, exit_reason
from vw_cpims_registration where exit_status = 'EXITED' {cbos} {areas} {fdate}
group by exit_reason order by dcount desc
'''

QUERIES['1D'] = '''
SELECT count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id, 'Active' as services
from vw_cpims_registration where exit_status='ACTIVE' {cbos} {areas} {fdate}
group by gender
UNION
SELECT count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id, 'Has Birth Certificate' as services
from vw_cpims_registration where exit_status='ACTIVE'
and birthcert = 'HAS BIRTHCERT' {cbos} {areas} {fdate}
group by gender
UNION
SELECT count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id, 'Has Disability' as services
from vw_cpims_registration where exit_status='ACTIVE'
and ovcdisability = 'HAS DISABILITY' {cbos} {areas} {fdate}
group by gender
UNION
SELECT count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id, 'School Going' as services
from vw_cpims_registration where exit_status='ACTIVE'
and schoollevel != 'Not in School' {cbos} {areas} {fdate}
group by gender
'''

QUERIES['1E'] = '''
Select count(distinct(cpims_ovc_id)) AS dcount,
gender as sex_id,
CASE
when ovchivstatus='POSITIVE' THEN 'HIV Status +Ve'
when ovchivstatus='NEGATIVE' THEN 'HIV Status -Ve'
when ovchivstatus='NOT KNOWN' THEN 'HIV Status Unknown'
when ovchivstatus='HIV Test Not Required' THEN 'HIV Test not Required'
when ovchivstatus='HIV Referred For Testing' THEN 'HIV Referred For Testing'
ELSE 'Others' END AS hivstat
from vw_cpims_registration where exit_status='ACTIVE' {cbos} {areas} {fdate}
group by gender, ovchivstatus order by dcount DESC
'''

QUERIES['1F'] = '''
SELECT count(cpims_ovc_id) as dcount,
'SMAL' as sex_id, eligibility
from vw_cpims_registration {ocbos} {oareas} {odate}
group by eligibility order by dcount desc
'''

QUERIES['1G'] = '''
select sum(counts) as dcount, agency, 'SMAL' as sex_id
from vw_cpims_dash_caseload {ocbos} {oareas}
group by agency
'''

QUERIES['2A'] = '''
SELECT count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id, 'Active' as hivstat
from vw_cpims_registration where exit_status='ACTIVE' {cbos} {fdate}
group by gender
UNION
Select count(distinct(cpims_ovc_id)) AS dcount,
gender as sex_id, 'Positive' as hivstat
from vw_cpims_registration where exit_status='ACTIVE'
and ovchivstatus='POSITIVE' {cbos} {fdate} group by gender
UNION
Select count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id, 'On ART' as hivstat
from vw_cpims_registration where exit_status='ACTIVE'
and ovchivstatus='POSITIVE' AND artstatus='ART' {cbos} {fdate}
group by gender
UNION
Select count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id, 'VL Accessed' as hivstat
from vw_cpims_viral_load {ocbos}
group by gender
UNION
Select count(distinct(v.cpims_ovc_id)) as dcount,
v.gender as sex_id, 'Valid VL' as hivstat
from vw_cpims_viral_load v
inner join (
select cpims_ovc_id, max(date_of_event) as most_current_vl_date
from vw_cpims_viral_load
group by cpims_ovc_id ) vl on v.cpims_ovc_id = vl.cpims_ovc_id
and v.date_of_event=vl.most_current_vl_date
where current_date - vl.most_current_vl_date <= 400 {vcbos}
group by v.gender
UNION
Select count(distinct(v.cpims_ovc_id)) AS dcount,
v.gender as sex_id, 'Suppressed' as hivstat
from vw_cpims_viral_load v
inner join (
select cpims_ovc_id, max(date_of_event) as most_current_vl_date
from vw_cpims_viral_load
group by cpims_ovc_id ) vl on v.cpims_ovc_id = vl.cpims_ovc_id
and v.date_of_event=vl.most_current_vl_date
where current_date - vl.most_current_vl_date <= 400
and v.viral_load < 1001 {vcbos} group by v.gender
UNION
Select count(distinct(v.cpims_ovc_id)) AS dcount,
v.gender as sex_id, 'Not Suppressed' as hivstat
from vw_cpims_viral_load v
inner join (
select cpims_ovc_id, max(date_of_event) as most_current_vl_date
from vw_cpims_viral_load
group by cpims_ovc_id ) vl on v.cpims_ovc_id=vl.cpims_ovc_id
and v.date_of_event=vl.most_current_vl_date
where current_date - vl.most_current_vl_date <=400
and v.viral_load > 1000 {vcbos}
group by v.gender
'''

QUERIES['2B'] = '''
Select count(distinct(cpims_ovc_id)) as dcount, gender as sex_id, agerange
from vw_cpims_viral_load where (current_date - date_of_event) < 401
and viral_load > 1000 {cbos} group by gender, agerange
'''

QUERIES['2C'] = '''
select sum(x.cnt) as dcount, x.gender as sex_id,
'OVC_SERV' as hivstat from
(
Select count(distinct(cpims_ovc_id)) as cnt,
gender from vw_cpims_active_beneficiary
group by gender
UNION ALL
Select count(distinct(cpims_ovc_id)) as cnt, gender
from vw_cpims_benchmark_achieved_v1 where (current_date - date_of_event) <= 400
AND cpara_score = 17 group by gender
) x group by x.gender
UNION
Select count(distinct(cpims_ovc_id)) AS dcount,
gender as sex_id,
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
from vw_cpims_active_beneficiary
UNION ALL
Select distinct(cpims_ovc_id)
from vw_cpims_benchmark_achieved_v1 where (current_date - date_of_event) <= 400
AND cpara_score = 17
) x)
and exit_status='ACTIVE'
group by gender, ovchivstatus
'''

QUERIES['2D'] = '''
select sum(x.cnt) as dcount, x.gender as sex_id,
'OVC_SERV' as hivstat from
(
Select count(distinct(cpims_ovc_id)) as cnt,
gender from vw_cpims_active_beneficiary
WHERE age < 18
group by gender
UNION ALL
Select count(distinct(cpims_ovc_id)) as cnt, gender
from vw_cpims_benchmark_achieved_v1 where age < 18 AND (current_date - date_of_event) <= 400
AND cpara_score = 17 group by gender
) x group by x.gender
UNION
Select count(distinct(cpims_ovc_id)) AS dcount,
gender as sex_id,
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
from vw_cpims_active_beneficiary
UNION ALL
Select distinct(cpims_ovc_id)
from vw_cpims_benchmark_achieved_v1 where (current_date - date_of_event) <= 400
AND cpara_score = 17
) x)
and exit_status='ACTIVE'
group by gender, ovchivstatus
'''

QUERIES['2E'] = '''
SELECT count(distinct(cpims_ovc_id)) as dcount,
'Male' as sex_id, 'Known HIV Status' as hivstat
from vw_cpims_registration where exit_status='ACTIVE'
UNION
Select count(distinct(cpims_ovc_id)) AS dcount,
'Male' as sex_id, 'On ART' as hivstat
from vw_cpims_registration where exit_status='ACTIVE'
and ovchivstatus='POSITIVE'
UNION
Select count(distinct(v.cpims_ovc_id)) as dcount,
'Male' as sex_id, 'Suppression' as hivstat
from vw_cpims_viral_load v
inner join (
select cpims_ovc_id, max(date_of_event) as most_current_vl_date
from vw_cpims_viral_load
group by cpims_ovc_id ) vl on v.cpims_ovc_id = vl.cpims_ovc_id
and v.date_of_event=vl.most_current_vl_date
where current_date - vl.most_current_vl_date <= 400
UNION
Select count(distinct(cpims_ovc_id)) AS dcount,
'Female' as sex_id, 'Known HIV Status' as hivstat
from vw_cpims_registration where exit_status='ACTIVE'
and (ovchivstatus='POSITIVE' or ovchivstatus='NEGATIVE'
or ovchivstatus='NOT KNOWN' or ovchivstatus='HIV Test Not Required'
or ovchivstatus='HIV Referred For Testing')
UNION
Select count(distinct(cpims_ovc_id)) as dcount,
'Female' as sex_id, 'On ART' as hivstat
from vw_cpims_registration where exit_status='ACTIVE'
and ovchivstatus='POSITIVE' AND artstatus='ART'
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
and v.viral_load < 1001
'''

QUERIES['2F'] = '''
select sum(count) as dcount, mechanism, agency FROM (
select sum(served) as count, mechanism, agency
from vw_Active_Beneficiary_APR22 group by mechanism, agency
UNION
select sum(graduated) as count, mechanism, agency
from vw_cpims_dash_graduated group by mechanism, agency
) srv
group by Agency, Mechanism
'''

QUERIES['3A'] = '''
SELECT count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id, 'Active' as services
from vw_cpims_registration where exit_status='ACTIVE' group by gender
UNION
Select count(distinct(person_id)) AS dcount,
gender as sex_id, 'Served Two Quarters' as services
from vw_cpims_two_quarters where (current_date - date_of_event) <=200
group by gender
UNION
Select count(distinct(cpims_ovc_id)) as dcount,
gender, 'Case Plans' as services
from vw_cpims_case_plan where (current_date - date_of_event) <= 400
group by gender
/* UNION
Select count(distinct(cpims_ovc_id)) as dcount,
gender, 'CPARA' as services
from vw_cpims_cpara_v1 where (current_date - date_of_event) <= 400
group by gender */
UNION
Select count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id, 'Graduated' as services
from vw_cpims_benchmark_achieved_v1
where (current_date - date_of_event) <= 400
AND cpara_score = 17
group by gender
UNION
Select count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id, 'Active Beneficiary' as services
from vw_cpims_active_beneficiary
group by gender
UNION
select sum(x.cnt) as dcount, x.gender as sex_id,
'OVC_SERV' as hivstat from
(
Select count(distinct(cpims_ovc_id)) as cnt,
gender from vw_cpims_active_beneficiary
group by gender
UNION ALL
Select count(distinct(cpims_ovc_id)), gender
from vw_cpims_benchmark_achieved_v1 where (current_date - date_of_event) <= 400
AND cpara_score = 17 group by gender
) x group by x.gender
UNION
Select count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id, 'Exit without Graduation' as services
from vw_cpims_registration where exit_status='ACTIVE'
AND cpims_ovc_id NOT IN
(select distinct(vw_cpims_registration.cpims_ovc_id)
from vw_cpims_two_quarters )
group by gender
'''

QUERIES['3B'] = '''
Select count(distinct(household_id)) as dcount,
 'Case Plans' as services, 'SMAL' as sex_id
from vw_cpims_case_plan where (current_date - date_of_event) <= 400
UNION
Select count(distinct(household)) as dcount,
'CPARA' as services, 'SMAL' as sex_id
from vw_cpims_cpara_v1 where (current_date - date_of_event) <= 400
'''

QUERIES['3C'] = '''
Select count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, domain as services
from vw_cpims_list_served {ocbos} group by domain
'''

QUERIES['3D'] = '''
SELECT count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id, 'OVC Comprehensive' as services
from vw_cpims_registration where exit_status='ACTIVE' {cbos} group by gender
'''

QUERIES['3E'] = '''
Select count(distinct(cpims_ovc_id)) as dcount,
 cpara_score as benchmark, 'SMAL' as sex_id
from vw_cpims_benchmark_achieved_v1
where (current_date - date_of_event) <= 400
group by cpara_score
'''

QUERIES['3F'] = '''
select count(distinct(household_id)) as dcount,
'SMAL' as sex_id, 1 as benchmark from vw_cpims_benchmark
where benchmark_1 = 1 and date_of_event > '2022-03-31' group by benchmark_1
UNION
select count(distinct(household_id)) as dcount,
'SMAL' as sex_id, 2 as benchmark from vw_cpims_benchmark
where benchmark_2 = 1 and date_of_event > '2022-03-31' group by benchmark_2
UNION
select count(distinct(household_id)) as dcount,
'SMAL' as sex_id, 3 as benchmark from vw_cpims_benchmark
where benchmark_3 = 1 and date_of_event > '2022-03-31' group by benchmark_3
UNION
select count(distinct(household_id)) as dcount,
'SMAL' as sex_id, 4 as benchmark from vw_cpims_benchmark
where benchmark_4 = 1 and date_of_event > '2022-03-31' group by benchmark_4
UNION
select count(distinct(household_id)) as dcount,
'SMAL' as sex_id, 5 as benchmark from vw_cpims_benchmark
where benchmark_5 = 1 and date_of_event > '2022-03-31' group by benchmark_5
UNION
select count(distinct(household_id)) as dcount,
'SMAL' as sex_id, 6 as benchmark from vw_cpims_benchmark
where benchmark_6 = 1 and date_of_event > '2022-03-31' group by benchmark_6
UNION
select count(distinct(household_id)) as dcount,
'SMAL' as sex_id, 7 as benchmark from vw_cpims_benchmark
where benchmark_7 = 1 and date_of_event > '2022-03-31' group by benchmark_7
UNION
select count(distinct(household_id)) as dcount,
'SMAL' as sex_id, 8 as benchmark from vw_cpims_benchmark
where benchmark_8 = 1 and date_of_event > '2022-03-31' group by benchmark_8
UNION
select count(distinct(household_id)) as dcount,
'SMAL' as sex_id, 9 as benchmark from vw_cpims_benchmark
where benchmark_9 = 1 and date_of_event > '2022-03-31' group by benchmark_9;
'''

QUERIES['3G'] = '''
Select count(distinct(cpims_ovc_id)) as dcount,
 cpara_score as services, 'SMAL' as sex_id
from vw_cpims_benchmark
where (current_date - date_of_event) <= 400
group by  cpara_score
'''

QUERIES['3H'] = '''
Select count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id, service as services
from vw_cpims_list_served
group by gender, service
order by dcount desc limit 35
'''

QUERIES['3I'] = '''
Select count(distinct(cpims_ovc_id)) as dcount,
domain, 'SMAL' as sex_id
from vw_cpims_list_served
group by domain
order by dcount desc
'''

QUERIES['3J'] = '''
select count(distinct(cpims_ovc_id)) as dcount,
domain, agency from vw_cpims_dash_list_served
group by  agency, domain
'''

QUERIES['3K'] = '''
select count(distinct(cpims_ovc_id)) as dcount,
domain, agency from vw_cpims_dash_list_served
group by  mechanism, domain
'''

QUERIES['3L'] = '''
select count(distinct(cpims_ovc_id)) as dcount,
domain, service, agency from vw_cpims_dash_list_served
group by agency, domain, service
order by cnt DESC limit 10
'''

QUERIES['4A'] = '''
SELECT count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id, 'Active' as services
from vw_cpims_registration where exit_status='ACTIVE' {cbos} group by gender
UNION
Select count(distinct(cpims_ovc_id)) as dcount,
gender, 'Current Case Plan' as services
from vw_cpims_case_plan where (current_date - date_of_event) <= 400 {cbos}
group by gender
'''

QUERIES['4B'] = '''
Select count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id, graduationpath as services
from vw_cpims_benchmark_achieved_v1
where (current_date - date_of_event) <= 400
group by gender, graduationpath
'''

QUERIES['4C'] = '''
select count(distinct(household_id)) as dcount, Graduation_pathway
from vw_cpims_benchmark where date_of_event > '2022-03-31' {cbos}
group by graduation_pathway
'''

QUERIES['4D'] = '''
Select count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id, 'Current CPARA' as services
from vw_cpims_cpara_v1 where (current_date - date_of_event) <= 400 {cbos}
group by gender
'''

QUERIES['4E'] = '''
'''

QUERIES['4F'] = '''
select sum(hhcount) as dcount, agency, 'SMAL' as sex_id
from vw_cpims_dash_case_plan group by agency
'''

QUERIES['4G'] = '''
select sum(hhcount) as dcount, mechanism, agency
from vw_cpims_dash_case_plan
group by mechanism, agency
'''

QUERIES['4H'] = '''
'''

QUERIES['5A'] = '''
select sum(count) as dcount, 'OVC_SERV' AS mechanism,
'OVC_SERV_FY' AS agency FROM (
select sum(served) as count, mechanism, agency
from vw_Active_Beneficiary_APR22 group by mechanism, agency
UNION
select sum(graduated) as count, mechanism, agency
from vw_cpims_dash_graduated group by mechanism, agency
) srv
UNION ALL
select sum(count) as dcount, 'OVC_SERV - >18' AS mechanism,
'OVC_SERV - >18 & <18' AS agency FROM (
select sum(served) as count
from vw_Active_Beneficiary_APR22 where agerange = 'f.[18-20yrs]'
UNION
select sum(graduated) as count
from vw_cpims_dash_graduated where agerange = 'f.[18-20yrs]'
) srv
UNION ALL
select sum(count) as dcount, 'OVC_SERV - <18' AS mechanism,
'OVC_SERV - >18 & <18' AS agency FROM (
select sum(served) as count
from vw_Active_Beneficiary_APR22 where agerange <> 'f.[18-20yrs]'
UNION
select sum(graduated) as count
from vw_cpims_dash_graduated where agerange <> 'f.[18-20yrs]'
) srv
UNION ALL
select count(hivinfo) as dcount, hivinfo AS mechanism, 'HIV Info' as agency
from vw_cpims_dash_hivstat group by hivinfo

UNION ALL
select sum(hivstat) as dcount, ovchivstatus as mechanism,
'HIV Status' as agency
from vw_cpims_dash_hivstat where hivinfo ='KNOWN HIV Info'
group by ovchivstatus

UNION ALL
select sum(hivstat) as dcount, artstatus as mechanism, 'ART Status' as agency
from vw_cpims_dash_hivstat where hivinfo ='KNOWN HIV Info'
and ovchivstatus='POSITIVE' group by artstatus
'''

QUERIES['5B'] = '''
select sum(not_served) as dcount, agency, 'SMAL' as sex_id
from vw_cpims_dash_not_served group by agency
order by dcount desc
'''

QUERIES['5C'] = '''
select sum(not_served) as dcount, agency, 'SMAL' as sex_id
from vw_cpims_dash_not_served group by agency
UNION ALL
select sum(attrition) as dcount, agency, 'SMAL' as sex_id
from vw_cpims_dash_attrition group by agency
order by dcount
'''

QUERIES['5D'] = '''
select sum(attrition) as dcount, exit_reason, agency, 'SMAL' as sex_id
from vw_cpims_dash_attrition group by exit_reason, agency
order by dcount desc
'''

QUERIES['5E'] = '''
select sum(not_served) as dcount, mechanism, agency
from vw_cpims_dash_not_served group by mechanism, agency
'''

QUERIES['5F'] = '''
select sum(dct) as dcount, agency, 'Female' as sex_id from (
select sum(not_served) as dct, agency
from vw_cpims_dash_not_served group by agency
UNION ALL
select sum(attrition) as dct, agency
from vw_cpims_dash_attrition group by agency
) srv
group by agency
UNION ALL
select sum(counts) AS dcount, agency, 'Male' as sex_id
from vw_cpims_dash_caseload group by agency
'''

QUERIES['1P-0'] = '''
select dcount, agency, agency, exit_reason as schoollevel,
'Test' as mechanism from test_report
'''

QUERIES['6A'] = '''
select count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id, agerange
from vw_cpims_dash_caseload {ocbos} {oareas}
group by gender, agerange
'''

QUERIES['6B'] = '''
select count(distinct(cpims_ovc_id)) as dcount,
'Case load' as services, 'SMAL' as sex_id
from vw_cpims_dash_caseload
UNION
select count(distinct(cpims_ovc_id)) as dcount,
'Active' as services, 'SMAL' as sex_id
from vw_cpims_dash_caseload where exit_status='ACTIVE'
UNION
select count(distinct(cpims_ovc_id)) as dcount,
'Transfers' as services, 'SMAL' as sex_id
from vw_cpims_dash_caseload
WHERE vw_cpims_dash_caseload.exit_reason = 'Transferred to PEPFAR partner' AND exit_status='EXITED'
OR vw_cpims_dash_caseload.exit_reason = 'Transferred to Non-PEPFAR partner'  AND exit_status='EXITED'
UNION
select count(distinct(cpims_ovc_id)) as dcount, 'Exits' as services, 'SMAL' as sex_id
from vw_cpims_dash_caseload
WHERE vw_cpims_dash_caseload.exit_reason <> 'Transferred to PEPFAR partner' AND exit_status='EXITED'
OR vw_cpims_dash_caseload.exit_reason <> 'Transferred to Non-PEPFAR partner'  AND exit_status='EXITED'
'''

QUERIES['6C'] = '''
select count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id, schoollevel as school_level
from vw_cpims_dash_caseload {ocbos} {oareas}
group by gender, schoollevel
'''

QUERIES['6D'] = '''
SELECT count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id, 'Active' as services
from vw_cpims_dash_caseload where exit_status='ACTIVE' {cbos} {areas}
group by gender
UNION
SELECT count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id, 'Has Birth Certificate' as services
from vw_cpims_dash_caseload where exit_status='ACTIVE'
and birthcert = 'HAS BIRTHCERT' {cbos} {areas}
group by gender
UNION
SELECT count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id, 'Has Disability' as services
from vw_cpims_dash_caseload where exit_status='ACTIVE'
and ovcdisability = 'HAS DISABILITY' {cbos} {areas}
group by gender
UNION
SELECT count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id, 'School Going' as services
from vw_cpims_dash_caseload where exit_status='ACTIVE'
and schoollevel != 'Not in School' {cbos} {areas}
group by gender
'''

QUERIES['6E'] = '''
Select count(distinct(cpims_ovc_id)) AS dcount,
gender as sex_id,
CASE
when ovchivstatus='POSITIVE' THEN 'HIV Status +Ve'
when ovchivstatus='NEGATIVE' THEN 'HIV Status -Ve'
when ovchivstatus='NOT KNOWN' THEN 'HIV Status Unknown'
when ovchivstatus='HIV Test Not Required' THEN 'HIV Test not Required'
when ovchivstatus='HIV Referred For Testing' THEN 'HIV Referred For Testing'
ELSE 'Others' END AS hivstat
from vw_cpims_registration where exit_status='ACTIVE' {cbos} {areas} {fdate}
group by gender, ovchivstatus order by dcount DESC
'''

QUERIES['6F-0'] = '''
SELECT count(cpims_ovc_id) as dcount,
gender as sex_id, eligibility
from vw_cpims_registration {ocbos} {oareas} {odate}
group by gender, eligibility order by dcount desc
'''

QUERIES['6F'] = '''
SELECT count(cpims_ovc_id) as dcount,
'SMAL' as sex_id, eligibility
from vw_cpims_registration {ocbos} {oareas} {odate}
group by eligibility order by dcount desc
'''

QUERIES['6G-0'] = '''
SELECT count(cpims_ovc_id) as dcount,
gender as sex_id, exit_reason
from vw_cpims_registration where exit_status = 'EXITED' {cbos} {areas} {fdate}
group by gender, exit_reason order by dcount desc
'''

QUERIES['6G'] = '''
SELECT count(cpims_ovc_id) as dcount,
'SMAL' as sex_id, exit_reason
from vw_cpims_registration where exit_status = 'EXITED' {cbos} {areas} {fdate}
group by exit_reason order by dcount desc
'''

QUERIES['6H'] = '''
select count(distinct(cpims_ovc_id)) as dcount, gender as sex_id
from vw_cpims_registration where registration_date >'2021-09-30'
group by gender;
'''

QUERIES['6I'] = '''
select sum(counts) as dcount, agency, 'SMAL' as sex_id
from vw_cpims_dash_caseload {ocbos} {oareas}
group by agency
'''

QUERIES['6J'] = '''
select sum(counts) as dcount, eligibility, 'SMAL' as sex_id
from vw_cpims_dash_caseload {ocbos} {oareas}
group by eligibility
order by dcount desc
'''

QUERIES['6K'] = '''
select sum(counts) as dcount, 'SMAL' as sex_id, schoollevel from
vw_cpims_dash_caseload where schoollevel <> 'Not in School' {cbos} {areas}
group by schoollevel
'''

QUERIES['6L'] = '''
select sum(counts) as dcount, agency, schoollevel
from vw_cpims_dash_caseload where schoollevel <> 'Not in School' {cbos} {areas}
group by schoollevel, agency
'''

QUERIES['6M'] = '''
select sum(counts) as dcount, gender as sex_id from
vw_cpims_dash_caseload where schoollevel <> 'Not in School' {cbos} {areas}
group by gender
'''

QUERIES['6N'] = '''
select sum(counts) as dcount, gender as sex_id, schoollevel
from vw_cpims_dash_caseload where schoollevel <> 'Not in School' {cbos} {areas}
group by gender, schoollevel
'''

QUERIES['6P'] = '''
select sum(counts) as dcount, schoollevel, mechanism, agency
from vw_cpims_dash_caseload where schoollevel <> 'Not in School' {cbos} {areas}
group by schoollevel, mechanism, agency
order by agency, mechanism
'''
