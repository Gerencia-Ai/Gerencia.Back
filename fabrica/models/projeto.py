from django.db import models
from usuario.models import Usuario
from uploader.models import Image


class Projeto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=2500)
    data = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='images/', null=True, blank=True)  
    professor = models.ForeignKey(Usuario, related_name='professor', on_delete=models.PROTECT) 
    alunos = models.ManyToManyField(Usuario, related_name='alunos') 
    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
    
    def __str__(self):
        return self.nome