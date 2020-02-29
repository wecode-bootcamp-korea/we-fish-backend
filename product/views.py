from .models      import Category, Product, ProductCategory

from django.views import View
from django.http  import HttpResponse, JsonResponse

#추천순
class RateView(View):
    def get(self, request):
        product_data = Product.objects.order_by('-rate').values('category__name','id','image_url','name','price')

        product_list  = []
        category_list = []
        for product in product_data:
            product_list.append(
                {
                    'category'  : product['category__name'],
                    'id'        : product['id'],
                    'image'     : product['image_url'],
                    'name'      : product['name'],
                    'price'     : product['price']
                }
            )

        categories = [category for category in Category.objects.values()]
        for i in range(len(categories)):
            category_list.append(
                {
                    categories[i]['name']:
                              [
                                  item for item in product_list
                               if item['category'] == categories[i]['name']
                              ]
                }
            )

        return JsonResponse({"rate":category_list}, status = 200)

#신상품순
class NewView(View):
    def get(self, request):
        product_data = Product.objects.order_by('-updated_at').values('category__name','id','image_url','name','price')

        product_list  = []
        category_list = []
        for product in product_data:
            product_list.append(
                {
                    'category'  : product['category__name'],
                    'id'        : product['id'],
                    'image'     : product['image_url'],
                    'name'      : product['name'],
                    'price'     : product['price']
                }
            )

        categories = [category for category in Category.objects.values()]
        for i in range(len(categories)):
            category_list.append(
                {
                    categories[i]['name']:
                              [
                                  item for item in product_list
                               if item['category'] == categories[i]['name']
                              ]
                }
            )

        return JsonResponse({"new":category_list}, status = 200)

#인기상품순
class HotView(View):
    def get(self, request):
        product_data = Product.objects.order_by('-sales').values('category__name','id','image_url','name','price')

        product_list  = []
        category_list = []
        for product in product_data:
            product_list.append(
                {
                    'category'  : product['category__name'],
                    'id'        : product['id'],
                    'image'     : product['image_url'],
                    'name'      : product['name'],
                    'price'     : product['price']
                }
            )

        categories = [category for category in Category.objects.values()]
        for i in range(len(categories)):
            category_list.append(
                {
                    categories[i]['name']:
                              [
                                  item for item in product_list
                               if item['category'] == categories[i]['name']
                              ]
                }
            )

        return JsonResponse({"hot":category_list}, status = 200)

#낮은 가격순
class AscendingPriceView(View):
    def get(self, request):
        product_data = Product.objects.order_by('price').values('category__name','id','image_url','name','price')

        product_list  = []
        category_list = []
        for product in product_data:
            product_list.append(
                {
                    'category'  : product['category__name'],
                    'id'        : product['id'],
                    'image'     : product['image_url'],
                    'name'      : product['name'],
                    'price'     : product['price']
                }
            )

        categories = [category for category in Category.objects.values()]
        for i in range(len(categories)):
            category_list.append(
                {
                    categories[i]['name']:
                              [
                                  item for item in product_list
                               if item['category'] == categories[i]['name']
                              ]
                }
            )

        return JsonResponse({"ascending_price":category_list}, status = 200)

#높은 가격순
class DescendingPriceView(View):
    def get(self, request):
        product_data = Product.objects.order_by('-price').values('category__name','id','image_url','name','price')

        product_list  = []
        category_list = []
        for product in product_data:
            product_list.append(
                {
                    'category'  : product['category__name'],
                    'id'        : product['id'],
                    'image'     : product['image_url'],
                    'name'      : product['name'],
                    'price'     : product['price']
                }
            )

        categories = [category for category in Category.objects.values()]
        for i in range(len(categories)):
            category_list.append(
                {
                    categories[i]['name']:
                              [
                                  item for item in product_list
                               if item['category'] == categories[i]['name']
                              ]
                }
            )

        return JsonResponse({"descending_price":category_list}, status = 200)
