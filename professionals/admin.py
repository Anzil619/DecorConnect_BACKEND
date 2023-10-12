from django.contrib import admin
from .models import FirmInfo,FirmVerification,Address,Project,ProjectImages,Review
# Register your models here.

admin.site.register(FirmInfo)
admin.site.register(FirmVerification)
admin.site.register(Address)
admin.site.register(Project)
admin.site.register(ProjectImages)
admin.site.register(Review)
