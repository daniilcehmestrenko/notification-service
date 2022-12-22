from django.db.models import Q
from config.celery import app

from .models import Client, Message, MailingList
from .service import MessageSender


@app.task
def mailing_list_task(pk):
    mailing_list = MailingList.objects.get(pk=pk)
    client_filter = (
            Q(tag=mailing_list.client_filter) |
            Q(code=mailing_list.client_filter)
        )
    clients = Client.objects.filter(client_filter)
    clients_acces = []
    clients_failed = []

    for client in clients:
        status = MessageSender.send_message(
                    pk=mailing_list.pk,
                    phone=client.phone,
                    text=mailing_list.text
                )

        if status:
            clients_acces.append(client)
        else:
            clients_failed.append(client)

    if clients_acces:
        Message.objects.create_message(
                    status=True,
                    mailing_list=mailing_list,
                    clients=clients_acces
                )
    if clients_failed:
        Message.objects.create_message(
                    status=False,
                    mailing_list=mailing_list,
                    clients=clients_failed
                )

