from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import ChatRoom, Message

# API Endpoint Tests
class ChatAPITests(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.chatrooms_url = reverse('chatrooms')
        self.user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123"
        }
        self.user = get_user_model().objects.create_user(**self.user_data)
        self.client.force_authenticate(user=self.user)

    def test_register(self):
        response = self.client.post(
            self.register_url,
            {"username": "newuser", "email": "new@example.com", "password": "password456"}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], "newuser")

    def test_create_chatroom(self):
        response = self.client.post(self.chatrooms_url, {"name": "Test Room"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], "Test Room")
        self.assertIn('participants', response.data)

    def test_get_chatroom_detail(self):
        chatroom = ChatRoom.objects.create(name="Room 1")
        chatroom.participants.add(self.user)
        url = reverse('chatroom-detail', kwargs={'pk': chatroom.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Room 1")

    def test_create_message(self):
        chatroom = ChatRoom.objects.create(name="Room 1")
        chatroom.participants.add(self.user)
        url = reverse('messages', kwargs={'room_id': chatroom.id})
        response = self.client.post(url, {"content": "Hello World!"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['content'], "Hello World!")


# WebSocket Tests using pytest and Channels
import pytest
from channels.testing import WebsocketCommunicator
from chatapp.asgi import application
from asgiref.sync import sync_to_async

@pytest.mark.asyncio
async def test_websocket_chat():
    # Create a chat room and a user asynchronously
    room = await sync_to_async(ChatRoom.objects.create)(name="Async Room")
    user = await sync_to_async(get_user_model().objects.create_user)(
        username="wsuser", email="ws@example.com", password="password"
    )
    await sync_to_async(room.participants.add)(user)

    # Create a WebSocket communicator; the URL must match the routing pattern
    communicator = WebsocketCommunicator(application, f'/ws/chat/{room.id}/')
    connected, _ = await communicator.connect()
    assert connected

    # Send a message via WebSocket
    message_data = {"message": "Hello WebSocket"}
    await communicator.send_json_to(message_data)
    response = await communicator.receive_json_from()
    assert response['message'] == "Hello WebSocket"
    # Depending on authentication, username may be 'wsuser' or 'Anonymous'
    assert response['username'] in ["wsuser", "Anonymous"]

    await communicator.disconnect()
