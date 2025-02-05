from django.urls import path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    path("ws/chat/", ChatConsumer.as_asgi()),
]

# from django.urls import re_path # type: ignore
# from . import consumers

# websocket_urlpatterns = [
#     re_path(r'ws/some_path/$', consumers.MyConsumer.as_asgi()),
# ]