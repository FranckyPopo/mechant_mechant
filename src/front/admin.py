from django.contrib import admin

from front import models

@admin.register(models.Categories)
class Categories(admin.ModelAdmin):
    list_display = ["name", "active", "created"]
    
@admin.register(models.Comments)
class Comment(admin.ModelAdmin):
    list_display = ["user", "message", "created"]
    
@admin.register(models.Products)
class Product(admin.ModelAdmin):
    list_display = ["name", "active", "original_price", "created"]
    
@admin.register(models.ImageProduct)
class ImageProduct(admin.ModelAdmin):
    list_display = ["product", "photo", "created"]
    
@admin.register(models.Promotion)
class Promotion(admin.ModelAdmin):
    list_display = ["product", "title", "mini_title","active", "created"]
    
@admin.register(models.DealOfTheWeenk)
class DealOfTheWeenk(admin.ModelAdmin):
    list_display = ["start_of_deal", "active", "product", "created"]
    
@admin.register(models.BestSellers)
class BestSellers(admin.ModelAdmin):
    list_display = ["product", "active", "created"]
    
@admin.register(models.SiteContact) 
class SiteContact(admin.ModelAdmin):
    list_display = ["phone_number", "email", "created"]
    
@admin.register(models.Cart)
class Cart(admin.ModelAdmin):
    list_display = ["user", "ordered", "created"]
    
@admin.register(models.Order)
class Order(admin.ModelAdmin):
    list_display = ["user", "ordered", "product", "quantity", "created"]
    
@admin.register(models.District)
class District(admin.ModelAdmin):
    list_display = ["name", "active", "created", "updated"]
    
@admin.register(models.City)
class City(admin.ModelAdmin):
    list_display = ["name", "active", "created", "updated"]
    
@admin.register(models.DeliveryAddress)
class DeliveryAddress(admin.ModelAdmin):
    list_display = ["addresse", "created", "updated"]
    
@admin.register(models.DeliveryInvoice)
class DeliveryInvoice(admin.ModelAdmin):
    list_display = ["confimation", "created", "updated"]
    
@admin.register(models.Payment)
class Payment(admin.ModelAdmin):
    list_display = ["name", "active", "created", "updated"]
    
@admin.register(models.DeliveryMethod)
class DeliveryMethod(admin.ModelAdmin):
    list_display = ["name", "info", "created", "active", "updated"]
    