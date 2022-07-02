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
        products = models.Products.objects.all().filter(active=True)
        
        data = {
            "categories": categories,
            "products": products,
        }
        return render(request, self.template_name, context=data)
    
    def post(self):
        pass
    
    
    
    
class FrontDetailProduct(View):
    template_name = "front/pages/product_detail.html"
    
    def get(self, request):
        return render(request, self.template_name)
    

