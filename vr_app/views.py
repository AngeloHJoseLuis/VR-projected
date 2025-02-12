from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from vr_app.models import Escena  # Se corrige la importación del modelo
from .serializers import EscenaSerializer


# 🔹 Vista para la página principal
def home(request):
    return render(request, 'index.html')


# 🔹 API REST para gestionar escenas
class EscenaViewSet(viewsets.ModelViewSet):
    """API REST para gestionar escenas 3D."""
    queryset = Escena.objects.all()
    serializer_class = EscenaSerializer

    def perform_create(self, serializer):
        """Guarda la escena y notifica a los usuarios en WebSockets."""
        escena = serializer.save()
        notify_users(f"Nuevo modelo 3D agregado: {escena.nombre}") # type: ignore


# 🔹 API para obtener modelos en AR
@api_view(['GET'])
def get_ar_models(request):
    """Devuelve la lista de modelos 3D disponibles para AR."""
    models = Escena.objects.values('id', 'nombre', 'archivo')
    data = [{"id": model["id"], "nombre": model["nombre"], "archivo": model.get("archivo", "")} for model in models]
    return Response(data)


# 🔹 Vista para l

# from channels.layers import get_channel_layer
# from asgiref.sync import async_to_sync

# from rest_framework import viewsets # Importa correctamente desde rest_framework
# from frontend.models import Escena
# from .serializers import EscenaSerializer
# from django.shortcuts import render
# from django.http import JsonResponse

# # Define la vista 'home'
# def home(request):
#     return render(request, 'index.html')

# class EscenaViewSet(viewsets.ModelViewSet):
#     queryset = Escena.objects.all()
#     serializer_class = EscenaSerializer

#     def perform_create(self, serializer):
#         escena = serializer.save()
#         notify_users(f"Nuevo modelo 3D agregado: {escena.nombre}")

# def get_ar_models(request):
#     models = Escena.objects.values('id', 'nombre', 'archivo')
#     return JsonResponse(list(models), safe=False)

# def voice_chat(request):
#     return render(request, "vr_app/voice_chat.html")

# def notify_users(message):
#     channel_layer = get_channel_layer()
#     async_to_sync(channel_layer.group_send)(
#         "notifications",
#         {"type": "send_notification", "message": message}
#     )

# # # 4. Modificar la API para enviar notificaciones al subir modelos
# # from channels.layers import get_channel_layer
# # from asgiref.sync import async_to_sync

# # from backend import views
# # from frontend.models import Escena
# # from vr_app.serializers import EscenaSerializer
# # from django.shortcuts import render
# # from django.http import JsonResponse

# # from rest_framework import viewsets # type: ignore
# # from frontend.models import Escena
# # from .serializers import EscenaSerializer

# # class EscenaViewSet(views.ModelViewSet): # viewsets
# #     queryset = Escena.objects.all()
# #     serializer_class = EscenaSerializer

# #     def perform_create(self, serializer):
# #         escena = serializer.save()
# #         notify_users(f"Nuevo modelo 3D agregado: {escena.nombre}")

# # def get_ar_models(request):
# #     models = Escena.objects.values('id', 'nombre', 'archivo')
# #     return JsonResponse(list(models), safe=False)

# # def voice_chat(request):
# #     return render(request, "vr_app/voice_chat.html")

# # def notify_users(message):
# #     channel_layer = get_channel_layer()
# #     async_to_sync(channel_layer.group_send)(
# #         "notifications",
# #         {"type": "send_notification", "message": message}
# #     )

# # # from django.shortcuts import render # type: ignore

# # # Create your views here.
