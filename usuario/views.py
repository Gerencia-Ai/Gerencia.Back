from rest_framework.viewsets import ModelViewSet

from .models import Usuario
from .serializers import UsuarioSerializer

from .models import TipoUsuario
from .serializers import TipoUsuarioSerializer


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class TipoUsuarioViewSet(ModelViewSet):
    queryset = TipoUsuario.objects.all()
    serializer_class = TipoUsuarioSerializer