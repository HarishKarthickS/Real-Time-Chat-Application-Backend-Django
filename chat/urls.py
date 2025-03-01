from django.urls import path
from .views import RegisterView, ChatRoomListCreateView, ChatRoomDetailView, MessageListCreateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('rooms/', ChatRoomListCreateView.as_view(), name='chatrooms'),
    path('rooms/<int:pk>/', ChatRoomDetailView.as_view(), name='chatroom-detail'),
    path('rooms/<int:room_id>/messages/', MessageListCreateView.as_view(), name='messages'),
]
