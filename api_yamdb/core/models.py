from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_moderator = models.BooleanField(blank=True, default=False)
    is_admin = models.BooleanField(blank=True, default=False)