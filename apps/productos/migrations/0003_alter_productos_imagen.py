# Generated by Django 4.2.2 on 2023-07-12 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_productos_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='imagen',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
