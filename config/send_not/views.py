from django.db.models import Count
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Client, MailingList, Message
from .serializers import ClientSerializer, MailingListSerializer, MessageSerializer, TotalStatsSerializer


class TotalStatsAPIView(APIView):

    def get(self, request):
        queryset = (
            MailingList.objects
            .filter(messages__status=True)
            .annotate(count_messages=Count('messages__clients'))
        )
        serializer = TotalStatsSerializer(queryset, many=True)

        return Response(serializer.data)



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
