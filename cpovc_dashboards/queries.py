QUERIES = {}

# ================= Section 1 =====================

QUERIES['1A'] = '''
SELECT count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id
from ft_cpims_registration where not (exit_status = 'EXITED' and
exit_reason = 'Duplicated') {cbos} {areas} {ftdates}
group by gender
'''

QUERIES['1B'] = '''
SELECT count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id,
CASE exit_status WHEN 'ACTIVE' THEN 'Current case load'
ELSE 'Exited(Left Program)' END AS active_status
from ft_cpims_registration where not (exit_status = 'EXITED' and
exit_reason = 'Duplicated') {cbos} {areas} {ftdates}
group by active_status
UNION
SELECT count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'Ever Registered' AS active_status
from ft_cpims_registration where not (exit_status = 'EXITED' and
exit_reason = 'Duplicated') {cbos} {areas} {ftdates}
'''

QUERIES['1C'] = '''
SELECT count(cpims_ovc_id) as dcount,
'SMAL' as sex_id, eligibility
from ft_cpims_registration where not (exit_status = 'EXITED' and
exit_reason = 'Duplicated') {cbos} {areas} {ftdates}
group by eligibility order by dcount desc
'''

QUERIES['1G'] = '''
SELECT count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, exit_reason
from ft_cpims_registration where exit_status = 'EXITED'
{cbos} {areas} {ftdates}
group by exit_reason order by dcount desc
'''

QUERIES['1D'] = '''
SELECT count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'Current case load' as services
from ft_cpims_registration where exit_status='ACTIVE'
{cbos} {areas} {areas} {ftdates}
UNION
SELECT count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'Has Birth Certificate' as services
from ft_cpims_registration where exit_status='ACTIVE'
and birthcert = 'HAS BIRTHCERT' {cbos} {areas} {ftdates}
UNION
SELECT count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'Has Disability' as services
from ft_cpims_registration where exit_status='ACTIVE'
and ovcdisability = 'HAS DISABILITY' {cbos} {areas} {ftdates}
UNION
SELECT count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'School Going' as services
from ft_cpims_registration where exit_status='ACTIVE'
and schoollevel != 'Not in School' {cbos} {areas} {ftdates}
'''

QUERIES['1E'] = '''
select sum(counts) as dcount, agency, 'SMAL' as sex_id
from ft_cpims_caseload {oftdates} {cbos} {areas}
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
from ft_cpims_registration where exit_status='ACTIVE' {cbos} {areas} {ftdates}
group by gender, ovchivstatus order by dcount DESC
'''

# ================= Section 2 =====================

QUERIES['2A'] = '''
select * from (
select count(distinct(cpims_ovc_id)) as dcount,
'Eligible for reporting' as services, 'SMAL' as sex_id
from ft_cpims_caseload {oftdates} {cbos}
UNION
select count(distinct(cpims_ovc_id)) as dcount,
'Case load' as services, 'SMAL' as sex_id
from ft_cpims_caseload where exit_status='ACTIVE' {cbos} {ftdates}
UNION
select count(distinct(cpims_ovc_id)) as dcount,
'Transfers' as services, 'SMAL' as sex_id
from ft_cpims_caseload
WHERE (ft_cpims_caseload.exit_reason = 'Transferred to PEPFAR partner' AND exit_status='EXITED'
OR ft_cpims_caseload.exit_reason = 'Transferred to Non-PEPFAR partner' AND exit_status='EXITED')
{cbos} {ftdates}
UNION
select count(distinct(cpims_ovc_id)) as dcount, 'Exits' as services, 'SMAL' as sex_id
from ft_cpims_caseload
WHERE exit_status='EXITED' AND (
ft_cpims_caseload.exit_reason = ' Adoption'
OR ft_cpims_caseload.exit_reason = 'Death'
OR ft_cpims_caseload.exit_reason = 'Drop Out'
OR ft_cpims_caseload.exit_reason = ' Family reconciliation'
OR ft_cpims_caseload.exit_reason = 'Family reintegration'
OR ft_cpims_caseload.exit_reason = 'Fostering'
OR ft_cpims_caseload.exit_reason = 'Ineligible'
OR ft_cpims_caseload.exit_reason = 'Left at will'
OR ft_cpims_caseload.exit_reason = 'Married'
OR ft_cpims_caseload.exit_reason = 'Not Traceable'
OR ft_cpims_caseload.exit_reason = 'Over 18'
OR ft_cpims_caseload.exit_reason = 'Over 18 yrs and out of School'
OR ft_cpims_caseload.exit_reason = 'Relocation'
OR ft_cpims_caseload.exit_reason = 'Self Employed'
OR ft_cpims_caseload.exit_reason = ''
OR ft_cpims_caseload.exit_reason = 'Transfered to GOK - DCS'
OR ft_cpims_caseload.exit_reason = 'Transition' )
{cbos} {ftdates}
UNION
select count(distinct(person_id)) as dcount, 'Graduated' as services,
'SMAL' as sex_id from ft_cpims_graduated
where agerange NOT IN ('g.[21+yrs]') {cbos} {ftdates}
) x
order by dcount desc
'''

QUERIES['2B'] = '''
select count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id, agerange
from ft_cpims_caseload {oftdates} {cbos} {areas}
group by gender, agerange
'''

QUERIES['2C'] = '''
SELECT count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, eligibility
from ft_cpims_caseload
WHERE eligibility != 'None' {cbos} {areas} {ftdates}
group by eligibility
having count(distinct(cpims_ovc_id)) > 0
order by dcount desc
'''

QUERIES['2D'] = '''
select count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id, schoollevel as school_level
from ft_cpims_caseload where exit_status='ACTIVE' {cbos} {areas} {ftdates}
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
from ft_cpims_caseload where exit_status='ACTIVE' {cbos} {areas} {ftdates}
group by gender, ovchivstatus order by dcount DESC
'''

QUERIES['2F'] = '''
SELECT count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'Current case load' as services
from ft_cpims_caseload where exit_status='ACTIVE' {cbos} {areas} {ftdates}
UNION
SELECT count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'Has Birth Certificate' as services
from ft_cpims_caseload where exit_status='ACTIVE'
and birthcert = 'HAS BIRTHCERT' {cbos} {areas} {ftdates}
UNION
SELECT count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'Has Disability' as services
from ft_cpims_caseload where exit_status='ACTIVE'
and ovcdisability = 'HAS DISABILITY' {cbos} {areas} {ftdates}
UNION
SELECT count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'School Going' as services
from ft_cpims_caseload where exit_status='ACTIVE'
and schoollevel != 'Not in School' {cbos} {areas} {ftdates}
'''

QUERIES['2G'] = '''
select count(distinct(cpims_ovc_id)) as dcount, gender as sex_id
from ft_cpims_registration where registration_date >'2021-09-30'
{cbos} {ftdates}
group by gender
'''


QUERIES['2H'] = '''
SELECT count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, exit_reason
from ft_cpims_caseload
WHERE (exit_reason != 'None' or exit_reason != 'Duplicated')
{cbos} {areas} {ftdates}
group by exit_reason
having count(distinct(cpims_ovc_id)) > 0
order by dcount desc
'''

QUERIES['2I'] = '''
select count(distinct(cpims_ovc_id)) as dcount, eligibility, 'SMAL' as sex_id
from ft_cpims_caseload where exit_status='ACTIVE' {cbos} {areas} {ftdates}
group by eligibility
order by dcount desc
'''

QUERIES['2J'] = '''
select count(distinct(cpims_ovc_id)) as dcount, agency, 'SMAL' as sex_id
from ft_cpims_caseload where exit_status='ACTIVE' {cbos} {areas} {ftdates}
group by agency
'''

QUERIES['2K'] = '''
select count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, schoollevel from ft_cpims_caseload where
exit_status='ACTIVE' AND schoollevel != 'Not in School'
{cbos} {areas} {ftdates}
group by schoollevel
'''

QUERIES['2L'] = '''
select count(distinct(cpims_ovc_id)) as dcount, agency, schoollevel
from ft_cpims_caseload where exit_status='ACTIVE' AND
schoollevel != 'Not in School' {cbos} {areas} {ftdates}
group by schoollevel, agency
'''

QUERIES['2M'] = '''
select count(distinct(cpims_ovc_id)) as dcount, gender as sex_id from
ft_cpims_caseload where exit_status='ACTIVE' and
schoollevel != 'Not in School' {cbos} {areas} {ftdates}
group by gender
'''

QUERIES['2N'] = '''
select count(distinct(cpims_ovc_id)) as dcount, gender as sex_id, schoollevel
from ft_cpims_caseload where exit_status='ACTIVE' AND
schoollevel != 'Not in School' {cbos} {areas} {ftdates}
group by gender, schoollevel
'''

QUERIES['2P'] = '''
select count(distinct(cpims_ovc_id)) as dcount, schoollevel, mechanism, agency
from ft_cpims_caseload where exit_status='ACTIVE' AND
schoollevel != 'Not in School' {cbos} {ftdates}
group by schoollevel, mechanism, agency
order by agency, mechanism
'''

