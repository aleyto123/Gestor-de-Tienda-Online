from rest_framework import serializers

from .models import Producto, Proveedor


class ProductoResumenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ["id", "nombre", "precio", "stock"]


class ProveedorSerializer(serializers.ModelSerializer):
    productos = ProductoResumenSerializer(many=True, read_only=True)

    class Meta:
        model = Proveedor
        fields = [
            "id",
            "nombre",
            "correo_contacto",
            "productos",
            "creado_en",
            "actualizado_en",
        ]
        read_only_fields = ["creado_en", "actualizado_en"]


class ProveedorDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ["id", "nombre", "correo_contacto"]


class ProductoSerializer(serializers.ModelSerializer):
    proveedor_detalle = ProveedorDetalleSerializer(source="proveedor", read_only=True)
    proveedor_nombre = serializers.CharField(source="proveedor.nombre", read_only=True)

    class Meta:
        model = Producto
        fields = [
            "id",
            "nombre",
            "precio",
            "stock",
            "proveedor",
            "proveedor_nombre",
            "proveedor_detalle",
            "creado_en",
            "actualizado_en",
        ]
        read_only_fields = ["creado_en", "actualizado_en"]

