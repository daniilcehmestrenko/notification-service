from django.urls import path

from .views import (ClientDetailAPIView, ClientListAPIView, MailingListAPIView,
                    MailingListDetailAPIView, MailingStartAPIView,
                    TotalStatsDetailAPIView, TotalStatsListAPIView,)


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
        'totalstats/',
        TotalStatsListAPIView.as_view(),
        name='total_stats'
    ),
    path(
        'totalstats/<int:pk>/',
        TotalStatsDetailAPIView.as_view(),
        name='total_stats_detail'
    ),
    path(
        'mailingstart/<int:pk>/',
        MailingStartAPIView.as_view(),
        name='mailingstart'
    ),
]
