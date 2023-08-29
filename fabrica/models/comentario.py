from django.db import models
from usuario.models import Usuario
from .post import Post


class Comentario(models.Model):
    texto = models.CharField(max_length=200)
    data = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, related_name="comentarios", on_delete=models.PROTECT)
    post = models.ForeignKey(Post, related_name="comentarios", on_delete=models.PROTECT) 
    
    def __str__(self):
        return self.texto