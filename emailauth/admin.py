from django.contrib import admin
from .models import User, UserProfile

# class UserAdmin(admin.ModelAdmin):
#     fields = ('id', 'username', 'email', 'is_authtenticated')
class UserAdmin(admin.ModelAdmin):
    fields = ( 'username', 'email', 'is_verified')
admin.site.register(User, UserAdmin)

admin.site.register(UserProfile)
