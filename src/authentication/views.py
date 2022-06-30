from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse 

from authentication import forms
# Create your views here.
class AuthenticationPageRegister(View):
    def get(self, request):
        form = forms.FormRegister
        return render(request, "front/pages/register.html", context={"form": form})
    
    def post(self, request):
        form = forms.FormRegister(request.POST)
                
        if form.is_valid():
            form.save()
            return HttpResponse("compte créé avec succése")
        else:
            return render(request, "front/pages/register.html", context={"form": form})
            
        return render(request, "front/pages/register.html", context={"form": form})
        # return redirect('authentication_register') 