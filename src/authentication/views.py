from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from authentication import forms

# Create your views here.
class AuthenticationPageRegister(View):
    form = forms.FormRegister
    template_name = "front/pages/register.html"
    
    def get(self, request):
        return render(request, self.template_name, context={"form": self.form})
    
    def post(self, request):
        form = self.form(request.POST)
                
        if form.is_valid():
            form.save()
            return redirect("authentication_login")
        return render(request, self.template_name, context={"form": form})

class AuthenticationLogin(View):
    form = forms.LoginForm
    template_name = "front/pages/connection.html"
    
    def get(self, request):
        return render(request, self.template_name, context={"form": self.form})
    
    def post(self, request):
        form = self.form(request.POST)
                
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                return redirect("front_index")
            
        return render(request, self.template_name, context={"form": self.form})
    
@login_required
def authentication_logout(request):
    logout(request)
    return redirect("authentication_login")
    
    