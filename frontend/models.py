from django.db import models

class Escena(models.Model):
    # Define los campos de tu modelo aquí
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

# from vr_app import models

# class Escena(models.Model):
#     nombre = models.CharField(max_length=255)
#     descripcion = models.TextField()
#     archivo = models.FileField(upload_to='escenas/')
#     fecha_creacion = models.DateTimeField(auto_now_add=True)
