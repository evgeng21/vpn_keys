from django.contrib import admin

from outline_users.models import OutlineUser, OutlineKey


@admin.register(OutlineUser)
class OutlineUserAdmin(admin.ModelAdmin):
    pass


@admin.register(OutlineKey)
class OutlineKeyAdmin(admin.ModelAdmin):
    pass
