"""serializers.py

Este módulo define el serializer PerfilSerializer
para serializar y deserializar instancias del modelo PerfilUsuario.

Autor: Christopher Villamarín (@xeland314)
"""

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from empresas.models import Empresa

from .models import PerfilUsuario
from .exceptions import (
    CedulaInvalida,
    ErrorDeConfirmacionDeContrasena,
    NombreInvalido,
    TelefonoInvalido
)
from .validators import (
    es_un_nombre_valido,
    es_una_cedula_valida,
    es_un_numero_de_telefono_valido
)

class PerfilSerializer(serializers.ModelSerializer):
    """
    Serializer para serializar y deserializar instancias del modelo PerfilUsuario.
    """
    empresa = serializers.PrimaryKeyRelatedField(
        queryset=Empresa.objects.all(),
        help_text=_("Empresa en la que labora el trabajador.")
    )
    nombres = serializers.CharField(
        write_only=True,
        required=True,
        help_text=_("Nombres del usuario.")
    )
    apellidos = serializers.CharField(
        write_only=True,
        required=True,
        help_text=_("Apellidos del usuario.")
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'},
        help_text=_("Contraseña del usuario.")
    )
    password_validator = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'},
        help_text=_("Campo para confirmar la contraseña del usuario.")
    )

    class Meta:
        """Clase interna para especificar el modelo y los campos a serializar.

        Atributos:
            - model: Modelo a serializar.
            - fields: Campos del modelo a serializar.
            - read_only_fields: Campos de solo lectura.
            - default_error_messages: Mensajes de error personalizados.
        """
        model = PerfilUsuario
        fields = (
            'id', 'nombres', 'apellidos', 'empresa', 'role', 'cedula', 'email',
            'direccion', 'telefono', 'fecha_nacimiento', 'nivel_educacion',
            'estado_civil', 'password', 'password_validator', 'fotografia'
        )
        read_only_fields = ('id',)
        default_error_messages = {
            'invalid': _('Datos inválidos.'),
            'required': _('Este campo es obligatorio.'),
        }

    def create(self, validated_data: dict):
        """Crea una nuevo PerfilUsuario a partir de los datos validados.

        Args:
            validated_data: Diccionario con los datos validados.

        Returns:
            PerfilUsuario: Nueva instancia del modelo PerfilUsuario
            creada a partir de los datos validados.
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
        usuario = PerfilUsuario.objects.create(user=user, **validated_data)
        return usuario

    def to_representation(self, instance: PerfilUsuario):
        representation = super().to_representation(instance)
        try:
            user: User = User.objects.get(username=representation.get('email'))
            representation['nombres'] = user.first_name
            representation['apellidos'] = user.last_name
        except ObjectDoesNotExist:
            representation['nombres'] = _('No se han encontrado datos')
            representation['apellidos'] = _('No se han encontrado datos')
        return representation

    def update(self, instance: PerfilUsuario, validated_data: dict):
        """Actualiza una instancia de PerfilUsuario con los datos validados.

        Args:
            instance: Instancia de PerfilUsuario a actualizar.
            validated_data: Diccionario con los datos validados.

        Returns:
            PerfilUsuario: Instancia de PerfilUsuario actualizada.
        """
        empresa = validated_data.pop('empresa', None)
        if empresa:
            instance.empresa = empresa
            instance.save()

        password = validated_data.pop('password', None)
        if password:
            instance.user.set_password(password)
            instance.user.save()

        nombres = validated_data.pop('nombres', None)
        if nombres:
            instance.user.first_name = nombres
            instance.user.save()

        apellidos = validated_data.pop('apellidos', None)
        if apellidos:
            instance.user.last_name = apellidos
            instance.user.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

    def validate(self, attrs: dict) -> dict:
        """Valida los datos del serializer.

        Este método verifica si la cédula y el número de teléfono
        son válidos y si las contraseñas coinciden.

        Args:
            attrs: Diccionario con los datos a validar.

        Returns:
            dict: Diccionario con los datos validados.

        Raises:
            serializers.ValidationError: Si la cédula o
            el número de teléfono son inválidos o si las contraseñas no coinciden.
        """
        nombres = attrs.get('nombres')
        if not es_un_nombre_valido(nombres):
            raise NombreInvalido('Es un nombre inválido.', params={'value': nombres})

        apellidos = attrs.get('apellidos')
        if not es_un_nombre_valido(apellidos):
            raise NombreInvalido('Es un apellido inválido.', params={'value': apellidos})

        cedula = attrs.get('cedula')
        if not es_una_cedula_valida(cedula):
            raise CedulaInvalida('Es una cédula inválida.', params={'value': cedula})

        telefono = attrs.get('telefono')
        if not es_un_numero_de_telefono_valido(telefono):
            raise TelefonoInvalido(params={'value': telefono})

        password1 = attrs.get('password')
        password2 = attrs.pop('password_validator', None)
        if password1 and password1 != password2:
            raise ErrorDeConfirmacionDeContrasena()

        return attrs
