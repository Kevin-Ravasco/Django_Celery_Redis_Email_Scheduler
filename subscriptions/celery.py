import os

from celery import Celery

from django.conf import settings

# set the default Django settings module for the 'celery' program.


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EmailShedulerProject.settings')

app = Celery('EmailShedulerProject')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


'''app.conf.broker_url = 'redis://localhost:6379/0'
app.conf.result_backend = 'redis://localhost:6379/0'
app.conf.result_backend_transport_options = {
    'retry_policy': {
       'timeout': 5.0
    }
}'''