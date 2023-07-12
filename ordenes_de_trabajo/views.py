from rest_framework import viewsets

from .serializers import OrdenTrabajoSerializer
from .models import OrdenTrabajo

class OrdenTrabajoView(viewsets.ModelViewSet):
    """
    Clase que define la vista para listar y crear ordenes de trabajo.
    """
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer
