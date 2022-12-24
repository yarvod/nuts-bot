from django.contrib import admin
from django.utils.html import format_html

from .models import Order, Product, ProductWeightPrice


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


class ProductWeightPriceInline(admin.TabularInline):
    model = ProductWeightPrice
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title', 'image_tag', 'is_active')
    readonly_fields = ('image_detail',)
    inlines = (ProductWeightPriceInline,)

    fieldsets = [
        ['Основное', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('is_active', 'slug', 'title', 'description')
        }],
        ['Фото', {
            'classes': ('wide', 'extrapretty'),
            'fields': ['photo', 'image_detail'],
        }]
    ]

    def image_tag(self, obj):
        return format_html('<img src="{url}" width="{width}" height={height}/>'.format(
            url=obj.photo.url,
            width=obj.photo.width // 15,
            height=obj.photo.height // 15
            ))

    def image_detail(self, obj):
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.photo.url,
            width=obj.photo.width // 5,
            height=obj.photo.height // 5,
            )
    )

    image_tag.short_description = 'Фото'
    image_detail.short_description = 'Фото превью'
