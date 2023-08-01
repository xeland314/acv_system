import coreapi
import coreschema
from django.utils.translation import gettext_lazy as _
from rest_framework import viewsets
from rest_framework.schemas import AutoSchema
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import OrdenTrabajoSerializer
from .models import OrdenTrabajo

class SearchSchema(AutoSchema):

    def get_description(self, path, method):
        if path == '/ordenes_trabajo/api/v1/ordenes_trabajo/search/':
            return 'Filtra las órdenes de trabajo en función de responsable.'
        return super().get_description(path, method)

    def get_manual_fields(self, path, method):
        extra_fields = []

        if path == '/ordenes_trabajo/api/v1/ordenes_trabajo/search/':
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

class OrdenTrabajoView(viewsets.ModelViewSet):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer

    @action(detail=False, methods=['get'], schema=SearchSchema())
    def search(self, request: Request):
        responsable_id = request.query_params.get('responsable_id')
        vehiculo_id = request.query_params.get('vehiculo_id')

        queryset = self.get_queryset()
        if responsable_id:
            queryset = queryset.filter(responsable__id=responsable_id)
        if vehiculo_id:
            queryset = queryset.filter(vehiculo__id=vehiculo_id)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
