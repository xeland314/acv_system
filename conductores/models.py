from datetime import date
from django.db import models
from django.utils.translation import gettext_lazy as _

from usuarios.models import PerfilUsuario

from .enums import TipoLicencia
from .validators import validar_vigencia_licencia

class Licencia(models.Model):
    """
    Representa una licencia de conducir.

    Atributos:
        tipo (str): El tipo de la licencia (A, B, C, etc.).
        fecha_de_caducidad (date): La fecha de caducidad de la licencia.

    Métodos:
        esta_vigente(): Retorna la validez de la licencia en el tiempo.
    """
    tipo = models.CharField(
        max_length=2,
        choices=TipoLicencia.choices(),
        help_text=_("El tipo de la licencia (A, B, C, etc.).")
    )
    fecha_de_emision = models.DateField(
        blank=False,
        help_text=_("La fecha de emisión de la licencia.")
    )
    fecha_de_caducidad = models.DateField(
        blank=False,
        help_text=_("La fecha de caducidad de la licencia."),
        validators=[validar_vigencia_licencia,]
    )
    puntos = models.PositiveSmallIntegerField(
        blank=False,
        help_text=_("Puntos vigentes de la licencia.")
    )

    def __str__(self):
        return f'{self.tipo} - {self.fecha_de_caducidad}'

    def esta_vigente(self):
        """Retorna la validez de la licencia en el tiempo."""
        return date.today() <= self.fecha_de_caducidad

class Conductor(PerfilUsuario):
    """
    Representa un conductor.

    Atributos:
        - heredados de PerfilUsuario.
        - licencia (Licencia): La licencia de conducir del conductor.

    Métodos:
        __str__(): Retorna una representación en string del conductor.
    """

    licencia = models.OneToOneField(Licencia, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Conductor")
        verbose_name_plural = _("Conductores")

    def __str__(self):
        return f'{self.cedula} - {self.nombres} {self.apellidos} - {self.licencia}'
