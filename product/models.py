from django.db import models
from order.models import Order
from user.models import User

class Category(models.Model):
    name       = models.CharField(max_length = 100)

    class Meta:
        db_table = 'categories'

class Product(models.Model):
    name        = models.CharField(max_length = 100)
    tagline     = models.CharField(max_length = 200, null=True)
    price       = models.DecimalField(max_digits = 10, decimal_places = 2, null=True)
    category    = models.ForeignKey(Category, on_delete = models.SET_NULL, null=True)
    unit        = models.CharField(max_length = 100, null=True)
    package     = models.CharField(max_length = 100, null=True)
    origin      = models.CharField(max_length = 100, null=True)
    delivery    = models.CharField(max_length = 100, null=True)
    caution     = models.CharField(max_length = 200, null=True)
    description = models.TextField(null=True)
    imgage      = models.URLField(null=True)
    created_at  = models.DateTimeField(auto_now_add = True)
    updated_at  = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'products'

class Date(models.Model):
    date    = models.DateField(auto_now = False)
    day     = models.CharField(max_length = 50)
    expired = models.BooleanField(null=True)

    class Meta:
        db_table = 'dates'

class ProductStock(models.Model):
    product = models.ForeignKey(Product, on_delete = models.SET_NULL, null=True)
    date    = models.ForeignKey(Date, on_delete = models.SET_NULL, null=True)
    stock   = models.IntegerField(null = True)

    class Meta:
        db_table = 'productstocks'

class Theme(models.Model):
    name    = models.CharField(max_length = 100)
    tagline = models.CharField(max_length = 200)
    image   = models.URLField(null=True)

    class Meta:
        db_table = 'themes'

class ThemeProduct(models.Model):
    theme   = models.ForeignKey(Theme, on_delete = models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete = models.SET_NULL, null=True)

    class Meta:
        db_table = 'themeproducts'

class Review(models.Model):
    product    = models.ForeignKey('Product', on_delete = models.SET_NULL, null=True)
    user       = models.ForeignKey('User', on_delete = models.SET_NULL, null=True)
    order      = models.ForeignKey('Order', on_delete = models.SET_NULL, null=True)
    rate       = models.IntegerField(null=True)
    content    = models.TextField(null=True)
    image      = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'reviews'

