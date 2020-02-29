from django.urls import path
from .views import RateView, NewView, HotView, AscendingPriceView, DescendingPriceView

urlpatterns = [
    path('/rate', RateView.as_view()),
    path('/new', NewView.as_view()),
    path('/hot', HotView.as_view()),
    path('/ascending-price', AscendingPriceView.as_view()),
    path('/descending-price', DescendingPriceView.as_view()),
]