QUERIES['2Q'] = '''
select count(distinct(cpims_ovc_id)) as dcount, agerange, gender as sex_id
from ft_cpims_caseload where exit_status='ACTIVE' AND
schoollevel='Not in School' {cbos} {areas} {ftdates}
group by agerange, gender
'''

QUERIES['2R'] = '''
select count(distinct(cpims_ovc_id)) as dcount, agerange,
CASE schoollevel WHEN 'Not in School' THEN 'a.Not in School'
ELSE schoollevel END AS schoollevel
from ft_cpims_caseload where exit_status='ACTIVE' {cbos} {areas} {ftdates}
group by agerange, schoollevel
order by agerange desc, schoollevel asc
'''

# =============== Section 3 ===========================

QUERIES['3A'] = '''
select * from (
select count(distinct(cpims_ovc_id)) as dcount,
'Eligible for reporting' as agency, 'Eligible for reporting' as services
from ft_cpims_caseload {oftdates} {cbos} 
UNION
select count(distinct(cpims_ovc_id)) as dcount,
'Case load' as agency, 'Program status' as services
from ft_cpims_caseload where exit_status='ACTIVE' {cbos} {ftdates}
UNION
select count(distinct(cpims_ovc_id)) as dcount,
'Transfers' as agency, 'Program status' as services
from ft_cpims_caseload
WHERE (ft_cpims_caseload.exit_reason = 'Transferred to PEPFAR partner' AND exit_status='EXITED'
OR ft_cpims_caseload.exit_reason = 'Transferred to Non-PEPFAR partner'  AND exit_status='EXITED')
{cbos} {ftdates}
UNION
select count(distinct(cpims_ovc_id)) as dcount, 'Exits' as agency, 'Program status' as services
from ft_cpims_caseload
WHERE exit_status='EXITED' AND (
ft_cpims_caseload.exit_reason = ' Adoption'
OR ft_cpims_caseload.exit_reason = 'Death'
OR ft_cpims_caseload.exit_reason = 'Drop Out'
OR ft_cpims_caseload.exit_reason = ' Family reconciliation'
OR ft_cpims_caseload.exit_reason = 'Family reintegration'
OR ft_cpims_caseload.exit_reason = 'Fostering'
OR ft_cpims_caseload.exit_reason = 'Ineligible'
OR ft_cpims_caseload.exit_reason = 'Left at will'
OR ft_cpims_caseload.exit_reason = 'Married'
OR ft_cpims_caseload.exit_reason = 'Not Traceable'
OR ft_cpims_caseload.exit_reason = 'Over 18'
OR ft_cpims_caseload.exit_reason = 'Over 18 yrs and out of School'
OR ft_cpims_caseload.exit_reason = 'Relocation'
OR ft_cpims_caseload.exit_reason = 'Self Employed'
OR ft_cpims_caseload.exit_reason = ''
OR ft_cpims_caseload.exit_reason = 'Transfered to GOK - DCS'
OR ft_cpims_caseload.exit_reason = 'Transition' )
{cbos} {ftdates}
) x order by services asc
'''

QUERIES['3B'] = '''
select sum(x.cnt) as dcount, 'OVC_SERV' AS mechanism,
'OVC_SERV_FY' AS agency FROM
    (
        select count(distinct(person_id)) as cnt, mechanism, agency
        from ft_cpims_active_beneficiary where agerange NOT IN ('g.[21+yrs]') {cbos} {ftdates}
        group by mechanism, agency
        UNION
        select count(distinct(person_id)) as cnt, mechanism, agency
        from ft_cpims_graduated where agerange NOT IN ('g.[21+yrs]') {cbos} {ftdates}
        group by mechanism, agency
    ) x
UNION ALL
select sum(count) as dcount, 'OVC_SERV 18-20' AS mechanism,
'OVC < 18 & OVC 18-20' AS agency FROM (
select count(distinct(person_id)) as count
from ft_cpims_active_beneficiary where agerange = 'f.[18-20yrs]' {cbos} {ftdates}
UNION
select count(distinct(person_id)) as count
from ft_cpims_graduated where agerange = 'f.[18-20yrs]' {cbos} {ftdates}
) srv
UNION ALL
select sum(count) as dcount, 'OVC_SERV < 18' AS mechanism,
'OVC < 18 & OVC 18-20' AS agency FROM (
select count(distinct(person_id)) as count
from ft_cpims_active_beneficiary where agerange NOT IN ('f.[18-20yrs]', 'g.[21+yrs]') {cbos} {ftdates}
UNION
select count(distinct(person_id)) as count
from ft_cpims_graduated where agerange NOT IN ('f.[18-20yrs]', 'g.[21+yrs]') {cbos} {ftdates}
) srv
UNION ALL
select count(distinct(person_id)) as dcount, ovchivstatus as mechanism,
'HIV Status' as agency
from ft_cpims_hivstat {oftdates} {cbos}
group by ovchivstatus
UNION ALL
select count(distinct(person_id)) as dcount, artstatus as mechanism,
'ART Status' as agency
from ft_cpims_hivstat where
ovchivstatus='POSITIVE' {cbos} {ftdates} group by artstatus
'''

QUERIES['3C'] = '''
select sum(x.cnt) as dcount, 'SMAL' as sex_id,
'OVC_SERV' as hivstat from
(
Select count(distinct(person_id)) as cnt
from ft_cpims_active_beneficiary 
where agerange NOT IN ('g.[21+yrs]') {cbos} {ftdates}
UNION ALL
Select count(distinct(person_id)) as cnt
from ft_cpims_graduated where agerange NOT IN ('g.[21+yrs]') {cbos} {ftdates}
) x
UNION
Select count(distinct(cpims_ovc_id)) AS dcount,
'SMAL' as sex_id,
CASE
when ovchivstatus='POSITIVE' THEN 'HIV Status +Ve'
when ovchivstatus='NEGATIVE' THEN 'HIV Status -Ve'
when ovchivstatus='NOT KNOWN' THEN 'HIV Status Unknown'
when ovchivstatus='HEI NOT KNOWN' THEN 'HEI Not Known'
when ovchivstatus='NULL' THEN 'HIV Status Unknown'
when ovchivstatus='HIV Test Not Required' THEN 'HIV Test not Required'
when ovchivstatus='HIV Referred For Testing' THEN 'HIV Status Unknown'
ELSE 'Others' END AS hivstat
from ft_cpims_registration where cpims_ovc_id IN
(select distinct(x.person_id) from
(
Select distinct(person_id)
from ft_cpims_active_beneficiary where agerange NOT IN ('g.[21+yrs]') {cbos} {ftdates}
UNION ALL
Select distinct(person_id)
from ft_cpims_graduated where agerange NOT IN ('g.[21+yrs]') {cbos} {ftdates}
) x )
group by hivstat
'''

QUERIES['3D'] = '''

select sum(x.cnt) as dcount, 'SMAL' as sex_id,
'OVC_SERV' as hivstat from
(
select count(distinct(person_id)) as cnt
from ft_cpims_active_beneficiary where agerange NOT IN ('f.[18-20yrs]', 'g.[21+yrs]') {cbos} {ftdates}
UNION
select count(distinct(person_id)) as cnt
from ft_cpims_graduated where agerange NOT IN ('f.[18-20yrs]', 'g.[21+yrs]') {cbos} {ftdates}
) x
UNION
Select count(distinct(cpims_ovc_id)) AS dcount,
'SMAL' as sex_id,
CASE
when ovchivstatus='POSITIVE' THEN 'HIV Status +Ve'
when ovchivstatus='NEGATIVE' THEN 'HIV Status -Ve'
when ovchivstatus='NOT KNOWN' THEN 'HIV Status Unknown'
when ovchivstatus='HEI NOT KNOWN' THEN 'HEI Not Known'
when ovchivstatus='NULL' THEN 'HIV Status Unknown'
when ovchivstatus='HIV Test Not Required' THEN 'HIV Test not Required'
when ovchivstatus='HIV Referred For Testing' THEN 'HIV Referred For Testing'
ELSE 'Others' END AS hivstat
from ft_cpims_registration where age < 18 AND cpims_ovc_id in
(select distinct(x.cpims_ovc_id) from
(
select distinct(person_id) as cpims_ovc_id
from ft_cpims_active_beneficiary where agerange NOT IN ('f.[18-20yrs]', 'g.[21+yrs]') {cbos} {ftdates}
UNION
select distinct(person_id) as cpims_ovc_id
from ft_cpims_graduated where agerange NOT IN ('f.[18-20yrs]', 'g.[21+yrs]') {cbos} {ftdates}
) x)
--and exit_status='ACTIVE'
group by hivstat
'''

