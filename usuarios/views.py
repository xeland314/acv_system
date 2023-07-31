"""views.py

Este módulo define la vista PerfilView para listar y crear usuarios.

Autor: Christopher Villamarín (@xeland314)
"""
import coreapi
import coreschema
from django.utils.translation import gettext_lazy as _
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from .models import PerfilUsuario
from .serializers import PerfilSerializer

class UserFilterSchema(AutoSchema):

    def get_description(self, path, method):
        """
        Devuelve una descripción personalizada para la vista.
        """
        if path == '/usuarios/api/v1/perfiles/filter_by_empresa_and_role/':
            return 'Filtra los perfiles de usuario por empresa y rol.'
        return super().get_description(path, method)

    def get_manual_fields(self, path, method):
        """
        Devuelve una lista de campos personalizados para la vista.
        """
        extra_fields = []

        if path == '/usuarios/api/v1/perfiles/filter_by_empresa_and_role/':
            extra_fields = [
                coreapi.Field(
                    name='empresa_id',
                    required=True,
                    location='query',
                    schema=coreschema.Integer(
                        title='Empresa ID',
                        description=_('El id de la empresa de este usuario.')
                    ),
                    description=_('El id de la empresa a filtrar.')
                ),
                coreapi.Field(
                    name='role',
                    required=True,
                    location='query',
                    schema=coreschema.String(
                        title='Rol',
                        description=_('Rol del usuario dentro de la empresa.')    
                    ),
                    description=_('El rol de los usuarios a filtrar.')
                )
            ]

        return super().get_manual_fields(path, method) + extra_fields

class PerfilView(ModelViewSet):
    """
    Perfiles de usuario
    """
    queryset = PerfilUsuario.objects.all()
    serializer_class = PerfilSerializer
    permission_classes =  [IsAuthenticated,]
    authentication_class = (TokenAuthentication,)

    @action(detail=False, methods=['get'], schema=UserFilterSchema())
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
            try:
                queryset = PerfilUsuario.objects.filter(empresa_id=empresa_id, role=role)
                serializer = PerfilSerializer(queryset, many=True)
                return Response(serializer.data)
            except PerfilUsuario.DoesNotExist:
                return Response(
                    {"error": _("No se ha encontrado ningún usuario con este rol en esta empresa")},
                    status=status.HTTP_404_NOT_FOUND
                )

        return Response(
            {"error": _("Parámetros de búsqueda incorrectos.")},
            status=status.HTTP_400_BAD_REQUEST
        )
