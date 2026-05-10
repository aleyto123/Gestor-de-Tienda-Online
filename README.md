# Shopverse API

AUTOR: Bellido Chambi Rony Widmer

API REST para un gestor de tienda online. El proyecto se desarrollara por partes usando Django y Django REST Framework.

## Parte 1: estructura inicial

En esta primera parte se creo la estructura base del proyecto `shopverse_api`.

## Parte 2: modelos de datos

Se agregaron los modelos principales del sistema:

- `Proveedor`: guarda `nombre` y `correo_contacto`.
- `Producto`: guarda `nombre`, `precio`, `stock` y su relacion con un `Proveedor`.

Tambien se agrego la migracion inicial para crear las tablas `proveedores` y `productos`.

## Parte 3: serializers

Se agregaron los serializers de Django REST Framework:

- `ProveedorSerializer`: muestra los datos del proveedor y sus productos asociados.
- `ProductoSerializer`: muestra los datos del producto, el id del proveedor y datos adicionales del proveedor.

La respuesta de productos incluye `proveedor_nombre` y `proveedor_detalle` para que el JSON sea mas claro al probar en Postman.

## Parte 4: vistas REST

Se agregaron las vistas principales usando `ModelViewSet` de Django REST Framework:

- `ProductoViewSet`: prepara el CRUD de productos y permite buscar por `nombre` o por el nombre del proveedor.
- `ProveedorViewSet`: prepara el CRUD de proveedores y permite buscar por `nombre` o `correo_contacto`.

Estas vistas usaran los serializers creados en la Parte 3. Las rutas se conectaran en la siguiente parte.

## Parte 5: rutas de la API

Se conectaron las rutas con `DefaultRouter` de Django REST Framework.

Endpoints disponibles desde esta parte:

- `GET /productos/`
- `POST /productos/`
- `GET /productos/{id}/`
- `PUT /productos/{id}/`
- `PATCH /productos/{id}/`
- `DELETE /productos/{id}/`
- `GET /proveedores/`
- `POST /proveedores/`
- `GET /proveedores/{id}/`
- `PUT /proveedores/{id}/`
- `PATCH /proveedores/{id}/`
- `DELETE /proveedores/{id}/`

Tambien se retiro la ruta del Django Admin para que la gestion se realice por la API REST.

## Tecnologias usadas

- Python
- Django
- Django REST Framework
- SQLite

## Como ejecutar el proyecto

Primero entra a la carpeta del proyecto:

```bash
cd shopverse_api
```

Luego instala las dependencias y ejecuta el servidor cuando el entorno virtual este preparado:

```bash
pip install -r requirements.txt
python manage.py runserver
```

Los endpoints se agregaran en las siguientes partes del desarrollo.
