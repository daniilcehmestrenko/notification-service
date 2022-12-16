from django.core.validators import RegexValidator
from django.db import models


class MailingList(models.Model):
    date_start = models.DateTimeField(
            verbose_name='Дата и время начала рассылки'
        )
    text = models.TextField(
            verbose_name='Текст рассылки'
        )
    client_filter = models.CharField(
            max_length=20,
            verbose_name='Фильтр клиентов'
        )
    date_end = models.DateTimeField(
            verbose_name='Дата и время окончания рассылки'
        )

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Client(models.Model):
    phone = models.CharField(
            max_length=11,
            verbose_name='Телефон',
            validators=[
                RegexValidator(regex=r'7\d{10}')
            ]
        )
    code = models.CharField(
            max_length=10,
            verbose_name='Код оператора'
        )
    tag = models.CharField(
            max_length=50,
            verbose_name='Произвольная метка'
        )
    time_zone = models.CharField(
            max_length=10,
            help_text='Формат: UCT+01:00',
            verbose_name='Часовой пояс'
        )

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Message(models.Model):
    date_create = models.DateTimeField(
            auto_now=True,
            verbose_name='Дата создания'
        )
    status = models.BooleanField(
            verbose_name='Статус отправки'
        )
    mailing_list = models.ForeignKey(
            'MailingList',
            on_delete=models.DO_NOTHING,
            related_name='messages',
            verbose_name='Рассылка'
        )
    clients = models.ManyToManyField(
            'Client',
            related_name='messages',
            verbose_name='Клиенты'
        )

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