QUERIES['3E'] = '''
select * from (
                  Select count(distinct(cpims_ovc_id)) AS dcount,
                         'SMAL' as sex_id, 'Positive' as services, 'Served' as agency
                  from ft_cpims_caseload where
                          ovchivstatus='POSITIVE' AND EXISTS (select distinct person_id from
                          ft_cpims_ovc_serv WHERE ft_cpims_caseload.cpims_ovc_id = ft_cpims_ovc_serv.person_id) {cbos} {ftdates}
                  UNION
                  Select count(distinct(cpims_ovc_id)) as dcount,
                      'SMAL' as sex_id, 'On ART' as services, 'Served' as agency
                  from ft_cpims_caseload
                  where ovchivstatus='POSITIVE' AND artstatus='ART' AND
                  EXISTS (select distinct person_id from ft_cpims_ovc_serv WHERE ft_cpims_caseload.cpims_ovc_id = ft_cpims_ovc_serv.person_id) {cbos} {ftdates}
                  UNION
                  Select count(distinct(cpims_ovc_id)) as dcount,
                      'SMAL' as sex_id, 'VL Accessed' as services, 'Served' as agency
                  from ft_cpims_viral_load WHERE EXISTS (select distinct person_id from
                  ft_cpims_ovc_serv WHERE ft_cpims_viral_load.cpims_ovc_id = ft_cpims_ovc_serv.person_id) {cbos} {ftdates}
                  UNION
                  Select count(distinct(cpims_ovc_id)) as dcount,
                      'SMAL' as sex_id, 'Valid VL' as services, 'Served' as agency
                  from ft_cpims_viral_load where vl_period_validity='Valid' AND
                  EXISTS (select distinct person_id from ft_cpims_ovc_serv WHERE
                  ft_cpims_viral_load.cpims_ovc_id = ft_cpims_ovc_serv.person_id) {cbos} {ftdates}
                  UNION
                  Select count(distinct(cpims_ovc_id)) AS dcount,
                      'SMAL' as sex_id, 'Suppressed' as services, 'Served' as agency
                  from ft_cpims_viral_load WHERE
                                                    (viral_load < 200 or viral_load is null) AND vl_period_validity='Valid'
                                                  AND EXISTS (select distinct person_id from ft_cpims_ovc_serv WHERE
                                                  ft_cpims_viral_load.cpims_ovc_id = ft_cpims_ovc_serv.person_id) {cbos} {ftdates}
                  UNION
                  Select count(distinct(cpims_ovc_id)) AS dcount,
                      'SMAL' as sex_id, 'Not Suppressed' as services, 'Served' as agency
                  from ft_cpims_viral_load WHERE viral_load > 199 AND vl_period_validity='Valid'
                                                  AND EXISTS (select distinct person_id from ft_cpims_ovc_serv WHERE
                                                  ft_cpims_viral_load.cpims_ovc_id = ft_cpims_ovc_serv.person_id) {cbos} {ftdates}
              ) x
  UNION

select * from (
                  Select count(distinct(cpims_ovc_id)) AS dcount,
                         'SMAL' as sex_id, 'Positive' as services, 'Not served' as agency
                  from ft_cpims_caseload where
                          ovchivstatus='POSITIVE' AND agerange != 'g.[21+yrs]' AND
                          NOT EXISTS (select distinct person_id from ft_cpims_ovc_serv WHERE
                          ft_cpims_caseload.cpims_ovc_id = ft_cpims_ovc_serv.person_id) {cbos} {ftdates}
                  UNION
                  Select count(distinct(cpims_ovc_id)) as dcount,
                      'SMAL' as sex_id, 'On ART' as services, 'Not served' as agency
                  from ft_cpims_caseload
                  where ovchivstatus='POSITIVE' AND artstatus='ART' AND agerange != 'g.[21+yrs]'
                  AND NOT EXISTS (select distinct person_id from ft_cpims_ovc_serv WHERE
                  ft_cpims_caseload.cpims_ovc_id = ft_cpims_ovc_serv.person_id) {cbos} {ftdates}
                  UNION
                  Select count(distinct(cpims_ovc_id)) as dcount,
                      'SMAL' as sex_id, 'VL Accessed' as services, 'Not served' as agency
                  from ft_cpims_viral_load WHERE  agerange != 'g.[21+yrs]' AND
                  NOT EXISTS (select distinct person_id from ft_cpims_ovc_serv WHERE
                  ft_cpims_viral_load.cpims_ovc_id = ft_cpims_ovc_serv.person_id) {cbos} {ftdates}
                  UNION
                  Select count(distinct(cpims_ovc_id)) as dcount,
                      'SMAL' as sex_id, 'Valid VL' as services, 'Not served' as agency
                  from ft_cpims_viral_load where vl_period_validity='Valid' AND agerange != 'g.[21+yrs]'
                  AND NOT EXISTS (select distinct person_id from ft_cpims_ovc_serv WHERE
                  ft_cpims_viral_load.cpims_ovc_id = ft_cpims_ovc_serv.person_id) {cbos} {ftdates}
                  UNION
                  Select count(distinct(cpims_ovc_id)) AS dcount,
                      'SMAL' as sex_id, 'Suppressed' as services, 'Not served' as agency
                  from ft_cpims_viral_load WHERE
                                                    (viral_load < 200 or viral_load is null)
                                                    AND vl_period_validity='Valid' AND agerange != 'g.[21+yrs]'
                                                  AND NOT EXISTS (select distinct person_id from ft_cpims_ovc_serv
                                                  WHERE ft_cpims_viral_load.cpims_ovc_id = ft_cpims_ovc_serv.person_id) {cbos} {ftdates}
                  UNION
                  Select count(distinct(cpims_ovc_id)) AS dcount,
                      'SMAL' as sex_id, 'Not Suppressed' as services, 'Not served' as agency
                  from ft_cpims_viral_load WHERE viral_load > 199 AND vl_period_validity='Valid' AND agerange != 'g.[21+yrs]'
                                                  AND NOT EXISTS (select distinct person_id from
                                                  ft_cpims_ovc_serv WHERE ft_cpims_viral_load.cpims_ovc_id = ft_cpims_ovc_serv.person_id) {cbos} {ftdates}
              ) x
order by agency asc, dcount desc
'''

QUERIES['3F'] = '''
SELECT count(distinct(cpims_ovc_id)) as dcount,
'Male' as sex_id, 'Known HIV Status' as hivstat
from ft_cpims_registration where exit_status='ACTIVE' AND agerange != 'g.[21+yrs]' {cbos} {ftdates}
UNION
Select count(distinct(cpims_ovc_id)) AS dcount,
'Male' as sex_id, 'On ART' as hivstat
from ft_cpims_registration where exit_status='ACTIVE'
and ovchivstatus='POSITIVE' AND agerange != 'g.[21+yrs]'  {cbos} {ftdates}
UNION
Select count(distinct(v.cpims_ovc_id)) AS dcount,
'Male' as sex_id, 'Suppression' as hivstat
from ft_cpims_viral_load v
WHERE v.vl_period_validity='Valid' AND
(viral_load < 200 or viral_load is null) AND agerange != 'g.[21+yrs]' {vcbos} {ftdates}
UNION
Select count(distinct(cpims_ovc_id)) AS dcount,
'Female' as sex_id, 'Known HIV Status' as hivstat
from ft_cpims_registration where exit_status='ACTIVE' AND agerange != 'g.[21+yrs]'
and (ovchivstatus='POSITIVE' or ovchivstatus='NEGATIVE'
or ovchivstatus='NOT KNOWN' or ovchivstatus='HIV Test Not Required'
or ovchivstatus='HIV Referred For Testing') {cbos}
UNION
Select count(distinct(cpims_ovc_id)) as dcount,
'Female' as sex_id, 'On ART' as hivstat
from ft_cpims_registration where exit_status='ACTIVE'
and ovchivstatus='POSITIVE' AND artstatus='ART' AND agerange != 'g.[21+yrs]' {cbos} {ftdates}
UNION
Select count(distinct(v.cpims_ovc_id)) AS dcount,
'Female' as sex_id, 'Suppression' as hivstat
from ft_cpims_viral_load v
WHERE v.vl_period_validity='Valid' AND
(viral_load < 200 or viral_load is null) AND agerange != 'g.[21+yrs]' {vcbos} {ftdates}
'''

QUERIES['3G'] = '''
Select count(distinct(cpims_ovc_id)) as dcount, gender as sex_id, agerange
from ft_cpims_viral_load where exit_status='ACTIVE' AND agerange!='[21+yrs]' AND
(current_date - date_of_event) < 401
and viral_load > 199 {cbos} {ftdates} group by gender, agerange
'''

QUERIES['3H'] = '''
Select count(distinct(cpims_ovc_id)) as dcount, gender as sex_id, agerange
from ft_cpims_viral_load where exit_status='ACTIVE' AND
(current_date - date_of_event) < 401
and viral_load > 199 AND agerange != 'g.[21+yrs]'
AND EXISTS (SELECT person_id FROM ft_cpims_ovc_serv WHERE
ft_cpims_viral_load.cpims_ovc_id = ft_cpims_ovc_serv.person_id)
{cbos} {ftdates} group by gender, agerange
'''

