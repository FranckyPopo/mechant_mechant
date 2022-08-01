from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.text import slugify

import random

from front.models import Products 

    
@receiver(pre_save, sender=Products)
def generator_slug(instance, *args, **kwargs):
    "Cette fonction va permtre de générer le slug de chaque produit"
    if not instance.slug:
        instance.slug = f"{slugify(instance.name)}-{random.randint(0, 100)}"    
     