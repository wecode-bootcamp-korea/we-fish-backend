from django.urls import path
from .views import SignUpView, SignInView, ProfileView, VerificationView, ConfirmaionView

urlpatterns = [
    path('',SignUpView.as_view()),
    path('/sign-up', SignUpView.as_view()),
    path('/sign-in', SignInView.as_view()),
    path('/profile', ProfileView.as_view()),
    path('/verify' , VerificationView.as_view()),
    path('/confirm', ConfirmaionView.as_view()),
]
