from rest_framework import viewsets
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

class CierreOrdenMovimientoView(viewsets.ModelViewSet):
    """
    Clase que define la vista para listar
    y crear los cierres de las órdenes de movimiento.
    """
    queryset = CierreOrdenMovimiento.objects.all()
    serializer_class = CierreOrdenMovimientoSerializer
