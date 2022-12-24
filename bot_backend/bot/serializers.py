from rest_framework import serializers

from bot.models import Product, ProductWeightPrice


class ProductWeightPriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductWeightPrice
        fields = ('weight', 'price')


class ProductSerializer(serializers.ModelSerializer):
    productweightprice_set = ProductWeightPriceSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'
