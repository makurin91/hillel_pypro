# Generated by Django 4.1.7 on 2023-03-27 17:33

from django.db import migrations
from faker import Faker

fake = Faker()


def start(apps, schema_editor):
    Product = apps.get_model('products', 'Product')
    Category = apps.get_model('products', 'Category')

    for _ in range(5):
        Category.objects.create(
            name=fake.word(),
            description=fake.sentence(),
        )

    for _ in range(10):
        product = Product.objects.create(
            name=fake.word(),
            description=fake.sentence(),
            sku=fake.random_number(),
            price=fake.pydecimal(left_digits=4, right_digits=2, positive=True)
        )
        categories = Category.objects.order_by('?')[:2]
        product.categories.add(*categories)


def end(apps, schema_editor):
    apps.get_model('products', 'Product')
    apps.get_model('products', 'Category')


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(
            start,
            end
        )
    ]
