from rest_framework import viewsets

from .models import Producto, Proveedor
from .serializers import ProductoSerializer, ProveedorSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.select_related("proveedor").all()
    serializer_class = ProductoSerializer
    search_fields = ["nombre", "proveedor__nombre"]


class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.prefetch_related("productos").all()
    serializer_class = ProveedorSerializer
    search_fields = ["nombre", "correo_contacto"]

