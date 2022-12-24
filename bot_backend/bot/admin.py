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
    list_filter = ('is_active',)
    search_fields = ('slug', 'title',)
    readonly_fields = ('image_detail',)
    inlines = (ProductWeightPriceInline,)
    actions = ('set_active', 'set_inactive',)

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
        ratio = obj.photo.width / obj.photo.height
        return format_html('<img src="{url}" width="{width}" height={height}/>'.format(
            url=obj.photo.url,
            width=50*ratio,
            height=50
            ))

    def image_detail(self, obj):
        ratio = obj.photo.width / obj.photo.height
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.photo.url,
            width=200*ratio,
            height=200,
            )
    )

    image_tag.short_description = 'Фото'
    image_detail.short_description = 'Фото превью'

    @admin.action(description='Установить ЕСТЬ в наличии')
    def set_active(modeladmin, request, queryset):
        queryset.update(is_active=True)

    @admin.action(description='Установить НЕТ в наличии')
    def set_inactive(modeladmin, request, queryset):
        queryset.update(is_active=False)
