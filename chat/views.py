from django.shortcuts import render
from .serializers import *
# from company.models import ApplyJobs
from rest_framework.filters import SearchFilter
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import CreateAPIView,ListAPIView,ListCreateAPIView


class ChatCreatingView(CreateAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()


class PreviousMessagesView(ListAPIView):
    serializer_class = MessageSerializer
    pagination_class = None

    def get_queryset(self):
        user1 = int(self.kwargs['user1'])
        user2 = int(self.kwargs['user2'])

        thread_suffix = f"{user1}_{user2}" if user1 > user2 else f"{user2}_{user1}"
        thread_name = 'chat_'+thread_suffix
        queryset = Message.objects.filter(
            thread_name=thread_name
        )
        return queryset
    

class Chatlist(ListCreateAPIView):
    queryset = ChatList.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['receiver__name']
    serializer_class = ChatListSerializer

    def get_queryset(self):
        sender_id = self.kwargs.get('sender_id')
        return ChatList.objects.filter(sender_id=sender_id)

class AddToChat(CreateAPIView):
    queryset = ChatList.objects.all()
    serializer_class = ChatListSerializer
    
    