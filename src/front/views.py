from http.client import HTTPResponse
from urllib import request
from venv import create
from django.shortcuts import render,redirect
from django.views.generic import View
from front import models
from django.shortcuts import get_object_or_404
from django.urls import reverse

    
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
        categories = models.Categories.objects.all().filter(active=True)
        single_cat =  models.Categories.objects.all()
        products = models.Products.objects.all().filter(active=True)
        
        data = {
    
            "categories": categories,
            "products": products,
        }
        return render(request, self.template_name, context=data)
    
    def post(self, request, product_id):
        
        pass
    
    
    
    
class FrontDetailProduct(View):
    template_name = "front/pages/product_detail.html"
    
    def get(self, request, product_id):
        product_id = models.Products.objects.get(id=product_id) 
        img_product = models.ImageProduct.objects.all()
        return render(request, self.template_name, locals())
    
    #panier 
class FrontAddCart(View):
    def post(self, request, productid):
        
        # user = request.user
        # produit = get_object_or_404(models.Products, id=product_id)
        # # silepanier n'existe on le cree avec 'cart'
        # cart,  _ = models.Cart.objects.get_or_create(user=user)
        # #si un objet order dans db existe on associe à user qui correspond au produit sinon on cree
        # orders, created = models.Order.objects.get_or_create(user=user, product=produit)

        # # si le prrodui
        # if created:
        #     cart.order.add(orders)
        #     cart.save()
        # else:
        #     orders.quantity += 1
        #     orders.save()
        return redirect("front_products")   #reverse("front_product_detail", kwargs={"product_id":product_id })


class FrontSingleCategory(View):
    template_name = "front/pages/categories.html"
    
    def get(self, request, cat_id):
        single_cat = models.Categories.objects.get(id=cat_id)
        return render(request, self.template_name, locals())


