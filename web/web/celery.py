import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'election_app.settings')

app = Celery('election_app', broker='redis://localhost')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
