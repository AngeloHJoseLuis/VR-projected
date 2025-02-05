from vr_app import models


class Escena(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    archivo = models.FileField(upload_to='escenas/')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
