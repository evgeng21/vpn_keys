from django.db import models


class OutlineUser(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Имя', null=True, blank=True)
    last_name = models.CharField(max_length=30, verbose_name='Фамилия', null=True, blank=True)
    outline_key = models.ForeignKey('OutlineKey', on_delete=models.SET_NULL, null=True, blank=True, related_name='outline_user')
    ip_address = models.CharField(max_length=30, verbose_name='IP адрес', null=True, blank=True)


class OutlineKey(models.Model):
    json_key = models.JSONField()
