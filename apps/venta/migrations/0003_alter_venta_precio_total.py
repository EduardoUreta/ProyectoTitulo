# Generated by Django 4.2.2 on 2023-11-26 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0002_remove_venta_cantidad_remove_venta_producto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='precio_total',
            field=models.PositiveIntegerField(editable=False, null=True),
        ),
    ]
