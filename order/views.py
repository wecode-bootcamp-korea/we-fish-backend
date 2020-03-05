import json

from .models    import Cart, Order
from user.utils import login_required

from django.views import View
from django.http  import JsonResponse

class CartView(View):
    @login_required
    def post(self, request):
        data = json.loads(request.body)['cart']
        order = Order.objects.create(user_id = request.user.id)
        cart_list = []
        for row in data:
            cart_list.append(Cart(
                product_id = row['product_id'],
                quantity   = row['quantity'],
                order      = order))
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
            'image_url' : product.product.image_url
        } for product in products]

        return JsonResponse({"cart_product":product_data}, status = 200)
