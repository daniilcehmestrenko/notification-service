from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Client, MailingList, Message
from .serializers import ClientSerializer, MailingListSerializer, MessageSerializer


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
