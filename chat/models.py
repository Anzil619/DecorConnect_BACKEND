from django.db import models
from homeowners.models import CustomUser


class Message(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True,related_name="sender_message_set")
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True,related_name="reciever_message_set")
    message = models.TextField(null=True, blank=True)
    thread_name = models.CharField(null=True, blank=True, max_length=200)
    timestamp = models.TimeField(auto_now_add=True)

    # def __str__(self) -> str:
    #     return f'{self.sender.name}-{self.sender.name}'

class ChatList(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True,related_name="sender")
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True,related_name="reciever")

    class Meta:
        unique_together = ('sender', 'receiver')

