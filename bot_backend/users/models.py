from django.contrib.auth.models import UserManager, AbstractUser, Group, GroupManager
from django.db import models


class CustomUserManager(UserManager):
    pass


class CustomGroup(Group):
    class Meta:
        proxy = True
        verbose_name = 'Группа пользователей'
        verbose_name_plural = 'Группы пользователей'


class User(AbstractUser):
    phone_number = models.CharField(max_length=17, null=True, blank=True, verbose_name='Номер телефона')
    first_name = models.CharField(max_length=150, blank=True, null=True, verbose_name='Имя')
    last_name = models.CharField(max_length=150, blank=True, null=True, verbose_name='Фамилия')
    username = models.CharField(
        max_length=150,
        unique=True,
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        error_messages={
            "unique": "A user with that username already exists."
        },
        verbose_name='Юзернейм'
    )

    objects = CustomUserManager()
