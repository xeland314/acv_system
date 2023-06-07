"""
Este módulo contiene los serializadores de los modelos de control_vehicular.

Autor: Christopher Villamarín (@xeland314)
"""

from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from login.serializers import PersonaSerializer
from .models import (
    Administrador, AperturaOrdenMovimiento, CierreOrdenMovimiento,
    OrdenTrabajo, Responsable
)

class AdministradorSerializer(PersonaSerializer):
    """
    Serializador para el modelo Administrador.
    """

    class Meta:
        model = Administrador
        fields = (
            'nombres', 'apellidos', 'cedula', 'email', 'direccion',
            'telefono', 'fecha_nacimiento', 'nivel_educacion',
            'estado_civil', 'contrasena', 'contrasena2', 'fotografia'
        )
        verbose_name_plural = _('Administradores')

    def create(self, validated_data: dict):
        """Crea una nueva instancia del modelo Persona a partir de los datos validados.

        Args:
            validated_data: Diccionario con los datos validados.

        Returns:
            Administrador: Nueva instancia del modelo Persona creada
            a partir de los datos validados.
        """
        password = validated_data.pop('contrasena')
        username = validated_data.get('cedula')
        email = validated_data.get('email')
        user = User.objects.create_user(username, email, password)
        validated_data['user'] = user
        usuario = Administrador.objects.create(**validated_data)
        return usuario

class ResponsableSerializer(PersonaSerializer):
    """
    Serializador para el modelo Administrador.
    """

    class Meta:
        model = Responsable
        fields = (
            'nombres', 'apellidos', 'cedula', 'email', 'direccion',
            'telefono', 'fecha_nacimiento', 'nivel_educacion',
            'estado_civil', 'contrasena', 'contrasena2', 'fotografia'
        )
        verbose_name_plural = _('Responsables')

    def create(self, validated_data: dict):
        """Crea una nueva instancia del modelo Persona a partir de los datos validados.

        Args:
            validated_data: Diccionario con los datos validados.

        Returns:
            Administrador: Nueva instancia del modelo Persona
            creada a partir de los datos validados.
        """
        password = validated_data.pop('contrasena')
        username = validated_data.get('cedula')
        email = validated_data.get('email')
        user = User.objects.create_user(username, email, password)
        validated_data['user'] = user
        usuario = Responsable.objects.create(**validated_data)
        return usuario

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
