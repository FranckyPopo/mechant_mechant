from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

class User(AbstractUser):
    telephone_number = PhoneNumberField(unique=True, region="CI")
    
    def __str__(self) -> str:
        return self.username
    
