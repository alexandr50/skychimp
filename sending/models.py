from django.db import models

from customer.models import Customer
from user.models import User



class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель')
    theme = models.CharField(max_length=50, verbose_name='Тема')
    content = models.TextField(verbose_name='Контент')


    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

class Sending(models.Model):

    ONE_A_DAY = 'раз в день'
    ONE_A_WEEK = 'раз в неделю'
    ONE_A_MONTH = 'раз в месяц'

    INTERVAL = (
        (ONE_A_DAY, 'раз в день'), (ONE_A_WEEK, 'раз в неделю'), (ONE_A_MONTH, 'раз в месяц')
    )
    COMPLITED = 'Завершена'
    CREATED = 'Создана'
    ACTIVATED = 'Запущена'

    STATUS = (
        (COMPLITED, 'завершена'), (CREATED, 'создана'), (ACTIVATED, 'активирована')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель')
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, verbose_name='Клиент', null=True)
    message = models.ForeignKey(Message, on_delete=models.SET_NULL, verbose_name='Сообщение', null=True)
    time_sending = models.DateTimeField(auto_now_add=True, verbose_name='Время рассылки', blank=True, null=True)
    interval = models.CharField(choices=INTERVAL, max_length=30, verbose_name='Периодичность')
    status_sending = models.CharField(choices=STATUS, max_length=30, verbose_name='статус')

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'




class TrySending(models.Model):
    last_attempt = models.DateTimeField(auto_now_add=True, verbose_name='Дата последней попытки')
    status_attempt = models.CharField(max_length=30, verbose_name='Текущий статус')
    answer_server = models.CharField(max_length=20, verbose_name='Ответ почтового сервера')


    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылок'