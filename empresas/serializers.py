"""serializers.py

Autor: Christopher Villamarín (@xeland314)
"""
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from .models import Empresa

class EmpresaSerializer(serializers.ModelSerializer):
    """Serializer para serializar y deserializar instancias del modelo Empresa.

    Este serializer hereda de ModelSerializer y define la clase Meta para especificar
    el modelo y los campos a serializar.

    Atributos:
        - Meta: Clase interna para especificar el modelo y los campos a serializar.
    """

    class Meta:
        """Clase interna para especificar el modelo y los campos a serializar.

        Atributos:
            - model: Modelo a serializar.
            - fields: Campos del modelo a serializar.
            - read_only_fields: Campos de solo lectura.
            - default_error_messages: Mensajes de error personalizados.
        """
        model = Empresa
        fields = (
            'id', 'nombre_comercial', 'ruc',
            'suscripcion', 'direccion', 'correo', 'telefono',
            'logo_empresa'
        )
        read_only_fields = ('id',)
        default_error_messages = {
            'invalid': _('Datos inválidos.'),
            'required': _('Este campo es obligatorio.'),
        }
