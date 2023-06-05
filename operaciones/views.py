from rest_framework import viewsets
from .serializers import (
    AdministradorSerializer, AperturaOrdenMovimientoSerializer,
    CierreOrdenMovimientoSerializer, OrdenTrabajoSerializer,
    ResponsableSerializer
)
from .models import (
    Administrador, AperturaOrdenMovimiento, CierreOrdenMovimiento,
    OrdenTrabajo, Responsable
)

class AdministradorView(viewsets.ModelViewSet):
    """
    Clase que define la vista para listar y crear administradores.
    """
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer

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

class ResponsableView(viewsets.ModelViewSet):
    """
    Clase que define la vista para listar y crear administradores.
    """
    queryset = Responsable.objects.all()
    serializer_class = ResponsableSerializer

