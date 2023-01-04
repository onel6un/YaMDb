from django.urls import path, include

from rest_framework import routers

from .views import *

APP_NAME = 'reviews'

router = routers.DefaultRouter()

router.register('v1/categories', CategoriesAPI)

urlpatterns = [
    path('', include(router.urls))
]
