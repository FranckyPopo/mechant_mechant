from django import forms
from authentication.models import User
#print(help(forms.PasswordInput))
class FormRegister(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ["last_name", "first_name", "email", "telephone_number", "password",]
