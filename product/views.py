import json

from .models import Category
from .models import Product

from django.views import View
from django.http  import JsonResponse


class CategoryView(View):
    def get(self, request):
        category_data = Category.objects.filter(is_real_category=True).values()

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
    def __init__(self):
        self.keyword = ''

    def post(self, request):
        data = json.loads(request.body)
        self.keyword = data['keyword']
        search_data = Product.objects.filter(name__icontains=self.keyword)
        if not search_data:

            return JsonResponse(
                {
                    'message':'검색 결과가 없습니다. 다른 키워드로 검색해 주세요'
                 },
                status = 200)

        return JsonResponse({'message':'상품을 검색중입니다.'}, status = 200)

    def get(self, request):
        search_data = Product.objects.filter(name__icontains=self.keyword).values

        return JsonResponse({'search_results':list(search_data)}, status = 200)
