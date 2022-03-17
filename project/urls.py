from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('emailauth.urls')),
    path('api/v1/', include('product.urls')),
    path('api/order/', include('order.urls')),
    path('api/v2/', include('coupon.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
