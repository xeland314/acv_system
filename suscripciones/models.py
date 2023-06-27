from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

class Funcionalidad(models.Model):
    """Modelo para almacenar información sobre funcionalidades.

    Este modelo define dos campos para almacenar
    información sobre una funcionalidad,
    como su nombre y descripción.

    Atributos:
        - id: Clave primaria del modelo.
        - nombre: Nombre de la funcionalidad.
        - descripcion: Descripción de la funcionalidad.
    """
    nombre = models.CharField(
        _('Nombre'),
        max_length=255,
        blank=False,
        help_text=_("Nombre de la funcionalidad.")
    )
    descripcion = models.TextField(
        _('Descripción'),
        blank=False,
        help_text=_("Descripción de la funcionalidad.")
    )

    class Meta:
        verbose_name = _("Funcionalidad")
        verbose_name_plural = _("Funcionalidades")

    def __str__(self) -> str:
        return f"{self.nombre}"

class Subscripcion(models.Model):
    """Modelo para almacenar información sobre suscripciones.

    Este modelo define varios campos para almacenar información sobre una suscripción,
    como su tipo, duración y funcionalidades. También tiene un campo para almacenar una
    referencia al usuario que creó la suscripción.

    Atributos:
        - id: Clave primaria del modelo.
        - tipo: Tipo de suscripción.
        - duracion: Duración de la suscripción en días.
        - features: Relación muchos a muchos con el modelo Funcionalidad.
        - created_by: Relación uno a muchos con el modelo User.
    """
    tipo = models.CharField(
        _('Tipo'),
        max_length=255,
        blank=False,
        help_text=_("Tipo de suscripción.")
    )
    fecha_emision = models.DateField(
        _('Fecha emisión'),
        blank=False,
        help_text=_("Fecha de emisión de la suscripción")
    )
    fecha_caducidad = models.DateField(
        _('Fecha de caducidad'),
        blank=False,
        help_text=_("Fecha de caducidad de la suscripción")
    )
    funcionalidades = models.ManyToManyField(
        Funcionalidad,
        help_text=_("Funcionalidades de la suscripción.")
    )
    precio = models.DecimalField(
        _("Precio de la suscripción"),
        max_digits=10,
        decimal_places=2,
        help_text=_("Precio de la suscripción")
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text=_("Usuario que creó la suscripción.")
    )

    class Meta:
        verbose_name = _("Suscripción")
        verbose_name_plural = _("Suscripciones")

    def __str__(self) -> str:
        return f"{self.tipo} - (Desde {self.fecha_emision} hasta {self.fecha_caducidad})"
