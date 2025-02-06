from django.urls import path, include # type: ignore
from rest_framework.routers import DefaultRouter # type: ignore
from .views import EscenaViewSet
from django.urls import re_path
from vr_app.consumers import voice_chat
from . import consumers
from django.urls import path
from .views import voice_chat

websocket_urlpatterns = [
    re_path(r'ws/some_path/$', voice_chat),
    # re_path(r'ws/some_path/$', consumers.voice_chat.as_asgi()),
]

router = DefaultRouter()
router.register(r'escenas', EscenaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include(router.urls)),
    re_path(r'ws/', include(websocket_urlpatterns)),
    path('voice_chat/', voice_chat, name='voice_chat'),
]