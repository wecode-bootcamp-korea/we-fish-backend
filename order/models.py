from django.db      import models
from user.models    import User
from product.models import Product





class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete = models.SET_NULL)
    quantity = models.IntegerField
    order = models.ForeignKey('Order', on_delete = models.SET_NULL)

class Order(models.Model):
    order_number = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete = models.SET_NULL)
    total_quantity = property(__total_quantity)
    total_price = property(__total_price)
    payment =
    ordered_at =



    def __total_quantity(self):
        from django.db.models import Sum
    #    obj = Cart.objects.filter(total_quantity=self).values('total_quantity').annotate(sum_quantity=Sum('quantity'))

        Cart.objects.filter(total_quantity=self).values('total_quantity').annotate(sum_quantity=Sum('quantity'))

    def __total_price(self):
        from django.db.models. import Sum
        obj =
