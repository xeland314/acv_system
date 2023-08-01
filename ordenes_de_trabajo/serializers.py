"""
Este módulo contiene los serializadores de los modelos de control_vehicular.

Autor: Christopher Villamarín (@xeland314)
"""
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from usuarios.models import PerfilUsuario
from vehiculos.models import Vehiculo

from .models import OrdenTrabajo

class OrdenTrabajoSerializer(serializers.ModelSerializer):
    """
    Serializer para serializar y deserializar instancias del modelo OrdenTrabajo.
    """
    secretario = serializers.PrimaryKeyRelatedField(
        queryset=PerfilUsuario.objects.all(),
        help_text=_("Responsable de emitir la orden de trabajo")
    )
    vehiculo = serializers.PrimaryKeyRelatedField(
        queryset=Vehiculo.objects.all(),
        help_text=_("Vehículo asociado con la orden de trabajo")
    )

    class Meta:
        model = OrdenTrabajo
        fields = '__all__'
