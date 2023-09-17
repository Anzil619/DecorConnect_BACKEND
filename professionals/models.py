from django.db import models
from homeowners.models import CustomUser


class Address(models.Model):
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    address_line = models.TextField()
    phone = models.PositiveIntegerField()



class FirmVerification(models.Model):
    owner_name = models.CharField(max_length=50)
    owner_pan_card = models.FileField()
    firm_liscense = models.FileField()
    gst_certificate = models.FileField()
    insurance = models.FileField()

    
class FirmInfo(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    firm_name = models.CharField(max_length=50)
    
    website = models.CharField(max_length=50,null=True,blank=True)
    about = models.TextField()
    cover_photo = models.ImageField(upload_to='coverphoto/')
    logo = models.ImageField(upload_to='logo/',null=True,blank=True)
    firm_description = models.TextField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE,null=True,blank=True)
    awards = models.CharField(max_length=100,null=True, blank=True)
    verification = models.ForeignKey(FirmVerification, on_delete=models.CASCADE,null=True,blank=True)
    

    









