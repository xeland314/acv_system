from rest_framework import viewsets
from .serializers import (
    BateriaSerializer, ConductorSerializer,
    LicenciaSerializer, LlantaSerializer,
    MatriculaSerializer, OdometroSerializer,
    VehiculoSerializer
)
from .models import (
    Bateria, Conductor, Licencia, Llanta,
    Matricula, Vehiculo, Odometro
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

class MatriculaView(viewsets.ModelViewSet):
    """
    Clase que define la vista para listar y crear matriculas.
    """
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class OdometroView(viewsets.ModelViewSet):
    queryset = Odometro.objects.all()
    serializer_class = OdometroSerializer

class VehiculoView(viewsets.ModelViewSet):
    """
    Clase que define la vista para listar y crear vehiculos.
    """
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
