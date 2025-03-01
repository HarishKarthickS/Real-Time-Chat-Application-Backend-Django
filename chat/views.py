from rest_framework import generics, permissions
from .models import ChatRoom, Message
from .serializers import UserSerializer, ChatRoomSerializer, MessageSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

# User Registration
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

# List and Create Chat Rooms
class ChatRoomListCreateView(generics.ListCreateAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        room = serializer.save()
        room.participants.add(self.request.user)

# Retrieve Chat Room Details
class ChatRoomDetailView(generics.RetrieveAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
    permission_classes = [permissions.IsAuthenticated]

# List and Create Messages for a Room
class MessageListCreateView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        room_id = self.kwargs.get('room_id')
        return Message.objects.filter(room__id=room_id).order_by('timestamp')

    def perform_create(self, serializer):
        room_id = self.kwargs.get('room_id')
        serializer.save(sender=self.request.user, room_id=room_id)
