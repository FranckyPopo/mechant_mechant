
from django.contrib import admin
from django.urls import path

from front import views
from features import views as vws
import authentication.views as authentication_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.FrontIndex.as_view(), name="front_index"),
    path('contact/', views.FrontContact.as_view(), name="front_contact"),
    
    
    path('products/', views.FrontProducts.as_view(), name="front_products"),
    path('products/product-detail/<int:product_id>/', views.FrontDetailProduct.as_view(), name="front_product_detail"),
    path('products/product-add_cart/<int:productid>/', views.FrontAddCart.as_view(),  name="add_to_card"),
    path('products/categories/single_category/<int:cat_id>/', views.FrontSingleCategory.as_view(), name="single_cat"),

    path('register/', authentication_view.AuthenticationPageRegister.as_view(), name="authentication_register"),
    path('login/', authentication_view.AuthenticationLogin.as_view(), name="authentication_login"),
    
<<<<<<< HEAD
    path('logout/', authentication_view.authentication_logout, name="authentication_logout"),
    
    path('user/accounts/edit-profile', authentication_view.authentication_edit_profile.as_view(), name="authentication_edit_profile"),
=======
    path(
        'user/accounts/edit-profile',
        authentication_view.authentication_edit_profile.as_view(),
        name="authentication_edit_profile"
    ),
    path("send/",
        vws.AuhthenticationNewsLaterAdd.as_view(),
        name="send_mail"),
>>>>>>> 34021d3 (reglage send message ,ajout connect page edit prpfile,)
    
]

# DEBUG = True
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
