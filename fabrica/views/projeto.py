from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from fabrica.models.projeto import Projeto
from fabrica.serializers.projeto import ProjetoSerializer

class ProjetoViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer
    