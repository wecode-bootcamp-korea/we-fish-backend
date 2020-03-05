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
