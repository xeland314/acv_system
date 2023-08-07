import coreapi
import coreschema
from django.utils.translation import gettext_lazy as _
from rest_framework import viewsets, status
from rest_framework.schemas import AutoSchema
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import OrdenTrabajoSerializer
from .models import OrdenTrabajo

class SearchSchema(AutoSchema):

    def get_description(self, path: str, method):
        if path.endswith('search_by'):
            return 'Filtra las órdenes de trabajo en función de responsable y vehículo.'
        return super().get_description(path, method)

    def get_manual_fields(self, path: str, method):
        extra_fields = []

        if path.endswith('search_by'):
            extra_fields = [
                coreapi.Field(
                    name='responsable_id',
                    required=False,
                    location='query',
                    schema=coreschema.Integer(
                        title='Responsable ID',
                        description='El id del responsable de la orden de trabajo.'
                    ),
                    description='El id del responsable a filtrar.'
                ),
                coreapi.Field(
                    name='vehiculo_id',
                    required=False,
                    location='query',
                    schema=coreschema.Integer(
                        title='Vehiculo ID',
                        description='El id del vehículo de la orden de trabajo.'
                    ),
                    description='El id del vehículo a filtrar.'
                )
            ]

        return super().get_manual_fields(path, method) + extra_fields

class OrdenTrabajoView(viewsets.ModelViewSet):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer

    @action(detail=False, methods=['get'], schema=SearchSchema())
    def search_by(self, request: Request):
        """Función de búsqueda para las órdenes de trabajo"""
        responsable_id = request.query_params.get('responsable_id')
        vehiculo_id = request.query_params.get('vehiculo_id')

        queryset = OrdenTrabajo.objects.all()
        if responsable_id and vehiculo_id:
            queryset = queryset.filter(responsable_id=responsable_id, vehiculo_id=vehiculo_id)
        elif responsable_id:
            queryset = queryset.filter(responsable_id=responsable_id)
        elif vehiculo_id:
            queryset = queryset.filter(vehiculo_id=vehiculo_id)
        else:
            return Response(
                {"error": _("Parámetros de búsqueda incorrectos.")},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not queryset.exists():
            return Response(
                {"error": _(
                    "No se encontraron órdenes de trabajo para los criterios especificados."
                )},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = OrdenTrabajoSerializer(queryset, many=True)
        return Response(serializer.data)
