
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from colorfield.fields import ColorField


class Categories(models.Model):
    name = models.fields.CharField(max_length=150)
    image = models.ImageField()
    description = models.CharField(max_length=150)
    active = models.BooleanField(default=True)
    
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=150)
    
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    

class Products(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    photo = models.ImageField()
    
    original_price = models.PositiveIntegerField()
    promotion_reduction = models.PositiveIntegerField(
        validators=[MinValueValidator(0)],
        blank=True,
        null=True
    )
    promotion_percentage = models.PositiveIntegerField(
        validators=[MaxValueValidator(100), 
        MinValueValidator(1)], 
        blank=True,
        null=True
    )
    additional_information = models.TextField()
    categories = models.ManyToManyField(Categories, related_name="product_categories")
    size = models.ManyToManyField(Size, related_name="product_size")
    longeur = models.CharField(max_length=50, blank=True)
    largeur = models.CharField(max_length=50, blank=True)
    stock = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    
    is_promotion = models.BooleanField(default=False)
    is_sold = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.name
    
    def is_new(self) -> bool:
        result = timezone.now() - self.created
        return result.days <= 7
    
    def get_product_reduction(self) -> int:
        if self.promotion_percentage:
            return self.original_price * self.promotion_percentage // 100
        return self.promotion_reduction
            
    def get_final_product_price(self) -> int:
        """
        _summary_

        _extended_summary_

        Returns:
            int: _description_
        """
        if self.is_promotion:
            if self.promotion_percentage:
                reduction = self.original_price * self.promotion_percentage // 100
                return self.original_price - reduction
            elif self.promotion_reduction:
                return self.original_price - self.promotion_reduction

    
class OrderItem(models.Model):
    session_id = models.CharField(max_length=150)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1)])
    
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
    def __str__(self) -> str:
        return str(self.product)
    
class Cart(models.Model):
    session = None
    product = None
    
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)

class ProductColor(models.Model):
    name = models.CharField(max_length=50, blank=True)
    code_hex = ColorField(default="#FF0000")
    product = models.ForeignKey(
        Products, 
        related_name="protruct_color", 
        on_delete=models.CASCADE
    )
    
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.name

class Comments(models.Model):
    user = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE, 
        related_name="user_comment"
    )
    product = models.ForeignKey(
        Products, 
        on_delete=models.CASCADE, 
        related_name="comment_product"
    )
    message = models.TextField()
    
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.user.username
    
class ImageProduct(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="image_product_product")
    photo = models.ImageField()
    
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.product.name

class Promotion(models.Model):
    product = models.ForeignKey(
        Products, 
        on_delete=models.CASCADE, 
        related_name="promotion_product"
    )
    active = models.BooleanField(default=True)
    
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.product.name    
    
class DealOfTheWeenk(models.Model):
    start_of_deal = models.DateTimeField()
    product = models.ForeignKey(
        Products, 
        on_delete=models.CASCADE, 
        related_name="DealOfTheWeenk_product"
    )
    
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.product.name

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
    