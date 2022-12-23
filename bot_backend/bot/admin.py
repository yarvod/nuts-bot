from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, Order, Product


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{url}" width="{width}" height={height}/>'.format(
            url=obj.photo.url,
            width=obj.photo.width // 15,
            height=obj.photo.height // 15
            ))

    def image_detail(self, obj):
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.photo.url,
            width=obj.photo.width // 5,
            height=obj.photo.height // 5,
            )
    )

    image_tag.short_description = 'Photo'

    list_display = ('code', 'title', 'amount', 'price', 'image_tag',)
    readonly_fields = ('image_detail',)

    fieldsets = [
        ['Main info', {
            'classes' : ('wide', 'extrapretty'),
            'fields' : ('code', 'title', 'description', 'amount', 'price')
        }],
        ['Photo', {
            'classes': ('wide', 'extrapretty'),
            'fields':['photo', 'image_detail']
        }],
    ]