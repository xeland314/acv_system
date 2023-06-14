from rest_framework import viewsets
from .serializers import (
    AperturaOrdenMovimientoSerializer,
    CierreOrdenMovimientoSerializer,
    OrdenTrabajoSerializer
)
from .models import (
    AperturaOrdenMovimiento,
    CierreOrdenMovimiento,
    OrdenTrabajo
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

class OrdenTrabajoView(viewsets.ModelViewSet):
    """
    Clase que define la vista para listar y crear ordenes de trabajo.
    """
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer
