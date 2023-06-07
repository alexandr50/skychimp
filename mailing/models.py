from django.db import models

from customer.models import Customer
from user.models import User



class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель')
    theme = models.CharField(max_length=50, verbose_name='Тема')
    content = models.TextField(verbose_name='Контент')

    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

class Sending(models.Model):

    ONE_A_DAY = 'раз в день'
    ONE_A_WEEK = 'раз в неделю'
    ONE_A_MONTH = 'раз в месяц'

    INTERVAL = (
        (ONE_A_DAY, 'one_a_day'), (ONE_A_WEEK, 'one_a_week'), (ONE_A_MONTH, 'one_a_month')
    )
    COMPLITED = 'Завершена'
    CREATED = 'Создана'
    ACTIVATED = 'Запущена'

    STATUS = (
        (COMPLITED, 'complited'), (CREATED, 'created'), (ACTIVATED, 'activated')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель')
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, verbose_name='Клиент', null=True)
    message = models.ForeignKey(Message, on_delete=models.SET_NULL, verbose_name='Сообщение', null=True)
    time_sending = models.DateTimeField(auto_now_add=True, verbose_name='Время рассылки', blank=True, null=True)
    interval = models.CharField(choices=INTERVAL, max_length=30, verbose_name='Периодичность')
    status_sending = models.CharField(choices=STATUS, max_length=30, verbose_name='статус')




class TrySending(models.Model):
    last_attempt = models.DateTimeField(auto_now_add=True, verbose_name='Дата последней попытки')
    status_attempt = models.CharField(max_length=30, verbose_name='Текущий статус')
    answer_server = models.CharField(max_length=20, verbose_name='Ответ почтового сервера')