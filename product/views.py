import json

from .models import Category
from .models import Product

from django.views import View
from django.http  import JsonResponse


class CategoryView(View):
    def get(self, request):
        category_data = Category.objects.filter(is_real_category=1).values()

        return JsonResponse({'category_list':list(category_data)}, status = 200)

class ProductListView(View):
    def get(self, request):
        productlist_data = Product.objects.values()

        return JsonResponse({'product_list':list(productlist_data)}, status = 200)

class ProductView(View):
    def get(self, request):
        product_data = Product.objects.values()

        return JsonResponse({'products':list(product_data)}, status = 200)

class SearchView(View):
    def post(self, request):
        data = json.loads(request.body)
        if data['keyword'].exists():
            keyword = data['keyword']

            return JsonResponse({'message':'Let me find it'}, status = 200)

    def get(self, request):
        search_data = Product.objects.filter(name__icontains=keyword).values

        return JsonResponse({'search_results':list(search_data)}, status = 200)
