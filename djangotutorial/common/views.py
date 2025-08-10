import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection
from django.db.utils import OperationalError
from .serializers import HealthCheckSerializer


class HealthCheckView(APIView):
    def get_serializer(self, *args, **kwargs):
        if self.request.method == 'POST':
            return HealthCheckSerializer(*args, **kwargs)


    def get(self, request):
        data = {'healthy': True}
        return Response(data)


    def post(self, request):
        data = {'healthy': True}
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        component = serializer.data["component"]

        if component == serializer.DATABASE:
            try:
                connection.ensure_connection()
            except OperationalError:
                data['healthy'] = False

        if component == serializer.API_INTEGRATION:
            response = requests.get("https://www.google.com")

            if response.status_code != 200:
                data["healthy"] = False

        return Response(data)
