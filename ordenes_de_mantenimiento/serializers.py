"""
Este módulo contiene los serializadores de los modelos de control_vehicular.

Autor: Christopher Villamarín (@xeland314)
"""
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from usuarios.enums import Roles

from usuarios.models import PerfilUsuario
from vehiculos.models import Vehiculo

from .models import (
    AperturaOrdenMovimiento,
    CierreOrdenMovimiento,
)

class AperturaOrdenMovimientoSerializer(serializers.ModelSerializer):
    """
    Serializer para serializar y deserializar instancias del modelo AperturaOrdenMovimiento.
    """
    responsable = serializers.PrimaryKeyRelatedField(
        queryset=PerfilUsuario.objects.filter(role=Roles.RESPONSABLE),
        help_text=_("Responsable de emitir la orden de mantenimiento")
    )
    conductor = serializers.PrimaryKeyRelatedField(
        queryset=PerfilUsuario.objects.all(),
        help_text=_("El conductor que va a conducir el vehículo de la orden de apertura.")
    )
    vehiculo = serializers.PrimaryKeyRelatedField(
        queryset=Vehiculo.objects.all(),
        help_text=_("El vehículo del cual se abre la orden de movimiento.")
    )

    class Meta:
        model = AperturaOrdenMovimiento
        fields = '__all__'

class CierreOrdenMovimientoSerializer(serializers.ModelSerializer):
    """
    Serializer para serializar y deserializar instancias del modelo CierreOrdenMovimiento.
    """
    apertura = AperturaOrdenMovimientoSerializer(read_only=True)
    apertura = serializers.PrimaryKeyRelatedField(
        queryset=AperturaOrdenMovimiento.objects.all(),
        write_only=True,
        help_text=_(
            "Apertura de la orden de movimiento a la que se vincula el cierre de la misma"
        )
    )

    class Meta:
        model = CierreOrdenMovimiento
        fields = '__all__'
