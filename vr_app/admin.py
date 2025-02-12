from django.contrib import admin
from .models import Escena  # Importar el modelo Escena

@admin.register(Escena)
class EscenaAdmin(admin.ModelAdmin):
    """Configuración del panel de administración para el modelo Escena."""
    list_display = ('nombre', 'fecha_creacion')  # Muestra estos campos en la lista
    search_fields = ('nombre',)  # Permite buscar por nombre
    list_filter = ('fecha_creacion',)  # Agrega filtros por fecha de creación

# from django.contrib import admin # type: ignore

# Register your models here.
