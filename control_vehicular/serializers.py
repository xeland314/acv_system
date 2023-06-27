"""
Este módulo contiene los serializadores de los modelos de control_vehicular.

Autor: Christopher Villamarín (@xeland314)
"""

from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from login.serializers import TrabajadorSerializer
from .models import (
    Bateria, Licencia,
    Conductor,Vehiculo,
    Llanta, Kilometraje, HojaMantenimiento,
    OperacionMantenimiento, Propietario
)

class LicenciaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Licencia.

    Campos:
        - tipo: tipo de licencia.
        - fecha_de_caducidad: fecha de caducidad de la licencia.
        - es_profesional: indica si la licencia es profesional.
    """

    class Meta:
        model = Licencia
        fields = ('tipo', 'fecha_de_emision', 'fecha_de_caducidad', 'puntos')

class ConductorSerializer(TrabajadorSerializer):
    """
    Serializador para el modelo Conductor.
    """
    licencia = LicenciaSerializer(
        help_text=_("Licencia del conductor.")
    )

    class Meta:
        model = Conductor
        fields = (
            'nombres', 'apellidos', 'cedula', 'email', 'direccion',
            'telefono', 'fecha_nacimiento', 'nivel_educacion',
            'estado_civil', 'contrasena', 'contrasena2', 'fotografia',
            'licencia'
        )
        verbose_name_plural = _('Conductores')

    def create(self, validated_data: dict):
        """Crea una nueva instancia del modelo Persona a partir de los datos validados.

        Args:
            validated_data: Diccionario con los datos validados.

        Returns:
            Conductor: Nueva instancia del modelo Persona creada a partir de los datos validados.
        """
        password = validated_data.pop('contrasena')
        username = validated_data.get('cedula')
        email = validated_data.get('email')
        datos_licencia = validated_data.pop('licencia')
        licencia = Licencia.objects.create(**datos_licencia)
        user = User.objects.create_user(username, email, password)
        validated_data['user'] = user
        validated_data['licencia'] = licencia
        usuario = Conductor.objects.create(**validated_data)
        return usuario

class KilometrajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kilometraje
        fields = (
            'vehiculo', 'kilometraje', 'unidad', 'fecha'
        )

class PropietarioSerializer(TrabajadorSerializer):
    """
    Serializador para el modelo Conductor.
    """

    class Meta:
        model = Propietario
        fields = (
            'nombres', 'apellidos', 'cedula', 'email', 'direccion',
            'telefono', 'fecha_nacimiento', 'nivel_educacion',
            'estado_civil', 'contrasena', 'contrasena2', 'fotografia'
        )
        verbose_name_plural = _('Propietarios')

    def create(self, validated_data: dict):
        """Crea una nueva instancia del modelo Persona a partir de los datos validados.

        Args:
            validated_data: Diccionario con los datos validados.

        Returns:
            Propietario: Nueva instancia del modelo Persona creada a partir de los datos validados.
        """
        password = validated_data.pop('contrasena')
        username = validated_data.get('cedula')
        email = validated_data.get('email')
        user = User.objects.create_user(username, email, password)
        validated_data['user'] = user
        propietario = Propietario.objects.create(**validated_data)
        return propietario

class VehiculoSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Vehiculo.
    """
    propietario = PropietarioSerializer(
        help_text=_("Propietario del vehículo.")
    )
    class Meta:
        model = Vehiculo
        fields = (
            'anio_de_fabricacion', 'cilindraje', 'color',
            'combustible', 'condicion', 'foto_matricula', 'foto_vehiculo',
            'marca', 'modelo', 'numero_de_chasis', 'placa',
            'tonelaje', 'unidad_carburante', 'propietario'
        )

    def create(self, validated_data: dict):
        """Crea una nueva instancia del modelo Persona a partir de los datos validados.

        Args:
            validated_data: Diccionario con los datos validados.

        Returns:
            Propietario: Nueva instancia del modelo Persona creada a partir de los datos validados.
        """
        datos_propietario = validated_data.pop('propietario')
        propietario = Propietario.objects.create(**datos_propietario)
        validated_data['propietario'] = propietario
        vehiculo = Vehiculo.objects.create(**validated_data)
        return vehiculo

class LlantaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Llanta.
    """
    class Meta:
        model = Llanta
        fields = (
            'vehiculo', 'codigo_de_fabricacion',
            'posicion_respecto_al_vehiculo'
        )

class BateriaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Batería.
    """
    class Meta:
        model = Bateria
        fields = ('vehiculo', 'codigo_de_fabricacion')

class OperacionMantenimientoSerializer(serializers.ModelSerializer):
    """
    Serializador para las operaciones de mantenimiento.
    """
    class Meta:
        model = OperacionMantenimiento
        fields = ('hoja_mantenimiento', 'tarea', 'sistema', 'sub_sistema', 'frecuencia', 'unidad')

class HojaMantenimientoSerializer(serializers.ModelSerializer):
    """
    Serializador para las hojas de mantenimiento.
    """

    class Meta:
        model = HojaMantenimiento
        fields = ('vehiculo', 'frecuencia_minima', 'final_ciclo', 'unidad')
