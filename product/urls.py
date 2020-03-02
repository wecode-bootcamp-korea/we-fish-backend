from django.urls import path
from .views      import CategoryView, ProductView

urlpatterns = [
    path('/category_list', CategoryView.as_view()),
    path('theme', ThemeView.as_view())
]
