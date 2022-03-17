from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField()

    def __str__(self):
        return self.code


# class CouponUser(models.Model):

#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User")
#     coupon = models.ForeignKey('Coupon', on_delete=models.CASCADE, verbose_name="Coupon")
#     times_used = models.IntegerField(verbose_name="Usage Count")

#     def __str__(self):
#         return str(self.user)

#     class Meta:
#         verbose_name = "Coupon User"
#         verbose_name_plural = "Coupon Users"
