"""views.py

Este módulo define la vista PerfilView para listar y crear usuarios.

Autor: Christopher Villamarín (@xeland314)
"""
from django.contrib.auth.models import Group
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import PerfilUsuario
from .serializers import PerfilSerializer, GroupSerializer

class PerfilView(ModelViewSet):
    """
    Perfiles de usuario
    """
    queryset = PerfilUsuario.objects.all()
    serializer_class = PerfilSerializer
    permission_classes =  [IsAuthenticated,]
    authentication_class = (TokenAuthentication,)

class GroupView(ModelViewSet):
    permission_classes = [IsAuthenticated,]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
