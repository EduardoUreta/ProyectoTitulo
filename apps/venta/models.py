from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from productos.views import enviar_notificacion_stock_bajo

from django.utils import timezone

# Create your models here.

class Vendedor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="vendedor")  
    celular = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to="avatars",blank=True, null=True)

    def __str__(self):
        return self.usuario.username

class Venta(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.DO_NOTHING)
    producto = models.ForeignKey("productos.Productos", on_delete=models.DO_NOTHING)
    cantidad = models.PositiveIntegerField()
    precio_total = models.PositiveIntegerField(editable=False)
    fecha_venta = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f'{self.producto.nombre}'
    
    class Meta:
        ordering = ("-fecha_venta",)


    def clean(self) -> None:
        if self.cantidad > self.producto.cantidad:
            raise ValidationError("La cantidad solicita es mayor al stock disponible")
        elif self.cantidad == 0:
            raise ValidationError("No puedes vender 0 productos")
        else: 
            self.producto.cantidad -= self.cantidad
            if self.producto.cantidad <= 10:
                enviar_notificacion_stock_bajo(self.producto)
        
    def save(self, *args, **kwargs):
        self.producto.save()
        self.precio_total = self.producto.precio * self.cantidad
        super(Venta, self).save(*args, **kwargs)


