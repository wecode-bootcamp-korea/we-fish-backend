from user.models  import User
# from order.models import Order

from django.db    import models


class Category(models.Model):
    name             = models.CharField(max_length = 100)
    is_real_category = models.BooleanField(null=True)

    class Meta:
        db_table = 'categories'

class Product(models.Model):
    name        = models.CharField(max_length = 100)
    tagline     = models.CharField(max_length = 200, null=True)
    price       = models.DecimalField(max_digits = 10, decimal_places = 2, null=True)
    category    = models.ManyToManyField(Category, through = 'ProductCategory')
    unit        = models.CharField(max_length = 100, null=True)
    package     = models.CharField(max_length = 100, null=True)
    origin      = models.CharField(max_length = 100, null=True)
    delivery    = models.CharField(max_length = 100, null=True)
    caution     = models.CharField(max_length = 200, null=True)
    description = models.TextField(null=True)
    image_url   = models.URLField(max_length = 2000, null=True)
    created_at  = models.DateTimeField(auto_now_add = True)
    updated_at  = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'products'

class ProductCategory(models.Model):
    product  = models.ForeignKey(Product, on_delete = models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null=True)

    class Meta:
        db_table = 'products_categories'

class SortKeyword(models.Model):
    name = models.CharField(max_length = 200, null=True)

    class Meta:
        db_table = 'sort_keywords'

class Date(models.Model):
    date = models.DateField(auto_now = False)

    class Meta:
        db_table = 'dates'

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete = models.SET_NULL, null=True)
    date    = models.ForeignKey(Date, on_delete = models.SET_NULL, null=True)
    stock   = models.IntegerField(null = True)

    class Meta:
        db_table = 'stocks'

class Section(models.Model):
    name    = models.CharField(max_length = 100)
    tagline = models.CharField(max_length = 200, null=True)

    class Meta:
        db_table = 'sections'

class Theme(models.Model):
    name      = models.CharField(max_length = 100)
    tagline   = models.CharField(max_length = 200)
    section   = models.ForeignKey(Section, on_delete = models.SET_NULL, null=True)
    image_url = models.URLField(max_length = 2000, null=True)
    start_at  = models.DateField(null=True)
    end_at    = models.DateField(null=True)

    class Meta:
        db_table = 'themes'

class ThemeProduct(models.Model):
    theme   = models.ForeignKey(Theme, on_delete = models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete = models.SET_NULL, null=True)

    class Meta:
        db_table = 'theme_products'

class Review(models.Model):
    product    = models.ForeignKey(Product, on_delete = models.SET_NULL, null=True)
    user       = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    # order      = models.ForeignKey('Order', on_delete = models.SET_NULL, null=True)
    rate       = models.IntegerField(null=True)
    content    = models.TextField(null=True)
    image_url  = models.URLField(max_length = 2000, null=True)
    created_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'reviews'
