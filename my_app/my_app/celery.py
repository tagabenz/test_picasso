import os 
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_app.settings")
os.environ.setdefault("C_FORCE_ROOT", "my_app.settings")
app = Celery("my_app")
app.config_from_object("django.conf:settings", namespace='CELERY')
app.autodiscover_tasks()