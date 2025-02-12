from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Escena

class EscenaModelTest(TestCase):
    """Pruebas para el modelo Escena."""

    def setUp(self):
        """Configura datos de prueba antes de cada test."""
        self.escena = Escena.objects.create(
            nombre="Test Scene",
            descripcion="Esta es una escena de prueba.",
            archivo=SimpleUploadedFile("modelo.glb", b"contenido_fake", content_type="model/gltf-binary"),
        )

    def test_creacion_escena(self):
        """Verifica que la escena se crea correctamente."""
        self.assertEqual(self.escena.nombre, "Test Scene")
        self.assertEqual(self.escena.descripcion, "Esta es una escena de prueba.")

    def test_str_method(self):
        """Verifica que el método __str__ devuelve el nombre."""
        self.assertEqual(str(self.escena), "Test Scene")

class EscenaAPITest(TestCase):
    """Pruebas para la API de escenas."""

    def test_api_crear_escena(self):
        """Verifica que se puede crear una escena a través de la API."""
        response = self.client.post('/api/escenas/', {
            'nombre': "Nueva Escena",
            'descripcion': "Descripción de prueba",
        })
        self.assertEqual(response.status_code, 201)  # Debe retornar HTTP 201 Created

# from django.test import TestCase # type: ignore

# Create your tests here.
