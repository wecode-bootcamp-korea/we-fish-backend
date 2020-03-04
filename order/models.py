import uuid

from django.db      import models
from user.models    import User
from product.models import Product


class Cart(models.Model):
    product  = models.ForeignKey(Product, on_delete = models.SET_NULL)
    quantity = models.IntegerField(null=True)
    order    = models.ForeignKey('Order', on_delete = models.SET_NULL)

class Order(models.Model):
    order_number = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user         = models.ForeignKey(User, on_delete = models.SET_NULL)
    total_price  = models.DecimalField(max_digits = 10, decimal_places = 2, null=True)
    ordered_at   = models.DateTiemfield(auto_now_add = True)
    status       = models.ForeignKey('Status', on_delete = models.SET_NULL, null=True)

class Status(models.Model):
    name = models.CharField(max_length = 100)
