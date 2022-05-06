python manage.py makemigrations cpovc_auth
python manage.py migrate --fake cpovc_auth
python manage.py makemigrations
python manage.py migrate --fake