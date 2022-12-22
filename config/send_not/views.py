from django_celery_beat.models import CrontabSchedule, PeriodicTask
from django.db.models import Count, F
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Client, MailingList
from .serializers import ClientSerializer, MailingListSerializer
from .tasks import mailing_list_task

class MailingStartAPIView(APIView):

    def get(self, request, pk):
        mailing_list_task.delay(pk)

        return Response({"Message": "Рассылка запущена"})


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

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        mailing_list = MailingList.objects.last()
        if mailing_list:
            date_start = mailing_list.date_start
            schedule = CrontabSchedule.objects.create(
                        minute=date_start.strftime('%M'),
                        hour=date_start.strftime('%H'),
                        day_of_week='*',
                        day_of_month=date_start.strftime('%d'),
                        month_of_year=date_start.strftime('%m'),
                    )
            PeriodicTask.objects.create(
                        crontab=schedule,
                        name=f'Mailing list {mailing_list.pk}',
                        task='send_not.tasks.mailing_list_task',
                        one_off=True,
                        args=[mailing_list.pk],
                        start_time=mailing_list.date_start
                    )

        return new_mailing_list


class MailingListDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = MailingList.objects.all()
    serializer_class = MailingListSerializer
