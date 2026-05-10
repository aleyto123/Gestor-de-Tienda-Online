from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProductoViewSet, ProveedorViewSet

router = DefaultRouter()
router.register("productos", ProductoViewSet, basename="producto")
router.register("proveedores", ProveedorViewSet, basename="proveedor")

urlpatterns = [
    path("", include(router.urls)),
]

