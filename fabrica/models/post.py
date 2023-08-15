from django.db import models

from .projeto import Projeto

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.CharField(max_length=2500)
    projeto_id = models.ForeignKey(Projeto, on_delete=models.PROTECT, related_name="posts")
    
    def __str__(self):
        return self.titulo

