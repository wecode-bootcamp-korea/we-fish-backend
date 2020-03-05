import json

from .models    import Cart, Order
from user.utils import login_required

from django.views import View
from django.http  import JsonResponse, HttpResponse

from django.db import IntegrityError, transaction
from django.db.models import Sum

class CartView(View):
    @login_required
    def post(self, request):
        data = json.loads(request.body)['cart']
        order = Order.objects.create(user_id = request.user.id)
        cart_list =[
            Cart(
                product_id = cart['product_id'],
                quantity   = cart['quantity'],
                order      = order) for cart in data]
        Cart.objects.bulk_create(cart_list)

        return JsonResponse({"order_number":order.order_number}, status = 200)

class CartDetailView(View):
    @login_required
    def get(self, request, order_number):
        products = Cart.objects.select_related('order', 'product').filter(order__order_number=order_number)
        product_data = [{
            'id' :product.product.id,
            'name' : product.product.name,
            'price' : product.product.price,
            'image_url' : product.product.image_url,
            'quantity' : product.quantity
        } for product in products]
        quantity_total = products.aggregate(Sum('quantity'))

        return JsonResponse({
            "cart_product" : product_data,
            "quantity_total" : quantity_total['quantity__sum']},
            status = 200)

    @login_required
    def post(self, request, order_number):
        order = Order.objects.get(order_number=order_number)
        data = json.loads(request.body)['cart']
        cart = Cart.objects.select_related('order').filter(order__order_number=order_number)
        try:
            with transaction.atomic():
                cart.delete()
                cart_list =[
                    Cart(
                        product_id = cart['product_id'],
                        quantity   = cart['quantity'],
                        order      = order) for cart in data]
                Cart.objects.bulk_create(cart_list)

            return HttpResponse(status = 200)

        except IntegrityError:
            return JsonResponse({"message":"Try again"}, status = 400)
