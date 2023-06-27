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

from .models import Empresa, Representante, Trabajador
from .serializers import EmpresaSerializer, RepresentanteSerializer, TrabajadorSerializer

class TrabajadorView(ModelViewSet):
    """Vista para listar y crear usuarios.

    Esta vista hereda de ModelViewSet y define los atributos queryset, serializer_class,
    permission_classes y authentication_class para listar y crear usuarios.

    Atributos:
        queryset: QuerySet que define los objetos a listar.
        serializer_class: Clase serializer para serializar y deserializar los datos.
        permission_classes: Tupla de clases de permisos para restringir el acceso a la vista.
        authentication_class: Tupla de clases de autenticación para autenticar las solicitudes.
    """

    queryset = Trabajador.objects.all()
    serializer_class = TrabajadorSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)


class EmpresaView(ModelViewSet):
    """Vista para listar y crear empresas.

    Esta vista hereda de ModelViewSet y define los atributos queryset, serializer_class,
    permission_classes y authentication_class para listar y crear empresas.

    Atributos:
        queryset: QuerySet que define los objetos a listar.
        serializer_class: Clase serializer para serializar y deserializar los datos.
        permission_classes: Tupla de clases de permisos para restringir el acceso a la vista.
        authentication_class: Tupla de clases de autenticación para autenticar las solicitudes.
    """
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

class RepresentanteView(ModelViewSet):
    """Vista para listar y crear representantes.

    Esta vista hereda de ModelViewSet y define los atributos queryset, serializer_class,
    permission_classes y authentication_class para listar y crear representantes.

    Atributos:
        queryset: QuerySet que define los objetos a listar.
        serializer_class: Clase serializer para serializar y deserializar los datos.
        permission_classes: Tupla de clases de permisos para restringir el acceso a la vista.
        authentication_class: Tupla de clases de autenticación para autenticar las solicitudes.
    """
    queryset = Representante.objects.all()
    serializer_class = RepresentanteSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
