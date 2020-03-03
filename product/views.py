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

class DetailView(View):
    def get(self, request, product_id):
        product_data = Product.objects.filter(id=product_id).values()

        return JsonResponse({'product_data':product_data}, status = 200)

class SearchView(View):
    def get(self, request):
        search_word = request.GET.get('keyword', '')
        try:
            search_data = Product.objects.filter(name__icontains=search_word).values('name', 'price', 'image_url')
            if not search_data:
                return JsonResponse({"message":"No Results."}, status = 200)
            return JsonResponse({"search_results":list(search_data)}, status = 200)

        except KeyError:
            return JsonResponse({"message":"INVALID_KEY"})
