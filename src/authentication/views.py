from django.shortcuts import render, redirect
from django.views.generic import View

from pprint import pprint

from authentication import forms
# Create your views here.
class AuthenticationPageRegister(View):
    def get(self, request):
        form = None
        return render(request, "front/pages/register.html", context={"form": forms.FormRegister })
    
    def post(self, request):
        form = forms.FormRegister(request.POST)
        print(self.request.POST)
        
        if form.is_valid():
            print("oui")
        else:
            print("nom")
            
            
        return redirect('authentication_register') 