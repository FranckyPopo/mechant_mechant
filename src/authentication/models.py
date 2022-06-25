from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    telephone_number = PhoneNumberField(unique=True)
    
    
    def __str__(self) -> str:
        return self.username