
from django.urls import path
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views_accounts import *
from .views import *
from .import views_accounts


urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('listuser/', ListUser.as_view(),name = 'listuser'),
    path('editdeleteuser/<int:pk>/', EditDeleteUser.as_view(),name = 'editdeleteuser'),
    path('approvefirm/<int:pk>/', ApproveFirm.as_view(),name = 'approvefirm'),
]
