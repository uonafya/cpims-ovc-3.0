# -- Registration dashboard
CHART = {}

CHART['1A'] = {}
CHART['1A']['desc'] = '''
The total number of OVC ever enrolled in to the Program
  disaggregated by sex (f, m)
'''
CHART['1A']['calc'] = '''
A count of all OVCs in the program consisting of program
participation status such as current case load,
(Newly registered and Transfer Ins) and Exits disaggregated by sex.
Exclude exits as duplicates and voids.
'''

# - Registrations by sex
CHART['1B'] = {}
CHART['1B']['desc'] = '''
The total number of OVC ever enrolled in to the Program disaggregated
by program status (current case load and Exits)
'''
CHART['1B']['calc'] = '''
A count of all OVCs in the program consisting of program participation
status such as case load), (Newly registered and Transfer Ins) and Exits
disaggregated by caseload and Exits. Exclude exits as duplicates and voids
'''


# - Eligibility criterias
CHART['1C'] = {}
CHART['1C']['desc'] = '''
Eligibility Criteria at enrolment for total number of OVC
ever enrolled in to the Program.
'''
CHART['1C']['calc'] = '''
A count of all OVCs ever enrolled disaggregated by eligibility criteria.
NB: an individual OVC can be in more than one eligibility category.
'''

# - Other summaries on birth certificates and disability
CHART['1D'] = {}
CHART['1D']['desc'] = '''
'''
CHART['1D']['calc'] = '''
'''

# - Caseload by Agency - New 29-Aug-2022
CHART['1E'] = {}
CHART['1E']['desc'] = '''
The total number of OVC ever enrolled in to the Program
disaggregated by funding agency
'''
CHART['1E']['calc'] = '''
A count of all OVCs ever enrolled disaggregated by funding agency
'''

# - HIV Status from registration list
CHART['1F'] = {}
CHART['1F']['desc'] = '''
'''
CHART['1F']['calc'] = '''
'''

#
CHART['1G'] = {}
CHART['1G']['desc'] = '''
Categorization of reasons that led to OVC exit from the Program over time
'''
CHART['1G']['calc'] = '''
A count of all OVCs ever exited disaggregated by Exit reasons.
NB - Discount Exit through duplicates and voids
'''


# =============== Case load dashboards ==================================

# - Registrations by sex
CHART['2A'] = {}
CHART['2A']['desc'] = '''
Total number of OVC eligible for reporting during any given reporting period.
This consists of Caseload at the beginning of the reporting period,
new enrolments, exits, transfers (both in and out) and graduations
within the reporting period.
'''
CHART['2A']['calc'] = '''
A count of all OVC- Caseload at the beginning of the reporting period,
new enrolments, exits, transfers and graduations within the reporting period
'''


CHART['2B'] = {}
CHART['2B']['desc'] = '''
Total number of OVC eligible for reporting during any given reporting period 
disaggregated by gender and age
'''
CHART['2B']['calc'] = '''
A count of all OVC- Caseload at the beginning of the reporting period, new 
enrolments, exits, transfers and graduations within the reporting period 
disaggregated by age and gender
'''

# - Eligibility criterias
CHART['2C'] = {}
CHART['2C']['desc'] = '''
Total number of OVC eligible for reporting during any given reporting period 
disaggregated by Eligibility Criteria at enrolment
NB: the eligibility criteria might change over time
'''
CHART['2C']['calc'] = '''
A count of all OVC- Caseload at the beginning of the reporting period, new enrolments, 
exits, transfers and graduations within the reporting period disaggregated by eligibility 
criteria at enrolment
NB: since the eligibility criteria might change over time, take note not to include latest 
updates in the calculations
'''

# - Registrations by school categories
CHART['2D'] = {}
CHART['2D']['desc'] = '''
Total number of OVC Caseload during given reporting period disaggregated Schooling 
information and gender
'''
CHART['2D']['calc'] = '''
A count of all OVC current caseload disaggregated by schooling information and gender
'''

# - HIV Status from registration list
CHART['2E'] = {}
CHART['2E']['desc'] = '''
Total number of OVC Caseload at the time of reporting disaggregated by HIV status and gender
NB Query should not include exits, transfers or case plan achievement
'''
CHART['2E']['calc'] = '''
A count of all OVC current caseload disaggregated by HIV status and gender
'''

