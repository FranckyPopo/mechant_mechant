from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

from front.models import DeliveryAddress

class User(AbstractUser):
    telephone_number = PhoneNumberField(unique=True, region="CI")
    delivery_address = models.ManyToManyField(
        DeliveryAddress,
        blank=True,
        null=True,
        related_name="user_delivery_address"
    )
    
    def __str__(self) -> str:
        return self.username
    
