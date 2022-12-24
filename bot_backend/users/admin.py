from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import Group

from users.models import User, CustomGroup


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ...


@admin.register(CustomGroup)
class GroupAdmin(BaseGroupAdmin):
    ...