# - Other summaries on birth certificates and disability
CHART['2F'] = {}
CHART['2F']['desc'] = '''
Total number of OVC Caseload at the time of reporting disaggregated by other information i.e.
a) Those still in the Program at current date
b) Those reported to have a birth certificate
c) Duration in program
d) School going OVC
NB Query should not include exits, transfers or case plan achievement
'''
CHART['2F']['calc'] = '''
A count of all OVC current caseload disaggregated by
a) Those still in the Program at current date 
b) Those reported to have a birth certificate 
c) Duration in program 
d) School going OVC
'''

CHART['2G'] = {}
CHART['2G']['desc'] = '''
Total number of OVC newly registered during the reporting disaggregated by OVC Sub populations i.e.
a) HEI
b) CALHIV
c) SVAC
d) Children of FSW
f) Pregnant and Breast-Feeding Adolescents <18 
g) Children of PLHIV e.t.c
NB the categories are not mutually exclusive
'''
CHART['2G']['calc'] = '''
A count of all newly enrolled OVC during the reporting period disaggregated by OVC Sub populations i.e.
a) HEI 
b) CALHIV 
c) SVAC 
d) Children of FSW 
f) Pregnant and Breast-Feeding Adolescents <18 
g) Children of PLHIV e.t.c
'''

# - Exit reasons
CHART['2H'] = {}
CHART['2H']['desc'] = '''
Total number of OVC eligible for reporting exited during 
given reporting period disaggregated by exit reasons
'''
CHART['2H']['calc'] = '''
A count of all exited OVCs under the eligible for reporting disaggregated by Exit reasons. 
NB - Discount Exit through duplicates and voids
'''

# - Caseload Profile - New 29-Aug-2022
CHART['2I'] = {}
CHART['2I']['desc'] = '''
Total number of OVC Caseload during given reporting period disaggregated by subpopulation
a) HEI
b) CALHIV
c) SVAC
d) Children of FSW
f) Pregnant and Breast-Feeding Adolescents <18 g) Children of PLHIV e.t.c
NB the categories are not mutually exclusive. If the OVC do not fall in any of the categories above, include under ineligible
'''
CHART['2I']['calc'] = '''
A count of all OVC current Caseload disaggregated by subpopulation
'''

# - Caseload by Agency - New 29-Aug-2022
CHART['2J'] = {}
CHART['2J']['desc'] = '''
Total number of current OVC Caseload in the Program disaggregated by funding agency
'''
CHART['2J']['calc'] = '''
A count of all OVC current Caseload disaggregated by funding agency
'''

# - School going - school level
CHART['2K'] = {}
CHART['2K']['desc'] = '''
'''
CHART['2K']['calc'] = '''
'''

# - School going - school level and agency
CHART['2L'] = {}
CHART['2L']['desc'] = '''
Total number of current OVC Caseload in the Program disaggregated by School level and funding agency
'''
CHART['2L']['calc'] = '''
A count of all OVC current Caseload in the Program disaggregated by School level and funding agency
'''

# - School going - by sex
CHART['2M'] = {}
CHART['2M']['desc'] = '''
'''
CHART['2M']['calc'] = '''
'''

# - School going - school level and sex
CHART['2N'] = {}
CHART['2N']['desc'] = '''
'''
CHART['2N']['calc'] = '''
'''

# - School going - school level and agency
CHART['2P'] = {}
CHART['2P']['desc'] = '''
Total number of current OVC Caseload in the Program disaggregated by funding agency, mechanism and school level
'''
CHART['2P']['calc'] = '''
A count of all OVC current Caseload in the Program disaggregated by funding agency, mechanism and school level
'''

# - Not in school - by agebands
CHART['2Q'] = {}
CHART['2Q']['desc'] = '''
Total number of current OVC Caseload in the Program not in school disaggregated by Age and gender
'''
CHART['2Q']['calc'] = '''
A count of all OVC current Caseload in the Program not in school disaggregated by age and gender
'''

# - School going - school level and sex
CHART['2R'] = {}
CHART['2R']['desc'] = '''
Total number of current OVC Caseload in the Program disaggregated by school level and age
'''
CHART['2R']['calc'] = '''
A count of all OVC current Caseload in the Program disaggregated by school level and age
'''


# =============== Viral Load and HIV_STAT ================================

CHART['3A'] = {}
CHART['3A']['desc'] = '''
'''
CHART['3A']['calc'] = '''
'''

# OVC_HIVSTAT Charts
CHART['3B'] = {}
CHART['3B']['desc'] = '''
Total number of OVC served under Comprehensive model disaggregated by age and HIV Status
'''
CHART['3B']['calc'] = '''
A count of all OVC served under OVC comprehensive model disaggregated by age and HIV status. 
NB: Comprehensive being summation of Active (served in 2 quarters) and Graduated. 
The disagregation by HIV status is only for under 18years.
'''

