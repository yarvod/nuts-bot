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


class Product(models.Model):
    code = models.PositiveIntegerField(unique=True)
    title = models.CharField(max_length=150)
    description = models.TextField()
    photo = models.ImageField(upload_to='media/photos/products')
    amount = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    finished = models.DateTimeField(null=True, blank=True)

    def finish(self):
        self.is_active = False


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_products')



