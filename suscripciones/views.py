from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Funcionalidad, Subscripcion
from .serializers import (
    FuncionalidadSerializer,
    SubscripcionSerializer
)

class FuncionalidadView(ModelViewSet):
    """Vista para listar y crear funcionalidades.

    Esta vista hereda de ModelViewSet y define los atributos queryset, serializer_class,
    permission_classes y authentication_class para listar y crear funcionalidades.

    Atributos:
        queryset: QuerySet que define los objetos a listar.
        serializer_class: Clase serializer para serializar y deserializar los datos.
        permission_classes: Tupla de clases de permisos para restringir el acceso a la vista.
        authentication_class: Tupla de clases de autenticación para autenticar las solicitudes.
    """
    queryset = Funcionalidad.objects.all()
    serializer_class = FuncionalidadSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

class SubscripcionView(ModelViewSet):
    """Vista para listar y crear suscripciones.

    Esta vista hereda de ModelViewSet y define los atributos queryset, serializer_class,
    permission_classes y authentication_class para listar y crear suscripciones.

    Atributos:
        queryset: QuerySet que define los objetos a listar.
        serializer_class: Clase serializer para serializar y deserializar los datos.
        permission_classes: Tupla de clases de permisos para restringir el acceso a la vista.
        authentication_class: Tupla de clases de autenticación para autenticar las solicitudes.
    """
    queryset = Subscripcion.objects.all()
    serializer_class = SubscripcionSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
