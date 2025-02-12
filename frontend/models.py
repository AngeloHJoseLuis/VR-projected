from django.db import models

class Escena(models.Model):
    """Modelo para almacenar escenas en la aplicación de VR."""
    nombre = models.CharField(max_length=255, unique=True)  # Agregado unique=True para evitar duplicados
    descripcion = models.TextField(blank=True, null=True)  # Permitir valores opcionales
    archivo = models.FileField(upload_to='escenas/', blank=True, null=True)  # Para subir modelos 3D
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha de creación automática

    def __str__(self):
        return self.nombre

# from django.db import models

# class Escena(models.Model):
#     # Define los campos de tu modelo aquí
#     nombre = models.CharField(max_length=100)
#     descripcion = models.TextField()

#     def __str__(self):
#         return self.nombre

# from vr_app import models

# class Escena(models.Model):
#     nombre = models.CharField(max_length=255)
#     descripcion = models.TextField()
#     archivo = models.FileField(upload_to='escenas/')
#     fecha_creacion = models.DateTimeField(auto_now_add=True)
