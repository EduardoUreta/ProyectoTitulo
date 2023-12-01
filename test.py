import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import date

from apps.productos.models import Categoria, Productos

def crear_categoria_prueba():
    return Categoria.objects.create(
        nombre='Electrónicos',
        descripcion='Productos electrónicos',
        imagen=SimpleUploadedFile('test_image.jpg', b'content', content_type='image/jpeg')
    )
