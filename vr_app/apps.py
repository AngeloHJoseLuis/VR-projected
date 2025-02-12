from django.apps import AppConfig


class VrAppConfig(AppConfig):
    """Configuración de la aplicación vr_app."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vr_app'
    verbose_name = "Aplicación de Realidad Virtual"  # Nombre más legible en Django Admin

    def ready(self):
        """Importa señales cuando la aplicación está lista."""
        # import vr_app.signals  # Asegura la carga de señales (si existen)

# from django.apps import AppConfig # type: ignore


# class VrAppConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'vr_app'
