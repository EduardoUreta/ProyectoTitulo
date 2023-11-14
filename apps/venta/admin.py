from django.contrib import admin

from . import models
# Register your models here.

@admin.register(models.Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ("vendedor", "producto", "cantidad", "precio_total","fecha_venta",)
    list_display_links = ("producto",)
    search_fields = ("productos.nombre", "vendedor",)
    list_filter =  ("vendedor",)
    date_hierarchy = "fecha_venta"

@admin.register(models.Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    ...
