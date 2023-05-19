"""
Este módulo contiene los serializadores de los modelos de control_vehicular.

Autor: Christopher Villamarín (@xeland314)
"""

from django.contrib.auth.models import User
from rest_framework import serializers
from login.serializers import PersonaSerializer
from .models import Bateria, Licencia, Conductor, Propietario, Vehiculo, Matricula, Llanta

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
    licencia = LicenciaSerializer()

    class Meta:
        model = Conductor
        fields = (
            'nombres', 'apellidos', 'cedula', 'email', 'direccion',
            'telefono', 'fecha_nacimiento', 'nivel_educacion',
            'estado_civil', 'contrasena', 'contrasena2', 'fotografia',
            'licencia'
        )
        verbose_name_plural = 'Conductores'

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

class PropietarioSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Propietario.
    """
    class Meta:
        model = Propietario
        fields = '__all__'

class VehiculoSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Vehiculo.
    """
    propietario = PropietarioSerializer()
    matricula = serializers.CharField(source='matricula.matricula', read_only=True)

    class Meta:
        model = Vehiculo
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Matricula.
    """
    propietario = PropietarioSerializer()
    vehiculo = VehiculoSerializer()

    class Meta:
        model = Matricula
        fields = '__all__'

class LlantaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Llanta.
    """
    vehiculo = VehiculoSerializer()

    class Meta:
        model = Llanta
        fields = '__all__'

class BateriaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Batería.
    """
    vehiculo = VehiculoSerializer()

    class Meta:
        model = Bateria
        fields = '__all__'
