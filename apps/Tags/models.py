from django.db import models



class Tag(models.Model):
    name = models.CharField(
        max_length=200, verbose_name="Nombre", blank=False, null=False
        )
    colour = models.CharField(
        max_length=200, verbose_name="Color", blank=False, null=False
        )
    hour = models.CharField(
        max_length=200, verbose_name="Hora", blank=False, null=False
        )
    day = models.CharField(
        max_length=200, verbose_name="Dia", blank=False, null=False
        )
    month = models.CharField(
        max_length=200, verbose_name="Mes", blank=False, null=False
        )
    year = models.CharField(
        max_length=200, verbose_name="Año", blank=False, null=False
        )
    priority = models.CharField(
        max_length=200, verbose_name="Prioridad", blank=False, null=False
        )
    
    class Meta:
        verbose_name = "Tag"
    def __str__(self):
        return self.name