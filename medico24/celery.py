import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medico24.settings')

app = Celery('medico24')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

