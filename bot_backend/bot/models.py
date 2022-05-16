from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    pass


class User(AbstractUser):

    phone_number = models.CharField(max_length=17, null=True, blank=True)

    objects = CustomUserManager()


