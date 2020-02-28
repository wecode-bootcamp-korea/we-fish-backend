from django.urls import path
from .views      import ProductListView, ProductView, ThemeView, ReviewView

urlpatterns = [
    path('/product_list', ProductListView.as_view()),
    path('/product_info', ProductView.as_view()),
    path('/theme', ThemeView.as_view()),
    path('/review', ReviewView.as_view()),
]
