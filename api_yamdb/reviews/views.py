from django.shortcuts import render

from rest_framework import viewsets

from .models import *
from .serializers import *


class CategoriesAPI(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GenriesAPI(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenresSerializer


class TitlesAPI(viewsets.ModelViewSet):
    queryset = Title.objects.all()

    # использование двух сериализаторов диктуеться ТЗ,
    # для записи поля genre и category используеться slugRelatedField
    # для чтения поля genre в виде списка словарей используеться вложенный сериализатор,
    # для чтения поля category в виде словаря используеться вложенный сериализатор,
    # что и требует отдельных сериализаторов для чтения и записи
    def get_serializer_class(self):
        print(self.action)
        if self.action is 'list' or self.action is 'retieve':
            return TitlesSerializerForRead
        return TitlesSerializerForCreate