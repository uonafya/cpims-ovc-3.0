# CPIMS OVC Upgrade

Code base for CPIMS OVC business process upgrade from python 2.7 / Django 1.8 to Python 3.10 / Django 4.0.2

## files edited by incognito
we upgraded all modules from

    python 2.7 to 3.10.0
    django 1.8 to 4.0.2
    changed templates staticfiles to static
    tests for cpovc_offline_mode
    commented login_required, is_allowed_groups, cache_control
    used default django middleware instead of the cpims middleware
    updated requirements.txt

#### install python 3.10 https://www.python.org/getit/
#### Installation
    clone the repository to your local machine
    git clone https://github.com/uonafya/cpims-ovc-3.0

#### install virtualenv windows

    pip install virtualenv

#### create virtualenv

    virtualenv venv

#### activate virtualenv

    venv\Scripts\activate

##### install requirements

    pip install -r requirements.txt

##### Install postgres https://www.postgresql.org/
##### open psql(shell)

    create database cpims;
    create user username with password 'userpassword';
    grant all privileges on database cpims to username;

##### Edit cpims/settings.py with credentials created above

    py manage.py makemigrations
    py manage.py migrate
    py manage.py check

##### runserver 

    py manage.py runserver

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
