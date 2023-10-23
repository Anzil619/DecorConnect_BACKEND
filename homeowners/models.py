from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager 
from django.utils import timezone



class CustomUserManager(BaseUserManager):
    def create_user(self,email,password=None, **extra_fields):
        if not email:
            raise ValueError('email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('role', 'admin')

        if extra_fields.get('role') != 'admin':
            raise ValueError('Superuser field role must be "admin"')
        
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser field is_active must be true')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser field is_staff must be true')

        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser field is_admin must be True')

        return self.create_user(email=email, password=password, **extra_fields)
        
        




class CustomUser(AbstractBaseUser):

    ROLE_CHOICES = [
        ('homeowner','homeowner'),
        ('professional','professional'),
        ('admin','admin')
    ]

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100,unique=True)
    phone = models.PositiveBigIntegerField(null=True,blank=True)
    role = models.CharField(max_length=100,default='homeowner',choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_google = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    profile_photo = models.ImageField(upload_to='user_profile_photo/',null=True,blank=True)
    cover_photo = models.ImageField(upload_to='user_cover_photo/',null=True,blank=True)
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role']


    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


class UserAddress(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address_line = models.TextField()
    phone = models.PositiveIntegerField()



class Posts(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/',null=True,blank=True)
    caption = models.TextField()
    location = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)

    

class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'post']  


    def __str__(self):
        return f'{self.user} likes {self.post}'




class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} commented on {self.post}: {self.text}'

