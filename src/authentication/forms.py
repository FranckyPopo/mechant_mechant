from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from authentication.models import User

class FormRegister(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["last_name", "first_name", "email", "username", "telephone_number"]
        