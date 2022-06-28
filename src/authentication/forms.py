from django import forms

from authentication.models import User

class FormRegister(forms.ModelForm):
    password2 = forms.PasswordInput(attrs={"type": "password"})
    password = forms.PasswordInput(attrs={"type": "password"})
    
    class Meta:
        model = User
        fields = ["last_name", "first_name", "email", "telephone_number", "password"]
