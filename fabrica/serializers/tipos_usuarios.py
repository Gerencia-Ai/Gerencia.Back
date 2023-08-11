from rest_framework.serializers import ModelSerializer

from fabrica.models.tipos_usuarios import TiposUsuarios

class TiposUsuariosSerializer(ModelSerializer):
    class Meta:
        model = TiposUsuarios
        fields = '__all__'