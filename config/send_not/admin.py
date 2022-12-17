from django.contrib import admin

from .models import Client, MailingList, Message


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('phone', 'code', 'tag')
    list_display_links = ('phone',)


@admin.register(MailingList)
class MailingListAdmin(admin.ModelAdmin):
    list_display = ('client_filter', 'date_start', 'date_end')
    list_display_links = ('client_filter',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'date_create', 'status')
    list_display_links = ('date_create',)
