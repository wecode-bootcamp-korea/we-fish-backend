from django.urls import path
from .views import SignUpView, SignInView, ProfileView, VerificationView, ConfirmationView, KakaoView

urlpatterns = [
    path('',SignUpView.as_view()),
    path('/sign-up', SignUpView.as_view()),
    path('/sign-in', SignInView.as_view()),
    path('/profile', ProfileView.as_view()),
    path('/verify' , VerificationView.as_view()),
    path('/confirm', ConfirmationView.as_view()),
    path('/kakao', KakaoView.as_view())
]
