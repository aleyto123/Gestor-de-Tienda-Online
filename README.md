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
