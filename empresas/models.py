from django.db import models
from django.utils.translation import gettext_lazy as _

from usuarios.validators import validar_numero_de_telefono

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
    id = models.BigAutoField(primary_key=True)
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

class Suscripcion(models.Model):
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
    id = models.BigAutoField(primary_key=True)
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

    class Meta:
        verbose_name = _("Suscripción")
        verbose_name_plural = _("Suscripciones")

    def __str__(self) -> str:
        return f"{self.id}:{self.tipo} - (Desde {self.fecha_emision} hasta {self.fecha_caducidad})"

class Empresa(models.Model):
    """Modelo para almacenar información sobre empresas.

    Este modelo define varios campos para almacenar información sobre una empresa,
    como su nombre comercial, RUC, dirección, correo electrónico y teléfono. También
    tiene campos para almacenar relaciones con otros modelos,
    como la suscripción de la empresa.
    """
    id = models.BigAutoField(primary_key=True)
    nombre_comercial = models.CharField(
        _('Nombre comercial'),
        blank=False,
        max_length=255,
        unique=True,
        help_text=_("Nombre comercial de la empresa.")
    )
    suscripcion = models.OneToOneField(
        Suscripcion,
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
