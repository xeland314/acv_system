from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Funcionalidad, Subscripcion
from .serializers import (
    FuncionalidadSerializer,
    SubscripcionSerializer
)

class FuncionalidadView(ModelViewSet):
    """Vista para listar y crear funcionalidades."""
    queryset = Funcionalidad.objects.all()
    serializer_class = FuncionalidadSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

class SubscripcionView(ModelViewSet):
    """Vista para listar y crear suscripciones."""
    queryset = Subscripcion.objects.all()
    serializer_class = SubscripcionSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
