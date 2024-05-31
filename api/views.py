from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Producto, Orden
from .serializers import ProductoSerializer, OrdenSerializer

@api_view(['POST'])
def create_product(request):
    """
    Crea un nuevo producto con SKU y nombre.
    """
    serializer = ProductoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def update_inventory(request, product_id):
    """
    Actualiza el stock de un producto específico.
    """
    try:
        producto = Producto.objects.get(pk=product_id)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if 'stock' in request.data:
        producto.stock += int(request.data['stock'])
        producto.save()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_order(request):
    """
    Crea una orden de compra de productos.
    """
    # Suponiendo que 'productos' es una lista de diccionarios con 'id' y 'cantidad'
    productos_data = request.data.get('productos')
    if not productos_data:
        return Response({'error': 'No se proporcionaron productos.'}, status=status.HTTP_400_BAD_REQUEST)

    orden = Orden.objects.create()
    for producto_data in productos_data:
        try:
            producto = Producto.objects.get(id=producto_data['id'])
            if producto.stock < producto_data['cantidad']:
                return Response({'error': f"Stock insuficiente para el producto {producto.name}."}, status=status.HTTP_400_BAD_REQUEST)
            producto.reducir_stock(producto_data['cantidad'])
            orden.productos.add(producto)
        except Producto.DoesNotExist:
            return Response({'error': 'Producto no encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            return Response({'error': 'Formato de datos incorrecto.'}, status=status.HTTP_400_BAD_REQUEST)

    orden_serializer = OrdenSerializer(orden)
    return Response(orden_serializer.data, status=status.HTTP_201_CREATED)

# Función para verificar el stock y disparar una alerta
def check_stock():
    """
    Verifica el stock de todos los productos y dispara una alerta si es necesario.
    """
    productos_con_bajo_stock = Producto.objects.filter(stock__lt=10)
    for producto in productos_con_bajo_stock:
        print(f"Alerta: El stock del producto {producto.name} (SKU: {producto.sku}) es bajo.")
