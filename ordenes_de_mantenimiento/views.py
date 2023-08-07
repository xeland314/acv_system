import coreapi
import coreschema
from django.utils.translation import gettext_lazy as _
from rest_framework import viewsets, status
from rest_framework.schemas import AutoSchema
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import (
    AperturaOrdenMovimientoSerializer,
    CierreOrdenMovimientoSerializer,
)
from .models import (
    AperturaOrdenMovimiento,
    CierreOrdenMovimiento,
)

class AperturaOrdenMovimientoSearchSchema(AutoSchema):
    def get_description(self, path: str, method):
        if path.endswith('search_by'):
            return (
                'Busca aperturas de órdenes de movimiento por'
                ' responsable, conductor o vehículo.'
            )
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
                        description=(
                            'El id del responsable de la apertura'
                            ' de la orden de movimiento.'
                        )
                    ),
                    description='El id del responsable a filtrar.'
                ),
                coreapi.Field(
                    name='conductor_id',
                    required=False,
                    location='query',
                    schema=coreschema.Integer(
                        title='Conductor ID',
                        description='El id del conductor de la apertura de la orden de movimiento.'
                    ),
                    description='El id del conductor a filtrar.'
                ),
                coreapi.Field(
                    name='vehiculo_id',
                    required=False,
                    location='query',
                    schema=coreschema.Integer(
                        title='Vehiculo ID',
                        description='El id del vehículo de la apertura de la orden de movimiento.'
                    ),
                    description='El id del vehículo a filtrar.'
                )
            ]

        return super().get_manual_fields(path, method) + extra_fields

class AperturaOrdenMovimientoView(viewsets.ModelViewSet):
    """
    Clase que define la vista para listar
    y crear las aperturas de órdenes de movimiento.
    """
    queryset = AperturaOrdenMovimiento.objects.all()
    serializer_class = AperturaOrdenMovimientoSerializer

    @action(detail=False, methods=['get'], schema=AperturaOrdenMovimientoSearchSchema())
    def search_by(self, request: Request):
        """Busca aperturas de órdenes de movimiento por responsable, conductor o vehículo.

        Esta función busca aperturas de órdenes de movimiento
        en la base de datos que coinciden con los
        parámetros `responsable_id`, `conductor_id` o `vehiculo_id` de la petición HTTP.

        Args:
            request (Request): La petición HTTP con los parámetros de búsqueda.

        Returns:
            Response: Una respuesta HTTP con los datos serializados
            de las aperturas de órdenes de movimiento
            que coinciden con los criterios de búsqueda,
            o un mensaje de error si los parámetros son incorrectos.
        """
        responsable_id = request.query_params.get('responsable_id')
        conductor_id = request.query_params.get('conductor_id')
        vehiculo_id = request.query_params.get('vehiculo_id')

        if not any([responsable_id, conductor_id, vehiculo_id]):
            return Response(
                {"error": _("Parámetros de búsqueda incorrectos.")},
                status=status.HTTP_400_BAD_REQUEST
            )

        queryset = AperturaOrdenMovimiento.objects.all()
        if responsable_id:
            queryset = queryset.filter(responsable_id=responsable_id)
        if conductor_id:
            queryset = queryset.filter(conductor_id=conductor_id)
        if vehiculo_id:
            queryset = queryset.filter(vehiculo_id=vehiculo_id)

        if not queryset.exists():
            return Response(
                {"error": _(
                    "No se encontraron aperturas de órdenes"
                    " de movimiento para los criterios especificados."
                )},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = AperturaOrdenMovimientoSerializer(queryset, many=True)
        return Response(serializer.data)

class CierreOrdenMovimientoView(viewsets.ModelViewSet):
    """
    Clase que define la vista para listar
    y crear los cierres de las órdenes de movimiento.
    """
    queryset = CierreOrdenMovimiento.objects.all()
    serializer_class = CierreOrdenMovimientoSerializer