# - OVC_HIVSTAT
CHART['3C'] = {}
CHART['3C']['desc'] = '''
Total number of OVC served under Comprehensive model disaggregated HIV Status
'''
CHART['3C']['calc'] = '''
A count of all OVC served under OVC comprehensive model disaggregated by HIV status. 
NB: Comprehensive being summation of Active (served in 2 quarters) and graduated.
The disaggregation by HIV status is for all comprehensive OVC served.
'''

# - OVC_HIVSTAT
CHART['3D'] = {}
CHART['3D']['desc'] = '''
'''
CHART['3D']['calc'] = '''
'''

CHART['3E'] = {}
CHART['3E']['desc'] = '''
Total number of HIV Positive OVC under current caseload during the reporting 
period disaggregated by Viral load tests and suppression status. 
NB: Current caseload excludes all exits and transfer outs irrespective of being served or not.
'''
CHART['3E']['calc'] = '''
Count of all HIV Positive OVC under current caseload during the reporting period disaggregated by 
Viral load tests and suppression status. 
NB: Current caseload excludes all exits and transfer outs irrespective of being served or not.
'''

# - OVC 95-95-95 Cascade
CHART['3F'] = {}
CHART['3F']['desc'] = '''
Total number of current OVC caseload disaggregated by those with 
known HIV status, Positive, On ART and VL suppression status
'''
CHART['3F']['calc'] = '''
A count of current OVC caseload disaggregated by those with known HIV status, Positive, 
On ART and VL suppression status. 
NB: Current caseload excludes all exits and transfer outs irrespective of being served or not.
'''

# New
CHART['3G'] = {}
CHART['3G']['desc'] = '''
Total number of unsuppressed CALHIV from current caseload with valid VL results 
(results within 12 months and VL>1000cps/ml) disaggregated by age and gender.
'''
CHART['3G']['calc'] = '''
A count of unsuppressed CALHIV from current caseload with valid VL results 
(results within 12 months and VL>1000cps/ml) disaggregated by age and gender. 
NB: Current caseload excludes all exits and transfer outs irrespective of being served or not.
'''

# CALHIV
CHART['3H'] = {}
CHART['3H']['desc'] = '''
Total number of CALHIV from current OVC caseload disaggregated by age cohorts
'''
CHART['3H']['calc'] = '''
A count of CALHIV from current OVC caseload disaggregated by age cohorts
'''


# =============== Services Reporting Charts ===============================

CHART['4A'] = {}
CHART['4A']['desc'] = '''
Total number of OVC eligible for reporting during any given reporting period disagregated by the different 
criteria for accounting for services provided (Total number of OVC eligible for reporting, Total OVC with 
caseplans, Received services, OVC Served 2 quarters, Newly enrolled Served Q2 (SAPR) or Q4(APR), Active, 
Graduated, OVC_SERV Comprehensive)
'''
CHART['4A']['calc'] = '''
A count of OVC eligible for reporting during any given reporting period disagregated by the different 
criteria for accounting for services provided (Total number of OVC eligible for reporting, Total OVC with 
caseplans, Received services, OVC Served 2 quarters, Newly enrolled Served Q2 (SAPR) or Q4(APR), Active, 
Graduated, OVC_SERV Comprehensive)
NB: Include both form 1A and Form 1B Services that are trickle down

'''

# New
CHART['4B'] = {}
CHART['4B']['desc'] = '''
'''
CHART['4B']['calc'] = '''
'''

# - Services by domain
CHART['4C'] = {}
CHART['4C']['desc'] = '''
Services provided to OVC eligible for reporting categorized by gender and domains (Healthy, Safe, Stable, Schooled)
'''
CHART['4C']['calc'] = '''
A count of Services provided to OVC eligible for reporting categorized by gender and domain (Healthy, Safe, Stable, Schooled)
NB: Include both form 1A and Form 1B Services that are trickle down
An OVC is counted only once per domain regardless of number services they received within a domain

'''

# Beneficiary categories
CHART['4D'] = {}
CHART['4D']['desc'] = '''
Total number of OVC provided with services under the OVC_SERV indicator disaggregated by Comprehensive, DREAMS and Preventive
NB: Take note when counting the DREAMS beneficiaries to ensure they are not already enrolled in Comprehensive program

'''
CHART['4D']['calc'] = '''
Count of all OVC provided with services during the reporting period under the OVC_SERV indicator disaggregated by Comprehensive, DREAMS and Preventive
'''

