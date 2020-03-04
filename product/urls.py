from .views      import (
    CategoryView,
    DetailView,
    SearchView,
    ProductListView,
    HoneyView
)

from django.urls import path

urlpatterns = [
    path('/category_list', CategoryView.as_view()),
    path('/detail/<int:product_id>', DetailView.as_view()),
    path('', ProductListView.as_view()),
    path('/search', SearchView.as_view()),
    path('/honey', HoneyView.as_view()),
]
