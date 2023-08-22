from django.contrib import admin

from mailing.models import Customer, Mailing, Massage


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'fio', 'email',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start', 'stop', 'interval', 'datetime')


@admin.register(Massage)
class MassageAdmin(admin.ModelAdmin):
    list_display = ('id', 'mail_subject')

