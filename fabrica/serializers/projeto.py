from rest_framework.serializers import ModelSerializer, SlugRelatedField

from fabrica.models.projeto import Projeto
from uploader.models import Image
from uploader.serializers import ImageSerializer
        
class ProjetoDetailSerializer(ModelSerializer):
    capa = ImageSerializer(required=False)
    class Meta:
        model = Projeto
        fields = '__all__'
        depth = 1

class ProjetoListSerializer(ModelSerializer):
    class Meta:
        model = Projeto
        fields = '__all__'
        depth = 1

class ProjetoSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)
    class Meta:
        model = Projeto
        fields = '__all__'