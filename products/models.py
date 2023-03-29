from os import path

from django.core.validators import MinValueValidator
from django.db import models

from project.constans import MAX_DIGITS, DECIMAL_PLACES
from project.mixins.models import PKMixin


def upload_to(instance, filename):
    _name, extension = path.splitext(filename)
    return f'products/images/{str(instance.pk)}{extension}'


class Category(PKMixin):
    name = models.CharField(max_length=255)
    description = models.TextField(
        blank=True,
        null=True
    )
    image = models.ImageField(upload_to=upload_to)


class Product(PKMixin):
    name = models.CharField(max_length=255)
    description = models.TextField(
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to=upload_to,
        null=True,
        blank=True
    )
    sku = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category, blank=True)
    products = models.ManyToManyField("products.Product", blank=True)
    price = models.DecimalField(
        validators=[MinValueValidator(0)],
        max_digits=MAX_DIGITS,
        decimal_places=DECIMAL_PLACES
    )


class Discount(models.Model):
    DISCOUNT_TYPE_CHOICES = [
        (0, 'money'),
        (1, 'percent'),
    ]

    amount = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    code = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    discount_type = models.IntegerField(choices=DISCOUNT_TYPE_CHOICES)
