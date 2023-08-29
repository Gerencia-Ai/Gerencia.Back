from rest_framework.serializers import ModelSerializer, CharField

from fabrica.models.comentario import Comentario

class ComentarioSerializer(ModelSerializer):
    usuario = CharField(source='usuario.email', read_only=True)
    class Meta:
        model = Comentario
        fields = '__all__'