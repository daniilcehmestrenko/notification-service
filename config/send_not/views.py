from django.db.models import Count, F
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Client, MailingList, Message
from .serializers import ClientSerializer, MailingListSerializer, MessageSerializer


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
                count_messages=Count('messages__clients'),
                mailing_list_pk=F('pk'),
                client_filter=F('client_filter')
            )
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


class MessageListAPIView(ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
