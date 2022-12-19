from rest_framework.serializers import ModelSerializer

from .models import Client, MailingList


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class MailingListSerializer(ModelSerializer):
    class Meta:
        model = MailingList
        fields = '__all__'
