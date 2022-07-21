from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View

import json

from front import models
from mechant import context_processors

    
class FrontCartList(View):
    template_name = "front/pages/cart_list.html"
    model = models.Cart
    
    def get(self, request):
        if request.user.is_authenticated:
            cart = self.model.objects.get(
                user=request.user
            )
            return render(request, self.template_name, context={"cart": cart})
        return render(request, self.template_name, context={"cart": cart})
    
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
        user = request.user
        product = models.Products.objects.get(pk=product_pk)
        cart, _ = models.Cart.objects.get_or_create(user=user)
        order, create = models.Order.objects.get_or_create(
            user=user,
            product=product
        )
        
        if create:
            cart.order.add(order)
            cart.save()
        else:
            order.quantity += 1
            order.save()
              
        return HttpResponse(
            "",
            headers={
                "HX-Trigger": json.dumps({
                    "product_add_cart": context_processors.get_total_number_products(request)
                })
            }
        )
    
class FrontProductDeleteCart(View):
    model = models.Cart
    
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

# Payments
class FrontPayments(View):
    template_name = "front/pages/payments.html"
    
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        request.COOKIES["order"] = "true"
        return redirect("authentication_login")