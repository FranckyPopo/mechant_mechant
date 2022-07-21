<<<<<<< HEAD
=======
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

class User(AbstractUser):
    telephone_number = PhoneNumberField(unique=False, region="CI")
    
    def __str__(self) -> str:
        return self.username
    
>>>>>>> 34021d3 (reglage send message ,ajout connect page edit prpfile,)
