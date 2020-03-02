from .models import Product
from .models import Theme
from .models import Review

from django.views import View
from django.http  import JsonResponse

class ThemeView(View):
    def get(self, request):
        theme_data = Theme.objects.values()

        return JsonResponse({'themes':list(theme_data)}, status = 200)
