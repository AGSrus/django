from django.db import models
from django.shortcuts import reverse
from django.conf import settings
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(default='')
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField(blank=True)
    category = models.ManyToManyField('Category', blank=True, related_name='products')

    def get_absolute_url(self):
        return reverse('show_product', kwargs={'id':self.id})

    def __str__(self):
        return f'{self.name}'


class Article(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    text = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    product = models.ManyToManyField('Product', blank=True, related_name='articles')

    def __str__(self):
        return '{}'.format(self.title)


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return '{}'.format(self.name)

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True)
    qty = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __str__(self):
        return '{}'.format(self.product.name)

class Cart(models.Model):
    items = models.ManyToManyField(CartItem, blank=True)
    cart_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __str__(self):
        return '{}'.format(self.id)

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(Cart, blank=True)
    total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
