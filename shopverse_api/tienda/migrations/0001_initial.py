from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Proveedor",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nombre", models.CharField(max_length=120)),
                ("correo_contacto", models.EmailField(max_length=254, unique=True)),
                ("creado_en", models.DateTimeField(auto_now_add=True)),
                ("actualizado_en", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "proveedor",
                "verbose_name_plural": "proveedores",
                "db_table": "proveedores",
                "ordering": ["nombre"],
            },
        ),
        migrations.CreateModel(
            name="Producto",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nombre", models.CharField(max_length=150)),
                ("precio", models.DecimalField(decimal_places=2, max_digits=10)),
                ("stock", models.PositiveIntegerField(default=0)),
                ("creado_en", models.DateTimeField(auto_now_add=True)),
                ("actualizado_en", models.DateTimeField(auto_now=True)),
                (
                    "proveedor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="productos",
                        to="tienda.proveedor",
                    ),
                ),
            ],
            options={
                "verbose_name": "producto",
                "verbose_name_plural": "productos",
                "db_table": "productos",
                "ordering": ["nombre"],
            },
        ),
    ]

