"""
Este módulo contiene los serializadores de los modelos de control_vehicular.

Autor: Christopher Villamarín (@xeland314)
"""

from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from empresas.models import Empresa

from usuarios.models import PerfilUsuario

from .models import (
    Bateria,
    Licencia,
    Vehiculo,
    Llanta,
    Kilometraje
)

class KilometrajeSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Kilometraje.
    """
    class Meta:
        model = Kilometraje
        fields = '__all__'
        read_only_fields = ('id',)

class VehiculoSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Vehiculo.
    """
    propietario = serializers.PrimaryKeyRelatedField(
        queryset=PerfilUsuario.objects.all(),
        help_text=_("Usuario al que pertenece el vehículo.")
    )
    empresa = serializers.PrimaryKeyRelatedField(
        queryset=Empresa.objects.all(),
        help_text=_("Empresa en la que se ha registrado el vehículo.")
    )

    class Meta:
        model = Vehiculo
        fields = '__all__'
        read_only_fields = ('id',)

class LlantaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Llanta.
    """
    class Meta:
        model = Llanta
        fields = '__all__'
        read_only_fields = ('id',)

class BateriaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Batería.
    """
    class Meta:
        model = Bateria
        fields = '__all__'
        read_only_fields = ('id',)

class LicenciaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Licencia.

    Campos:
        - tipo: tipo de licencia.
        - fecha_de_caducidad: fecha de caducidad de la licencia.
        - es_profesional: indica si la licencia es profesional.
    """
    conductor = serializers.PrimaryKeyRelatedField(
        queryset=PerfilUsuario.objects.all(),
        help_text=_("Usuario al que pertenece la licencia.")
    )

    class Meta:
        model = Licencia
        fields = '__all__'
        read_only_fields = ('id',)
