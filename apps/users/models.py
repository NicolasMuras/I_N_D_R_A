from django.db import models
from apps.tags.models import Tag



class User(models.Model):
    name = models.CharField(
        max_length=200, verbose_name="Nombre", blank=False, null=False
        )
    password = models.CharField(
        max_length=200, verbose_name="Contraseña", blank=False, null=False
        )
    tags = models.ManyToManyField(Tag)
  
    class Meta:
        verbose_name = "User"
        
    def __str__(self):
        return self.name