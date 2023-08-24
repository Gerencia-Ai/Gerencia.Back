from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from fabrica.models.comentario import Comentario
from fabrica.serializers.comentario import ComentarioSerializer

class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    