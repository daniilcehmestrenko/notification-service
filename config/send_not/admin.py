from django.contrib import admin

from .models import Client, MailingList, Message

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('phone', 'code', 'tag')
    list_display_links = ('phone',)


@admin.register(MailingList)
class MailingListAdmin(admin.ModelAdmin):
    list_display = ('name', 'client_filter')
    list_display_links = ('name',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('text',)
