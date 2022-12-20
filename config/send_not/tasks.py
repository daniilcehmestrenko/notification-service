from django.db.models import Q
from config.celery import app

from .models import Client, Message, MailingList
from .service import MessageSender


@app.task
def send_message_task(pk):
    mailing_list = MailingList.objects.get(pk=pk)
    client_filter = (
            Q(tag=mailing_list.client_filter) |
            Q(code=mailing_list.client_filter)
        )
    clients = Client.objects.filter(client_filter)
    clients_accept = []
    clients_failed = []

    for client in clients:
        if MessageSender.send_message(
                pk=mailing_list.pk,
                phone=int(client.phone),
                text=mailing_list.text
            ):
            clients_accept.append(client)
        else:
            clients_failed.append(client)

    if clients_accept:
        Message.objects.create_message(
                mailing_list=mailing_list,
                status=True,
                clients=clients_accept
            )

    if clients_failed:
        Message.objects.create_message(
                mailing_list=mailing_list,
                status=False,
                clients=clients_failed
            )
