from django.contrib import admin

from authentication.models import *

class UserAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_moderator', 'is_admin', 'confirm_code') 
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_moderator', 'is_admin')
    # Добавляем возможность фильтрации 
    list_filter = ('id', 'username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_moderator', 'is_admin')

admin.site.register(User, UserAdmin)