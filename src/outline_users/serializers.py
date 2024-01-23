from rest_framework import serializers

from outline_users.models import OutlineKey


class OutlineKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = OutlineKey
        fields = ['outline_key']
