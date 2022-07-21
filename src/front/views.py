from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.serializers import serialize
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
        else:
            pk_product_cart = request.session["cart"].keys()
            cart = [models.Products.objects.get(pk=pk) for pk in pk_product_cart]
            
            return render(request, self.template_name, context={"cart_session": cart})
    
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
            request.session.save()
            cart = request.session.get("cart", False)
            product = models.Products.objects.filter(pk=product_pk)   
            
            if cart:
                for order in cart:
                    if order["product"] == product:
                        
                        order["quantity"] += 1
                        request.session["cart"] = cart
                        break
                else:
                    print(type(order["product"]))
                    cart.append({
                        "product": serialize("json", product),
                        "quantity": 1,
                    })
                    request.session["cart"] = cart
            else:
                request.session["cart"] = [
                    {
                        "product": serialize("json", product),
                        "quantity": 1,
                    }
                ]
                
            print(request.session["cart"])

            return HttpResponse(
                "",
                headers={
                    "HX-Trigger": json.dumps({
                        "product_add_cart": context_processors.get_total_number_products_user_anonyme(request)
                    })
                }
            )
    
class FrontProductDeleteCart(View):
    model = models.Cart
    
    def post(self, request, product_pk):
        
        models.Cart.delete_to_cart(request, product_pk)

        
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