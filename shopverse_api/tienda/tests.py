from decimal import Decimal

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Producto, Proveedor


class ProductoApiTests(APITestCase):
    def setUp(self):
        self.proveedor = Proveedor.objects.create(
            nombre="Distribuidora Lima",
            correo_contacto="ventas@lima.pe",
        )
        self.producto = Producto.objects.create(
            nombre="Laptop Lenovo",
            precio=Decimal("2500.00"),
            stock=8,
            proveedor=self.proveedor,
        )

    def test_lista_productos_con_datos_del_proveedor(self):
        respuesta = self.client.get(reverse("producto-list"))

        self.assertEqual(respuesta.status_code, status.HTTP_200_OK)
        self.assertEqual(respuesta.data[0]["nombre"], "Laptop Lenovo")
        self.assertEqual(respuesta.data[0]["proveedor_nombre"], "Distribuidora Lima")
        self.assertEqual(
            respuesta.data[0]["proveedor_detalle"]["correo_contacto"],
            "ventas@lima.pe",
        )

    def test_crea_producto(self):
        respuesta = self.client.post(
            reverse("producto-list"),
            {
                "nombre": "Mouse Gamer",
                "precio": "89.90",
                "stock": 20,
                "proveedor": self.proveedor.id,
            },
            format="json",
        )

        self.assertEqual(respuesta.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Producto.objects.filter(nombre="Mouse Gamer").exists())

    def test_actualiza_producto(self):
        respuesta = self.client.patch(
            reverse("producto-detail", args=[self.producto.id]),
            {"stock": 12},
            format="json",
        )

        self.assertEqual(respuesta.status_code, status.HTTP_200_OK)
        self.producto.refresh_from_db()
        self.assertEqual(self.producto.stock, 12)

    def test_elimina_producto(self):
        respuesta = self.client.delete(reverse("producto-detail", args=[self.producto.id]))

        self.assertEqual(respuesta.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Producto.objects.filter(id=self.producto.id).exists())

    def test_busca_producto_por_nombre_o_proveedor(self):
        respuesta = self.client.get(reverse("producto-list"), {"search": "lima"})

        self.assertEqual(respuesta.status_code, status.HTTP_200_OK)
        self.assertEqual(len(respuesta.data), 1)


class ProveedorApiTests(APITestCase):
    def test_crud_proveedor_y_productos_asociados(self):
        crear = self.client.post(
            reverse("proveedor-list"),
            {
                "nombre": "Importaciones Andinas",
                "correo_contacto": "contacto@andinas.pe",
            },
            format="json",
        )
        self.assertEqual(crear.status_code, status.HTTP_201_CREATED)

        proveedor_id = crear.data["id"]
        Producto.objects.create(
            nombre="Teclado Mecanico",
            precio=Decimal("150.00"),
            stock=5,
            proveedor_id=proveedor_id,
        )

        detalle = self.client.get(reverse("proveedor-detail", args=[proveedor_id]))
        self.assertEqual(detalle.status_code, status.HTTP_200_OK)
        self.assertEqual(detalle.data["productos"][0]["nombre"], "Teclado Mecanico")

        editar = self.client.put(
            reverse("proveedor-detail", args=[proveedor_id]),
            {
                "nombre": "Importaciones Andinas SAC",
                "correo_contacto": "contacto@andinas.pe",
            },
            format="json",
        )
        self.assertEqual(editar.status_code, status.HTTP_200_OK)

        eliminar = self.client.delete(reverse("proveedor-detail", args=[proveedor_id]))
        self.assertEqual(eliminar.status_code, status.HTTP_204_NO_CONTENT)

