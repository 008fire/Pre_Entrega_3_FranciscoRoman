# Generated by Django 4.2.3 on 2023-07-31 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_control', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='delivery',
            old_name='habilitada',
            new_name='habilitado',
        ),
        migrations.RenameField(
            model_name='delivery',
            old_name='ubicación',
            new_name='ubicacion',
        ),
        migrations.AlterField(
            model_name='articulos',
            name='precio',
            field=models.IntegerField(null=True),
        ),
    ]
