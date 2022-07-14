from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from front import views
import authentication.views as authentication_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.FrontIndex.as_view(), name="front_index"),
    path('contact/', views.FrontContact.as_view(), name="front_contact"),
    
    path('products/', views.FrontProducts.as_view(), name="front_products"),
    path(
        'products/product-detail/<int:product_id>/',
        views.FrontDetailProduct.as_view(), 
        name="front_product_detail"
    ),
    
    # Path cart 
    path(
        'product-add-cart/<int:product_pk>/',
        views.FrontProductAddCart.as_view(),
        name="front_product_add_cart"
    ),
    path(
        'product-delete-cart/<int:product_pk>/',
        views.FrontProductDeleteCart.as_view(),
        name="front_product_delete_cart"
    ),
    path('cart-list/', views.FrontCartList.as_view(), name="front_cart_list"),
    

    path('register/', authentication_view.AuthenticationPageRegister.as_view(), name="authentication_register"),
    path('login/', authentication_view.AuthenticationLogin.as_view(), name="authentication_login"),
    path('logout/', authentication_view.authentication_logout, name="authentication_logout"),
    
    path(
        'user/accounts/edit-profile',
        authentication_view.authentication_edit_profile.as_view(),
        name="authentication_edit_profile"
    ),
    

    
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT
    )
