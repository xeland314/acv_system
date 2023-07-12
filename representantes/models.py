from django.db import models
from django.utils.translation import gettext_lazy as _

from usuarios.models import PerfilUsuario

class Representante(PerfilUsuario):
    """Modelo para almacenar información sobre representantes.

    Este modelo hereda de la clase Persona y agrega un campo adicional para almacenar
    el RUC del representante.
    """
    ruc = models.CharField(
        _('RUC'),
        max_length=13,
        blank=False,
        help_text=_("RUC del representante.")
    )

    class Meta:
        verbose_name = _("Representante")
        verbose_name_plural = _("Representantes")

    def __str__(self) -> str:
        return f"{self.cedula} - {self.user.first_name} {self.user.last_name}"
