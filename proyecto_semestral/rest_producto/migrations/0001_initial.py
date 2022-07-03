# Generated by Django 3.2.13 on 2022-07-03 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Producto')),
                ('nombreProducto', models.CharField(max_length=200, verbose_name='Nombre de Producto')),
                ('precioProducto', models.FloatField()),
                ('digital', models.BooleanField(blank=True, default=False, null=True)),
                ('imagenProducto', models.CharField(blank=True, max_length=300, null=True, verbose_name='Imagen Producto')),
            ],
        ),
    ]
