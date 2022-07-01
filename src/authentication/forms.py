from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

import re

from authentication.models import User

class FormRegister(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["last_name", "first_name", "email", "username", "telephone_number"]
    
class FormEditProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ["last_name", "first_name", "email", "username", "telephone_number"]
    
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        
        if not first_name:
            raise ValidationError("Ce champ est obligatoire")
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        
        if not last_name:
            raise ValidationError("Ce champ est obligatoire")
        return last_name
        
    def clean_email(self):
        email = self.cleaned_data['email']

        if not email:
            raise ValidationError("Ce champ est obligatoire")
        return email
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)