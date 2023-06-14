"""
Modelos de Django para el manejo de información de:
    - Administradores
    - Responsables
    - Órdenes de trabajo
    - Apertura y cierre de órdenes de movimiento

Autor: Christopher Villamarín (@xeland314)

Dependencias:
    - Django 3.2.4
    - El modelo Persona del módulo login.models
    - El módulo utils.py para definir constantes.
"""

from django.db import models
from django.utils.translation import gettext_lazy as _

from control_vehicular.models import Vehiculo, Conductor

from login.models import Persona

from .utils import (
    ESTADOS_CUMPLIMIENTO, TIPOS_MANTENIMIENTO
)

class OrdenTrabajo(models.Model):
    """
    Representa una orden de trabajo para el mantenimiento de vehículos.

    Atributos:
        - fecha_emision (DateField): La fecha en que se emitió la orden de trabajo.
        - responsable (ForeignKey): La persona responsable de la orden de trabajo.
        - vehiculo (ForeignKey): El vehículo asociado con la orden de trabajo.
        - tipo_mantenimiento (CharField): El tipo de mantenimiento a realizar.
        - tipo_trabajo (TextField): Una descripción del trabajo a realizar.
        - cumplimiento (CharField): El estado de cumplimiento de la orden de trabajo
            ("Pendiente", "Cumplido").
    """
    fecha_emision = models.DateField(
        auto_now=True,
        blank=False,
        help_text=_("Fecha de emisión de la orden de trabajo")
    )
    persona = models.ForeignKey(
        Persona,
        on_delete=models.PROTECT,
        help_text=_("Responsable de la orden de trabajo")
    )
    vehiculo = models.ForeignKey(
        Vehiculo,
        on_delete=models.PROTECT,
        help_text=_("Vehículo asociado con la orden de trabajo")
    )
    tipo_mantenimiento = models.CharField(
        max_length=30,
        choices=TIPOS_MANTENIMIENTO,
        help_text=_("Tipo de mantenimiento a realizar")
    )
    tipo_trabajo = models.TextField(help_text=_("Descripción del trabajo a realizar"))
    cumplimiento = models.CharField(
        max_length=20,
        choices=ESTADOS_CUMPLIMIENTO,
        help_text=_("Estado de cumplimiento de la orden de trabajo")
    )

    class Meta:
        verbose_name = _("Orden de trabajo")
        verbose_name_plural = _("Órdenes de trabajo")

    def __str__(self) -> str:
        return f"{self.vehiculo} - {self.fecha_emision}"

class AperturaOrdenMovimiento(models.Model):
    """
    Representa la apertura de una OrdenMovimiento.

    Atributos:
        - vehiculo (ForeignKey): El vehículo asociado con la OrdenMovimiento.
        - conductor (ForeignKey): El conductor asociado con la OrdenMovimiento.
        - fecha_de_emision_orden (DateField): La fecha en que se emitió la OrdenMovimiento.
        - fecha_salida_vehiculo (DateField): La fecha en que el vehículo salió.
        - kilometraje_salida (IntegerField): El kilometraje del vehículo al momento de la salida.
        - itinerario (TextField): El itinerario o viaje asociado con la OrdenMovimiento.
        - detalle_comision (TextField): Detalles sobre la comisión asociada con la OrdenMovimiento.
    """
    persona = models.ForeignKey(
        Persona,
        on_delete=models.PROTECT,
        help_text=_("Responsable de la orden de trabajo")
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
    kilometraje_salida = models.IntegerField(
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

    Atributos:
        - apertura (OneToOneField): La Apertura asociada con este Cierre.
        - fecha_de_cierre_orden (DateField): La fecha en que se cerró la OrdenMovimiento.
        - fecha_retorno_vehiculo (DateField): La fecha en que el vehículo regresó.
        - kilometraje_retorno (IntegerField): El kilometraje del vehículo al momento del retorno.
        - cumplimiento (CharField): El estado de cumplimiento de la OrdenMovimiento
            ("Pendiente", "Cumplido").
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
    kilometraje_retorno = models.IntegerField(
        help_text=_("Kilometraje del vehículo al momento del retorno")
    )
    cumplimiento = models.CharField(
        max_length=20,
        choices=ESTADOS_CUMPLIMIENTO,
        help_text=_("Estado de cumplimiento de la orden de movimiento")
    )

    class Meta:
        verbose_name = _("Cierre de orden de movimiento")
        verbose_name_plural = _("Cierres de órdenes de movimiento")

    def __str__(self) -> str:
        return f"{self.apertura} - {self.fecha_retorno_vehiculo}"
