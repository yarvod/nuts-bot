from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    pass


class User(AbstractUser):

    phone_number = models.CharField(max_length=17, null=True, blank=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    username = models.CharField(
        max_length=150,
        unique=True,
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        error_messages={
            "unique": "A user with that username already exists."
        }
    )

    objects = CustomUserManager()


# class Product(models.Model):
#     title = models.CharField(max_length=150)
#     description = models.TextField()
#
#     photo = models.FilePathField(null=True, blank=True)
#
#     price = models.PositiveIntegerField(default=0)



