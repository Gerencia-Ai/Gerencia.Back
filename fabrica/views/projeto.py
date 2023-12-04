from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from fabrica.models.projeto import Projeto
from fabrica.serializers.projeto import ProjetoSerializer, ProjetoDetailSerializer, ProjetoListSerializer

class ProjetoViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Projeto.objects.all()
    def get_serializer_class(self):
        if self.action == "list":
            return ProjetoListSerializer
        elif self.action == "retrieve":
            return ProjetoDetailSerializer
        return ProjetoSerializer