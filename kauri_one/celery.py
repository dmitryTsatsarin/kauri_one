from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kauri_one.settings')

app = Celery('kauri_one')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


app.conf.task_routes = {'market_data_normalization.tasks.*': {'queue': 'market_data_normalization'}}


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))