QUERIES['3I'] = '''
select count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id, agerange
from ft_cpims_caseload where exit_status='ACTIVE' AND
ovchivstatus='POSITIVE' AND agerange != 'g.[21+yrs]' {cbos} {ftdates}
group by gender, agerange
'''
QUERIES['3J'] = '''
select count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id, agerange
from ft_cpims_caseload where exit_status='ACTIVE' AND
ovchivstatus='POSITIVE' AND agerange != 'g.[21+yrs]'
AND EXISTS (SELECT person_id FROM ft_cpims_ovc_serv WHERE
ft_cpims_caseload.cpims_ovc_id = ft_cpims_ovc_serv.person_id) {cbos} {ftdates}
group by gender, agerange
'''

QUERIES['3K'] = '''
select count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id, agerange
from ft_cpims_caseload
where ovchivstatus='POSITIVE' AND exit_status='ACTIVE' AND agerange != 'g.[21+yrs]'
AND (current_date - registration_date) < 366 {cbos} {ftdates}
group by gender, agerange
'''

QUERIES['3L'] = '''
select count(distinct(cpims_ovc_id)) as dcount,
gender as sex_id, agerange
from ft_cpims_caseload
where ovchivstatus='POSITIVE' AND exit_status='ACTIVE' AND agerange != 'g.[21+yrs]'
AND (current_date - registration_date) < 366
AND EXISTS (SELECT person_id FROM ft_cpims_ovc_serv WHERE
ft_cpims_caseload.cpims_ovc_id = ft_cpims_ovc_serv.person_id) {cbos} {ftdates}
group by gender, agerange
'''

# ========= Section 4 ===============================

QUERIES['4A'] = '''
select count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'Eligible for reporting' as services
from ft_cpims_caseload {oftdates} {cbos}
UNION
SELECT count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'Received Services' as services
from ft_cpims_list_served {oftdates} {cbos}
UNION
Select count(distinct(person_id)) AS dcount,
'SMAL' as sex_id, 'Served Two Quarters' as services
from ft_cpims_two_quarters where ('2023-09-30' - date_of_event) <=200
AND date_of_event < '2023-09-30' {cbos} {ftdates}
UNION
Select count(distinct(person_id)) as dcount,
'SMAL' as sex_id, 'Case Plans' as services
from ft_cpims_case_plan where ('2023-09-30' - date_of_event) <= 400
AND date_of_event < '2023-09-30' {cbos} {ftdates}
UNION
select count(distinct(person_id)) as dcount,  'SMAL' as sex_id,
'Graduated' as services from ft_cpims_graduated
where agerange NOT IN ( 'g.[21+yrs]')  {cbos} {ftdates}
UNION
Select count(distinct(person_id)) as dcount,
'SMAL' as sex_id, 'Active Beneficiary' as services
from ft_cpims_active_beneficiary
where agerange NOT IN ( 'g.[21+yrs]') {cbos} {ftdates}
UNION

select sum(x.cnt) as dcount, 'SMAL' as sex_id,
'OVC_SERV' as hivstat from
(
Select count(distinct(person_id)) as cnt,
'SMAL' as sex_id from ft_cpims_active_beneficiary
where agerange NOT IN ( 'g.[21+yrs]') {cbos} {ftdates}
group by gender
UNION ALL
select count(distinct(person_id)) as cnt,  'SMAL' as sex_id
from ft_cpims_graduated
where agerange NOT IN ( 'g.[21+yrs]') {cbos} {ftdates}
) x

UNION
Select count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'Exit without Graduation' as services
from ft_cpims_caseload where exit_status='ACTIVE'
AND NOT exists
(select distinct(person_id) from ft_cpims_two_quarters where
ft_cpims_two_quarters.person_id = ft_cpims_caseload.cpims_ovc_id)
{cbos} {ftdates}
'''

QUERIES['4B'] = '''
Select count(distinct(household_id)) as dcount,
 'Case Plans' as services, 'SMAL' as sex_id
from ft_cpims_case_plan where (current_date - date_of_event) <= 400 {cbos} {ftdates}
UNION
Select sum(dcount) as dcount, services, sex_id from (
Select count(distinct(household)) as dcount,
'CPARA' as services, 'SMAL' as sex_id
from ft_cpims_cpara_v1 where (current_date - date_of_event) <= 400 {cbos} {ftdates}
UNION
Select count(distinct(household)) as dcount,
'CPARA' as services, 'SMAL' as sex_id
from ft_cpims_cpara where (current_date - date_of_event) <= 457 {cbos} {ftdates}
)cp
group by cp.services, cp.sex_id
'''

QUERIES['4C'] = '''
Select count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, domain as services
from ft_cpims_list_served {oftdates} {cbos} group by domain
order by dcount desc
'''

QUERIES['4D'] = '''
select sum(x.cnt) as dcount, 'SMAL' as sex_id, 
'OVC_SERV_Comprehensive' as services from
(
Select count(distinct(person_id)) as cnt,
'SMAL' as sex_id from ft_cpims_active_beneficiary where agerange NOT IN ('g.[21+yrs]') {cbos} {ftdates}
group by gender
UNION ALL
select count(distinct(person_id)) as cnt,  'SMAL' as sex_id
 from ft_cpims_graduated where agerange NOT IN ('g.[21+yrs]') {cbos} {ftdates}
) x
'''

QUERIES['4E'] = '''
Select count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, service as services
from ft_cpims_list_served
where date_of_service > '2022-03-31' {cbos} {ftdates}
group by service
order by dcount desc limit 35
'''

QUERIES['4F'] = '''
Select count(distinct(cpims_ovc_id)) as dcount,
domain, gender as sex_id from ft_cpims_list_served {oftdates} {cbos}
group by domain, gender
order by dcount desc
'''

QUERIES['4G'] = '''
select count(distinct(household)) as dcount, domain,
'SMAL' as sex_id from ft_cpims_list_served {oftdates} {cbos} group by domain
'''

QUERIES['4H'] = '''
select count(distinct(cpims_ovc_id)) as dcount,
domain, agency from ft_cpims_list_served {oftdates} {cbos}
group by agency, domain
'''

QUERIES['4I'] = '''
select dcount, domain as agency, service as mechanism,
'Service' as schoollevel from (
(select count(distinct(cpims_ovc_id)) as dcount,
domain, service from ft_cpims_list_served
Where domain='Healthy' {cbos} {ftdates}
group by domain, service
order by dcount DESC limit 5)
UNION
(select count(distinct(cpims_ovc_id)) as dcount,
domain, service from ft_cpims_list_served
Where domain='Stable' {cbos} {ftdates}
group by domain, service
order by dcount DESC limit 5)
Union
(select count(distinct(cpims_ovc_id)) as dcount,
domain, service from ft_cpims_list_served
Where domain='Safe' {cbos} {ftdates}
group by domain, service
order by dcount DESC limit 5)
union
(select count(distinct(cpims_ovc_id)) as dcount,
domain, service from ft_cpims_list_served
Where domain='Schooled' {cbos} {ftdates}
group by domain, service
order by dcount DESC limit 5)
) x
order by domain asc, dcount desc
'''

# ============= Section 5 ===========================

QUERIES['5A'] = '''
SELECT count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'Current Case load (ACTIVE)' as services
from ft_cpims_registration where exit_status='ACTIVE' {cbos} {ftdates}
UNION
Select count(distinct(person_id)) as dcount,
'SMAL' as sex_id, 'Current Case Plan' as services
from ft_cpims_case_plan where ('2022-09-30' - date_of_event) <= 400
{cbos} {ftdates}
'''

QUERIES['5B'] = '''
Select count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, graduationpath as services
from ft_cpims_benchmark_achieved_v1
where exit_status='ACTIVE' and (current_date - date_of_event) <= 400
{cbos} {ftdates}
group by graduationpath
'''

QUERIES['5C'] = '''
select count(distinct(cpims_ovc_id)) as dcount,
graduation_pathway, 'SMAL' as sex_id
from ft_cpims_benchmark
where exit_status='ACTIVE' AND date_of_event > '2022-03-31' {cbos} {ftdates}
group by graduation_pathway
'''

QUERIES['5D'] = '''
Select count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'Current CPARA' as services
from ft_cpims_cpara where (current_date - date_of_event) <= 400 {cbos} {ftdates}
'''

QUERIES['5E'] = '''
select count(distinct(household)) as dcount, agency, 'SMAL' as sex_id
from ft_cpims_caseload  where exit_status='ACTIVE' {cbos} {ftdates} group by agency
'''

QUERIES['5F'] = '''
select * from (
select count(distinct(household)) as dcount, agency,
'HH without case plans' as services from ft_cpims_caseload
where exit_status='ACTIVE' AND agency is not null and not exists
(select household_id from ft_cpims_case_plan where
ft_cpims_caseload.household = ft_cpims_case_plan.household_id) {cbos} {ftdates}
group by agency
UNION
select count(distinct(household_id)) as dcount, agency,
'HH with case plans' as services
from ft_cpims_case_plan
where agency is not null {cbos} {ftdates} group by agency
) y order by dcount asc
'''

