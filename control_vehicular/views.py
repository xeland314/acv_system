from rest_framework import viewsets
from .serializers import VehiculoSerializer
from .models import Vehiculo

class VehiculoView(viewsets.ModelViewSet):
    """
    Clase que define la vista para listar y crear vehiculos.
    """
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer 
