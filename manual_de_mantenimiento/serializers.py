from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from vehiculos.models import Vehiculo
from .models import (
    ManualMantenimiento,
    OperacionMantenimiento,
    Sistema,
    Subsistema
)

class ManualMantenimientoSerializer(serializers.ModelSerializer):
    """
    Serializer para serializar y deserializar instancias del modelo ManualMantenimiento.
    """
    vehiculo = serializers.PrimaryKeyRelatedField(
        queryset=Vehiculo.objects.all(),
        help_text=_("El vehículo al que pertenece la hoja de mantenimiento.")
    )

    class Meta:
        model = ManualMantenimiento
        fields = (
            'id', 'vehiculo', 'frecuencia_minima', 'final_ciclo', 'unidad'
        )

    def create(self, validated_data: dict):
        """Crea una nueva instancia del modelo ManualMantenimiento a partir de los datos validados.

        Args:
            validated_data: Diccionario con los datos validados.

        Returns:
            ManualMantenimiento: Nueva instancia del modelo ManualMantenimiento creada a partir de los datos validados.
        """
        manual = ManualMantenimiento.objects.create(**validated_data)
        return manual

    def update(self, instance: ManualMantenimiento, validated_data: dict):
        """Actualiza una instancia existente del modelo ManualMantenimiento
        con los datos validados.

        Args:
            instance (ManualMantenimiento):
            Instancia del modelo ManualMantenimiento que se va a actualizar.
            validated_data (dict): Diccionario con los datos validados.

        Returns:
            ManualMantenimiento:
            Instancia del modelo ManualMantenimiento actualizada con los nuevos datos.
        """
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

class SistemaSerializer(serializers.ModelSerializer):
    """
    Serializer para serializar y deserializar instancias del modelo Sistema.
    """
    hoja_mantenimiento = serializers.PrimaryKeyRelatedField(
        queryset=ManualMantenimiento.objects.all(),
        help_text=_("Hoja mantenimiento a la que pertenece este sistema.")
    )

    class Meta:
        model = Sistema
        fields = ('id', 'hoja_mantenimiento', 'nombre')

class SubsistemaSerializer(serializers.ModelSerializer):
    """
    Serializer para serializar y deserializar instancias del modelo Subsistema.
    """
    sistema = serializers.PrimaryKeyRelatedField(
        queryset=Sistema.objects.all(),
        help_text=_("Subsistema del sistema principal del vehículo.")
    )

    class Meta:
        model = Subsistema
        fields = ('id', 'sistema', 'nombre')

class OperacionMantenimientoSerializer(serializers.ModelSerializer):
    """
    Serializer para serializar y deserializar instancias del modelo OperacionMantenimiento.
    """
    subsistema = serializers.PrimaryKeyRelatedField(
        queryset=Subsistema.objects.all(),
        help_text=_("Operación de mantenimiento que se debe realizar en un vehículo.")
    )

    class Meta:
        model = OperacionMantenimiento
        fields = ('id', 'subsistema', 'tarea', 'descripcion','frecuencia', 'unidad')
