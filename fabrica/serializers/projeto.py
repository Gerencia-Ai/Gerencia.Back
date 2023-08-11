from rest_framework.serializers import ModelSerializer

from fabrica.models.projeto import Projeto

class ProjetoSerializer(ModelSerializer):
    class Meta:
        model = Projeto
        fields = '__all__'