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
    date = models.DateField(verbose_name="Fecha")
    priority = models.CharField(
        max_length=200, verbose_name="Prioridad", blank=False, null=False
        )
    
    class Meta:
        verbose_name = "Tag"
    def __str__(self):
        return self.name