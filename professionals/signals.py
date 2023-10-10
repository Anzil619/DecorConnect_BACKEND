from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import models
from .models import FirmInfo
from .helpers import send_firm_approval_email

@receiver(pre_save, sender=FirmInfo)
def send_approval_email(sender, instance, **kwargs):
    if instance._state.adding or instance.status != FirmInfo.objects.get(pk=instance.pk).status:
        if instance.status == 'approved':
            user_email = instance.user.email
            send_firm_approval_email(user_email)
