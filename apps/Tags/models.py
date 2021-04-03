from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    colour = models.CharField(max_length=200, verbose_name="Color")
    hour = models.CharField(max_length=200, verbose_name="Hora")
    day = models.CharField(max_length=200, verbose_name="Dia")
    month = models.CharField(max_length=200, verbose_name="Mes")
    year = models.CharField(max_length=200, verbose_name="Año")
    priority = models.CharField(max_length=200, verbose_name="Prioridad")
    class Meta:
        verbose_name = "Tag"
    def __str__(self):
        return self.name