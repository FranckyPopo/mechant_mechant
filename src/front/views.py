from urllib.request import Request
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from front import models
    
class FrontProducts(View):
    template_name = "front/pages/categories.html"
    
    def get(self, request):
        return render(request, self.template_name)

class FrontContact(View):
    template_name = "front/pages/contact.html"
    
    def get(self, request):
        return render(request, self.template_name)
    
class FrontIndex(View):
    template_name = "front/pages/index.html"
    
    def get(self, request):
        data = {
            "categories": models.Categories.objects.all().filter(active=True),
            "products": models.Products.objects.all().filter(active=True),
        }
        return render(request, self.template_name, context=data)
    
class FrontDetailProduct(View):
    template_name = "front/pages/product_detail.html"
    
    def get(self, request):
        return render(request, self.template_name)
    
class FrontProductAddCart(View):
    template_name = None
    
    def post(self, request, product_pk):
        session_id = request.session._get_or_create_session_key()
        product = models.Products.objects.get(pk=product_pk)
        objet, create = models.OrderItem.objects.get_or_create(session_id=session_id, product=product)
        
        if not create:
            objet.quantity += 1
            objet.save()
        
        return HttpResponse("")
        
