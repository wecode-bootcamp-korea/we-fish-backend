import json

from .models import Category
from .models import Product
from .models import Theme

from django.views import View
from django.http  import JsonResponse


class CategoryView(View):
    def get(self, request):
        category_data = Category.objects.filter(is_real_category=True).values()

        return JsonResponse({'category_list':list(category_data)}, status = 200)

class ThemeView(View):
    def get(self, request):
        theme_data = Theme.objects.values()

        return JsonResponse({'themes':list(theme_data)}, status = 200)

class ProductView(View):
    def get(self, request, product_id):
        product_data = Product.objects.filter(id=product_id).values()

        return JsonResponse({'product_data':product_data}, status = 200)
