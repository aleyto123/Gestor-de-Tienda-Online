from django.db import models


class Proveedor(models.Model):
    nombre = models.CharField(max_length=120)
    correo_contacto = models.EmailField(unique=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "proveedores"
        ordering = ["nombre"]
        verbose_name = "proveedor"
        verbose_name_plural = "proveedores"

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    proveedor = models.ForeignKey(
        Proveedor,
        related_name="productos",
        on_delete=models.CASCADE,
    )
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "productos"
        ordering = ["nombre"]
        verbose_name = "producto"
        verbose_name_plural = "productos"

    def __str__(self):
        return self.nombre

