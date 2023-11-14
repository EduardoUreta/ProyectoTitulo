from django.http import HttpResponse
from django.shortcuts import redirect, render
from carrito.cart import Carrito

from productos.models import Productos

from django.core.mail import send_mail
from django.shortcuts import render, redirect

def carrito(request):
    productos = Productos.objects.all()
    return render(request, "carrito/index.html",{"productos": productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Productos.objects.get(id=producto_id)
    carrito.agregar_prod(producto)
    return redirect("productos:index")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Productos.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("productos:index")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Productos.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("productos:index")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("productos:index")

def enviar_correo(request):
    if request.method == "POST":
        correo = request.POST.get("correo")  # Obtener la dirección de correo del formulario

        # Recopilar la información del carrito
        carrito_info = ""
        total = 0

        for key, value in request.session['carrito'].items():
            carrito_info += f"Producto: {value['nombre']}\n"
            carrito_info += f"Precio: ${value['precio']}\n"
            carrito_info += f"Cantidad: {value['cantidad']}\n"
            carrito_info += f"Subtotal: ${value['acumulado']}\n\n"
            
            # Sumar el subtotal al total
            total += value['acumulado']

        # Componer el cuerpo del correo
        mensaje = f"Tus productos escogidos son: \n\n{carrito_info} \n Total de tu reserva: ${total}"

        # Enviar el correo
        send_mail(
            "Detalles del carrito de compras - Minimarket Los Tios",
            mensaje,
            correo,  # Remitente
            [correo, "minimarket.lostios@gmail.com"],  # Destinatario
            fail_silently=False
        )

        carrito = Carrito(request)
        carrito.limpiar()

    return render(request, "carrito/confirmacion.html")
