from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    pass


class TypeJewelry(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Jewelry(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(TypeJewelry, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    jewelries = models.ManyToManyField(Jewelry, through='BasketJewelry', related_name='baskets')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Basket of {self.user.username}"


class BasketJewelry(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    jewelry = models.ForeignKey(Jewelry, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.jewelry.name} in basket of {self.basket.user.username}"