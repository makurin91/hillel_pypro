# Generated by Django 4.1.7 on 2023-03-29 23:46

import django.core.validators
from django.db import migrations, models
import products.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to=products.models.upload_to)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('code', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('discount_type', models.IntegerField(choices=[(0, 'money'), (1, 'percent')])),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=products.models.upload_to)),
                ('sku', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=18, validators=[django.core.validators.MinValueValidator(0)])),
                ('categories', models.ManyToManyField(blank=True, to='products.category')),
                ('products', models.ManyToManyField(blank=True, to='products.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
