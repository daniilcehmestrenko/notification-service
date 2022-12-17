from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from .models import Client, MailingList, Message


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class MailingListSerializer(ModelSerializer):
    class Meta:
        model = MailingList
        fields = '__all__'


class MessageSerializer(ModelSerializer):
    mailing_list = MailingListSerializer(
                read_only=True
            )
    mailing_list_id = PrimaryKeyRelatedField(
                write_only=True,
                source='mailing_list',
                queryset=MailingList.objects.all()
            )
    clients = ClientSerializer(
                read_only=True,
                many=True,
            )
    clients_id = PrimaryKeyRelatedField(
                write_only=True,
                many=True,
                source='clients',
                queryset=Client.objects.all()
            )

    class Meta:
        model = Message
        fields = '__all__'
