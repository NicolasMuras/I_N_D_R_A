from django.db import models



class Tag(models.Model):
    name = models.CharField(
        max_length=200, verbose_name="Nombre", blank=True, null=True
        )
    colour = models.CharField(
        max_length=200, verbose_name="Color", blank=True, null=True
        )
    hour = models.CharField(
        max_length=200, verbose_name="Hora", blank=True, null=True
        )
    day = models.CharField(
        max_length=200, verbose_name="Dia", blank=True, null=True
        )
    month = models.CharField(
        max_length=200, verbose_name="Mes", blank=True, null=True
        )
    year = models.CharField(
        max_length=200, verbose_name="Año", blank=True, null=True
        )
    priority = models.CharField(
        max_length=200, verbose_name="Prioridad", blank=True, null=True
        )
    
    class Meta:
        verbose_name = "Tag"
    def __str__(self):
        return self.name