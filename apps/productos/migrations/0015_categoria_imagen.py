# Generated by Django 4.2.2 on 2023-07-31 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0014_alter_productos_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imgprod'),
        ),
    ]
