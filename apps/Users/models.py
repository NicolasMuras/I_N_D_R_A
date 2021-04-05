from django.db import models
from apps.Tags.models import Tag



class User(models.Model):
    name = models.CharField(
        max_length=200, verbose_name="Nombre", blank=False, null=False
        )
    password = models.CharField(
        max_length=200, verbose_name="Contraseña", blank=False, null=False
        )
    tags = models.ForeignKey(
        Tag, on_delete=models.CASCADE, blank=True, null=True, related_name='user_tags'
        )
  
    class Meta:
        verbose_name = "User"
        
    def __str__(self):
        return self.name