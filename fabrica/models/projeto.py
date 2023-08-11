from django.db import models
from usuario.models import Usuario
class Projeto(models.Model):
    nome = models.CharField(max_length=200)
    texto = models.CharField(max_length=2500)
    data = models.DateTimeField(auto_now_add=True)
    membros = models.ManyToManyField(Usuario, related_name="membros",)
    
    
    def __str__(self):
        return self.nome