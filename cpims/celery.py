import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cpims.settings")
app = Celery("cpims")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

# python -m celery -A cpims worker -l info