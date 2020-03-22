from datetime import datetime

from django.conf import settings
from django.core.mail import send_mail
from django.utils.timezone import utc

from notification.models import Notification
from reminder.celery import app

TITLE = 'Напоминание'
MESSAGE_TEMPLATE = 'Заголовок: {title}\nОписание: {description}\n' \
                   'Место: {place}\nУчастники: {recipients}\n' \
                   'Дата создания: {creation_date}\n' \
                   'Дата наступления: {completion_date}'


@app.task
def send_notifications():
    notifications = Notification.objects.select_related(
        'owner'
    ).prefetch_related(
        'recipients'
    ).filter(
        is_completed=False,
        completion_date__lte=datetime.now(tz=utc)
    )

    for ntf in notifications:
        message = MESSAGE_TEMPLATE.format(
            title=ntf.title,
            description=ntf.description,
            place=ntf.place,
            recipients=", ".join([r.username for r in ntf.recipients.all()]),
            creation_date=ntf.creation_date.strftime("%Y-%m-%d %H:%M:%S"),
            completion_date=ntf.completion_date.strftime("%Y-%m-%d %H:%M:%S"),
        )
        all_recipients_emails = list({r.email for r in ntf.recipients.all()} |
                                     {ntf.owner.email})
        for recipient in all_recipients_emails:
            send_mail(TITLE, message, settings.EMAIL_HOST_USER, [recipient])
        ntf.is_completed = True
        ntf.save()
