from django.db import models

class Articulos(models.Model):
    # los atributos de clase (son las columnas de la tabla)
    nombre = models.CharField(max_length=64)
    marca = models.CharField(max_length=64)
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.nombre},{self.marca}, {self.precio}"


class Cliente(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    dni = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField(null=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"


#class Profesor(models.Model):
#    apellido = models.CharField(max_length=256)
#    nombre = models.CharField(max_length=256)
#    dni = models.CharField(max_length=32)
#    email = models.EmailField(blank=True)
#    fecha_nacimiento = models.DateField(null=True, blank=True)
#    profesion = models.CharField(max_length=128)
#    bio = models.TextField(blank=True)

#    def __str__(self):
#        return f"{self.apellido}, {self.nombre}"


class delivery(models.Model):
    nombre = models.CharField(max_length=256)
    ubicación = models.CharField(max_length=256)
    habilitada = models.BooleanField(default=False) 
    def __str__(self):
        return f"{self.nombre}"
