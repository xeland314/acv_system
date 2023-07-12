from rest_framework.viewsets import ModelViewSet

from .models import (
    ManualMantenimiento,
    OperacionMantenimiento,
    Sistema,
    Subsistema
)
from .serializers import (
    ManualMantenimientoSerializer,
    OperacionMantenimientoSerializer,
    SistemaSerializer,
    SubsistemaSerializer
)

class ManualMantenimientoViewSet(ModelViewSet):
    """
    ViewSet para el modelo ManualMantenimiento.
    """
    queryset = ManualMantenimiento.objects.all()
    serializer_class = ManualMantenimientoSerializer

class SistemaViewSet(ModelViewSet):
    """
    ViewSet para el modelo Sistema.
    """
    queryset = Sistema.objects.all()
    serializer_class = SistemaSerializer

class SubsistemaViewSet(ModelViewSet):
    """
    ViewSet para el modelo Subsistema.
    """
    queryset = Subsistema.objects.all()
    serializer_class = SubsistemaSerializer

class OperacionMantenimientoViewSet(ModelViewSet):
    """
    ViewSet para el modelo OperacionMantenimiento.
    """
    queryset = OperacionMantenimiento.objects.all()
    serializer_class = OperacionMantenimientoSerializer
