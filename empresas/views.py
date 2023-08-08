"""views.py

Autor: Christopher Villamarín (@xeland314)
"""
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Empresa, Funcionalidad, Suscripcion
from .serializers import EmpresaSerializer, FuncionalidadSerializer, SuscripcionSerializer

class FuncionalidadView(ModelViewSet):
    """Vista para listar y crear funcionalidades."""
    queryset = Funcionalidad.objects.all()
    serializer_class = FuncionalidadSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

class SuscripcionView(ModelViewSet):
    """Vista para listar y crear suscripciones."""
    queryset = Suscripcion.objects.all()
    serializer_class = SuscripcionSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class EmpresaView(ModelViewSet):
    """Vista para listar y crear empresas."""
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
