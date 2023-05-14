from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Persona
from .utils import es_una_cedula_valida, es_un_numero_de_telefono_valido

class PersonaSerializer(serializers.ModelSerializer):
    
    contrasena = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    contrasena2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = Persona
        fields = (
            'nombres', 'apellidos', 'cedula', 'email',
            'telefono', 'fecha_nacimiento', 'nivel_educacion',
            'estado_civil', 'contrasena', 'contrasena2', 'fotografia'
        )

    def create(self, validated_data: dict):
        password = validated_data.pop('contrasena')
        username = validated_data.get('cedula')
        email = validated_data.get('email')
        user = User.objects.create_user(username, email, password)
        usuario = Persona.objects.create(user=user, **validated_data)
        return usuario

    def validate(self, attrs: dict) -> dict:

        cedula = attrs.get('cedula')
        if not es_una_cedula_valida(cedula):
            raise serializers.ValidationError('Es una cédula inválida.')

        telefono = attrs.get('telefono')
        if not es_un_numero_de_telefono_valido(telefono):
            raise serializers.ValidationError('Número de teléfono inválido')

        password1 = attrs.get('contrasena')
        password2 = attrs.pop('contrasena2', None)
        if password1 and password1 != password2:
            raise serializers.ValidationError("Las contraseñas no coinciden.")

        return attrs
