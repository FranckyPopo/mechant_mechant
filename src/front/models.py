
from itertools import product
from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField

class Categories(models.Model):
    name = models.fields.CharField(max_length=150)
    active = models.BooleanField(default=True)
    
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=150)
    photo = models.ImageField()
    description = models.TextField()
    original_price = models.PositiveIntegerField()
    promotion_price = models.PositiveIntegerField()
    additional_information = models.TextField()
    promotion = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    categories = models.ManyToManyField(Categories, related_name="product_categories")
    
    # Ajouter des champs color, size, dimension, longeur largeur
    
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="user_comment")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comment_product")
    message = models.TextField()
    
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.user.username
    
class ImageProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    photo = models.ImageField()
    
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
    def __str__(self) -> str:
        return str(self.product.name)

class Promotion(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="promotion_product")
    active = models.BooleanField(default=False)
    
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title    
    
class DealOfTheWeenk(models.Model):
    start_of_deal = models.DateTimeField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="DealOfTheWeenk_product")
    
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)

class BestSellers(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
class SiteContact(models.Model):
    phone_number = PhoneNumberField()
    email = models.EmailField()
    link_facebook = models.URLField()
    link_twitter = models.URLField()
    link_instagram = models.URLField()
    link_skype = models.URLField()
    link_pinterest = models.URLField()
    link_google_more = models.URLField()
    
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
    
    