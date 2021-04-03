from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=200)
    edad = models.IntegerField(unique=True)