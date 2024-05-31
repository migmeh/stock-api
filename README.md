# stock-api

## Usar POST Para el endpoint /api/products

Ejemplo de uso del endpoint /api/products (POST) para crear un nuevo producto: Supongamos que quieres crear un producto con el SKU “ABC123” y el nombre “Producto Ejemplo”. Enviarías una solicitud POST a /api/products con el siguiente cuerpo JSON:

```
{
  "sku": "ABC123",
  "name": "Producto Ejemplo"
}
```
Si la solicitud es exitosa, recibirías una respuesta con el código de estado HTTP 201 (Created), junto con el cuerpo del producto recién creado, incluyendo el stock inicial de 100:



### Usar PATCH Para el endpoint /api/inventories/product/{PRODUCT_ID} 

Ejemplo de uso del endpoint /api/inventories/product/{PRODUCT_ID} (PATCH) para agregar stock al producto: Si deseas agregar, por ejemplo, 50 unidades más al stock de un producto con ID 1, enviarías una solicitud PATCH a /api/inventories/product/2 con el siguiente cuerpo JSON:

```

{
  "stock": 50
}
```

### Usar POST Para el endpoint /api/orders

Para probar este endpoint, enviarías una solicitud POST a /api/orders con un cuerpo JSON como el siguiente:

```

{
  "productos": [
    {
      "id": 1,
      "cantidad": 2
    },
    {
      "id": 3,
      "cantidad": 1
    }
  ]
}
```

###Documentacion


para acceder a ala documentacion de swagger

```
http://127.0.0.1:7000/swagger/
```
para acceder a ala documentacion de redoc

```
http://127.0.0.1:7000/redoc/
```
