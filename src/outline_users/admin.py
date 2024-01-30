from django.contrib import admin

from outline_users.models import OutlineUser, OutlineKey, Logging


@admin.register(OutlineUser)
class OutlineUserAdmin(admin.ModelAdmin):
    fields = [
        'first_name',
        'last_name',
        'outline_key',
        'ip_address',
        'uniq_id',
    ]

    readonly_fields = ['uniq_id']


@admin.register(OutlineKey)
class OutlineKeyAdmin(admin.ModelAdmin):
    pass


@admin.register(Logging)
class LoggingAdmin(admin.ModelAdmin):
    pass
