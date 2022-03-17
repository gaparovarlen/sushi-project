from rest_framework.response import Response
from .models import Coupon
from django.utils import timezone


from .serializers import CouponSerializer
from rest_framework import status, generics
from rest_framework.generics import GenericAPIView


class CouponView(generics.GenericAPIView):
    now = timezone.now()
    def post(self, request):
        try:
            code = self.request.data['code']
            coupon = Coupon.objects.get(code__iexact=code,
                                        valid_from__lte=self.now,
                                        valid_to__gte=self.now,
                                        active=True)
            serializer_class = CouponSerializer(coupon)
            return Response(serializer_class.data, status=status.HTTP_200_OK)
        except Coupon.DoesNotExist:
            return Response("coupon doesn't exist", status=status.HTTP_400_BAD_REQUEST)

