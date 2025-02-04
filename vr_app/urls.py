from django.urls import path, include # type: ignore
from rest_framework.routers import DefaultRouter # type: ignore
from .views import EscenaViewSet

router = DefaultRouter()
router.register(r'escenas', EscenaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]