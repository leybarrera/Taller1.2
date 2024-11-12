# ventas/views.py

from django.shortcuts import render, get_object_or_404
from .models import Categoria, Producto, Cliente, Orden

# Vista para listar categorías
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'ventas/lista_categorias.html', {'categorias': categorias})

# Vista para listar productos
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'ventas/lista_productos.html', {'productos': productos})

# Vista para ver detalles de un producto
def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'ventas/detalle_producto.html', {'producto': producto})

# Vista para listar clientes
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'ventas/lista_clientes.html', {'clientes': clientes})

# Vista para listar órdenes
def lista_ordenes(request):
    ordenes = Orden.objects.all()
    return render(request, 'ventas/lista_ordenes.html', {'ordenes': ordenes})

# Vista para ver detalles de una orden
def detalle_orden(request, orden_id):
    orden = get_object_or_404(Orden, id=orden_id)
    return render(request, 'ventas/detalle_orden.html', {'orden': orden})
