import json

from .models import Category
from .models import Product
from .models import ProductCategory
from .models import SortKeyword
from .models import Theme

from django.views import View
from django.http  import HttpResponse, JsonResponse


class CategoryView(View):
    def get(self, request):
        category_data = Category.objects.filter(is_real_category=True).values()

        return JsonResponse({'category_list':list(category_data)}, status = 200)

class ThemeView(View):
    def get(self, request):
        theme_data = Theme.objects.values()

        return JsonResponse({'themes':list(theme_data)}, status = 200)

class DetailView(View):
    def get(self, request, product_id):
        product_data = Product.objects.filter(id=product_id).values()

        return JsonResponse({'product_data':product_data}, status = 200)

class SortView(View):
    def get(self, request):
        keyword = SortKeyword.objects.values()

        return JsonResponse({'keyword' : list(keyword)}, status = 200)

class ProductListView(View):
    def get(self, request):
        category = request.GET.get('category', 1)
        query = request.GET.get('query', 'price')
        product_data = Product.objects.prefetch_related('category').filter(category__id = category).order_by(query)
        product_list = [{
                'category_id'    : product.category.get(id= category).id,
                'id'             : product.id,
                'image'          : product.image_url,
                'name'           : product.name,
                'price'          : product.price
                } for product in product_data ]

        return JsonResponse({"data" : product_list}, status = 200)

