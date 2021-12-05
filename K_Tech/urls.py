"""K_Tech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URConf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from K_Tech import settings
from django.conf.urls.static import static

from Mainpage.views import mainindex, Add_cart, checkout, productView, Login, Logout, Signup, add_product, min_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainindex, name='Home_page'),
    path('Cart/', Add_cart, name="ADD to Cart"),
    path('add/<int:id>', add_product),
    path('min/<int:id>', min_product),

    path('checkout/', checkout, name="checkout page"),

    path('register/', Signup),
    path('Login/', Login, name='login'),
    path('Logout/', Logout, name='Logout'),

    path('productview/<int:id>', productView, name='Product_detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
