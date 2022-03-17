from .views import CouponView
from django.urls import path


urlpatterns = [
    path('coupon/', CouponView.as_view()),
    ]