"""
Modelos de Django para el manejo de información de:
    - Órdenes de trabajo

Autor: Christopher Villamarín (@xeland314)
"""

from django.db import models
from django.utils.translation import gettext_lazy as _

from vehiculos.models import Vehiculo

from usuarios.models import PerfilUsuario

from .enums import (
    EstadoCumplimiento, TipoMantenimiento
)

class OrdenTrabajo(models.Model):
    """
    Representa una orden de trabajo para el mantenimiento de vehículos.
    """
    fecha_emision = models.DateField(
        _("Fecha de emisión"),
        auto_now=True,
        blank=False,
        help_text=_("Fecha de emisión de la orden de trabajo")
    )
    responsable = models.ForeignKey(
        PerfilUsuario,
        on_delete=models.PROTECT,
        related_name="orden_trabajo_responsables",
        help_text=_("Responsable de emitir la orden de trabajo")
    )
    vehiculo = models.ForeignKey(
        Vehiculo,
        on_delete=models.PROTECT,
        related_name="orden_trabajo_vehiculos",
        help_text=_("Vehículo asociado con la orden de trabajo")
    )
    tipo_mantenimiento = models.CharField(
        _("Tipo de mantenimiento"),
        max_length=30,
        choices=TipoMantenimiento.choices(),
        help_text=_("Tipo de mantenimiento a realizar")
    )
    tipo_trabajo = models.TextField(
        _("Observaciones"),
        help_text=_("Descripción del trabajo a realizar")
    )
    cumplimiento = models.CharField(
        _("Cumplimiento"),
        max_length=20,
        choices=EstadoCumplimiento.choices(),
        help_text=_("Estado de cumplimiento de la orden de trabajo")
    )
    costo_mantenimiento = models.DecimalField(
        _("Costo del mantenimiento"),
        default=0,
        decimal_places=2,
        max_digits=10
    )

    class Meta:
        verbose_name = _("Orden de trabajo")
        verbose_name_plural = _("Órdenes de trabajo")

    def __str__(self) -> str:
        return f"{self.vehiculo} - {self.fecha_emision}"
