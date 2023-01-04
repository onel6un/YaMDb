from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view

from .serializer import *


class RegistrationAPI(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetTokenAPI(APIView):
    permission_classes = (AllowAny,)
    serializer_class = GetTokenSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
