from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views_accounts import *
from .views_profile import *
from .import views_accounts
from .import views_profile


urlpatterns = [
    
    path('register/', ProfessionalRegister.as_view(), name='ProfessionalRegister'), 
    path('googleprofessional/', GoogleProfessional.as_view(), name='ProfessionalRegister'), 
    path('profilecompletion/', profile_completions.as_view(), name='profile_completion'), 
    
]