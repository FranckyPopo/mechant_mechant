# Generated by Django 4.0.5 on 2022-07-16 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newslater',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]