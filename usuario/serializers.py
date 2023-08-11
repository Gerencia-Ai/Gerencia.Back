from rest_framework.serializers import ModelSerializer, SlugRelatedField

from .models import Usuario
from .models import TipoUsuario


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"

class TipoUsuarioSerializer(ModelSerializer):
    class Meta:
        model = TipoUsuario
        fields = "__all__"