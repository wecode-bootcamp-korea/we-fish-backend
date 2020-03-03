import json

from .models import Category, Theme, Review, Product

from django.views import View
from django.http  import JsonResponse, HttpResponse


class CategoryView(View):
    def get(self, request):
        category_data = Category.objects.filter(is_real_category=True).values()

        return JsonResponse({'category_list':list(category_data)}, status = 200)

class ThemeView(View):
    def get(self, request):
        theme_data = Theme.objects.values()

        return JsonResponse({'themes':list(theme_data)}, status = 200)

class ReviewView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            Review(
                product_id = data['product_id'],
                user_id    = data['user_id'],
#                order_id   = data['order_id'],
                rate       = data['rate'],
                content    = data['content'],
                image_url  = data['image']
            ).save()

            return HttpResponse(status = 200)

        except KeyError:
            return JsonResponse({"message":"INVALID_KEYS"}, status = 400)

class DetailView(View):
    def get(self, request, product_id):
        product_data = Product.objects.filter(id=product_id).values()

        return JsonResponse({'product_data':product_data}, status = 200)

class SearchView(View):
    def get(self, request):
        search_word = request.GET.get('keyword', '')

        if search_word == '':
            return JsonResponse({"message":"Bad Request"}, status = 400)

        search_data = Product.objects.filter(name__icontains=search_word).values('id', 'name', 'price', 'image_url')
        try:
            if search_data :
                return JsonResponse({"search_results":list(search_data)}, status = 200)
            return JsonResponse({"message":"No Results."}, status = 200)

        except KeyError:
            return JsonResponse({"message":"INVALID_KEY"}, status = 400)