QUERIES['5G'] = '''
select count(distinct(person_id)) as dcount, mechanism, agency
from ft_cpims_case_plan where agency is not null {cbos} {ftdates}
group by mechanism, agency
'''

QUERIES['5H-0'] = '''
Select count(distinct(cpims_ovc_id)) as dcount, 'SMAL' as sex_id,
graduationpath as services
from ft_cpims_benchmark_achieved_v1
where (current_date - date_of_event) <= 400 {cbos} {ftdates}
group by graduationpath
'''

QUERIES['5H'] = '''
select count(distinct(household_id)) as dcount,
graduation_pathway, 'SMAL' as sex_id
from ft_cpims_benchmark
where exit_status='ACTIVE' AND date_of_event > '2022-03-31' {cbos} {ftdates}
group by graduation_pathway
'''

QUERIES['5I'] = '''
select * from (
select count(distinct(household)) as dcount, 'SMAL' as sex_id,
'BM01: HIV Risk assessment done and HIV testing referrals completed' as benchmark
from ft_cpims_benchmark_achieved_v1 where bench1 = 1
and date_of_event < '2022-04-01' {cbos} {ftdates} group by bench1
UNION
select count(distinct(household)) as dcount, 'SMAL' as sex_id,
'BM02: Caregivers know the HIV+ status of the children they care as well as their own' as benchmark
from ft_cpims_benchmark_achieved_v1 where bench2 = 1
and date_of_event < '2022-04-01' {cbos} {ftdates} group by bench2
UNION
select count(distinct(household)) as dcount, 'SMAL' as sex_id,
'BM03: HIV+ persons in the household have been on ART for last 12 months' as benchmark
from ft_cpims_benchmark_achieved_v1 where bench3 = 1
and date_of_event < '2022-04-01' {cbos} {ftdates} group by bench3
UNION
select count(distinct(household)) as dcount, 'SMAL' as sex_id,
'BM04: Enrolled women/ adolescent girls who are/become pregnant receive HIV testing' as benchmark
from ft_cpims_benchmark_achieved_v1 where bench4 = 1
and date_of_event < '2022-04-01' {cbos} {ftdates} group by bench4
UNION
select count(distinct(household)) as dcount, 'SMAL' as sex_id,
'BM05: Adolescents and their caregivers have knowledge to decrease their HIV risk' as benchmark
from ft_cpims_benchmark_achieved_v1 where bench5 = 1
and date_of_event < '2022-04-01' {cbos} {ftdates} group by bench5
UNION
select count(distinct(household)) as dcount, 'SMAL' as sex_id,
'BM06: Children living with chronic illness/disability receive treatment' as benchmark
from ft_cpims_benchmark_achieved_v1 where bench6 = 1
and date_of_event < '2022-04-01' {cbos} {ftdates} group by bench6
UNION
select count(distinct(household)) as dcount, 'SMAL' as sex_id,
'BM07: HH able to provide a minimum of two meals/day' as benchmark
from ft_cpims_benchmark_achieved_v1 where bench7 = 1
and date_of_event < '2022-04-01' {cbos} {ftdates} group by bench7
UNION
select count(distinct(household)) as dcount, 'SMAL' as sex_id,
'BM08: HH able to pay for child(ren)’s basic needs' as benchmark
from ft_cpims_benchmark_achieved_v1 where bench8 = 1
and date_of_event < '2022-04-01' {cbos} {ftdates} group by bench8
UNION
select count(distinct(household)) as dcount, 'SMAL' as sex_id,
'BM09: HH able to pay for emergency expenses' as benchmark
from ft_cpims_benchmark_achieved_v1 where bench9 = 1
and date_of_event < '2022-04-01' {cbos} {ftdates} group by bench9
UNION
select count(distinct(household)) as dcount, 'SMAL' as sex_id,
'BM10:The caregiver has demonstrated knowledge on access to critical services' as benchmark
from ft_cpims_benchmark_achieved_v1 where bench10 = 1
and date_of_event < '2022-04-01' {cbos} {ftdates} group by bench10
UNION
select count(distinct(household)) as dcount, 'SMAL' as sex_id,
'BM11: Child-headed HHs have received child and social protection services' as benchmark
from ft_cpims_benchmark_achieved_v1 where bench11 = 1
and date_of_event < '2022-04-01' {cbos} {ftdates} group by bench11
UNION
select count(distinct(household)) as dcount, 'SMAL' as sex_id,
'BM12: All children in the HH able to participate in daily activities and engage with others' as benchmark
from ft_cpims_benchmark_achieved_v1 where bench12 = 1
and date_of_event < '2022-04-01' {cbos} {ftdates} group by bench12
UNION
select count(distinct(household)) as dcount, 'SMAL' as sex_id,
'BM13: Children at risk of abuse have been referred to and are receiving appropriate services' as benchmark
from ft_cpims_benchmark_achieved_v1 where bench13 = 1
and date_of_event < '2022-04-01' {cbos} {ftdates} group by bench13
UNION
select count(distinct(household)) as dcount, 'SMAL' as sex_id,
'BM14: Caregivers can identify individual or group providing social or emotional support' as benchmark
from ft_cpims_benchmark_achieved_v1 where bench14 = 1
and date_of_event < '2022-04-01' {cbos} {ftdates} group by bench14
UNION
select count(distinct(household)) as dcount, 'SMAL' as sex_id,
'BM15: Caregivers have completed a parenting skills or able to clearly articulate positive parenting' as benchmark
from ft_cpims_benchmark_achieved_v1 where bench15 = 1
and date_of_event < '2022-04-01' {cbos} {ftdates} group by bench15
UNION
select count(distinct(household)) as dcount, 'SMAL' as sex_id,
'BM16: All 6-17 children enrolled and attend school regularly' as benchmark
from ft_cpims_benchmark_achieved_v1 where bench16 = 1
and date_of_event < '2022-04-01' {cbos} {ftdates} group by bench16
UNION
select count(distinct(household)) as dcount, 'SMAL' as sex_id,
'BM17: Adolescents enrolled in vocational attend regularly' as benchmark
from ft_cpims_benchmark_achieved_v1 where bench17 = 1
and date_of_event < '2022-04-01' {cbos} {ftdates} group by bench17
) x order by benchmark asc
'''

QUERIES['5J'] = '''
select * from (
select count(distinct(household_id)) as dcount,
'SMAL' as sex_id, 'BM1: All children, adolescents, and caregivers in the household have known HIV status or a test is not required based on risk assessment' as benchmark from ft_cpims_benchmark
where benchmark_1 = 1 and date_of_event > '2022-03-31' {cbos} {ftdates}
group by benchmark_1
UNION
select count(distinct(household_id)) as dcount,
'SMAL' as sex_id, 'BM2: All HIV+ children, adolescents, and caregivers in the household with a viral load result documented in the medical record and/or laboratory information systems (LIS) have been virally suppressed for the last 12 months' as benchmark from ft_cpims_benchmark
where benchmark_2 = 1 and date_of_event > '2022-03-31' {cbos} {ftdates}
group by benchmark_2
UNION
select count(distinct(household_id)) as dcount,
'SMAL' as sex_id, 'BM3: All adolescents 10-17 years of age in the household have key knowledge about preventing HIV infection' as benchmark from ft_cpims_benchmark
where benchmark_3 = 1 and date_of_event > '2022-03-31' {cbos} {ftdates}
group by benchmark_3
UNION
select count(distinct(household_id)) as dcount,
'SMAL' as sex_id, 'BM4: No children < 5 years in the household are undernourished' as benchmark from ft_cpims_benchmark
where benchmark_4 = 1 and date_of_event > '2022-03-31' {cbos} {ftdates}
group by benchmark_4
UNION
select count(distinct(household_id)) as dcount,
'SMAL' as sex_id, 'BM5: Caregivers are able to access money (without selling productive assets) to pay for school fees, medical costs (buy medicine, transport to facility etc), legal and other administrative fees (related to guardianship, civil registration, or inheritance) for children 0-17 years' as benchmark from ft_cpims_benchmark
where benchmark_5 = 1 and date_of_event > '2022-03-31' {cbos} {ftdates}
group by benchmark_5
UNION
select count(distinct(household_id)) as dcount,
'SMAL' as sex_id, 'BM6: No children, adolescents, and caregivers in the household report experiences of violence (including physical violence, emotional violence, sexual violence, gender-based violence, and neglect) in the last six months' as benchmark from ft_cpims_benchmark
where benchmark_6 = 1 and date_of_event > '2022-03-31' {cbos} {ftdates}
group by benchmark_6
UNION
select count(distinct(household_id)) as dcount,
'SMAL' as sex_id, 'BM7: All children and adolescents in the household are under the care of a stable adult caregiver' as benchmark from ft_cpims_benchmark
where benchmark_7 = 1 and date_of_event > '2022-03-31' {cbos} {ftdates}
group by benchmark_7
UNION
select count(distinct(household_id)) as dcount,
'SMAL' as sex_id, 'BM8: All children <18 years have legal proof of identity' as benchmark from ft_cpims_benchmark
where benchmark_8 = 1 and date_of_event > '2022-03-31' {cbos} {ftdates}
group by benchmark_8
UNION
select count(distinct(household_id)) as dcount,
'SMAL' as sex_id, 'BM9: All school-aged children (4-17) and adolescents aged 18-20 enrolled in secondary school in the household regularly attended school and progressed during the last year.' as benchmark from ft_cpims_benchmark
where benchmark_9 = 1 and date_of_event > '2022-03-31' {cbos} {ftdates}
group by benchmark_9
) x order by benchmark asc
'''

