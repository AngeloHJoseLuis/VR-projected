from rest_framework import serializers
from .models import Escena

class EscenaSerializer(serializers.ModelSerializer):
    """Serializador para el modelo Escena, usado en la API REST."""
    
    def validate_archivo(self, value):
        """Validar que el archivo tenga una extensión permitida."""
        valid_extensions = ['.glb', '.gltf', '.obj', '.fbx']
        if value and not any(value.name.lower().endswith(ext) for ext in valid_extensions):
            raise serializers.ValidationError("Formato de archivo no permitido. Usa: .glb, .gltf, .obj, .fbx")
        return value

    class Meta:
        model = Escena
        fields = ['id', 'nombre', 'descripcion', 'archivo', 'fecha_creacion']
        read_only_fields = ['id', 'fecha_creacion']  # Estos campos no se pueden modificar

# from rest_framework import serializers # type: ignore
# from .models import Escena

# class EscenaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Escena
#         fields = '__all__'
