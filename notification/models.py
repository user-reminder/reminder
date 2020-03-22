from django.db import models
from user.models import User


class Notification(models.Model):
    """Уведомление"""
    title = models.CharField(verbose_name="Заголовок", max_length=256)
    description = models.TextField(verbose_name="Описание")
    place = models.CharField(verbose_name="Место", max_length=256)
    creation_date = models.DateTimeField(verbose_name="Дата создания",
                                         auto_now_add=True)
    completion_date = models.DateTimeField(verbose_name="Дата наступления")
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='owner', verbose_name='Автор')
    recipients = models.ManyToManyField(User, related_name='recipients',
                                        verbose_name='Участники')
    is_completed = models.BooleanField(verbose_name='Завершен', default=False)

    class Meta:
        db_table = 'notification'
        verbose_name = u'Уведомление'
