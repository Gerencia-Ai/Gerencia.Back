from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from fabrica.models.tarefa import Tarefa
from fabrica.serializers.tarefa import TarefaSerializer

class TarefaViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    