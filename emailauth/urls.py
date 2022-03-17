from .views import UserRegistrationView, \
UserLoginView, VerifyEmail, ForgotPassView, ChangePassView
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view()),
    path('signin/', UserLoginView.as_view()),  
    path('email-verify/<str:pk>/', VerifyEmail.as_view()),  
    path('forgot-pass/', ForgotPassView.as_view()),  
    path('change-pass/<str:pk>/', ChangePassView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]