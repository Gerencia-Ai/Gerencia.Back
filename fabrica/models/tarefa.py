from django.db import models

from usuario.models import Usuario

class Tarefa(models.Model):
    professor = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='professor_tarefa')
    aluno = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='aluno_tarefa')
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=2500)
    anexos = models.FileField(upload_to='documents/', null=True, blank=True)
    imagens = models.ImageField(upload_to='images/', null=True, blank=True)
    data_criado = models.DateTimeField(auto_now_add=True)
    data_prazo = models.DateTimeField()
    data_inicio = models.DateTimeField(null=True, blank=True)
    data_fim = models.DateTimeField(null=True, blank=True)