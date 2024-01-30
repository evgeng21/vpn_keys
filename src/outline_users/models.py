import uuid

from django.db import models


class OutlineUser(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Имя', null=True, blank=True)
    last_name = models.CharField(max_length=30, verbose_name='Фамилия', null=True, blank=True)
    outline_key = models.ForeignKey('OutlineKey', on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='outline_user')
    ip_address = models.CharField(max_length=30, verbose_name='IP адрес', null=True, blank=True)
    uniq_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)


class OutlineKey(models.Model):
    outline_key = models.CharField(max_length=1000)


class Logging(models.Model):
    outline_user = models.ForeignKey(OutlineUser, on_delete=models.CASCADE)
    outline_key = models.ForeignKey(OutlineKey, on_delete=models.CASCADE)
    date_entry = models.DateTimeField(auto_now_add=True)
    ip_address = models.CharField(max_length=20)