# - Specific services
CHART['4E'] = {}
CHART['4E']['desc'] = '''
Top 35 unique services provided to OVC based on frequency in the reporting period
'''
CHART['4E']['calc'] = '''
A count of Top 35 unique services provided to OVC based on frequency in the reporting period
'''

# - Services by Domain - ALL
CHART['4F'] = {}
CHART['4F']['desc'] = '''
'''
CHART['4F']['calc'] = '''
'''

# - Services by Domain - Agency
CHART['4G'] = {}
CHART['4G']['desc'] = '''
Number of unique services per HH provided to OVC by LIPs or Ips categorized by the different domains 
(Healthy, Safe, Stable, Schooled) and sex
'''
CHART['4G']['calc'] = '''
Count of unique services per HH provided to OVC by LIPs or IPs categorized by the different domains 
(Healthy, Safe, Stable, Schooled) and sex
'''

# - Services by Domain - IP
CHART['4H'] = {}
CHART['4H']['desc'] = '''
Proportional Distribution of services provided to OVC by domain for each funding agency
'''
CHART['4H']['calc'] = '''
Denominator: Count of all services provided to OVC by domain across all domains.
Numerator: Count of all services provided to OVC by domain per domain.
'''

# - Top 5 Services by Domain - Agency
CHART['4I'] = {}
CHART['4I']['desc'] = '''
Total number of Top 5 unique services provided by frequency and Domain
'''
CHART['4I']['calc'] = '''
A count of Top 5 unique services provided by frequency and Domain
'''


# =============== Case Management OVC ==========================

CHART['5A'] = {}
CHART['5A']['desc'] = '''
OVC receives at least one eligible PEPFAR OVC program service in each of the preceding two quarters 
or newly enrolled served in Q2 and Q4 for SAPR and APR respectively with case plan updated.
'''
CHART['5A']['calc'] = '''
Number of OVC with a case plan developed or updated in the last 12 months
'''

# - Graduation pathways - Old
CHART['5B'] = {}
CHART['5B']['desc'] = '''
Number of OVCs with CPARA assessment in the last 12 months relative 
to the reporting period disaggregated by graduation pathways
'''
CHART['5B']['calc'] = '''
Count of All OVC that were or are in the Program during the reporting period who have been done 
for CPARA assessment and are currently actively participating in to
'''

# - Graduation pathways
CHART['5C'] = {}
CHART['5C']['desc'] = '''
Number of OVCs categorized by graduation pathways based on CPARA (Highly Vulnerable, Low Vulnerability, 
Medium Vulnerability, Ready For Graduation)
'''
CHART['5C']['calc'] = '''
All HH with CPARA are categorized by pathways
'''

# -- Case Management - HH
CHART['5D'] = {}
CHART['5D']['desc'] = '''
Number of HH with current CPARA both V1 and revised CPARA too
'''
CHART['5D']['calc'] = '''
Number of HH with current CPARA both V1 and revised CPARA tool
'''

# - Services reporting
CHART['5E'] = {}
CHART['5E']['desc'] = '''
Number of HHs from the current caseload disaggregated by funding agency
'''
CHART['5E']['calc'] = '''
A count of all HHs from the current caseload disaggregated by funding agency
'''

# - Case plans - HH by Agency
CHART['5F'] = {}
CHART['5F']['desc'] = '''
Count all HHs from the current caseload with a case plan during the reporting period
'''
CHART['5F']['calc'] = '''
Number of HH with case plans and without case plans should aggregate with number of active HH presented in 4E (OVC not HH)
'''

# - Case plans - HH by IP
CHART['5G'] = {}
CHART['5G']['desc'] = '''
Current OVC caseload with case plans in the reporting period by IP
'''
CHART['5G']['calc'] = '''
Count all OVC with a caseplan during the reporting period
'''

# - OVC HH along Graduation pathway
CHART['5H'] = {}
CHART['5H']['desc'] = '''
'''
CHART['5H']['calc'] = '''
'''

# - Benchmarks Version 1
CHART['5I'] = {}
CHART['5I']['desc'] = '''
Number of HH achieving individual CPARA benchmarks
'''
CHART['5I']['calc'] = '''
Count of HH with CPARA 1(From current OVC caseload) during the reporting period.)
'''

