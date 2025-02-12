from django.contrib.auth.models import AnonymousUser, User
from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware
from channels.auth import AuthMiddlewareStack
from django.db import close_old_connections
from urllib.parse import parse_qs
import json
from channels.generic.websocket import AsyncWebsocketConsumer


# 🔹 Middleware de autenticación personalizada para WebSockets
class CustomAuthMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        query_string = parse_qs(scope['query_string'].decode())
        username = query_string.get('username', [None])[0]

        if username:
            scope['user'] = await self.get_user(username)
        else:
            scope['user'] = AnonymousUser()

        return await super().__call__(scope, receive, send)

    @database_sync_to_async
    def get_user(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return AnonymousUser()


# 🔹 WebSocket para Notificaciones
class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "notifications"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            message = data.get("message", "🔔 Nueva notificación recibida.")

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "send_notification",
                    "message": message,
                },
            )
        except json.JSONDecodeError:
            await self.send(text_data=json.dumps({"error": "Formato JSON inválido"}))

    async def send_notification(self, event):
        await self.send(text_data=json.dumps({"message": event["message"]}))


# 🔹 WebSocket para Chat en VR
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "chat_vr"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            message = data.get("message", "")
            user = data.get("user", "Anónimo")

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat_message",
                    "message": message,
                    "user": user,
                },
            )
        except json.JSONDecodeError:
            await self.send(text_data=json.dumps({"error": "Formato JSON inválido"}))

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({"message": event["message"], "user": event["user"]}))


# 🔹 WebSocket para Chat de Voz en VR
class VoiceChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "voice_chat"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            message = text_data_json.get("message", "")

            await self.channel_layer.group_send(
                self.room_group_name,
                {"type": "voice_chat_message", "message": message},
            )
        except json.JSONDecodeError:
            await self.send(text_data=json.dumps({"error": "Formato JSON inválido"}))

    async def voice_chat_message(self, event):
        await self.send(text_data=json.dumps({"message": event["message"]}))


# Para usarlo en `routing.py`
voice_chat = VoiceChatConsumer.as_asgi()
chat_vr = ChatConsumer.as_asgi()
notifications = NotificationConsumer.as_asgi()

# from django.contrib.auth.models import AnonymousUser
# from channels.db import database_sync_to_async
# from channels.middleware import BaseMiddleware
# from channels.auth import AuthMiddlewareStack
# from django.db import close_old_connections
# from urllib.parse import parse_qs
# from django.contrib.auth.models import User

# class CustomAuthMiddleware(BaseMiddleware):
#     async def __call__(self, scope, receive, send):
#         query_string = parse_qs(scope['query_string'].decode())
#         username = query_string.get('username', [None])[0]
        
#         if username:
#             scope['user'] = await self.get_user(username)
        
#         return await super().__call__(scope, receive, send)

#     @database_sync_to_async
#     def get_user(self, username):
#         try:
#             return User.objects.get(username=username)
#         except User.DoesNotExist:
#             return AnonymousUser()

# # 1. Agregar WebSockets para notificaciones
# import json
# from channels.generic.websocket import AsyncWebsocketConsumer

# class NotificationConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.room_group_name = "notifications"
#         await self.channel_layer.group_add(self.room_group_name, self.channel_name)
#         await self.accept()

#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

#     async def receive(self, text_data):
#         data = json.loads(text_data)
#         message = data['message']

#         await self.channel_layer.group_send(
#             self.room_group_name,
#             {
#                 'type': 'send_notification',
#                 'message': message
#             }
#         )

#     async def send_notification(self, event):
#         await self.send(text_data=json.dumps({
#             'message': event['message']
#         }))

# import json
# from channels.generic.websocket import AsyncWebsocketConsumer

# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.room_group_name = "chat_vr"
#         await self.channel_layer.group_add(self.room_group_name, self.channel_name)
#         await self.accept()

#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

#     async def receive(self, text_data):
#         data = json.loads(text_data)
#         message = data['message']
#         user = data['user']

#         await self.channel_layer.group_send(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message,
#                 'user': user
#             }
#         )

#     async def chat_message(self, event):
#         await self.send(text_data=json.dumps({
#             'message': event['message'],
#             'user': event['user']
#         }))

# import json
# from channels.generic.websocket import AsyncWebsocketConsumer # type: ignore

# class VoiceChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()

#     async def disconnect(self, close_code):
#         pass

#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']
#         await self.send(text_data=json.dumps({
#             'message': message
#         }))

# voice_chat = VoiceChatConsumer.as_asgi()