import uuid

from user.models    import User

from django.db      import models

class Cart(models.Model):
    product  = models.ForeignKey('product.Product', on_delete = models.SET_NULL, null=True)
    quantity = models.IntegerField(null=True)
    order    = models.ForeignKey('Order', on_delete = models.SET_NULL, null=True)

    class Meta:
        db_table = 'carts'

class Order(models.Model):
    order_number     = models.UUIDField(default=uuid.uuid4, editable=False)
    user             = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    product_info     = models.CharField(max_length = 100, null=True)
    total_price      = models.DecimalField(max_digits = 10, decimal_places = 2, null=True)
    delivery_invoice = models.CharField(max_length = 20, null=True)
    delivery_date    = models.ForeignKey('product.Date', on_delete = models.SET_NULL, null=True)
    ordered_at       = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table = 'orders'
