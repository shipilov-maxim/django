from django.contrib.auth.models import AbstractUser
from django.db import models
from catalog.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    country = models.CharField(max_length=150, verbose_name='Страна', **NULLABLE)
    token = models.CharField(max_length=35, verbose_name='token', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='Статус')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
