import base64

from rest_framework.response import Response
from rest_framework.views import APIView

from outline_users.serializers import OutlineKeySerializer
from outline_users.models import OutlineKey, OutlineUser, Logging


class OutlineKeysView(APIView):

    def get(self, request, pk):
        key_data = OutlineKey.objects.get(pk=pk)
        serializer = OutlineKeySerializer(key_data)
        user_ip_1 = request.META.get('REMOTE_ADDR')
        user_ip_2 = request.META.get('HTTP_X_FORWARDER_FOR')
        print(user_ip_1)
        print(user_ip_2)
        uniq_id = request.GET.get('uniq_id')
        outline_user = OutlineUser.objects.get(uniq_id=uniq_id)
        outline_user.ip_address = user_ip_1
        outline_user.save()

        log_write = Logging()
        log_write.outline_key = key_data
        log_write.ip_address = user_ip_2
        log_write.outline_user = outline_user
        log_write.save()

        key, server_data = serializer.data.get('outline_key').split('//')[1].split('@')
        decode_key = base64.b64decode(key).decode('utf-8')
        method, password = decode_key.split(':')
        server, server_port = server_data.split('/')[0].split(':')
        key_data = {
                'server': server,
                'server_port': server_port,
                'password': password,
                'method': method,
        }
        return Response(key_data)

    def post(self, request):
        key_data = {'outline_key': request.data.get('outline_key')}
        serializer = OutlineKeySerializer(data=key_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class KeyForOutline(APIView):

    def get(self, request, pk):
        host = request.get_host()
        uniq_id = request.GET.get('uniq_id')
        string_for_encode = f'{host}/post-key/{pk}?uniq_id={uniq_id}'
        encoded_host = base64.b64encode(string_for_encode.encode()).decode()
        return Response(f'ssconf://{encoded_host}')