QUERIES['5K'] = '''
Select count(distinct(household_id)) as dcount,
 cpara_score as services, 'SMAL' as sex_id
from ft_cpims_benchmark
where (current_date - date_of_event) <= 400 {cbos} {ftdates}
group by cpara_score order by cpara_score asc
'''

QUERIES['5L'] = '''
Select count(distinct(household)) as dcount,
 cpara_score as benchmark_total_scores, 'SMAL' as sex_id
from ft_cpims_benchmark_achieved_v1
where (current_date - date_of_event) <= 400 {cbos} {ftdates}
group by cpara_score order by cpara_score asc
'''

# ==== Section 6 ===============================


QUERIES['6A'] = '''
select count(distinct(cpims_ovc_id)) as dcount,
'Eligible for reporting' as agency, 'Eligible for reporting' as services
from ft_cpims_caseload {oftdates} {cbos}
UNION
select count(distinct(cpims_ovc_id)) as dcount,
'Case load' as agency, 'Program status' as services
from ft_cpims_caseload where exit_status='ACTIVE' {cbos} {ftdates}
UNION
select count(distinct(cpims_ovc_id)) as dcount,
'Transfers' as agency, 'Program status' as services
from ft_cpims_caseload
WHERE (ft_cpims_caseload.exit_reason = 'Transferred to PEPFAR partner' AND exit_status='EXITED'
OR ft_cpims_caseload.exit_reason = 'Transferred to Non-PEPFAR partner' AND exit_status='EXITED') {cbos} {ftdates}
UNION
select count(distinct(cpims_ovc_id)) as dcount, 'Exits' as agency, 'Program status' as services
from ft_cpims_caseload
WHERE (ft_cpims_caseload.exit_reason != 'Transferred to PEPFAR partner' AND exit_status='EXITED'
OR ft_cpims_caseload.exit_reason != 'Transferred to Non-PEPFAR partner' AND exit_status='EXITED') {cbos} {ftdates}
'''

QUERIES['6B'] = '''
select sum(count) as dcount, 'OVC_SERV' AS mechanism,
'OVC_SERV_FY' AS agency FROM (
select count(distinct(person_id)) as count, mechanism, agency
from ft_cpims_active_beneficiary where agerange NOT IN ('g.[21+yrs]') {cbos} {ftdates}
group by mechanism, agency
UNION
select count(distinct(person_id)) as count, mechanism, agency
from ft_cpims_graduated where agerange NOT IN ('g.[21+yrs]')
{cbos} {ftdates} group by mechanism, agency
) srv
UNION ALL
select sum(count) as dcount, 'OVC_SERV 18-20' AS mechanism,
'OVC < 18 & OVC 18-20' AS agency FROM (
select count(distinct(person_id)) as count
from ft_cpims_active_beneficiary where agerange = 'f.[18-20yrs]' {cbos} {ftdates}
UNION
select count(distinct(person_id)) as count
from ft_cpims_graduated where agerange = 'f.[18-20yrs]' {cbos} {ftdates}
) srv
UNION ALL
select sum(count) as dcount, 'OVC_SERV < 18' AS mechanism,
'OVC < 18 & OVC 18-20' AS agency FROM (
select count(distinct(person_id)) as count
from ft_cpims_active_beneficiary where agerange NOT IN ('f.[18-20yrs]', 'g.[21+yrs]') {cbos} {ftdates}
UNION
select count(distinct(person_id)) as count
from ft_cpims_graduated where agerange NOT IN ('f.[18-20yrs]', 'g.[21+yrs]') {cbos} {ftdates}
) srv
UNION ALL
select count(distinct(person_id)) as dcount, ovchivstatus as mechanism,
'HIV Status' as agency
from ft_cpims_hivstat {oftdates} {cbos}
group by ovchivstatus
UNION ALL
select count(distinct(person_id)) as dcount, artstatus as mechanism,
'ART Status' as agency
from ft_cpims_hivstat where ovchivstatus='POSITIVE' {cbos} {ftdates} group by artstatus
'''

QUERIES['6C'] = '''
select sum(count) as dcount, gender as sex_id, agerange FROM (
select count(distinct(person_id)) as count, gender, agerange
from ft_cpims_active_beneficiary where agerange NOT IN ('f.[18-20yrs]', 'g.[21+yrs]') {cbos} {ftdates}
group by gender, agerange
UNION
select count(distinct(person_id)) as count, gender, agerange
from ft_cpims_graduated where agerange NOT IN ('f.[18-20yrs]', 'g.[21+yrs]') {cbos} {ftdates}
group by gender, agerange
) srv
group by gender, agerange
'''

QUERIES['6D'] = '''
select count(distinct(cpims_ovc_id)) as dcount, agency, 'SMAL' as sex_id
from ft_cpims_not_served {oftdates} {cbos} group by agency
order by dcount desc
'''

QUERIES['6E'] = '''
select * from (
select count(distinct(cpims_ovc_id)) as dcount,
agency, 'Not served 2Q' as services
from ft_cpims_not_served {oftdates} {cbos} group by agency
UNION ALL
select count(distinct(cpims_ovc_id)) as dcount, agency, 'Attrition' as services
from ft_cpims_attrition {oftdates} {cbos} group by agency
) x
order by dcount asc
'''

QUERIES['6F'] = '''
select count(distinct(cpims_ovc_id)) as dcount, exit_reason as services, agency
from ft_cpims_attrition {oftdates} {cbos} group by services, agency
order by agency desc, dcount desc
'''

QUERIES['6G'] = '''

select count(distinct(cpims_ovc_id)) as dcount, mechanism, agency
from ft_cpims_not_served {oftdates} {cbos} group by mechanism, agency
order by agency desc, dcount desc

'''

QUERIES['6H'] = '''
select sum(dct) as dcount, agency, 'Female' as sex_id from (
select sum(not_served) as dct, agency
from ft_cpims_not_served {oftdates} {cbos} group by agency
UNION ALL
select sum(attrition) as dct, agency
from ft_cpims_attrition {oftdates} {cbos} group by agency
) srv
group by agency
UNION ALL
select count(distinct(cpims_ovc_id)) as dcount, agency, 'Male' as sex_id
from ft_cpims_caseload {oftdates} {cbos} group by agency
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
from ft_cpims_caseload {oftdates} {cbos}
UNION
select count(distinct(cpims_ovc_id)) as dcount,
'Active' as agency, 'Program status' as services
from ft_cpims_caseload where exit_status='ACTIVE' {cbos} {ftdates}
UNION
select count(distinct(cpims_ovc_id)) as dcount,
'Transfers' as agency, 'Program status' as services
from ft_cpims_caseload
WHERE (ft_cpims_caseload.exit_reason = 'Transferred to PEPFAR partner' AND exit_status='EXITED'
OR ft_cpims_caseload.exit_reason = 'Transferred to Non-PEPFAR partner'  AND exit_status='EXITED')
{cbos} {ftdates}
UNION
select count(distinct(cpims_ovc_id)) as dcount, 'Exits' as agency, 'Program status' as services
from ft_cpims_caseload
WHERE (ft_cpims_caseload.exit_reason != 'Transferred to PEPFAR partner' AND exit_status='EXITED'
OR ft_cpims_caseload.exit_reason != 'Transferred to Non-PEPFAR partner'  AND exit_status='EXITED')
{cbos} {ftdates}
) x order by services asc
'''


