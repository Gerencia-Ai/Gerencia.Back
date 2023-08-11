from django.db import models

from .projeto import Projeto
from usuario.models import Usuario
from usuario.models import TipoUsuario

class TiposUsuarios(models.Model):
    usuario_id = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name="membros_projeto",)
    tipo_usuario_id = models.ForeignKey(TipoUsuario, on_delete=models.PROTECT, related_name="tipo_usuario_id",)
    
    def __str__(self):
        return str(self.projeto_id) + " | " + str(self.usuario_id)