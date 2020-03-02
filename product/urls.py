from django.urls import path
from .views      import CategoryView, ThemeView, SearchView

urlpatterns = [
    path('/category_list', CategoryView.as_view()),
    path('/theme', ThemeView.as_view()),
    path('/reviews', SearchView.as_view()),
]