# - Benchmarks Version 1
CHART['5J'] = {}
CHART['5J']['desc'] = '''
Frequency of HHs achieving each of the individual benchmark based on CPARA
'''
CHART['5J']['calc'] = '''
Count of  HH with CPARA 1(From current OVC caseload) during the reporting period.
'''

# - Benchmarks Total scores
CHART['5K'] = {}
CHART['5K']['desc'] = '''
Frequency of HHs by benchmark scores based on CPARA (current score 9)
'''
CHART['5K']['calc'] = '''
'''

# - Benchmarks Total scores Version 1
CHART['5L'] = {}
CHART['5L']['desc'] = '''
Frequency of HHs by benchmark scores based on CPARA version 1 (CPARA v1 score 17 benchmarks)
'''
CHART['5L']['calc'] = '''
Current HH with CPARA (current caseload
'''

CHART['5M'] = {}
CHART['5M']['desc'] = '''
'''
CHART['5M']['calc'] = '''
'''


CHART['5N'] = {}
CHART['5N']['desc'] = '''
'''
CHART['5N']['calc'] = '''
'''


CHART['5P'] = {}
CHART['5P']['desc'] = '''
'''
CHART['5P']['calc'] = '''
'''


CHART['5Q'] = {}
CHART['5Q']['desc'] = '''
'''
CHART['5Q']['calc'] = '''
'''


CHART['5R'] = {}
CHART['5R']['desc'] = '''
'''
CHART['5R']['calc'] = '''
'''


CHART['5S'] = {}
CHART['5S']['desc'] = '''
'''
CHART['5S']['calc'] = '''
'''


CHART['5T'] = {}
CHART['5T']['desc'] = '''
'''
CHART['5T']['calc'] = '''
'''

# =============== Performance Charts =================================

CHART['6A'] = {}
CHART['6A']['desc'] = '''
'''
CHART['6A']['calc'] = '''
'''

# OVC_HIVSTAT Charts
CHART['6B'] = {}
CHART['6B']['desc'] = '''
'''
CHART['6B']['calc'] = '''
'''

# Exit without graduation - Agency
CHART['6C'] = {}
CHART['6C']['desc'] = '''
'''
CHART['6C']['calc'] = '''
'''

# Exit without graduation - Agency
CHART['6D'] = {}
CHART['6D']['desc'] = '''
Number of  OVC who in two consecutive quarters received at least a 
service in one quarter or none of the quarters
'''
CHART['6D']['calc'] = '''
Count all those served only once and those not served at all during the period
'''

# Exit without graduation - Agency, IP, County
CHART['6E'] = {}
CHART['6E']['desc'] = '''
Number of OVC classified as exit without graduation based on service provision and attrition by agency
'''
CHART['6E']['calc'] = '''
Count all those served only once and those not served at all during the period for both those who were 
exited and those not exited. Do not include those who have never been reported as Active in the previous periods.
Sum of Exited OVC due to attrition and exit based on services

'''

# Attrition - Agency
CHART['6F'] = {}
CHART['6F']['desc'] = '''
All OVC exited from the Program for reasons other than lack of service provision in the reporting period. 
This is a subset of entire exit without graduation
'''
CHART['6F']['calc'] = '''
Count all those who were reported as exit without graduation due to attrition by exit reasons. 
'''

# Exit without graduation - Agency - ALL IPs
CHART['6G'] = {}
CHART['6G']['desc'] = '''
Exit Without Graduation - OVC who has not received program services in each of the past two preceding 
quarters or is lost-to-follow up, re-located,died, or the child has aged-out of the program without the 
household meeting graduation benchmarks from the PEPFAR OVC program. 
'''
CHART['6G']['calc'] = '''
A count of OVC who has not received program services in each of the past two preceding quarters or is lost-to-follow up, 
re-located,died, or the child has aged-out of the program without the household meeting graduation benchmarks from the PEPFAR OVC Program
'''

# Exit without graduation - Agency - ALL IPs
CHART['6H'] = {}
CHART['6H']['desc'] = '''
Exit Without Graduation - OVC who has not received program services in each of the past two preceding 
quarters or is lost-to-follow up, re-located,died, or the child has aged-out of the program without the 
household meeting graduation benchmarks from the PEPFAR OVC program.
'''
CHART['6H']['calc'] = '''
A count of OVC who has not received program services in each of the past two preceding quarters or is lost-to-follow up, 
re-located,died, or the child has aged-out of the program without the household meeting graduation benchmarks from the PEPFAR OVC Program
'''

