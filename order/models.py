import uuid

from user.models    import User
from product.models import Product

from django.db      import models

class Cart(models.Model):
    product  = models.ForeignKey(Product, on_delete = models.SET_NULL, null=True)
    quantity = models.IntegerField(null=True)
    order    = models.ForeignKey('Order', on_delete = models.SET_NULL, null=True)

    class Meta:
        db_table = 'carts'

class Order(models.Model):
    order_number     = models.UUIDField(default=uuid.uuid4, editable=False)
    user             = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    total_price      = models.DecimalField(max_digits = 10, decimal_places = 2, null=True)
    delivery_invoice = models.CharField(max_length = 20, null=True)
    ordered_at       = models.DateTimeField(auto_now_add = True)
    status           = models.ForeignKey('Status', on_delete = models.SET_NULL, null=True)

    class Meta:
        db_table = 'orders'

class Status(models.Model):
    name = models.CharField(max_length = 100)

    class Meta:
        db_table = 'status'
