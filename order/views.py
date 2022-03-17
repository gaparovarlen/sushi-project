from emailauth.models import User
from django.http import Http404

from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order, OrderItem
from coupon.models import Coupon
from .serializers import OrderSerializer
from decimal import Decimal

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        paid_amount = sum(item.get('quantity') * item.get('product').price for item in serializer.validated_data['items'])
        coupon = serializer.validated_data['coupon']
        if coupon:
            coupon = Coupon.objects.get(pk=coupon.id)
            if coupon:
                discount = (coupon.discount / Decimal('100')) * paid_amount
                paid_amount = paid_amount - discount

        serializer.save(user=request.user, paid_amount=paid_amount)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)