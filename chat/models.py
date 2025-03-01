from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Extend or add fields as needed
    pass

class ChatRoom(models.Model):
    """
    ChatRoom for group chats. For direct messaging, you can create a ChatRoom
    with exactly two participants.
    """
    name = models.CharField(max_length=255, blank=True)
    participants = models.ManyToManyField(User, related_name='chatrooms')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name if self.name else f'Room {self.id}'

class Message(models.Model):
    room = models.ForeignKey(ChatRoom, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.sender.username} in {self.room}'
