from rest_framework import viewsets
from .serializers import (
    BateriaSerializer, ConductorSerializer,
    LicenciaSerializer, LlantaSerializer,
    KilometrajeSerializer,
    VehiculoSerializer, HojaMantenimientoSerializer,
    OperacionMantenimientoSerializer,
    PropietarioSerializer
)
from .models import (
    Bateria, Conductor, Licencia, Llanta,
    Vehiculo, Kilometraje, OperacionMantenimiento,
    HojaMantenimiento, Propietario
)

class BateriaView(viewsets.ModelViewSet):
    """
    Clase que define la vista para listar y crear baterías.
    """
    queryset = Bateria.objects.all()
    serializer_class = BateriaSerializer

class ConductorView(viewsets.ModelViewSet):
    """
    Clase que define la vista para listar y crear conductores.
    """
    queryset = Conductor.objects.all()
    serializer_class = ConductorSerializer

class LicenciaView(viewsets.ModelViewSet):
    """
    Clase que define la vista para listar y crear licencias.
    """
    queryset = Licencia.objects.all()
    serializer_class = LicenciaSerializer

class LlantaView(viewsets.ModelViewSet):
    """
    Clase que define la vista para listar y crear llantas.
    """
    queryset = Llanta.objects.all()
    serializer_class = LlantaSerializer

class PropietarioView(viewsets.ModelViewSet):
    """
    Clase que define la vista para listar y crear conductores.
    """
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer

class KilometrajeView(viewsets.ModelViewSet):
    """
    Clase que define la vista para listar y crear odometros.
    """
    queryset = Kilometraje.objects.all()
    serializer_class = KilometrajeSerializer

class OperacionMatenimientoView(viewsets.ModelViewSet):
    """
    Clase que define la vista para listar y crear Operaciones.
    """
    queryset = OperacionMantenimiento.objects.all()
    serializer_class = OperacionMantenimientoSerializer

class HojaMantenimientoView(viewsets.ModelViewSet):
    """
    Clase que define la vista para listar y crear hojas de mantenimiento.
    """
    queryset = HojaMantenimiento.objects.all()
    serializer_class = HojaMantenimientoSerializer

class VehiculoView(viewsets.ModelViewSet):
    """
    Clase que define la vista para listar y crear vehiculos.
    """
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