QUERIES['7C'] = '''

select sum(x.cnt) as dcount, 'SMAL' as sex_id,
       'OVC_SERV' as hivstat from
    (
        select count(distinct(person_id)) as cnt, mechanism, agency
        from ft_cpims_active_beneficiary
        where agerange NOT IN ('f.[18-20yrs]' , 'g.[21+yrs]') {cbos} {ftdates}
        group by mechanism, agency
        UNION
        select count(distinct(person_id)) as cnt, mechanism, agency
        from ft_cpims_graduated
        where agerange NOT IN ('f.[18-20yrs]' , 'g.[21+yrs]') {cbos} {ftdates}
        group by mechanism, agency
    ) x
UNION
Select count(distinct(cpims_ovc_id)) AS dcount,
       'SMAL' as sex_id,
       CASE
           when ovchivstatus='POSITIVE' THEN 'HIV Status +Ve'
           when ovchivstatus='NEGATIVE' THEN 'HIV Status -Ve'
           when ovchivstatus= 'NOT KNOWN' THEN 'HIV Status Unknown'
           when ovchivstatus='HEI NOT KNOWN' THEN 'HIV Status Unknown'
           when ovchivstatus='NULL' THEN 'HIV Status Unknown'
           when ovchivstatus='HIV Test Not Required' THEN 'HIV Test not Required'
           when ovchivstatus='HIV Referred For Testing' THEN 'HIV Status Unknown'
           ELSE 'Others' END AS hivstat
from ft_cpims_registration where cpims_ovc_id in
                                      (select distinct(x.cpims_ovc_id) from
                                          (
                                              Select distinct person_id as cpims_ovc_id
                                              from ft_cpims_active_beneficiary {oftdates} {cbos}
                                              UNION
                                              Select distinct person_id as cpims_ovc_id
                                              from ft_cpims_graduated {oftdates} {cbos}
                                          ) x )
                                   AND agerange NOT IN ('f.[18-20yrs]', 'g.[21+yrs]') {cbos} {ftdates}
group by hivstat
'''


QUERIES['7B'] = '''
select sum(count) as dcount, 'OVC_SERV < 18' AS mechanism,
'OVC_SERV < 18' AS agency FROM (
select count(distinct(person_id)) as count
from ft_cpims_active_beneficiary  where agerange NOT IN ('f.[18-20yrs]' , 'g.[21+yrs]') {cbos} {ftdates}
UNION
select count(distinct(person_id)) as count
from ft_cpims_graduated  where agerange NOT IN ('f.[18-20yrs]' , 'g.[21+yrs]') {cbos} {ftdates}
) srv

UNION ALL
select sum(dcount) as dcount, mechanism, agency FROM (
select count(distinct(person_id)) as dcount, 
CASE
WHEN ft_cpims_hivstat.ovchivstatus='HEI NOT KNOWN' THEN 'NOT KNOWN'
WHEN ft_cpims_hivstat.ovchivstatus='NOT KNOWN' THEN 'NOT KNOWN'
WHEN ft_cpims_hivstat.ovchivstatus='NULL' THEN 'NOT KNOWN'
WHEN ft_cpims_hivstat.ovchivstatus='HIV Test Not Required' THEN 'HIV Test Not Required'
WHEN ft_cpims_hivstat.ovchivstatus='NEGATIVE' THEN 'NEGATIVE'
WHEN ft_cpims_hivstat.ovchivstatus='POSITIVE' THEN 'POSITIVE'
END AS mechanism,
'HIV Status' as agency
from ft_cpims_hivstat where hivinfo ='KNOWN HIV Info' 
AND  agerange NOT IN ('f.[18-20yrs]' , 'g.[21+yrs]') {cbos} {ftdates}
group by ovchivstatus
)srv group by  mechanism, agency

UNION ALL
select count(distinct(person_id)) as dcount, artstatus as mechanism, 'ART Status' as agency
from ft_cpims_hivstat where hivinfo ='KNOWN HIV Info'
and ovchivstatus='POSITIVE' 
AND agerange NOT IN ('f.[18-20yrs]' , 'g.[21+yrs]') {cbos} {ftdates}
group by artstatus
'''

# ======= Section 8 =======================

QUERIES['8A'] = '''

Select count(distinct(cpims_ovc_id)) AS dcount,
'SMAL' as sex_id, 'Positive' as hivstat
from ft_cpims_registration where exit_status='ACTIVE'
and ovchivstatus='POSITIVE' {cbos} {ftdates}
UNION
Select count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'On ART' as hivstat
from ft_cpims_registration where exit_status='ACTIVE'
and ovchivstatus='POSITIVE' AND artstatus='ART' {cbos} {ftdates}
UNION
Select count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'VL Accessed' as hivstat
from ft_cpims_viral_load WHERE exit_status='ACTIVE'
and ovchivstatus='POSITIVE' AND artstatus='ART' {cbos} {ftdates}
UNION

Select count(distinct(cpims_ovc_id)) as dcount,
'SMAL' as sex_id, 'Valid VL' as hivstat
from ft_cpims_viral_load
where  vl_period_validity='Valid' {cbos} {ftdates}
UNION

Select count(distinct(cpims_ovc_id)) AS dcount,
'SMAL' as sex_id, 'Suppressed' as hivstat
from ft_cpims_viral_load
WHERE vl_period_validity='Valid' AND
(viral_load < 1000 or viral_load is null) {cbos} {ftdates}
UNION

Select count(distinct(cpims_ovc_id)) AS dcount,
'SMAL' as sex_id, 'Not Suppressed' as hivstat
from ft_cpims_viral_load
WHERE vl_period_validity='Valid' AND viral_load > 999 {cbos} {ftdates}
'''

QUERIES['8B'] = '''
SELECT count(distinct(cpims_ovc_id)) as dcount,
'Male' as sex_id, 'Known HIV Status' as hivstat
from ft_cpims_registration where exit_status='ACTIVE' {cbos} {ftdates}
UNION
Select count(distinct(cpims_ovc_id)) AS dcount,
'Male' as sex_id, 'On ART' as hivstat
from ft_cpims_registration where exit_status='ACTIVE'
and ovchivstatus='POSITIVE' {cbos} {ftdates}
UNION
Select count(distinct(cpims_ovc_id)) AS dcount,
'Male' as sex_id, 'Suppression' as hivstat
from ft_cpims_viral_load
WHERE vl_period_validity='Valid' AND
(viral_load < 1000 or viral_load is null) {cbos} {ftdates}
UNION
Select count(distinct(cpims_ovc_id)) AS dcount,
'Female' as sex_id, 'Known HIV Status' as hivstat
from ft_cpims_registration where exit_status='ACTIVE'
and (ovchivstatus='POSITIVE' or ovchivstatus='NEGATIVE'
or ovchivstatus='NOT KNOWN' or ovchivstatus='HIV Test Not Required'
or ovchivstatus='HIV Referred For Testing') {cbos} {ftdates}
UNION
Select count(distinct(cpims_ovc_id)) as dcount,
'Female' as sex_id, 'On ART' as hivstat
from ft_cpims_registration where exit_status='ACTIVE'
and ovchivstatus='POSITIVE' AND artstatus='ART' {cbos} {ftdates}
UNION
Select count(distinct(cpims_ovc_id)) AS dcount,
'Female' as sex_id, 'Suppression' as hivstat
from ft_cpims_viral_load
WHERE vl_period_validity='Valid' AND
(viral_load < 1000 or viral_load is null) {cbos} {ftdates}
'''


QUERIES['8C'] = '''
select count(distinct(cpims_ovc_id)) as dcount, agency,
CASE
when ovchivstatus='POSITIVE' THEN 'HIV+'
ELSE 'Case load and not HIV+ (-Ve, Unknown, Test Not Required)' END AS services
from ft_cpims_caseload where cbo is not NULL {cbos} {ftdates}
group by agency, services
order by agency asc, services desc, dcount desc
'''

QUERIES['8D'] = '''
select count(distinct(cpims_ovc_id)) as dcount, mechanism as ip,
CASE
when ovchivstatus='POSITIVE' THEN 'HIV+'
ELSE 'Case load and not HIV+ (-Ve, Unknown, Test Not Required)' END AS services
from ft_cpims_caseload where cbo is not NULL {cbos} {ftdates}
group by mechanism, services, agency
order by agency asc, services desc, dcount desc
'''

QUERIES['8E'] = '''
select count(distinct(cpims_ovc_id)) as dcount, cbo as lip,
CASE
when ovchivstatus='POSITIVE' THEN 'HIV+'
ELSE 'Case load and not HIV+ (-Ve, Unknown, Test Not Required)' END AS services
from ft_cpims_caseload where cbo is not NULL {cbos} {ftdates}
group by cbo, services, agency
order by agency asc, services desc, dcount desc
'''


QUERIES['8F'] = '''
select count(distinct(cpims_ovc_id)) as dcount, county,
CASE
when ovchivstatus='POSITIVE' THEN 'HIV+'
ELSE 'Case load and not HIV+ (-Ve, Unknown, Test Not Required)' END AS services
from ft_cpims_caseload where county is not NULL {cbos} {ftdates}
group by county, services
order by services desc, dcount desc, county desc
'''

QUERIES['8G'] = '''
select count(distinct(cpims_ovc_id)) as dcount, agency,
CASE
when artstatus='ART' THEN 'On ART'
ELSE 'Not on ART' END AS services
from ft_cpims_caseload where ovchivstatus='POSITIVE'
and cbo is not NULL {cbos} {ftdates}
group by agency, services
order by agency asc, services asc, dcount desc
'''

QUERIES['8H'] = '''
select count(distinct(cpims_ovc_id)) as dcount, mechanism as ip,
CASE
when artstatus='ART' THEN 'On ART'
ELSE 'Not on ART' END AS services
from ft_cpims_caseload
where ovchivstatus='POSITIVE' and cbo is not NULL {cbos} {ftdates}
group by mechanism, services, agency
order by agency asc, services asc, dcount desc
'''

