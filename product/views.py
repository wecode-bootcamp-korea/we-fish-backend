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

class ProductView(View):
    def get(self, request):
        product_data = Product.objects.values('name', 'tagline', 'price', 'unit', 'package', 'origin', 'delivery', 'caution', 'image_url')

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
                    'message':'No results. Please input another keyword.'
                 },
                status = 200)

        return JsonResponse({'message':'Okay. Let me find it.'}, status = 200)

    def get(self, request):
        search_data = Product.objects.filter(name__icontains=self.keyword).values()

        return JsonResponse({'search_results':list(search_data)}, status = 200)

class ThemeView(View):
    def get(self, request):
        theme_data = Theme.objects.values()

        return JsonResponse({'themes':list(theme_data)}, status = 200)
