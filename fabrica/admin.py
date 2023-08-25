from django.contrib import admin

from fabrica.models import Comentario, Projeto, Post, Tarefa

admin.site.register(Comentario)
admin.site.register(Projeto)
admin.site.register(Post)
admin.site.register(Tarefa)

