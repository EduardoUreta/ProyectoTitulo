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

@pytest.mark.django_db
def test_categoria_creation():
    categoria = crear_categoria_prueba()
    assert categoria.nombre == 'Electrónicos'
    assert categoria.descripcion == 'Productos electrónicos'

@pytest.mark.django_db
def test_productos_creation():
    categoria = crear_categoria_prueba()
    producto = Productos.objects.create(
        nombre='Laptop',
        precio=1000,
        cantidad=50,
        fecha_ingreso=date.today(),
        categoria=categoria,
        umbral_minimo=10,
        imagen=SimpleUploadedFile('test_image.jpg', b'content', content_type='image/jpeg')
    )
    assert producto.nombre == 'Laptop'
    assert producto.precio == 1000
