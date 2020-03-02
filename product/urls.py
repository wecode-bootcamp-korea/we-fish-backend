from django.urls import path
from .views      import CategoryView, ThemeView, ProductView

urlpatterns = [
    path('/category_list', CategoryView.as_view()),
    path('/theme', ThemeView.as_view()),
    path('/detail/<int:product_id>', ProductView.as_view()),
]
