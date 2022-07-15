from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

class User(AbstractUser):
    telephone_number = PhoneNumberField(unique=True, region="CI")
    
    def __str__(self) -> str:
        return self.username
    
class Cart(models.Model):
    session = None
    product = None
    
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)