# Generated by Django 3.1 on 2022-06-09 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20220607_0219'),
    ]

    operations = [
        migrations.AddField(
            model_name='flor',
            name='imagenFlor',
            field=models.CharField(default=0, max_length=300, verbose_name='Imagen flor'),
            preserve_default=False,
        ),
    ]
