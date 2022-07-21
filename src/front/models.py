


import email
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from colorfield.fields import ColorField
import datetime
from front import views
class Categories(models.Model):
    name = models.fields.CharField(max_length=150)
    active = models.BooleanField(default=True)
    cat_image = models.ImageField(upload_to="product_cats")
    cat_description = models.TextField()
    
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Products(models.Model):
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
    
    
    name = models.CharField(max_length=150)
    main_image = models.ImageField()
    description = models.TextField()
    
    original_price = models.PositiveIntegerField()
    is_promotion = models.BooleanField(default=False)
    promotion_reduction = models.PositiveIntegerField(default=0)
    promotion_percentage = models.PositiveIntegerField(validators=[MaxValueValidator(100)],default=0)
    additional_information = models.TextField()
    is_solde = models.BooleanField(default=False)
    stock = models.PositiveIntegerField()
    
    active = models.BooleanField(default=True)
    categories = models.ManyToManyField(Categories, related_name="product_categories")

    size = models.CharField(max_length=50, blank=True)
    longeur = models.CharField(max_length=50, blank=True)
    largeur = models.CharField(max_length=50, blank=True)
    
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)

    
    
    
    def is_new(self):
        now = datetime.datetime.now()
        dif_date = now - self.created 
        
        return dif_date.days < 2
    
    def get_product_reduction(self):
        
        if self.promotion_percentage :
            
            return self.original_price * self.promotion_percentage // 100
        
        return self.promotion_reduction
        
    
    def get_final_product_price(self):
        if self.is_promotion:
            if self.promotion_percentage :
                reduction = self.original_price * self.promotion_percentage // 100
                return self.original_price - reduction
            
            elif self.promotion_reduction:
                return self.original_price - self.promotion_reduction
            else:
                return self.original_price
        else:
            return self.original_price
        
    
    def __str__(self):
        return self.name
        
    # applique une vue  du produit depuisla admin
    def get_absolute_url(self):
        pass
        #return reverse() 
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="order_user")
    Product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="Card_products")
    Quantity = models.PositiveIntegerField(default=1)
    is_ordered = models.BooleanField(default=False)

    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
    def __str__(self):
        return self.Product.name

class Cart(models.Model):
    #Session_id = 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart_order")
    order= models.ForeignKey(Order, on_delete=models.CASCADE, related_name="oder_cart")
    is_order = models.BooleanField(default=False)

    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
    def __str__(self):
        return self.customer.username



   

class ProductColor(models.Model):
    product = models.ForeignKey(Products,related_name="protruct_color",on_delete=models.CASCADE)
    color = models.CharField(max_length=50, blank=True)
    color_code = ColorField(default = "#FF0000")
    
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
    def __str__(self):
        return self.color_code
    
class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comment")
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="comment_product")
    message = models.TextField()
    
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username
    
class ImageProduct(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="image_product_product")
    photo = models.ImageField(upload_to="img_product")
    photo_desc_1 = models.ImageField(upload_to="img_product_desc1", blank=True)
    photo_desc_2 = models.ImageField(upload_to="img_product_desc2", blank=True)
    photo_desc_3 = models.ImageField(upload_to="img_product_desc2", blank=True)

    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
    def __str__(self):
        return str(self.product.name)

class Promotion(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="promotion_product")
    active = models.BooleanField(default=True)
    
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
    def __str__(self):
        return self.title    
    
class DealOfTheWeenk(models.Model):
    start_of_deal = models.DateTimeField()
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="DealOfTheWeenk_product")
    
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
    def __str__(self):
        return self.product

class BestSellers(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    
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

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    web_site = models.CharField(max_length=20)
    message = models.TextField()
    is_active = models.BooleanField(default=True)

    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
