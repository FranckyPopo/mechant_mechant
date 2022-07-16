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
    
@admin.register(models.ProductColor)
class ProductColor(admin.ModelAdmin):
    list_display = ["product", "color"]

    
@admin.register(models.Cart)
class CartProduct(admin.ModelAdmin):
    list_display = ["order", "is_order"]

@admin.register(models.Order)
class OrderProduct(admin.ModelAdmin):
    list_display = ["Product", "Quantity","is_ordered"]
    