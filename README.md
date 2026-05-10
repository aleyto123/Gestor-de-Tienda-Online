# Shopverse API

AUTOR: Bellido Chambi Rony Widmer

## Descripcion

Shopverse API es una API REST para administrar una tienda online. Permite gestionar productos y proveedores usando Django y Django REST Framework.

Cada producto pertenece a un proveedor. La gestion se realiza mediante endpoints REST, sin usar Django Admin como interfaz de gestion.

## Tecnologias usadas

- Python
- Django
- Django REST Framework
- SQLite
- Git y GitHub

## Historial de desarrollo por partes

| Parte | Avance |
| --- | --- |
| Parte 1 | Estructura inicial del proyecto `shopverse_api`. |
| Parte 2 | Modelos `Producto` y `Proveedor`, con migracion inicial. |
| Parte 3 | Serializers para productos y proveedores. |
| Parte 4 | Vistas REST con `ModelViewSet`. |
| Parte 5 | Rutas de la API con `DefaultRouter`. |
| Parte 6 | Pruebas de endpoints con `APITestCase`. |
| Parte 7 | Documentacion final del README. |

## Instrucciones para ejecutar el servidor

Clonar el repositorio:

```bash
git clone https://github.com/aleyto123/Gestor-de-Tienda-Online.git
cd Gestor-de-Tienda-Online/shopverse_api
```

Crear y activar el entorno virtual:

```bash
python3 -m venv venv
.\venv\Scripts\activate
```

Si tu instalacion de Python usa el comando `python` en lugar de `python3`, puedes reemplazar `python3` por `python` en los comandos.

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar migraciones:

```bash
python3 manage.py migrate
```

Iniciar el servidor:

```bash
python3 manage.py runserver
```

La API estara disponible en:

```text
http://127.0.0.1:8000/
```

## Ejecutar pruebas

Desde la carpeta `shopverse_api`:

```bash
python3 manage.py test
```

## Endpoints disponibles

### Productos

| Accion | Metodo | Endpoint |
| --- | --- | --- |
| Listar productos | GET | `/productos/` |
| Crear producto | POST | `/productos/` |
| Ver producto | GET | `/productos/{id}/` |
| Actualizar producto completo | PUT | `/productos/{id}/` |
| Actualizar producto parcial | PATCH | `/productos/{id}/` |
| Eliminar producto | DELETE | `/productos/{id}/` |
| Buscar producto | GET | `/productos/?search=texto` |

### Proveedores

| Accion | Metodo | Endpoint |
| --- | --- | --- |
| Listar proveedores | GET | `/proveedores/` |
| Crear proveedor | POST | `/proveedores/` |
| Ver proveedor | GET | `/proveedores/{id}/` |
| Actualizar proveedor completo | PUT | `/proveedores/{id}/` |
| Actualizar proveedor parcial | PATCH | `/proveedores/{id}/` |
| Eliminar proveedor | DELETE | `/proveedores/{id}/` |
| Buscar proveedor | GET | `/proveedores/?search=texto` |

## Ejemplos de uso con curl

Crear proveedor:

```bash
curl -X POST http://127.0.0.1:8000/proveedores/ -H "Content-Type: application/json" -d "{\"nombre\":\"Distribuidora Lima\",\"correo_contacto\":\"ventas@lima.pe\"}"
```

Listar proveedores:

```bash
curl http://127.0.0.1:8000/proveedores/
```

Crear producto:

```bash
curl -X POST http://127.0.0.1:8000/productos/ -H "Content-Type: application/json" -d "{\"nombre\":\"Laptop Lenovo\",\"precio\":\"2500.00\",\"stock\":8,\"proveedor\":1}"
```

Listar productos:

```bash
curl http://127.0.0.1:8000/productos/
```

Buscar producto:

```bash
curl "http://127.0.0.1:8000/productos/?search=laptop"
```

Actualizar producto:

```bash
curl -X PATCH http://127.0.0.1:8000/productos/1/ -H "Content-Type: application/json" -d "{\"stock\":12}"
```

Eliminar producto:

```bash
curl -X DELETE http://127.0.0.1:8000/productos/1/
```

## Ejemplo de respuesta personalizada

Al listar productos, la respuesta incluye informacion del proveedor asociado:

```json
{
  "id": 1,
  "nombre": "Laptop Lenovo",
  "precio": "2500.00",
  "stock": 8,
  "proveedor": 1,
  "proveedor_nombre": "Distribuidora Lima",
  "proveedor_detalle": {
    "id": 1,
    "nombre": "Distribuidora Lima",
    "correo_contacto": "ventas@lima.pe"
  },
  "creado_en": "2026-05-09T20:00:00-05:00",
  "actualizado_en": "2026-05-09T20:00:00-05:00"
}
```

## Notas para Postman

Antes de crear un producto, primero se debe crear un proveedor. Luego se usa el `id` del proveedor en el campo `proveedor`.

Campos para crear proveedor:

```json
{
  "nombre": "Distribuidora Lima",
  "correo_contacto": "ventas@lima.pe"
}
```

Campos para crear producto:

```json
{
  "nombre": "Laptop Lenovo",
  "precio": "2500.00",
  "stock": 8,
  "proveedor": 1
}
```
