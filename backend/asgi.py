"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application # type: ignore
from channels.routing import ProtocolTypeRouter, URLRouter # type: ignore
from channels.auth import AuthMiddlewareStack # type: ignore
# from channels.sessions import SessionMiddlewareStack # type: ignore
from vr_app.routing import websocket_urlpatterns # type: ignore
# from vr_app.middleware import CustomAuthMiddleware # type: ignore
# from django.urls import path
# from backend import consumers

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'virtual_reality.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# application = get_asgi_application()

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": URLRouter(websocket_urlpatterns),
# })

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": CustomAuthMiddleware(URLRouter(websocket_urlpatterns)),
# })

# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# from vr_app.routing import websocket_urlpatterns
# from vr_app.middleware import CustomAuthMiddleware # type: ignore

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": CustomAuthMiddleware(URLRouter(websocket_urlpatterns)),
# })

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # (http->django views is added by default)
    # Asegúrate de incluir tus rutas WebSocket aquí
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
            # path("ws/some_path/", consumers.TuConsumidor.as_asgi()), # webrtc),
            # websocket_urlpatterns  # Importa las rutas de WebSocket aquí
            # Importa tus rutas de WebSocket aquí
            # Por ejemplo:
            # myapp.routing.websocket_urlpatterns
        )
    ),
}) # type: ignore