from django.db import models
from apps.Tags.models import Tag



class User(models.Model):
    name = models.CharField(
        max_length=200, verbose_name="Nombre", blank=True, null=True
        )
    passsword = models.CharField(
        max_length=200, verbose_name="Contraseña", blank=True, null=True
        )
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        verbose_name = "Users"
        
    def __str__(self):
        return self.name