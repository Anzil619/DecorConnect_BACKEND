from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views_accounts import *
from .views_profile import *
from .views import *

from .import views_accounts
from .import views_profile


urlpatterns = [
    
    path('register/', ProfessionalRegister.as_view(), name='ProfessionalRegister'), 
    path('googleprofessional/', GoogleProfessional.as_view(), name='ProfessionalRegister'), 
    path('profilecompletion/', FirmCreation.as_view(), name='profile_completion'), 
    path('createproject/', CreateProject.as_view(), name='createproject'), 
    path('createprojectimages/', CreateProjectImages.as_view(), name='createprojectimages'), 
    path('fetchfirminfo/<int:user_id>/', GetFirmInfo.as_view(), name='fetchfirminfo'), 
    path('firmcompletion/<int:pk>/', Firm_Completion.as_view(), name='firmcompletion'), 
    path('firmverificationupdate/<int:pk>/', FirmVerificationUpdate.as_view(), name='firmverificationupdate'), 
    path('editfirminfo/<int:pk>/', EditFirmInfo.as_view(), name='editfirminfo'), 
    path('editproject/<int:pk>/', EditProject.as_view(), name='editproject'), 
    path('editdeleteprojectimages/<int:pk>/', EditDeleteProjectImages.as_view(), name='editdeleteprojectimages'), 
    
]