from rest_framework import viewsets
from .serializers import (
    ConductorSerializer,
    LicenciaSerializer
)
from .models import (
    Conductor, Licencia
)

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
