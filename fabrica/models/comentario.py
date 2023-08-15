from django.db import models
from usuario.models import Usuario
from .post import Post


class Comentario(models.Model):
    texto = models.CharField(max_length=200)
    data = models.DateTimeField(auto_now_add=True)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name="comentarios")
    post_id = models.ForeignKey(Post, on_delete=models.PROTECT, related_name="comentarios")
    
    
    def __str__(self):
        return self.texto