# Generated by Django 4.0.5 on 2022-08-01 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0029_products_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
