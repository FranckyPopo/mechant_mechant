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
    

class FrontSingleCategory(View):
    template_name = "front/pages/categories.html"
    
    def get(self, request, cat_id):
        single_cat = models.Categories.objects.get(id=cat_id)
        return render(request, self.template_name, locals())


def add_to_card(requrest):
    pass