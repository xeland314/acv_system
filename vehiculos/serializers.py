"""
Este módulo contiene los serializadores de los modelos de control_vehicular.

Autor: Christopher Villamarín (@xeland314)
"""

from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from usuarios.models import PerfilUsuario
from usuarios.serializers import PerfilSerializer

from .models import (
    Bateria,
    Vehiculo,
    Llanta,
    Kilometraje
)

class KilometrajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kilometraje
        fields = (
            'vehiculo', 'kilometraje', 'unidad', 'fecha'
        )

class PropietarioSerializer(PerfilSerializer):
    """
    Serializador para el modelo Conductor.
    """

    class Meta:
        model = PerfilUsuario
        fields = (
            'nombres', 'apellidos', 'cedula', 'email', 'direccion',
            'telefono', 'fecha_nacimiento', 'nivel_educacion',
            'estado_civil', 'password', 'password_validator', 'fotografia'
        )
        verbose_name_plural = _('Propietarios')

    def create(self, validated_data: dict):
        """Crea una nueva instancia del modelo Persona a partir de los datos validados.

        Args:
            validated_data: Diccionario con los datos validados.

        Returns:
            Propietario: Nueva instancia del modelo Persona creada a partir de los datos validados.
        """
        password = validated_data.pop('password')
        username = validated_data.get('email')
        email = validated_data.get('email')
        nombres = validated_data.pop('nombres')
        apellidos = validated_data.pop('apellidos')
        user = User.objects.create_user(
            username, email, password,
            first_name=nombres,
            last_name=apellidos
        )
        validated_data['user'] = user
        validated_data['role'] = 'Propietario'
        propietario = PerfilUsuario.objects.create(**validated_data)
        return propietario

class VehiculoSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Vehiculo.
    """
    propietario = serializers.PrimaryKeyRelatedField(
        queryset=PerfilUsuario.objects.all(),
        help_text=_("Usuario al que pertenece el vehículo.")
    )

    class Meta:
        model = Vehiculo
        fields = (
            'anio_de_fabricacion', 'cilindraje', 'color',
            'combustible', 'condicion', 'foto_matricula', 'foto_vehiculo',
            'marca', 'modelo', 'numero_de_chasis', 'placa',
            'tonelaje', 'unidad_carburante', 'propietario'
        )
        read_only_fields = ('propietario', )

    def create(self, validated_data: dict):
        """Crea una nueva instancia del modelo Persona a partir de los datos validados.

        Args:
            validated_data: Diccionario con los datos validados.

        Returns:
            Propietario: Nueva instancia del modelo Persona creada a partir de los datos validados.
        """
        propietario = validated_data.pop('email_propietario')
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
