import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from front import models
from mechant import context_processors

    
class FrontCartList(View):
    template_name = "front/pages/cart_list.html"
    model = models.OrderItem
    
    def get(self, request):
        orders = self.model.objects.filter(
            session_id=request.session._get_or_create_session_key()
        )
        return render(request, self.template_name, context={"orders": orders})
    
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

# Views cart
class FrontProductAddCart(View):
    
    def post(self, request, product_pk):
        session_id = request.session._get_or_create_session_key()
        product = models.Products.objects.get(pk=product_pk)
        
        objet, create = models.OrderItem.objects.get_or_create(session_id=session_id, product=product)
        quantity = request.POST.get("quantity")
        
        if quantity:
            objet.quantity = quantity
            objet.save()
        else:
            objet.quantity += 1
            objet.save()
        
        return HttpResponse(
            "",
            headers={
                "HX-Trigger": json.dumps({
                    "product_add_cart": context_processors.get_total_number_products(request)
                })
            }
        )
    
class FrontProductDeleteCart(View):
    model = models.OrderItem
    
    def post(self, request, product_pk):
        self.model.objects.get(pk=product_pk).delete()
        
        return HttpResponse(
            "",
            headers={
                "HX-Trigger": json.dumps({
                    "product_delete_cart": context_processors.get_total_number_products(request)
                })
            }
        )
