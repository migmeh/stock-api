from django.contrib import admin

# Register your models here.

from .models import Producto, Orden
admin.site.register(Producto)
admin.site.register(Orden)
