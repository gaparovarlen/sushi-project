from django.conf import settings
from django.db import models

from product.models import Product

from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from coupon.models import Coupon


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='orders', on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    coupon = models.ForeignKey(Coupon,
                                related_name='orders',
                                null=True,
                                blank=True,
                                on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at',]

    def __str__(self):
        return self.user.username

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_query_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '%s' %self.id
