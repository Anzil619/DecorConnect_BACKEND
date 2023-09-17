from django.contrib import admin
from .models import FirmInfo,FirmVerification,Address
# Register your models here.

admin.site.register(FirmInfo)
admin.site.register(FirmVerification)
admin.site.register(Address)