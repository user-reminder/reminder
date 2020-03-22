import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reminder.settings')

app = Celery('reminder')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-emails-every-minute': {
        'task': 'notification.tasks.send_notifications',
        'schedule': crontab(),
    },
}
