from django.conf import settings
from rest_framework import serializers

from bot.models import Product, ProductWeightPrice


class ProductWeightPriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductWeightPrice
        fields = ('weight', 'price')


class ProductSerializer(serializers.ModelSerializer):
    productweightprice_set = ProductWeightPriceSerializer(many=True)
    photo = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('slug', 'title', 'description', 'photo', 'productweightprice_set')

    @staticmethod
    def get_photo(obj):
        if obj.photo:
            return settings.MEDIA_PREFIX + obj.photo.url
        return None
