from django.urls import path
from rest_framework import routers
from authentication.views import *
from rest_framework_simplejwt.views import TokenObtainPairView

APP_NAME = 'auth'

urlpatterns = [
    path('register/', RegistrationAPI.as_view()),
    path('token/', GetTokenAPI.as_view()),
]
