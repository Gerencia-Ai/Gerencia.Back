from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from fabrica.models.tipos_usuarios import TiposUsuarios
from fabrica.serializers.tipos_usuarios import TiposUsuariosSerializer

class TiposUsuariosViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = TiposUsuarios.objects.all()
    serializer_class = TiposUsuariosSerializer
    