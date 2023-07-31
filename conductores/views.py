import coreapi
import coreschema
from django.utils.translation import gettext_lazy as _
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema

from .serializers import ConductorSerializer, LicenciaSerializer
from .models import Conductor, Licencia

class ConductorFilterSchema(AutoSchema):

    def get_description(self, path, method):
        if path == '/conductores/api/v1/conductores/filter_by_empresa_and_role/':
            return 'Filtra los perfiles de usuario por empresa y rol.'
        return super().get_description(path, method)

    def get_manual_fields(self, path, method):
        extra_fields = []

        if path == '/conductores/api/v1/conductores/filter_by_empresa_and_role/':
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

class ConductorView(viewsets.ModelViewSet):
    """
    Clase que define la vista para listar y crear conductores.
    """
    queryset = Conductor.objects.all()
    serializer_class = ConductorSerializer

    @action(detail=False, methods=['get'], schema=ConductorFilterSchema())
    def filter_by_empresa_and_role(self, request: Request):
        """
        Filtra los conductores por empresa y rol.

        Esta función filtra los conductores en la base de datos que pertenecen a la empresa
        y tienen el rol especificado en los parámetros de consulta `empresa_id` y `role`
        de la petición HTTP.

        Args:
            request (Request): La petición HTTP con los parámetros de búsqueda.

        Returns:
            Response: Una respuesta HTTP con los datos serializados de los conductores
            que pertenecen a la empresa y tienen el rol especificado, o un mensaje de error
            si no se encontraron conductores o si los parámetros de búsqueda son incorrectos.
        """
        empresa_id = request.query_params.get('empresa_id')
        role = request.query_params.get('role')

        if empresa_id and role:
            try:
                conductores = Conductor.objects.filter(empresa_id=empresa_id, role=role)
                serializer = ConductorSerializer(conductores, many=True)
                return Response(serializer.data)
            except Conductor.DoesNotExist:
                return Response(
                    {"error": "No se encontraron conductores para la empresa y rol especificados."},
                    status=status.HTTP_404_NOT_FOUND
                )

        return Response(
            {"error": "Parámetros de búsqueda incorrectos. Se requiere empresa_id y role."},
            status=status.HTTP_400_BAD_REQUEST
        )

class LicenciaView(viewsets.ModelViewSet):
    """
    Clase que define la vista para listar y crear licencias.
    """
    queryset = Licencia.objects.all()
    serializer_class = LicenciaSerializer
