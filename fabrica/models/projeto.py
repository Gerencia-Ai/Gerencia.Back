from django.db import models
from django.contrib.auth.models import Group
from usuario.models import Usuario


class Projeto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=2500)
    data = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='images/', null=True, blank=True)
    grupo_id = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    
    
    def __str__(self):
        return self.nome