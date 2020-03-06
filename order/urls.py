from .views      import CartView, CartDetailView, OrderCompleteView

from django.urls import path

urlpatterns = [
    path('/cart', CartView.as_view()),
    path('/cart_detail/<str:order_number>', CartDetailView.as_view()),
    path('/complete/<str:order_number>', OrderCompleteView.as_view())
]
