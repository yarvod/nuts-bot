from django.db import models

from bot.constants import Weights


class Product(models.Model):
    is_active = models.BooleanField(default=False, verbose_name='Есть в наличии')
    slug = models.SlugField(verbose_name='Идентификатор', db_index=True, help_text='Уникальная строка')
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='media/photos/products', verbose_name='Фото')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


class ProductWeightPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    weight = models.IntegerField(choices=Weights.CHOICES, default=Weights.WT90, verbose_name='Вес')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')

    class Meta:
        verbose_name = 'Развесовка продукта'
        verbose_name_plural = 'Развесовки продукта'

    def __str__(self):
        return f"{self.product.slug}; {self.weight}; {self.price}"


class Order(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='orders', verbose_name='Пользователь')
    is_active = models.BooleanField(default=True, verbose_name='Заказ активен')
    is_refused = models.BooleanField(default=True, verbose_name='Заказ отменен')
    is_success = models.BooleanField(default=True, verbose_name='Заказ успешно завершен')
    created = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    finished = models.DateTimeField(null=True, blank=True, verbose_name='Дата завершения')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-created',)

    def __str__(self):
        return f"Заказ {self.id}"

    def finish(self):
        self.is_active = False


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    amount = models.PositiveIntegerField(default=0, verbose_name='Количество упаковок')
    weight = models.IntegerField(choices=Weights.CHOICES, default=Weights.WT90, verbose_name='Вес')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_products', verbose_name='Заказ')

    class Meta:
        verbose_name = 'Продукт в заказе'
        verbose_name_plural = 'Продукты в заказе'

    def __str__(self):
        return f"Продукт {self.product.slug} в заказе {self.order.id}"
