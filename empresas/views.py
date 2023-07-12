"""views.py

Autor: Christopher Villamarín (@xeland314)
"""
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Empresa
from .serializers import EmpresaSerializer

class EmpresaView(ModelViewSet):
    """Vista para listar y crear empresas."""
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
