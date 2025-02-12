"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
# from . import views
from django.urls import re_path, include
from vr_app import consumers
# from . import consumers
from vr_app import views

websocket_urlpatterns = [
    re_path(r'ws/some_path/$', consumers.VoiceChatConsumer.as_asgi()),
]

# websocket_urlpatterns = [
#     re_path(r'ws/some_path/$', consumers.voice_chat.as_asgi()),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('vr_app.urls')),
    path('', views.home, name='home'),  # Define una vista para la raíz
    re_path(r'ws/', include(websocket_urlpatterns)),
]