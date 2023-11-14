from django import forms
from . import models

class ProductosForm(forms.ModelForm):
    class Meta:
        model = models.Productos
        fields = ["nombre", "precio", "cantidad", "fecha_ingreso", "categoria", "imagen"]

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = models.Categoria
        fields = "__all__"