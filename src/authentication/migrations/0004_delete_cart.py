# Generated by Django 4.0.5 on 2022-07-16 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_cart'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
