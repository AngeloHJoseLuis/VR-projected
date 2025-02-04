from rest_framework import serializers # type: ignore
from .models import Escena

class EscenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escena
        fields = '__all__'
