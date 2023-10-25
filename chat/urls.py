from django.urls import path
from .views import *
urlpatterns = [

    path("user-previous-chats/<int:user1>/<int:user2>/", PreviousMessagesView.as_view()),
    path("chatlist/<int:sender_id>/", Chatlist.as_view(),name="chatlist"),
    path("addtochat/", AddToChat.as_view(),name="addtochat"),

]

 