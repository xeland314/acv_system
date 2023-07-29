"""views.py

Este módulo define la vista PerfilView para listar y crear usuarios.

Autor: Christopher Villamarín (@xeland314)
"""
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import PerfilUsuario
from .serializers import PerfilSerializer

class PerfilView(ModelViewSet):
    """
    Perfiles de usuario
    """
    queryset = PerfilUsuario.objects.all()
    serializer_class = PerfilSerializer
    permission_classes =  [IsAuthenticated,]
    authentication_class = (TokenAuthentication,)

    @action(detail=False, methods=['get'])
    def filter_by_empresa_and_role(self, request: Request):
        """Filtra los perfiles de usuario por empresa y rol.

        Args:
            request (Request): La petición HTTP con los parámetros de búsqueda.

        Returns:
            Response: Una respuesta HTTP con los datos serializados de los perfiles
            que coinciden con los criterios de búsqueda, o un mensaje de error si
            los parámetros son incorrectos.

        Raises:
            ValidationError: Si los parámetros de búsqueda no son válidos.
        """
        empresa_id = request.query_params.get('empresa_id')
        role = request.query_params.get('role')

        if empresa_id and role:
            queryset = PerfilUsuario.objects.filter(empresa_id=empresa_id, role=role)
            serializer = PerfilSerializer(queryset, many=True)
            return Response(serializer.data)

        return Response({"error": "Parámetros de búsqueda incorrectos."})
