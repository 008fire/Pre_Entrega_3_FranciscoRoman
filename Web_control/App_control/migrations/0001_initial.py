# Generated by Django 4.2.3 on 2023-07-27 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('marca', models.CharField(max_length=64)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=256)),
                ('nombre', models.CharField(max_length=256)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('telefono', models.CharField(blank=True, max_length=20)),
                ('dni', models.CharField(max_length=32)),
                ('fecha_nacimiento', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=256)),
                ('ubicación', models.CharField(max_length=256)),
                ('habilitada', models.BooleanField(default=False)),
            ],
        ),
    ]
