from django.contrib import admin

from front import models

@admin.register(models.Categories)
class Categories(admin.ModelAdmin):
    list_display = ["name", "active", "created"]
    
@admin.register(models.Comment)
class Comment(admin.ModelAdmin):
    list_display = ["user", "message", "created"]
    
@admin.register(models.Product)
class Product(admin.ModelAdmin):
    list_display = ["name", "active", "original_price", "created"]
    
@admin.register(models.ImageProduct)
class ImageProduct(admin.ModelAdmin):
    list_display = ["product", "photo", "created"]
    
@admin.register(models.Promotion)
class Promotion(admin.ModelAdmin):
    list_display = ["product", "active", "created"]
    
@admin.register(models.DealOfTheWeenk)
class DealOfTheWeenk(admin.ModelAdmin):
    list_display = ["start_of_deal","product", "created"]
    
@admin.register(models.BestSellers)
class BestSellers(admin.ModelAdmin):
    list_display = ["product", "active", "created"]
    
@admin.register(models.SiteContact)
class SiteContact(admin.ModelAdmin):
    list_display = ["phone_number", "email", "created"]
    