from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from .models import (
    ManualMantenimiento,
    OperacionMantenimiento,
    Sistema,
    Subsistema
)

class OperacionMantenimientoSerializer(serializers.ModelSerializer):
    """
    Serializer para serializar y deserializar instancias del modelo OperacionMantenimiento.
    """
    class Meta:
        model = OperacionMantenimiento
        fields = '__all__'


class SubsistemaSerializer(serializers.ModelSerializer):
    """
    Serializer para serializar y deserializar instancias del modelo Subsistema.
    """
    operaciones_mantenimiento = OperacionMantenimientoSerializer(many=True, read_only=True)

    class Meta:
        model = Subsistema
        fields = '__all__'

class SistemaSerializer(serializers.ModelSerializer):
    """
    Serializer para serializar y deserializar instancias del modelo Sistema.
    """
    subsistemas_vehiculos = SubsistemaSerializer(many=True, read_only=True)

    class Meta:
        model = Sistema
        fields = '__all__'

class ManualMantenimientoSerializer(serializers.ModelSerializer):
    """
    Serializer para serializar y deserializar instancias del modelo ManualMantenimiento.
    """
    sistemas_vehiculos = SistemaSerializer(many=True, read_only=True)

    class Meta:
        model = ManualMantenimiento
        fields = '__all__'
