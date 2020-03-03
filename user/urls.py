from .views import SignUpView, SignInView, ProfileView, VerificationView, ConfirmationView, AskView, AskEditView
from django.urls import path

urlpatterns = [
    path('',SignUpView.as_view()),
    path('/sign-up', SignUpView.as_view()),
    path('/sign-in', SignInView.as_view()),
    path('/profile', ProfileView.as_view()),
    path('/verify' , VerificationView.as_view()),
    path('/confirm', ConfirmationView.as_view()),
    path('/ask', AskView.as_view()),
    path('/edit/<int:id>', AskEditView.as_view()),
]
