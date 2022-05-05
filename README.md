# CPIMS OVC Upgrade

Code base for CPIMS OVC business process upgrade from python 2.7 / Django 1.8 to Python 3.10 / Django 4.0.2

# install python 3.10 https://www.python.org/getit/
## Installation
// clone the repository to your local machine
git clone https://github.com/uonafya/cpims-ovc-3.0

# install virtualenv windows
pip install virtualenv

# create virtualenv
virtualenv venv

# activate virtualenv
venv\Scripts\activate

# install requirements
pip install -r requirements.txt

# Install postgres https://www.postgresql.org/
# open psql(shell)
create database cpims;
create user username with password 'userpassword';
grant all privileges on database cpims to username;

# Edit cpims/settings.py with credentials created above

py manage.py makemigrations
py manage.pt migrate
py manage.py check

# runserver 
py manage.py runserver