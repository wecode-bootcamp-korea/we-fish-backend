from django.urls import path
from .views      import CategoryView, ThemeView, ReviewView

urlpatterns = [
    path('/category_list', CategoryView.as_view()),
    path('/theme', ThemeView.as_view()),
    path('/reviews', ReviewView.as_view()),
]
