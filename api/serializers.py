from rest_framework import serializers
from .models import Orden, Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'sku', 'name', 'stock']

class OrdenSerializer(serializers.ModelSerializer):
    productos = ProductoSerializer(many=True, read_only=True)

    class Meta:
        model = Orden
        fields = ['id', 'productos', 'fecha_creacion']