QUERIES['8I'] = '''
select count(distinct(cpims_ovc_id)) as dcount, cbo as lip,
CASE
when artstatus='ART' THEN 'On ART'
ELSE 'Not on ART' END AS services
from ft_cpims_caseload
where ovchivstatus='POSITIVE' and cbo is not NULL {cbos} {ftdates}
group by cbo, services, agency
order by agency asc, services asc, dcount desc
'''

QUERIES['8J'] = '''
select count(distinct(cpims_ovc_id)) as dcount, county,
CASE
when artstatus='ART' THEN 'On ART'
ELSE 'Not on ART' END AS services
from ft_cpims_caseload
where ovchivstatus='POSITIVE' and county is not NULL {cbos} {ftdates}
group by county, services, agency
order by agency asc, services asc, dcount desc
'''

QUERIES['8K'] = '''
select * from (
select count(distinct(cpims_ovc_id)) as dcount, agency,
'Valid VL' as services
from ft_cpims_viral_load where agency is not null
and vl_period_validity='Valid' {cbos} {ftdates}
group by agency
UNION
select count(distinct(cpims_ovc_id)) as dcount, agency,
'On ART without valid VL' as services
from ft_cpims_caseload where ovchivstatus='POSITIVE' and artstatus='ART'
and cpims_ovc_id not in (
select distinct(cpims_ovc_id) from ft_cpims_viral_load
where agency is not null and vl_period_validity='Valid' {cbos} {ftdates}
) {cbos} {ftdates}
group by agency
) x
order by agency asc, services desc, dcount desc
'''

QUERIES['8L'] = '''
select * from (
select count(distinct(cpims_ovc_id)) as dcount, mechanism as ip,
'Valid VL' as services
from ft_cpims_viral_load where agency is not null
and vl_period_validity='Valid' {cbos} {ftdates}
group by mechanism
UNION
select count(distinct(cpims_ovc_id)) as dcount, mechanism as ip,
'On ART without valid VL' as services
from ft_cpims_caseload where ovchivstatus='POSITIVE'
and artstatus='ART' and agency is not null
and cpims_ovc_id not in (
select distinct(cpims_ovc_id) from ft_cpims_viral_load
where agency is not null and vl_period_validity='Valid' {cbos} {ftdates}
) {cbos} {ftdates}
group by mechanism
) x
order by services desc, dcount desc
'''

QUERIES['8M'] = '''
select * from (
select count(distinct(cpims_ovc_id)) as dcount, cbo as lip,
'Valid VL' as services
from ft_cpims_viral_load where cbo is not null
and vl_period_validity='Valid' {cbos} {ftdates}
group by cbo
UNION
select count(distinct(cpims_ovc_id)) as dcount, cbo as lip,
'On ART without valid VL' as services
from ft_cpims_caseload where ovchivstatus='POSITIVE'
and artstatus='ART' and cbo is not null
and cpims_ovc_id not in (
select distinct(cpims_ovc_id) from ft_cpims_viral_load
where agency is not null and vl_period_validity='Valid' {cbos} {ftdates}
) {cbos} {ftdates}
group by cbo
) x
order by services desc, dcount desc
'''

QUERIES['8N'] = '''
select * from (
select count(distinct(cpims_ovc_id)) as dcount, county,
'Valid VL' as services
from ft_cpims_viral_load where county is not null
and vl_period_validity='Valid' {cbos} {ftdates}
group by county
UNION
select count(distinct(cpims_ovc_id)) as dcount, county,
'On ART without valid VL' as services
from ft_cpims_caseload where ovchivstatus='POSITIVE'
and artstatus='ART' and county is not null
and cpims_ovc_id not in (
select distinct(cpims_ovc_id) from ft_cpims_viral_load
where agency is not null and vl_period_validity='Valid' {cbos} {ftdates}
) {cbos} {ftdates}
group by county
) x
order by services desc, dcount desc
'''

QUERIES['8P'] = '''
select * from (
select count(distinct(cpims_ovc_id)) as dcount, agency,
'Suppressed' as services
from ft_cpims_viral_load where agency is not null
and vl_period_validity='Valid' and (suppression = '0-400'
or suppression = '400 - 999'
or suppression = 'LDL') {cbos} {ftdates}
group by agency
UNION
select count(distinct(cpims_ovc_id)) as dcount, agency,
'On ART and not suppressed' as services
from ft_cpims_caseload where ovchivstatus='POSITIVE' and artstatus='ART'
and cpims_ovc_id in (
select distinct(cpims_ovc_id) from ft_cpims_viral_load
where agency is not null and vl_period_validity='Valid' {cbos} {ftdates}
)
and cpims_ovc_id not in (
select distinct(cpims_ovc_id) from ft_cpims_viral_load
where agency is not null and vl_period_validity='Valid'
and (suppression = '0-400' or suppression = '400 - 999'
or suppression = 'LDL') {cbos} {ftdates}
)
group by agency
) x
order by services desc, dcount desc
'''


QUERIES['8Q'] = '''
select * from (
select count(distinct(cpims_ovc_id)) as dcount, mechanism as ip,
'Suppressed' as services
from ft_cpims_viral_load where agency is not null
and vl_period_validity='Valid' and (suppression = '0-400'
or suppression = '400 - 999'
or suppression = 'LDL') {cbos} {ftdates}
group by mechanism
UNION
select count(distinct(cpims_ovc_id)) as dcount, mechanism as ip,
'On ART and not suppressed' as services
from ft_cpims_caseload where ovchivstatus='POSITIVE' and artstatus='ART'
and cpims_ovc_id in (
select distinct(cpims_ovc_id) from ft_cpims_viral_load
where agency is not null and vl_period_validity='Valid' {cbos} {ftdates}
)
and cpims_ovc_id not in (
select distinct(cpims_ovc_id) from ft_cpims_viral_load
where agency is not null and vl_period_validity='Valid'
and (suppression = '0-400' or suppression = '400 - 999'
or suppression = 'LDL') {cbos} {ftdates}
)
group by mechanism
) x
order by services desc, dcount desc
'''

QUERIES['8R'] = '''
select * from (
select count(distinct(cpims_ovc_id)) as dcount, cbo as lip,
'Suppressed' as services
from ft_cpims_viral_load where agency is not null
and vl_period_validity='Valid' and (suppression = '0-400'
or suppression = '400 - 999'
or suppression = 'LDL') {cbos} {ftdates}
group by cbo
UNION
select count(distinct(cpims_ovc_id)) as dcount, cbo as lip,
'On ART and not suppressed' as services
from ft_cpims_caseload where ovchivstatus='POSITIVE' and artstatus='ART'
and cpims_ovc_id in (
select distinct(cpims_ovc_id) from ft_cpims_viral_load
where agency is not null and vl_period_validity='Valid' {cbos} {ftdates}
)
and cpims_ovc_id not in (
select distinct(cpims_ovc_id) from ft_cpims_viral_load
where agency is not null and vl_period_validity='Valid'
and (suppression = '0-400' or suppression = '400 - 999'
or suppression = 'LDL') {cbos} {ftdates}
)
group by cbo
) x
order by services desc, dcount desc
'''

QUERIES['8S'] = '''
select * from (
select count(distinct(cpims_ovc_id)) as dcount, county,
'Suppressed' as services
from ft_cpims_viral_load where agency is not null and county is not null
and vl_period_validity='Valid' and (suppression = '0-400'
or suppression = '400 - 999'
or suppression = 'LDL') {cbos} {ftdates}
group by county
UNION
select count(distinct(cpims_ovc_id)) as dcount, county,
'On ART and not suppressed' as services
from ft_cpims_caseload where ovchivstatus='POSITIVE' and artstatus='ART'
and cpims_ovc_id in (
select distinct(cpims_ovc_id) from ft_cpims_viral_load
where agency is not null and county is not null
and vl_period_validity='Valid' {cbos} {ftdates}
)
and cpims_ovc_id not in (
select distinct(cpims_ovc_id) from ft_cpims_viral_load
where agency is not null and county is not null and vl_period_validity='Valid'
and (suppression = '0-400' or suppression = '400 - 999'
or suppression = 'LDL') {cbos} {ftdates}
)
group by county
) x
order by services desc, dcount desc
'''

QUERIES['8T'] = '''
select count(distinct(cpims_ovc_id)) as dcount, agency, suppression
from ft_cpims_viral_load where agency is not null
and suppression is not null
and vl_period_validity='Valid' group by agency, suppression
'''

QUERIES['8U'] = '''
select count(distinct(cpims_ovc_id)) as dcount,
CONCAT(agency, ' : ', suppression) as services, duration_on_art
from ft_cpims_viral_load where agency is not null
and suppression is not null and duration_on_art is not null
and vl_period_validity='Valid'
group by agency, suppression, duration_on_art
order by duration_on_art
'''
