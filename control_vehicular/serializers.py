"""
Este módulo contiene los serializadores de los modelos de control_vehicular.

Autor: Christopher Villamarín (@xeland314)
"""

from rest_framework import serializers
from .models import Bateria, Licencia, Conductor, Propietario, Vehiculo, Matricula, Llanta

class LicenciaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Licencia.

    Campos:
        - tipo: tipo de licencia.
        - fecha_de_caducidad: fecha de caducidad de la licencia.
        - es_profesional: indica si la licencia es profesional.
    """
    es_profesional = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Licencia
        fields = ('tipo', 'fecha_de_caducidad', 'es_profesional')

    def get_es_profesional(self, obj):
        """
        Método para determinar si la licencia es profesional en función del tipo de licencia.
        """
        return obj.tipo in ['A1', 'C', 'C1', 'D', 'D1', 'E', 'E1']

    def create(self, validated_data: dict):
        """Asignar es_profesional automáticamente en función del tipo de licencia"""
        tipo_licencia = validated_data.get('tipo')
        es_profesional = False
        if tipo_licencia in ['A1', 'C', 'C1', 'D', 'D1', 'E', 'E1']:
            es_profesional = True
        validated_data['es_profesional'] = es_profesional
        return super().create(validated_data)

class ConductorSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Conductor.
    """
    licencia = LicenciaSerializer()

    class Meta:
        model = Conductor
        fields = '__all__'

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
