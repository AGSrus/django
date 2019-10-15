"""diploma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from app.views import index, cart, show_mobiles, login, empty, show_product, add_product_in_cart, order_create, sing_up, logout_user


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('cart/', cart, name='cart'),
    path('mobiles/', show_mobiles, name='mobiles'),
    path('login/', login, name='login'),
    path('logout/', logout_user, name='logout_user'),
    path('empty/', empty, name='empty'),
    path('product/<str:id>/', show_product, name='show_product'),
    path('add/<str:product_id>/', add_product_in_cart, name='add_product_in_cart'),
    path('order/', order_create, name='order'),
    path('singup', sing_up, name='sing_up')

]
