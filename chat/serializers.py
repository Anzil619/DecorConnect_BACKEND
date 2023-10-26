from rest_framework.serializers import ModelSerializer
from .models import *
# from company.models import ApplyJobs
# from api.serializers import UserSerializer
from rest_framework import serializers


class MessageSerializer(ModelSerializer):
    sender_email = serializers.EmailField(source='sender.email')

    class Meta:
        model = Message
        fields = ['message', 'sender_email','timestamp']


class ChatListSerializer(serializers.ModelSerializer):
    receiver_profile = serializers.ImageField(source='receiver.profile_photo', read_only=True)
    receiver_name = serializers.CharField(source='receiver.name', read_only=True)
    receiver_email = serializers.EmailField(source='receiver.email', read_only=True)
    
    class Meta:
        model = ChatList
        fields = '__all__'

