from django.db import models # type: ignore

# Create your models here.

class Escena(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre