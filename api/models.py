from django.db import models

class Producto(models.Model):
    sku = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    stock = models.IntegerField(default=100)

    def __str__(self):
        return f"{self.name} (SKU: {self.sku}) - Stock: {self.stock}"

    def agregar_stock(self, cantidad):
        """
        Agrega la cantidad especificada al stock del producto.
        """
        self.stock += cantidad
        self.save()

    def reducir_stock(self, cantidad):
        """
        Reduce la cantidad especificada del stock del producto.
        Si la cantidad a reducir es mayor que el stock disponible,
        lanza una excepción.
        """
        if cantidad > self.stock:
            raise ValueError("No hay suficiente stock disponible.")
        self.stock -= cantidad
        self.save()


class Orden(models.Model):
    productos = models.ManyToManyField(Producto)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Orden {self.id} - Fecha: {self.fecha_creacion.strftime('%Y-%m-%d %H:%M')}"