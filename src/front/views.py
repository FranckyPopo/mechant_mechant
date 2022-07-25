from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt

import json

from front import models, forms
from mechant import context_processors

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
    
class FrontCartList(View):
    template_name = "front/pages/cart_list.html"
    model = models.Cart
    
    def get(self, request):
        if request.user.is_authenticated:
            cart = self.model.objects.get(
                user=request.user
            )
            return render(request, self.template_name, context={"cart": cart})
        else:
            cart_session = self.get_cart_session(request)
            return render(request, self.template_name, context={"cart_session": cart_session})
        
    def get_cart_session(self, request: HttpRequest) -> list:
        """Cette méthode va nous permetre de récupérer le panier
        de l'utilisateur via ça session"""
        
        cart = request.session.get("cart", [])
        cart_session = []
        
        for order in cart:
            instance = {
                "product": models.Products.objects.get(pk=order["pk"]),
                "quantity": order["quantity"]
            }
            cart_session.append(instance)
            
        return cart_session


# Views cart
class FrontProductAddCart(View):
    
    def post(self, request, product_pk):
        if request.user.is_authenticated:
            models.Cart.add_to_cart(request, product_pk)
            return HttpResponse(
                "",
                headers={
                    "HX-Trigger": json.dumps({
                        "product_add_cart": context_processors.get_total_number_products(request)
                    })
                }
            )
        else:
            self.add_to_cart_session(request, str(product_pk))
            return HttpResponse(
                "",
                headers={
                    "HX-Trigger": json.dumps({
                        "product_add_cart": context_processors.get_total_number_products(request)
                    })
                }
            )
        
    def http_method_not_allowed(self, request, *args, **kwargs):
        return redirect("front_index")

    def add_to_cart_session(self, request: HttpRequest, product_pk: str) -> None:
        """Cette méthode va permtre d'ajouter des produits
        dans un panier via la session de l'utilisateur"""
        
        request.session.save()
        quantity = request.POST.get("quantity", False)
        cart = request.session.get("cart", False)
            
        if quantity:
            for order in cart:
                if order["pk"] == product_pk:
                    order["quantity"] = int(quantity)
                    request.session["cart"] = cart
                    break
        elif cart:
            for order in cart:
                if order["pk"] == product_pk:
                    order["quantity"] += 1
                    request.session["cart"] = cart
                    break
            else:
                cart.append({
                    "pk": product_pk,
                    "quantity": 1
                })
                request.session["cart"] = cart
        elif not cart:
            request.session["cart"] = [
                {"pk": product_pk, "quantity": 1}
            ]
    
class FrontProductDeleteCart(View):
    model = models.Cart
    
    def post(self, request, product_pk):
        if request.user.is_authenticated:        
            models.Cart.delete_to_cart(request, product_pk)
            return HttpResponse(
                "",
                headers={
                    "HX-Trigger": json.dumps({
                        "product_delete_cart": context_processors.get_total_number_products(request)
                    })
                }
            )
        else:
            self.delete_to_cart_session(request, str(product_pk))
            return HttpResponse(
                "",
                headers={
                    "HX-Trigger": json.dumps({
                        "product_delete_cart": context_processors.get_total_number_products(request)
                    })
                }
            )
            
    def http_method_not_allowed(self, request, *args, **kwargs):
        return redirect("front_index")

    def delete_to_cart_session(self, request: HttpRequest, product_pk: str) -> None:
        cart = request.session.get("cart", False)
        
        for order in cart:
            if order["pk"] == product_pk:
                cart.remove(order)
                request.session["cart"] = cart
                break
        
# Payments
class FrontPayments(View):
    template_name = "front/pages/payments.html"
    
    def get(self, request):      
        url = reverse("authentication_login")  
        response = HttpResponseRedirect(url)
        response.set_cookie("buy", 1)
        
        context = {
            "cities": models.City.get_cities_active(),
            "districts": models.District.get_districts_active(),
            "list_address": models.DeliveryAddress.objects.filter(user=request.user),
            "form": forms.FormAddress
        }
        
        if request.user.is_authenticated:
            return render(request, self.template_name, context)
        return response
    
    
class FrontAddresseAdd(View):
    
    def post(self, request):
        form = forms.FormAddress(request.POST)
        
        if form.is_valid:
            models.DeliveryAddress.add_address(request)
            return redirect("front_payments")
        return HttpResponse("")
    