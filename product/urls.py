from django.urls import path

from .views      import CategoryView, ThemeView, DetailView, SearchView

urlpatterns = [
    path('/category_list', CategoryView.as_view()),
    path('/theme', ThemeView.as_view()),
    path('/detail/<int:product_id>', DetailView.as_view()),
    path('/search/<str:keyword>', SearchView.as_view()),
]
