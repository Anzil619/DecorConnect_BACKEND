from django.contrib import admin

from .models import CustomUser,UserAddress,Posts,Like

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(UserAddress)
admin.site.register(Posts)
admin.site.register(Like)