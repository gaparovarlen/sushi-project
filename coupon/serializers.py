from rest_framework import serializers
from .models import Coupon
from django.contrib.auth.models import User


# class UserSerializer(serializers.ModelSerializer):
#     all_users = serializers.BooleanField(read_only=True)
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'id', 'all_users')


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon 
        fields = (
            "id",
            "code",
            "valid_from",
            "valid_to",
            "discount",
            "active",
        )

# class CouponUserSerializer(serializers.ModelSerializer):

#     # user = UserSerializer()
#     coupon = CouponSerializer()
#     times_used = serializers.IntegerField()
#     class Meta:
#         model = CouponUser
#         fields = (
#             "id",
#             # 'user',
#             'coupon',
#             "times_used",
#         )
