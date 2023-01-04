import jwt

from datetime import timedelta, datetime
from random import randrange
from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import RefreshToken


from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager


class UserManagerCustom(UserManager):
    ''' Кастомный менеджр посльзователей'''
    
    def create_user(self, username, email, password):
        if username is None:
            return TypeError('Пользователь должен иметь username')
        
        if email is None:
            return TypeError('Пользователь должен иметь email')
        
        if password is None:
            return TypeError('Пользователь должен иметь пароль')

        # сгенирируем подтверждающий код
        confirm_code = self.set_confirm_code()

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.confirm_code = confirm_code
        user.save()

        # отправим писькмо с кодом подтверждения
        self.send_confirm_mail(email, confirm_code)

        return user


    def set_confirm_code(self):
        return randrange(100000, 999999)
    
    def send_confirm_mail(self, email, confim_code):
        text = f'Ваш код активации:{confim_code}'
        send_mail(
            subject='Подтверждение активации',
            message=text,
            from_email=email,
            recipient_list=[email],
        )


class User(AbstractUser):
    'Переопределили модель пользователя'
    is_confirm= models.BooleanField(default=False)
    is_moderator = models.BooleanField(blank=True, default=False)
    is_admin = models.BooleanField(blank=True, default=False)
    confirm_code = models.IntegerField(blank=True, null=True)
 

    #определим менеджер пользователей для данной модели
    objects = UserManagerCustom()

    def __str__(self):
        return self.username

    @property
    def token(self):
        ''' Получение токена путем вызова user._generate_jwt_token()'''
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        '''Генерирует JWT токен'''
        refresh = RefreshToken.for_user(self)

        return str(refresh.access_token)