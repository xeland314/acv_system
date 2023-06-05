"""
Este módulo contiene los serializadores de los modelos de control_vehicular.

Autor: Christopher Villamarín (@xeland314)
"""

from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from login.serializers import PersonaSerializer
from .models import (
    Administrador, OrdenMovimiento,
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
            Administrador: Nueva instancia del modelo Persona creada a partir de los datos validados.
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
        model = Administrador
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
            Administrador: Nueva instancia del modelo Persona creada a partir de los datos validados.
        """
        password = validated_data.pop('contrasena')
        username = validated_data.get('cedula')
        email = validated_data.get('email')
        user = User.objects.create_user(username, email, password)
        validated_data['user'] = user
        usuario = Responsable.objects.create(**validated_data)
        return usuario

class OrdenTrabajoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenTrabajo
        fields = (
            'id', 'fecha_emision', 'responsable', 'vehiculo',
            'tipo_mantenimiento', 'tipo_trabajo', 'cumplimiento'
        )
        verbose_name = _("Orden de trabajo")
        verbose_name_plural = _("Órdenes de trabajo")

class OrdenMovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenMovimiento
        fields = (
            'id', 'fecha_emision', 'vehiculo', 'conductor',
            'itineario', 'detalle_comision', 'fecha_retorno',
            'km_retorno', 'km_actual', 'cumplimiento'
        )
        verbose_name = _("Orden de movimiento")
        verbose_name_plural = _("Órdenes de movimiento")
