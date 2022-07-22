from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

import json

from authentication import forms, models
from front.models import Cart

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
                
                # Si l'utilisateur a un panier dans ça session on l'ajout a la bd 
                if request.session.get("cart", False):
                    Cart.add_cart_session_bd(request)
                return redirect("front_index")
            
        return render(request, self.template_name, context={"form": self.form})

class authentication_edit_profile(LoginRequiredMixin, View):
    template_name = "front/pages/settings_account.html"
    model_form = forms.FormEditProfile
    
    def get(self, request):
        user = models.User.objects.get(username=request.user)
        form = self.model_form(instance=user)
        return render(request, self.template_name, context={"form": form})
    
    def post(self, request):
        user = models.User.objects.get(username=request.user)
        form = self.model_form(request.POST, instance=user)
        
        if form.is_valid():
            form.save()
            return redirect("authentication_edit_profile")
        return render(request, self.template_name, context={"form": form})
    
    
@login_required
def authentication_logout(request):
    logout(request)
    return redirect("authentication_login")

    