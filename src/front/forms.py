from django import forms

from front.models import DeliveryAddress

class FormAddress(forms.ModelForm):
    class Meta:
        model = DeliveryAddress
        fields = ["addresse", "phone", "additional_information"]