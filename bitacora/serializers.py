from rest_framework import serializers
from .models import Dispositivo, CuentaApi, EstadoDispositivo, Alarma

class DispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivo
        fields = '__all__'

class CuentaApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuentaApi
        fields = '__all__'

class EstadoDispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoDispositivo
        fields = '__all__'

class AlarmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alarma
        fields = '__all__'
