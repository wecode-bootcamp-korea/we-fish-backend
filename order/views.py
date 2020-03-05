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
        for row in data:
            Cart.objects.create(
                product_id = row['product_id'],
                quantity   = row['quantity'],
                order_id   = order.id)

        return JsonResponse({"order_number":order.order_number}, status = 200)
