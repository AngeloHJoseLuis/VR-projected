from django.db import models

class Escena(models.Model):
    """Modelo para almacenar escenas 3D en la aplicación de VR."""
    nombre = models.CharField(max_length=255, unique=True, verbose_name="Nombre de la escena")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    archivo = models.FileField(upload_to='escenas/', blank=True, null=True, verbose_name="Archivo 3D")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    class Meta:
        verbose_name = "Escena"
        verbose_name_plural = "Escenas"
        ordering = ["-fecha_creacion"]  # Ordenar por fecha más reciente

    def __str__(self):
        return self.nombre

# from django.db import models # type: ignore

# # Create your models here.

# class Escena(models.Model):
#     nombre = models.CharField(max_length=100)
#     descripcion = models.TextField()

#     def __str__(self):
#         return self.nombre