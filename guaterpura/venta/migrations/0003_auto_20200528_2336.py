# Generated by Django 2.2.7 on 2020-05-29 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0002_auto_20200525_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha_a',
            field=models.DateField(auto_now_add=True, unique=True, verbose_name='Fecha Apertura'),
        ),
    ]
