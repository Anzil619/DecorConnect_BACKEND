

from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views_accounts import *
from .views import *
from .import views
from .import views_accounts

urlpatterns = [

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegistration.as_view(),name = 'register'),
    path('googlehomeowner/', GoogleHomeowner.as_view(),name = 'googlehomeowner'),
    path('forgotpassword/', ForgotPassword.as_view(),name = 'googlehomeowner'),
    path('userinfo/<int:pk>/', SingleUserInfo.as_view(),name = 'userinfo'),
     path('reset-validate/<uidb64>/<token> ',
         views_accounts.reset_validate, name='reset_validate'),
    path('reset-password/', ResetPassword.as_view()),
    path('activate/<uidb64>/<token> ', views_accounts.activate, name='activate'),

]
