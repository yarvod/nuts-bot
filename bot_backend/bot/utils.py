from collections import OrderedDict

from bot.models import Product
from bot.serializers import ProductSerializer
from users.models import User


def update_or_create_user(user) -> None:
    user_db, created = User.objects.update_or_create(
        id=user.id,
        defaults=dict(
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name
        )
    )


def get_catalog() -> OrderedDict:
    queryset = Product.objects.prefetch_related('productweightprice_set').filter(is_active=True)
    return ProductSerializer(queryset, many=True).data


def get_product(slug: str):
    if not slug:
        return None
    obj = Product.objects.filter(slug=slug).first()
    return ProductSerializer(obj).data

