
from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.http import HttpRequest
from django.db.models.query import QuerySet
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
        return self.original_price

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f"{self.product} ({self.quantity})"
    
class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order = models.ManyToManyField(Order)
    
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.user.username
    
    @classmethod
    def add_to_cart(cls, request: HttpRequest, product_pk: int) -> None:
        """Cette méthode va permetre d'ajouter des produits dans
        le panier de 'utilisate quand il est connecté"""
        
        user = request.user
        quantity = request.POST.get("quantity", False)
        product = Products.objects.get(pk=product_pk)
        cart, _ = cls.objects.get_or_create(user=user)
        order, create = Order.objects.get_or_create(
            user=user,
            product=product
        )
        
        if quantity:
            order.quantity = quantity
            order.save()
        elif create:
            cart.order.add(order)
            cart.save()
        else:
            order.quantity += 1
            order.save()
            
    @classmethod
    def delete_to_cart(cls, request: HttpRequest, product_pk: int) -> None:
        """Cette méthode va permetre de supprimer un produit dans
        le panier de l'utilisateur quand il est connecté"""
        
        user = request.user
        product = cls.objects.get(user=user).order.get(product__pk=product_pk)
        product.delete()
            
    @classmethod
    def add_cart_session_bd(cls, request: HttpRequest) -> None:
        """Cette méthode va permetre d'ajouter le pannier qui se
        trouve dans la session de l'utilisateur dans le model Cart"""
        
        cart_session = request.session.get("cart")
        user = request.user
        cart, _ = cls.objects.get_or_create(user=user)
        
        for item in cart_session:
            product = Products.objects.get(pk=item["pk"])
            order, create = Order.objects.get_or_create(
                user=user,
                product=product
            )
            
            if create:
                order.quantity = item["quantity"]
                order.save()
                cart.order.add(order)
                cart.save()
            else:
                order.quantity += item["quantity"]
                order.save()
     
    @classmethod
    def get_price_total_cart(cls, user) -> int:
        cart = cls.objects.get(user=user)
        list_price = [order.product.get_final_product_price() * order.quantity for order in cart.order.all()]
        
        return sum(list_price)
        
class City(models.Model):
    name = models.CharField(max_length=150)
    active = models.BooleanField(default=True)
    
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.name
    
    @classmethod
    def get_cities_active(cls):
        return cls.objects.filter(active=True)
        
class District(models.Model):
    name = models.CharField(max_length=150)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.name
    
    @classmethod
    def get_districts_active(cls):
        return cls.objects.filter(active=True)
    
class DeliveryAddress(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="delivery_address_user"
        )
    phone = PhoneNumberField(region="CI")
    addresse = models.CharField(max_length=150)
    additional_information = models.CharField(max_length=1000)
    district = models.ForeignKey(
        District,
        on_delete=models.CASCADE,
        related_name="delivery_address_district"
    )

    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.username
    
    @classmethod
    def add_address(cls, request: HttpRequest) -> None:
        """Cette méthode va permetre de d'enregistrer des
        addresses"""
        
        user = request.user
        phone = request.POST.get("phone", False)
        addresse = request.POST.get("addresse", False)
        additional_information = request.POST.get("additional_information", False)
        district_pk = request.POST.get("district", False)
        district = District.objects.get(pk=district_pk)
        
        address = cls.objects.create(
            user=user,
            phone=phone,
            addresse=addresse,
            district=district,
            additional_information=additional_information,
        )
        
        user.delivery_address.add(address)
        user.save()

class DeliveryMethod(models.Model):
    name = models.CharField(max_length=150)
    info =  models.CharField(max_length=1000)
    active = models.BooleanField(default=True)

    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.name
    
    @classmethod
    def get_delivery_method_active(cls):
        return cls.objects.filter(active=True)
    
class Payment(models.Model):
    name = models.CharField(max_length=150)
    active = models.BooleanField(default=True)

    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.name
    
    @classmethod
    def get_payments_active(cls: QuerySet) -> QuerySet:
        return cls.objects.filter(active=True)

class Livraison(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    delivery_address = models.ForeignKey(DeliveryAddress, on_delete=models.CASCADE)
    livraison = models.BooleanField(default=False)
    delivery_method = models.ForeignKey(DeliveryMethod, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.user.username
    
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
        settings.AUTH_USER_MODEL, 
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
    product = models.ForeignKey(
        Products, 
        on_delete=models.CASCADE, 
        related_name="image_product_product"
    )
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
    product = models.ForeignKey(
        Products, 
        on_delete=models.CASCADE,
        related_name="best_sellers_product"
    )
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
    