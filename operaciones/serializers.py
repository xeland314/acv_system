"""
Este módulo contiene los serializadores de los modelos de control_vehicular.

Autor: Christopher Villamarín (@xeland314)
"""

from rest_framework import serializers

from .models import (
    AperturaOrdenMovimiento,
    CierreOrdenMovimiento,
    OrdenTrabajo
)

class AperturaOrdenMovimientoSerializer(serializers.ModelSerializer):
    """
    Serializador de las aperturas de órdenes de movimiento.
    """
    class Meta:
        model = AperturaOrdenMovimiento
        fields = (
            'id', 'vehiculo', 'kilometraje_salida', 'fecha_de_emision_orden',
            'fecha_salida_vehiculo', 'itinerario', 'conductor', 'detalle_comision'
        )

class CierreOrdenMovimientoSerializer(serializers.ModelSerializer):
    """
    Serializador de los cierres de órdenes de movimiento.
    """
    class Meta:
        model = CierreOrdenMovimiento
        fields = (
            'id', 'apertura', 'fecha_retorno_vehiculo', 'fecha_de_cierre_orden',
            'kilometraje_retorno', 'cumplimiento'
        )

class OrdenTrabajoSerializer(serializers.ModelSerializer):
    """
    Serializador de las órdenes de trabajo.
    """
    class Meta:
        model = OrdenTrabajo
        fields = (
            'id', 'fecha_emision', 'responsable', 'vehiculo',
            'tipo_mantenimiento', 'tipo_trabajo', 'cumplimiento'
        )
