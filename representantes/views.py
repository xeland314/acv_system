"""views.py

Autor: Christopher Villamarín (@xeland314)
"""
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Representante
from .serializers import RepresentanteSerializer

class RepresentanteView(ModelViewSet):
    """Vista para listar y crear representantes."""
    queryset = Representante.objects.all()
    serializer_class = RepresentanteSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
