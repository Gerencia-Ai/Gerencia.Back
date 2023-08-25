from django.db import models
from usuario.models import Usuario


class Projeto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=2500)
    data = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='images/', null=True, blank=True)  
    professor = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='professor') 
    alunos = models.ManyToManyField(Usuario, on_delete=models.PROTECT, related_name='alunos') 
    
    def __str__(self):
        return self.nome