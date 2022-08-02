from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.text import slugify

from front.models import Products

import random


@receiver(pre_save, sender=Products)
def slug_ganerator(instance, *args, **kwargs):
    if not instance.slug:
        instance.slug =  f"{slugify(instance.name)}-{random.randint(0, 1000)}"

