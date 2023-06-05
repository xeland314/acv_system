from rest_framework import viewsets
from .serializers import (
    AdministradorSerializer, OrdenMovimientoSerializer,
    OrdenTrabajoSerializer, ResponsableSerializer
)
from .models import (
    Administrador, OrdenMovimiento,
    OrdenTrabajo, Responsable
)

class AdministradorView(viewsets.ModelViewSet):
    """
    Clase que define la vista para listar y crear administradores.
    """
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer

class OrdenTrabajoView(viewsets.ModelViewSet):
    """
    Clase que define la vista para listar y crear ordenes de trabajo.
    """
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer

class OrdenMovimientoView(viewsets.ModelViewSet):
    """
    Clase que define la vista para listar y crear ordenes de movimiento.
    """
    queryset = OrdenMovimiento.objects.all()
    serializer_class = OrdenMovimientoSerializer


class ResponsableView(viewsets.ModelViewSet):
    """
    Clase que define la vista para listar y crear administradores.
    """
    queryset = Responsable.objects.all()
    serializer_class = ResponsableSerializer

