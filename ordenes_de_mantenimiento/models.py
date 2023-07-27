"""
Modelos de Django para el manejo de información de:
    - Apertura y cierre de órdenes de movimiento

Autor: Christopher Villamarín (@xeland314)
"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from conductores.models import Conductor

from usuarios.models import PerfilUsuario
from vehiculos.models import Kilometraje, Vehiculo

from .enums import EstadoCumplimiento

class AperturaOrdenMovimiento(models.Model):
    """
    Representa la apertura de una OrdenMovimiento.
    """
    persona = models.ForeignKey(
        PerfilUsuario,
        on_delete=models.PROTECT,
        help_text=_("Responsable de emitir la orden de mantenimiento")
    )
    conductor = models.ForeignKey(
        Conductor,
        on_delete=models.PROTECT,
        help_text=_("El conductor que va a conducir el vehículo de la orden de apertura."),
        related_name='aperturas_conductor'
    )
    vehiculo = models.ForeignKey(
        Vehiculo,
        on_delete=models.PROTECT,
        help_text=_("El vehículo del cual se abre la orden de movimiento.")
    )
    kilometraje_salida = models.OneToOneField(
        Kilometraje,
        on_delete=models.CASCADE,
        help_text=_("Kilometraje del vehículo al momento de la salida")
    )
    fecha_de_emision_orden = models.DateField(
        auto_now=True, blank=False,
        help_text=_("Fecha de emisión de la orden de movimiento")
    )
    fecha_salida_vehiculo = models.DateField(
        help_text=_("Fecha de salida del vehículo")
    )
    itinerario = models.TextField(help_text=_("Itinerario o viaje"))
    detalle_comision = models.TextField(help_text=_("Detalle de la comisión"))

    class Meta:
        verbose_name = _("Apertura de orden de movimiento")
        verbose_name_plural = _("Aperturas de órdenes de movimiento")

    def __str__(self) -> str:
        return f"{self.vehiculo} - {self.fecha_de_emision_orden}"

class CierreOrdenMovimiento(models.Model):
    """
    Representa el cierre de una OrdenMovimiento.
    """
    apertura = models.OneToOneField(
        AperturaOrdenMovimiento,
        on_delete=models.PROTECT,
        help_text=_("Apertura de la orden de movimiento a la que se vincula el cierre de la misma")
    )
    fecha_de_cierre_orden = models.DateField(
        auto_now=True, blank=False,
        help_text=_("Fecha del cierre de la orden de movimiento")
    )
    fecha_retorno_vehiculo = models.DateField(
        help_text=_("Fecha de retorno del vehículo")
    )
    kilometraje_retorno = models.OneToOneField(
        Kilometraje,
        on_delete=models.CASCADE,
        help_text=_("Kilometraje del vehículo al momento del retorno")
    )
    cumplimiento = models.CharField(
        max_length=20,
        choices=EstadoCumplimiento.choices(),
        help_text=_("Estado de cumplimiento de la orden de movimiento")
    )

    class Meta:
        verbose_name = _("Cierre de orden de movimiento")
        verbose_name_plural = _("Cierres de órdenes de movimiento")

    def __str__(self) -> str:
        return f"{self.apertura} - {self.fecha_retorno_vehiculo}"
