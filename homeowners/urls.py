

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
    path('updateuser/<int:pk>/', UpdateUser.as_view(),name = 'updateuser'),
    path('firmlist/', FirmsList.as_view(),name = 'firmlist'),
    path('adduseraddress/', AddUserAddress.as_view(),name = 'adduseraddress'),
    path('useraddress/<int:user_id>/', UserAddress.as_view(),name = 'useraddress'),
    path('getproject/<int:pk>/', GetProject.as_view(),name = 'getproject'),
    path('userinfo/<int:pk>/', SingleUserInfo.as_view(),name = 'userinfo'),
    path('singlefirminfo/<int:pk>/', SingleFirmInfo.as_view(),name = 'singlefirminfo'),
    path('getuserpost/<int:user_id>/', GetUserPosts.as_view(),name = 'getuserpost'),
    path('listlikes/<int:post_id>/', ListLikes.as_view(),name = 'listlikes'),
    path('dislike/<int:user_id>/<int:post_id>/', Dislike.as_view(),name = 'dislike'),
    path('createlike/', CreateLike.as_view(),name = 'createlike'),
    path('listpost/', ListPost.as_view(),name = 'listpost'),
    path('createpost/', CreatePost.as_view(),name = 'createpost'),
    path('editdelete/<int:pk>/', DeleteEditPost.as_view(),name = 'editdelete'),
    path('createcomment/', CreateComment.as_view(),name = 'createcomment'),
    path('deletecomment/<int:pk>/', DeleteComment.as_view(),name = 'deletecomment'),
    path('suggestionfirm/', SuggestionFirm.as_view(),name = 'suggestionfirm'),
     path('reset-validate/<uidb64>/<token> ',
         views_accounts.reset_validate, name='reset_validate'),
    path('reset-password/', ResetPassword.as_view()),
    path('activate/<uidb64>/<token> ', views_accounts.activate, name='activate'),
    
]
