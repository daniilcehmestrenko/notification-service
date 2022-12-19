from django.db.models import Count, F, Q
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Client, MailingList, Message
from .serializers import ClientSerializer, MailingListSerializer
from .service import SendMail


class MailingStartAPIView(SendMail, APIView):

    def create_message(self, status, mailing_list, clients):
        new_message = Message.objects.create(
                status=status,
                mailing_list=mailing_list,
            )
        new_message.clients.set(clients)

    def get(self, request, pk):
        mailing_list = MailingList.objects.get(pk=pk)
        client_filter = (
                Q(tag=mailing_list.client_filter) |
                Q(code=mailing_list.client_filter)
            )
        clients = Client.objects.filter(client_filter)
        clients_accept = []
        clients_failed = []

        for client in clients:
            if self.send_mail(
                    pk=pk,
                    phone=int(client.phone),
                    text=mailing_list.text):
                clients_accept.append(client)
            else:
                clients_failed.append(client)

        if clients_accept:
            self.create_message(
                    mailing_list=mailing_list,
                    status=True,
                    clients=clients_accept
                )

        if clients_failed:
            self.create_message(
                    mailing_list=mailing_list,
                    status=False,
                    clients=clients_failed
                )

        return Response({"Message": "Рассылка прошла успешно"})


class TotalStatsDetailAPIView(APIView):

    def get(self, request, pk):
        mailing_list = MailingList.objects.get(pk=pk)
        data = (
                mailing_list.messages
                .values('status')
                .annotate(
                    count_message=Count('clients')
                )
                .values(
                    message_status=F('status'),
                    count_message=F('count_message'),
                )
            )
        mailing_list_data = {
                "mailing_list_pk": pk,
                "client_filter": mailing_list.client_filter,
                "mailing_stats": data
            }

        return Response(mailing_list_data)


class TotalStatsListAPIView(APIView):

    def get(self, request):
        queryset = (
            MailingList.objects
            .values('messages__status')
            .annotate(
                count_message=Count('messages__clients'),
            )
            .values(
                message_status=F('messages__status'),
                mailing_list_pk=F('pk'),
                client_filter=F('client_filter'),
                count_message=F('count_message')
            )
            .order_by('client_filter')
        )

        return Response(queryset)



class ClientListAPIView(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class MailingListAPIView(ListCreateAPIView):
    queryset = MailingList.objects.all()
    serializer_class = MailingListSerializer


class MailingListDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = MailingList.objects.all()
    serializer_class = MailingListSerializer
