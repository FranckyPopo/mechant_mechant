from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

import re

from features.models import NewsLater

class AuhthenticationNewsLaterAdd(View):
    model = NewsLater
    
    def post(self, request):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        email = request.POST.get("email")
        
        if re.fullmatch(regex, email):
            objet, created = self.model.objects.get_or_create(email=email)
            
            if created:
                return HttpResponse("Email ajouter a la newslater")
            return HttpResponse("Cet email existe déjà")
        return HttpResponse("Email incorrect")