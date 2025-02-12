from django.urls import path
from .consumers import ChatConsumer, VoiceChatConsumer, NotificationConsumer

# Definir las rutas WebSocket correctamente en una sola lista
websocket_urlpatterns = [
    path("ws/voice_chat/", VoiceChatConsumer.as_asgi()),
    path("ws/notifications/", NotificationConsumer.as_asgi()),
    path("ws/chat/", ChatConsumer.as_asgi()),
]

# from django.urls import path
# from .consumers import ChatConsumer
# from django.urls import re_path
# from .consumers import VoiceChatConsumer
# # 2. Agregar las rutas WebSocket
# from .consumers import NotificationConsumer

# websocket_urlpatterns = [
#     re_path(r'ws/voice_chat/$', VoiceChatConsumer.as_asgi()),
# ]

# websocket_urlpatterns = [
#     path("ws/notifications/", NotificationConsumer.as_asgi()),
# ]

# websocket_urlpatterns = [
#     path("ws/chat/", ChatConsumer.as_asgi()),
# ]

# from django.urls import re_path # type: ignore
# from . import consumers

# websocket_urlpatterns = [
#     re_path(r'ws/some_path/$', consumers.MyConsumer.as_asgi()),
# ]