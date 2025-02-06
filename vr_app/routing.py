from django.urls import path
from .consumers import ChatConsumer
# 2. Agregar las rutas WebSocket
from .consumers import NotificationConsumer

websocket_urlpatterns = [
    path("ws/notifications/", NotificationConsumer.as_asgi()),
]

websocket_urlpatterns = [
    path("ws/chat/", ChatConsumer.as_asgi()),
]

# from django.urls import re_path # type: ignore
# from . import consumers

# websocket_urlpatterns = [
#     re_path(r'ws/some_path/$', consumers.MyConsumer.as_asgi()),
# ]