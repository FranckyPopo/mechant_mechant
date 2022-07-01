"""mechant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from front import views
import authentication.views as authentication_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.FrontIndex.as_view(), name="front_index"),
    path('contact/', views.FrontContact.as_view(), name="front_contact"),
    
    path('products/', views.FrontProducts.as_view(), name="front_products"),
    path('products/product-detail/<int:product_id>/', views.FrontDetailProduct.as_view(), name="front_product_detail"),

    path('register/', authentication_view.AuthenticationPageRegister.as_view(), name="authentication_register"),
    path('login/', authentication_view.AuthenticationLogin.as_view(), name="authentication_login"),
    path('logout/', authentication_view.authentication_logout, name="authentication_logout"),
    
    path('user/accounts/edit-profile', authentication_view.authentication_edit_profile.as_view(), name="authentication_edit_profile"),
    
]
