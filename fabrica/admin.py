from django.contrib import admin

from fabrica.models import Comentario, Projeto, MembrosProjeto

admin.site.register(Comentario)
admin.site.register(Projeto)
admin.site.register(MembrosProjeto)

