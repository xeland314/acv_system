from rest_framework import viewsets
from .models import Dispositivo, CuentaApi, EstadoDispositivo, Alarma
from .serializers import DispositivoSerializer, CuentaApiSerializer, EstadoDispositivoSerializer, AlarmaSerializer

class DispositivoViewSet(viewsets.ModelViewSet):
    queryset = Dispositivo.objects.all()
    serializer_class = DispositivoSerializer

class CuentaApiViewSet(viewsets.ModelViewSet):
    queryset = CuentaApi.objects.all()
    serializer_class = CuentaApiSerializer

class EstadoDispositivoViewSet(viewsets.ModelViewSet):
    queryset = EstadoDispositivo.objects.all()
    serializer_class = EstadoDispositivoSerializer

class AlarmaViewSet(viewsets.ModelViewSet):
    queryset = Alarma.objects.all()
    serializer_class = AlarmaSerializer
