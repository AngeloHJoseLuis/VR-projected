from django.shortcuts import render # type: ignore

# Create your views here.

from rest_framework import viewsets # type: ignore
from .models import Escena
from .serializers import EscenaSerializer

class EscenaViewSet(viewsets.ModelViewSet):
    queryset = Escena.objects.all()
    serializer_class = EscenaSerializer
