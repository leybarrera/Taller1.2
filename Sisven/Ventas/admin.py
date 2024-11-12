# Ventas/admin.py
from django.contrib import admin
from .models import Categoria, Producto, Cliente, Orden

# Registra los modelos para que aparezcan en el panel de administración
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Orden)
