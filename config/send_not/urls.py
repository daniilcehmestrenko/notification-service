from django.urls import path

from .views import (ClientDetailAPIView, ClientListAPIView, MailingListAPIView,
                    MailingListDetailAPIView, MessageDetailAPIView, MessageListAPIView,)


urlpatterns = [
    path(
        'client/',
        ClientListAPIView.as_view(),
        name='clients'
    ),
    path(
        'client/<int:pk>/',
        ClientDetailAPIView.as_view(),
        name='client_detail'
    ),
    path(
        'mailinglist/',
        MailingListAPIView.as_view(),
        name='mailing_list'
    ),
    path(
        'mailinglist/<int:pk>/',
        MailingListDetailAPIView.as_view(),
        name='mailing_list_detail'
    ),
    path(
        'message/',
        MessageListAPIView.as_view(),
        name='messages'
    ),
    path(
        'message/<int:pk>/',
        MessageDetailAPIView.as_view(),
        name='message_detail'
    ),
]
