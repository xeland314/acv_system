from rest_framework import viewsets

from usuarios.models import PerfilUsuario
from .serializers import (
    BateriaSerializer,
    LlantaSerializer,
    KilometrajeSerializer,
    VehiculoSerializer,
    PropietarioSerializer
)
from .models import (
    Bateria, Llanta,
    Vehiculo, Kilometraje,
)

class BateriaView(viewsets.ModelViewSet):
    """
    Clase que define la vista para listar y crear baterías.
    """
    queryset = Bateria.objects.all()
    serializer_class = BateriaSerializer

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
    queryset = PerfilUsuario.objects.filter(
        role='Propietario'
    )
    serializer_class = PropietarioSerializer

class KilometrajeView(viewsets.ModelViewSet):
    """
    Clase que define la vista para listar y crear odometros.
    """
    queryset = Kilometraje.objects.all()
    serializer_class = KilometrajeSerializer

class VehiculoView(viewsets.ModelViewSet):
    """
    Clase que define la vista para listar y crear vehiculos.
    """
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
