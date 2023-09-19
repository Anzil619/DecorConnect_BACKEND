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
    owner_pan_card = models.FileField(null=True,blank=True)
    firm_liscense = models.FileField(null=True,blank=True)
    gst_certificate = models.FileField(null=True,blank=True)
    insurance = models.FileField(null=True,blank=True)

class ProjectImages(models.Model):
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'




class Project(models.Model):
    project_name = models.CharField(max_length=50)
    year = models.PositiveSmallIntegerField()
    project_description = models.TextField()
    cost = models.PositiveIntegerField()
    project_address = models.TextField()
    images = models.ManyToManyField(ProjectImages,null=True,blank=True)


    
class FirmInfo(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    firm_name = models.CharField(max_length=50,null=True,blank=True)
    website = models.CharField(max_length=50,null=True,blank=True)
    about = models.TextField(null=True,blank=True)
    cover_photo = models.ImageField(upload_to='coverphoto/',null=True,blank=True)
    logo = models.ImageField(upload_to='logo/',null=True,blank=True)
    firm_description = models.TextField(null=True,blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE,null=True,blank=True)
    awards = models.CharField(max_length=100,null=True, blank=True)
    verification = models.ForeignKey(FirmVerification, on_delete=models.CASCADE,null=True,blank=True)
    project = models.ManyToManyField(Project,null=True,blank=True)
    

    













