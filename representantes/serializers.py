"""serializers.py

Autor: Christopher Villamarín (@xeland314)
"""

from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from usuarios.models import PerfilUsuario
from usuarios.serializers import PerfilSerializer

from .models import Representante

class RepresentanteSerializer(PerfilSerializer):
    """Serializer para serializar y deserializar
    instancias del modelo Representante.
    """

    class Meta:
        """Clase interna para especificar el modelo y los campos a serializar.

        Atributos:
            - model: Modelo a serializar.
            - fields: Campos del modelo a serializar.
            - read_only_fields: Campos de solo lectura.
            - default_error_messages: Mensajes de error personalizados.
        """
        model = Representante
        fields = (
            'id', 'empresa', 'nombres', 'apellidos', 'cedula', 'ruc', 'email', 'direccion',
            'telefono', 'fecha_nacimiento', 'nivel_educacion',
            'estado_civil', 'password', 'password_validator', 'fotografia'
        )
        read_only_fields = ('id',)
        default_error_messages = {
            'invalid': _('Datos inválidos.'),
            'required': _('Este campo es obligatorio.'),
        }

    def create(self, validated_data: dict):
        """Crea una nueva instancia del modelo Representante a partir de los datos validados.

        Args:
            validated_data: Diccionario con los datos validados.

        Returns:
            Representante: Nueva instancia del modelo Representante creada a partir de los datos validados.
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
        validated_data['user'] = user
        usuario = Representante.objects.create(**validated_data)
        return usuario

    def update(self, instance: Representante, validated_data: dict):
        """Actualiza una instancia existente del modelo Representante con los datos validados.

        Args:
            instance (Representante): Instancia del modelo Representante que se va a actualizar.
            validated_data (dict): Diccionario con los datos validados.

        Returns:
            Representante: Instancia del modelo Representante actualizada con los nuevos datos.
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

        # Update Representante fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
