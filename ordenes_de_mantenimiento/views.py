from rest_framework import viewsets
from rest_framework.schemas.openapi import AutoSchema

from .serializers import (
    AperturaOrdenMovimientoSerializer,
    CierreOrdenMovimientoSerializer,
)
from .models import (
    AperturaOrdenMovimiento,
    CierreOrdenMovimiento,
)

class AperturaOrdenMovimientoView(viewsets.ModelViewSet):
    """
    Clase que define la vista para listar
    y crear las aperturas de órdenes de movimiento.
    """
    queryset = AperturaOrdenMovimiento.objects.all()
    serializer_class = AperturaOrdenMovimientoSerializer
    schema = AutoSchema(tags=['AperturaOrdenMovimiento'])

    def get_queryset(self):
        queryset = super().get_queryset()
        vehiculo_id = self.request.query_params.get('vehiculo_id')
        responsable_id = self.request.query_params.get('responsable_id')
        conductor_id = self.request.query_params.get('conductor_id')

        if vehiculo_id:
            queryset = queryset.filter(vehiculo_id=vehiculo_id)
        if responsable_id:
            queryset = queryset.filter(responsable_id=responsable_id)
        if conductor_id:
            queryset = queryset.filter(conductor_id=conductor_id)

        return queryset

class CierreOrdenMovimientoView(viewsets.ModelViewSet):
    """
    Clase que define la vista para listar
    y crear los cierres de las órdenes de movimiento.
    """
    queryset = CierreOrdenMovimiento.objects.all()
    serializer_class = CierreOrdenMovimientoSerializer
