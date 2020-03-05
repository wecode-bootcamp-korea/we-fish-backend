from .views      import CartView, CartDetailView

from django.urls import path

urlpatterns = [
    path('/cart', CartView.as_view()),
    path('/cart_detail/<str:order_number>', CartDetailView.as_view()),
]