# =============== MER Reportinng charts ================================
# - Caseload by Agency - New 29-Aug-2022
CHART['7A'] = {}
CHART['7A']['desc'] = '''
Proportion of OVC categorized under each of the Program status (Active/Exits/Transfers
'''
CHART['7A']['calc'] = '''
'''

# OVC_HIVSTAT Charts
CHART['7B'] = {}
CHART['7B']['desc'] = '''
'''
CHART['7B']['calc'] = '''
'''

# - OVC_HIVSTAT
CHART['7C'] = {}
CHART['7C']['desc'] = '''
Percentage of orphans and vulnerable children (<18 years old) served in the OVC 
Comprehensive program with HIV status reported to implementing partner.
'''
CHART['7C']['calc'] = '''
'''

# =============== Epidemic control
# -- Viral Load and HIV_STAT charts ----------------------------------------
CHART['8A'] = {}
CHART['8A']['desc'] = '''
Percentage of orphans and vulnerable children enrolled in the OVC
Comprehensive program with HIV status reported to implementing partner
'''
CHART['8A']['calc'] = '''
'''

# - OVC 95-95-95 Cascade
CHART['8B'] = {}
CHART['8B']['desc'] = '''
HIV treatment cascade (95-95-95). Known HIV status, on ART and suppression.
'''
CHART['8B']['calc'] = '''
'''

CHART['8C'] = {}
CHART['8C']['desc'] = '''
OVC caseload categorized by those who are HIV positive or Other HIV status by funding agency, IP and County
'''
CHART['8C']['calc'] = '''
'''

CHART['8D'] = {}
CHART['8D']['desc'] = '''
OVC caseload categorized by those who are HIV positive or Other HIV status by funding agency, IP and County
'''
CHART['8D']['calc'] = '''
'''

CHART['8E'] = {}
CHART['8E']['desc'] = '''
OVC caseload categorized by those who are HIV positive or Other HIV status by funding agency, IP and County
'''
CHART['8E']['calc'] = '''
'''

CHART['8F'] = {}
CHART['8F']['desc'] = '''
OVC caseload categorized by those who are HIV positive or Other HIV status by funding agency, IP and County
'''
CHART['8F']['calc'] = '''
'''


CHART['8G'] = {}
CHART['8G']['desc'] = '''
Number of HIV positive OVC categorized by on ART or Not on ART by funding agency
'''
CHART['8G']['calc'] = '''
'''

CHART['8H'] = {}
CHART['8H']['desc'] = '''
Number of OVC per IP living with HIV but are not on ART.
'''
CHART['8H']['calc'] = '''
'''

CHART['8I'] = {}
CHART['8I']['desc'] = '''
Number of OVC per LIP and county living with HIV but are not on ART.
'''
CHART['8I']['calc'] = '''
'''


CHART['8J'] = {}
CHART['8J']['desc'] = '''
Number of OVC per LIP and county living with HIV but are not on ART.
'''
CHART['8J']['calc'] = '''
'''

CHART['8K'] = {}
CHART['8K']['desc'] = '''
Number of HIV positive OVC categorized by on Having a valid VL and On ART without a valid VL per agency and IP
'''
CHART['8K']['calc'] = '''
'''

CHART['8L'] = {}
CHART['8L']['desc'] = '''
Number of HIV positive OVC categorized by on Having a valid VL and On ART without a valid VL per agency and IP
'''
CHART['8L']['calc'] = '''
'''

CHART['8M'] = {}
CHART['8M']['desc'] = '''
'''
CHART['8M']['calc'] = '''
'''

CHART['8N'] = {}
CHART['8N']['desc'] = '''
'''
CHART['8N']['calc'] = '''
'''

CHART['8P'] = {}
CHART['8P']['desc'] = '''
'''
CHART['8P']['calc'] = '''
'''

CHART['8Q'] = {}
CHART['8Q']['desc'] = '''
'''
CHART['8Q']['calc'] = '''
'''

CHART['8R'] = {}
CHART['8R']['desc'] = '''
'''
CHART['8R']['calc'] = '''
'''

CHART['8S'] = {}
CHART['8S']['desc'] = '''
'''
CHART['8S']['calc'] = '''
'''

CHART['8T'] = {}
CHART['8T']['desc'] = '''
Number of OVC's living with HIV and are suppressed
'''
CHART['8T']['calc'] = '''
'''

CHART['8U'] = {}
CHART['8U']['desc'] = '''
Number of OVC's living with HIV and are suppressed
'''
CHART['8U']['calc'] = '''
'''
