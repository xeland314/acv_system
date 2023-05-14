from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Persona
from .serializers import PersonaSerializer

class UsuarioView(ModelViewSet):
    """
    Clase que define la vista para listar y crear usuarios.
    """
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer 
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)
