from django.db import models
from django.utils.translation import gettext_lazy as _

from vehiculos.models import Vehiculo

from .enums import (
    Tareas,
    UnidadOdometro
)

class ManualMantenimiento(models.Model):
    """
    Representa un manual de mantenimiento para un vehículo.

    Atributos:
        - vehiculo (Vehiculo): El vehículo al que pertenece la hoja de mantenimiento.
        - operaciones (list[Operacion]): Las operaciones de mantenimiento a realizar en el vehículo.
    """
    vehiculo = models.OneToOneField(
        Vehiculo,
        on_delete=models.CASCADE,
        help_text=_("El vehículo al que pertenece la hoja de mantenimiento.")
    )
    frecuencia_minima = models.DecimalField(
        _('Frecuencia mínima'),
        max_digits=10,
        decimal_places=2,
        blank=False,
        help_text=_("El kilometraje/tiempo mínimo en el que se deben realizar las operaciones.")
    )
    final_ciclo = models.DecimalField(
        _('Final de ciclo de mantenimiento'),
        max_digits=10,
        decimal_places=2,
        blank=False,
        help_text=_("El kilometraje/tiempo límite que marca el fin de cada ciclo de mantenimiento.")
    )
    unidad = models.CharField(
        _('Unidad'),
        max_length=10,
        blank=False,
        choices=UnidadOdometro.choices(),
        help_text=_("La unidad de medida del kilometraje.")
    )

    class Meta:
        verbose_name = _("Manual de mantenimiento")
        verbose_name_plural = _("Manuales de mantenimiento")

    def __str__(self):
        return (
            f'{self.vehiculo}'
            f' - Frecuencia mínima: {self.frecuencia_minima} {self.unidad}'
            f' - Final de ciclo: {self.final_ciclo} {self.unidad}'
        )

class Sistema(models.Model):
    hoja_mantenimiento = models.ForeignKey(
        ManualMantenimiento,
        on_delete=models.CASCADE,
        related_name='sistemas_vehiculos',
        help_text=_("Hoja mantenimiento a la que pertenece este sistema.")
    )
    nombre = models.CharField(
        _('Sistema'),
        max_length=50,
        blank=False,
        help_text=_("El sistema del vehículo.")
    )

    class Meta:
        verbose_name = _("Sistema del vehículo")
        verbose_name_plural = _("Sistemas del vehículo")

class Subsistema(models.Model):
    sistema = models.ForeignKey(
        Sistema,
        on_delete=models.CASCADE,
        related_name='subsistemas_vehiculos',
        help_text=_("Subsistema del sistema principal del vehículo.")
    )
    nombre = models.CharField(
        _('Sub-sistema'),
        max_length=50,
        blank=False,
        help_text=_("El sub-sistema del vehículo al que pertenece la operación.")
    )

    class Meta:
        verbose_name = _("Subsistema del vehículo")
        verbose_name_plural = _("Subsistemas del vehículo")

class OperacionMantenimiento(models.Model):
    """
    Representa una operación de mantenimiento.
    """
    subsistema = models.ForeignKey(
        Subsistema,
        on_delete=models.CASCADE,
        related_name='operaciones_mantenimiento',
        help_text=_("Operación de mantenimiento que se debe realizar en un vehículo.")
    )
    tarea = models.CharField(
        _('Tarea'),
        max_length=50,
        blank=False,
        choices=Tareas.choices(),
        help_text=_("La tarea a realizar en la operación.")
    )
    descripcion = models.TextField(
        _('Descripción'),
        blank=True,
        help_text=_('Descripción de la tarea a realizar')
    )
    frecuencia = models.DecimalField(
        _('Frecuencia'),
        max_digits=10,
        decimal_places=2,
        blank=False,
        help_text=_("El kilometraje/tiempo en el que se debe realizar la operación.")
    )
    unidad = models.CharField(
        _('Unidad'),
        max_length=10,
        blank=False,
        choices=UnidadOdometro.choices(),
        help_text=_("La unidad de medida del kilometraje.")
    )

    class Meta:
        verbose_name = _("Operación de mantenimiento")
        verbose_name_plural = _("Operaciones de mantenimiento")

    def __str__(self):
        return f'{self.tarea} cada {self.frecuencia} {self.unidad}'
