"""views.py

Este módulo define la vista UsuarioView para listar y crear usuarios.

Autor: Christopher Villamarín (@xeland314)
Dependencias: rest_framework.authentication.TokenAuthentication,
    rest_framework.permissions.IsAuthenticated,
    rest_framework.viewsets.ModelViewSet,
    .models.Persona,
    .serializers.PersonaSerializer
"""

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Persona
from .serializers import PersonaSerializer

class UsuarioView(ModelViewSet):
    """Vista para listar y crear usuarios.

    Esta vista hereda de ModelViewSet y define los atributos queryset, serializer_class,
    permission_classes y authentication_class para listar y crear usuarios.

    Atributos:
        queryset: QuerySet que define los objetos a listar.
        serializer_class: Clase serializer para serializar y deserializar los datos.
        permission_classes: Tupla de clases de permisos para restringir el acceso a la vista.
        authentication_class: Tupla de clases de autenticación para autenticar las solicitudes.
    """

    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)
