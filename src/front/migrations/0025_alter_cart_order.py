# Generated by Django 4.0.5 on 2022-07-26 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0024_cart_ordered_alter_cart_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='order',
            field=models.ManyToManyField(blank=True, null=True, to='front.order'),
        ),
    ]