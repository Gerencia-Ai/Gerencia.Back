from rest_framework.serializers import ModelSerializer

from fabrica.models.comentario import Comentario

class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'