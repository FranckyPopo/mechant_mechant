
import json
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib import messages


from front import models
from .models import Products, Cart
from mechant import context_processors

def app_product_to_cart(request):
    
    if request.method == "POST":
        
        session_id=request.session._get_or_create_session_key()
        product_id = request.POST.get("product_id")
        if product_id:
            selected_product = Products.objects.get(id = product_id)
            selectedCart, newCard = Cart.objects.get_or_create(product = selected_product,session_id = session_id)
            
            if newCard:
                pass
            else:
                selectedCart.quantity += 1
                selectedCart.save()
                
        messages.add_message(request,messages.SUCCESS,"Produit ajouter avec success")
        return redirect("/")
    else :
        messages.add_message(request,messages.ERROR,"Oups un truc c'est mal passé a l'ajout du product")
        return render("/")
def cart_list(request):
    carts = Cart.objects.filter(session_id = request.session._get_or_create_session_key())
    return render(request, "front/pages/cart_list2.html", context={"carts": carts})

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
        
        messages.add_message(request,messages.SUCCESS,"Bojour le monde")
        return render(request, self.template_name, context=data)

    
class FrontDetailProduct(View):
    template_name = "front/pages/product_detail.html"
    
    def get(self, request):
        return render(request, self.template_name)
    
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
                    "order_add": context_processors.get_total_number_products(request)
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
                    "order_add": context_processors.get_total_number_products(request)
                })
            }
        )
