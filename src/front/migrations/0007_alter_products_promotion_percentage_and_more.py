# Generated by Django 4.0.5 on 2022-07-15 18:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0006_remove_products_promotion_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='promotion_percentage',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='products',
            name='promotion_reduction',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]
