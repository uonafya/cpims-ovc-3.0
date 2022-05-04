# CPIMS OVC Upgrade

Code base for Child Protection Management Information System (CPIMS) OVC business process and technology stack upgrade from python 2.7 and Django 1.8.5

## Technology stack
Python - 3.10
Django - 4.0.4
Postgresql - 14


## Functionality
### Existing
Register Org Unit, Workforce, CHV, Caregiver(s), OVC
Enroll OVC to Comprehensive care
Offer Services and monitoring / assessments
Exit OVC from the program

### New
Enroll, follow up and exit Preventive care - Sinovuyo, FMP and Family Support
PMTCT functionality
Revised tools implementation (Version March 2022)

## Installation

git clone https://github.com/uonafya/cpims-ovc-3.0
Edit cpims/settings.py with your credentials

python manage.py makemigrations
python manage.pt migrate
python manage.py check
python manage.py runserver
