from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views_accounts import *
from .import views_accounts


urlpatterns = [
    path('register/', ProfessionalRegister.as_view(), name='ProfessionalRegister'), 
    path('googleprofessional/', GoogleProfessional.as_view(), name='ProfessionalRegister'), 
    
    
]