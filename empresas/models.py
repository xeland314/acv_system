from django.db import models
from django.utils.translation import gettext_lazy as _

from suscripciones.models import Subscripcion
from usuarios.validators import validar_numero_de_telefono

class Empresa(models.Model):
    """Modelo para almacenar información sobre empresas.

    Este modelo define varios campos para almacenar información sobre una empresa,
    como su nombre comercial, RUC, dirección, correo electrónico y teléfono. También
    tiene campos para almacenar relaciones con otros modelos,
    como la suscripción de la empresa.
    """
    id = models.AutoField(primary_key=True)
    nombre_comercial = models.CharField(
        _('Nombre comercial'),
        blank=False,
        max_length=255,
        unique=True,
        help_text=_("Nombre comercial de la empresa.")
    )
    suscripcion = models.OneToOneField(
        Subscripcion,
        on_delete=models.CASCADE,
        unique=True,
        help_text=_("Suscripción de la empresa.")
    )
    ruc = models.CharField(
        _('RUC'),
        max_length=13,
        blank=False,
        help_text=_("RUC de la empresa.")
    )
    direccion = models.TextField(
        _('Dirección'),
        blank=False,
        help_text=_("Dirección de la empresa.")
    )
    correo = models.EmailField(
        _('Correo electrónico'),
        max_length=100,
        blank=False,
        help_text=_("Correo electrónico de la empresa.")
    )
    telefono = models.CharField(
        _('Teléfono'),
        max_length=15,
        blank=False,
        validators=[validar_numero_de_telefono],
        help_text=_("Teléfono de la empresa.")
    )
    logo_empresa = models.ImageField(
      _('Logo de la empresa'),
      null=True,
      blank=True,
      help_text=_("Logo de la empresa.")
    )

    class Meta:
        verbose_name = _("Empresa")
        verbose_name_plural = _("Empresas")

    def __str__(self) -> str:
        return f"{self.nombre_comercial} ({self.ruc})"
