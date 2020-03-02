import json

from .models import Category, Theme, Product

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

class SearchView(View):
    def get(self, request, keyword):
        search_data = Product.objects.filter(name__icontains=keyword).values('name', 'price', 'image_url')
        if not search_data:

            return JsonResponse(
                {
                    'message':'No Results. Please input another word.'
                },
                status = 200)
        return JsonResponse({'search_results':list(search_data)}, status = 200)
