from .models import Product
from .models import Theme
from .models import Review

from django.views import View
from django.http  import JsonResponse

class ProductView(View):
    def get(self, request):
        product_data = Product.objects.values()

        return JsonResponse({'products':list(product_data)}, status = 200)

class ThemeView(View):
    def get(self, request):
        theme_data = Theme.objects.values()

        return JsonResponse({'themes':list(theme_data)}, status = 200)

class ReviewView(View):
    def get(self, request):
        review_data = Review.objects.values()

        return JsonResponse({'reviews':list(review_data)}, status = 200)
