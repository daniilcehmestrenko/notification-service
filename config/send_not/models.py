from django.core.validators import RegexValidator
from django.db import models


class MailingList(models.Model):
    name = models.CharField(
            max_length=20,
            verbose_name='Название рассылки'
        )
    start_date = models.DateTimeField(
            verbose_name='Дата и время запуска рассылки'
        )
    message = models.ForeignKey(
            'Message',
            on_delete=models.DO_NOTHING,
            related_name='message',
            verbose_name='Cообщение'
        )
    client_filter = models.CharField(
            max_length=20,
            verbose_name='Код оператора или тег',
            help_text='По данному полю будут фильтроваться клиенты'
        )
    expiration_date = models.DateTimeField(
            verbose_name='Дата и время окончания рассылки'
        )
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Client(models.Model):
    phone = models.CharField(
            max_length=11,
            verbose_name='Номер телефона',
            help_text='формат:7XXXXXXXXXX',
            validators=[
                RegexValidator(regex=r'7\d{10}')
            ]
        )
    code = models.CharField(
            max_length=10,
            verbose_name='Код оператора'
        )
    timezone = models.CharField(
            max_length=10,
            verbose_name='Часовой пояс',
        )
    tag = models.CharField(
            max_length=50,
            verbose_name='Произвольная метка'
        )

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural='Клиенты'


class Message(models.Model):
    text = models.TextField(
            verbose_name='Текст сообщения'
        )

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
