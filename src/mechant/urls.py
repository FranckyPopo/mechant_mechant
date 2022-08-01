from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from front import views
import authentication.views as authentication_view
import features.views as features_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.FrontIndex.as_view(), name="front_index"),
    path('contact/', views.FrontContact.as_view(), name="front_contact"),
    
    path('products/', views.FrontProducts.as_view(), name="front_products"),
    path(
        'products/<slug:slug_product>/',
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
    path(
        'newslater-add/',
        features_view.AuhthenticationNewsLaterAdd.as_view(),
        name="auhthentication_newsLater_add"
    ),

    # Payements
    path("payments/", views.FrontPayments.as_view(), name="front_payments"),
    path("addresse-add/", views.FrontAddresseAdd.as_view(), name="front_addresse_add"),

    
    # Authentication
    path('register/', authentication_view.AuthenticationPageRegister.as_view(), name="authentication_register"),
    path('login/', authentication_view.AuthenticationLogin.as_view(), name="authentication_login"),
    path('logout/', authentication_view.authentication_logout, name="authentication_logout"),
    
    # Settings user
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
