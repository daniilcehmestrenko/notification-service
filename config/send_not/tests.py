from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Client, MailingList
from .serializers import ClientSerializer, MailingListSerializer


class SendNotTests(APITestCase):
    
    def setUp(self):
        self.one_mailing_list = MailingList.objects.create(
                date_start='2022-12-22T11:11:00Z',
                text='Test!',
                client_filter='#mts',
                date_end='2022-12-22T11:11:00Z'
            )

        self.one_client = Client.objects.create(
                phone='79172414137',
                code='7',
                tag='#mts',
                time_zone='UCT+00:00'
            )

    def test_client_list(self):
        serializer = ClientSerializer(self.one_client)
        response = self.client.get(reverse('clients'))
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(serializer.data in response.json())

    def test_client_detail(self):
        serializer = ClientSerializer(self.one_client)
        response = self.client.get(
                reverse(
                    'client_detail',
                    kwargs={'pk': self.one_client.pk}
                )
            )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serializer.data)

    def test_mailing_list(self):
        serializer = MailingListSerializer(self.one_mailing_list)
        response = self.client.get(reverse('mailing_list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(serializer.data in response.json())

    def test_mailing_detail(self):
        serializer = MailingListSerializer(self.one_mailing_list)
        response = self.client.get(
                reverse(
                    'mailing_list_detail',
                    kwargs={'pk': self.one_mailing_list.pk}
                )
            )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serializer.data)
