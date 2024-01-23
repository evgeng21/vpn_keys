import base64

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from outline_users.serializers import OutlineKeySerializer
from outline_users.models import OutlineKey


class OutlineKeysView(APIView):

    def get(self, request, pk):
        key_data = OutlineKey.objects.get(pk=pk)
        serializer = OutlineKeySerializer(key_data)
        user_ip = request.META.get('REMOTE_ADDR', 'HTTP_X_FORWARDER_FOR')
        outline_user = key_data.outline_user.all().first()
        outline_user.ip_address = user_ip
        outline_user.save()
        return Response(serializer.data.get('json_key'))

    def post(self, request):
        key, server_data = request.data.get('outline_key').split('//')[1].split('@')
        decode_key = base64.b64decode(key).decode('utf-8')
        method, password = decode_key.split(':')
        server, server_port = server_data.split('/')[0].split(':')
        key_data = {
            'json_key': {
                'server': server,
                'server_port': server_port,
                'password': password,
                'method': method,
            }
        }
        serializer = OutlineKeySerializer(data=key_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
