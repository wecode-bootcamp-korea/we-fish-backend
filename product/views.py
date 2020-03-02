import json

from .models import Category, Theme, Review

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

class ReviewWriteView(View):
    def post(self, request):
        data = json.loads(request.body)

        Review(
            product_id = data['product_id'],
            user_id    = data['user_id'],
#            order_id   = data['order_id'],
            rate       = data['rate'],
            content    = data['content'],
            image_url  = data['image']
        ).save()

        return JsonResponse({'message':'Okay'}, status = 200)
