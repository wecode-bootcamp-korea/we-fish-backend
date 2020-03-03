from django.urls import path
from .views      import CategoryView, ThemeView, DetailView, SortView, ProductListView

urlpatterns = [
    path('/category_list', CategoryView.as_view()),
    path('/theme', ThemeView.as_view()),
    path('/detail/<int:product_id>', DetailView.as_view()),
    path('/sort', SortView.as_view()),
    path('', ProductListView.as_view())
]
