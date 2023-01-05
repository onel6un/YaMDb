from django.urls import path, include

from rest_framework import routers

from .views import *

APP_NAME = 'reviews'

router = routers.DefaultRouter()

router.register('v1/categories', CategoriesAPI)
router.register('v1/genries', GenriesAPI)
router.register('v1/titles', TitlesAPI)

urlpatterns = [
    path('', include(router.urls))
]
