"""
Este módulo contiene los serializadores de los modelos de control_vehicular.

Autor: Christopher Villamarín (@xeland314)
"""

from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from login.serializers import PersonaSerializer
from .models import (
    Bateria, Licencia,
    Conductor,Vehiculo,
    Matricula, Llanta,
    Odometro, HojaMantenimiento,
    Operacion
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
        fields = ('tipo', 'fecha_de_caducidad')

class ConductorSerializer(PersonaSerializer):
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

class VehiculoSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Vehiculo.
    """
    propietario = PersonaSerializer(
        help_text=_("Propietario del vehículo.")
    )
    matricula = serializers.CharField(
        source='matricula.matricula',
        read_only=True,
        help_text=_("Matrícula del vehículo.")
    )
    class Meta:
        model = Vehiculo
        fields = (
            'propietario', 'matricula', 'marca', 'modelo',
            'placa', 'anio_de_fabricacion', 'color',
            'cilindraje', 'unidad_carburante', 'combustible',
            'condicion', 'fotografia'
        )

class OdometroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Odometro
        fields = ['id', 'vehiculo', 'kilometraje', 'unidad', 'fecha_inicial']

class MatriculaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Matricula.
    """
    propietario = PersonaSerializer(
        help_text=_("Propietario de la matrícula.")
    )
    vehiculo = VehiculoSerializer(
        help_text=_("Vehículo al que pertenece la matrícula.")
    )

    class Meta:
        model = Matricula
        fields = (
            'propietario', 'vehiculo', 'matricula', 'foto'
        )

class LlantaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Llanta.
    """
    vehiculo = VehiculoSerializer(
        help_text=_("Vehículo al que pertenece la llanta.")
    )

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
    vehiculo = VehiculoSerializer(help_text=_("Vehículo al que pertenece la batería."))

    class Meta:
        model = Bateria
        fields = ('vehiculo', 'codigo_de_fabricacion')

class OperacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operacion
        fields = ('tarea', 'sistema', 'sub_sistema', 'frecuencia', 'unidad')

class HojaMantenimientoSerializer(serializers.ModelSerializer):
    operaciones = OperacionSerializer(many=True)

    class Meta:
        model = HojaMantenimiento
        fields = ('vehiculo', 'operaciones')
