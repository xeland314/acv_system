"""
Este módulo contiene los serializadores del modelo de Conductor y Licencia.

Autor: Christopher Villamarín (@xeland314)
"""
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from usuarios.models import PerfilUsuario

from usuarios.serializers import PerfilSerializer

from .models import Licencia, Conductor

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
        fields = '__all__'

class ConductorSerializer(PerfilSerializer):
    """
    Serializador para el modelo Conductor.
    """
    licencia = LicenciaSerializer(
        help_text=_("Licencia del conductor.")
    )

    class Meta:
        model = Conductor
        fields = (
            'id', 'nombres', 'apellidos', 'role', 'cedula', 'email', 'direccion',
            'telefono', 'fecha_nacimiento', 'nivel_educacion',
            'estado_civil', 'password', 'password_validator', 'fotografia',
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
        # Crear un usuario:
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
        usuario = PerfilUsuario.objects.create(user=user, **validated_data)
        # Crear licencia del conductor:
        datos_licencia = validated_data.pop('licencia')
        licencia = Licencia.objects.create(**datos_licencia)
        # Crear un conductor:
        validated_data['user'] = user
        validated_data['licencia'] = licencia
        usuario = Conductor.objects.create(**validated_data)
        return usuario

    def update(self, instance: Conductor, validated_data: dict):
        """
        Actualiza una instancia existente del modelo Conductor con los datos validados.

        Args:
            instance (Conductor): Instancia del modelo Conductor que se va a actualizar.
            validated_data (dict): Diccionario con los datos validados.

        Returns:
            Conductor: Instancia del modelo Conductor actualizada con los nuevos datos.
        """
        empresa = validated_data.pop('empresa', None)
        if empresa:
            instance.empresa = empresa
            instance.save()

        # Update user fields
        user_data: dict = validated_data.pop('user', None)
        if user_data:
            password = user_data.pop('password', None)
            if password:
                instance.user.set_password(password)
                instance.user.save()

            nombres = user_data.pop('nombres', None)
            if nombres:
                instance.user.first_name = nombres
                instance.user.save()

            apellidos = user_data.pop('apellidos', None)
            if apellidos:
                instance.user.last_name = apellidos
                instance.user.save()

            for attr, value in user_data.items():
                setattr(instance.user, attr, value)
            instance.user.save()

        # Update Licencia fields
        licencia_data: dict = validated_data.pop('licencia', None)
        if licencia_data:
            for attr, value in licencia_data.items():
                setattr(instance.licencia, attr, value)
            instance.licencia.save()

        # Update Conductor fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
