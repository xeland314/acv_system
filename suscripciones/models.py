from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from login.models import (
    Persona,
    validar_numero_de_telefono
)

class Representante(Persona):
    """Modelo para almacenar información sobre representantes.

    Este modelo hereda de la clase Persona y agrega un campo adicional para almacenar
    el RUC del representante.

    Atributos:
        - ruc: RUC del representante.
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
        return f"{self.cedula} - {self.nombres} {self.apellidos}"

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
    duracion = models.IntegerField(
        _('Duración'),
        blank=False,
        help_text=_("Duración de la suscripción en días.")
    )
    funcionalidades = models.ManyToManyField(
        Funcionalidad,
        help_text=_("Funcionalidades de la suscripción.")
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
        return f"{self.tipo} ({self.duracion} días)"

class Empresa(models.Model):
    """Modelo para almacenar información sobre empresas.

    Este modelo define varios campos para almacenar información sobre una empresa,
    como su nombre comercial, RUC, dirección, correo electrónico y teléfono. También
    tiene campos para almacenar relaciones con otros modelos, como el representante legal
    de la empresa y la suscripción de la empresa.

    Atributos:
        - id: Clave primaria del modelo.
        - nombre_comercial: Nombre comercial de la empresa.
        - ruc: RUC de la empresa.
        - representante_legal: Relación uno a uno con el modelo Representante.
        - suscripcion: Relación uno a uno con el modelo Subscripcion.
        - direccion: Dirección de la empresa.
        - correo: Correo electrónico de la empresa.
        - telefono: Teléfono de la empresa.
    """
    nombre_comercial = models.CharField(
        _('Nombre comercial'),
        max_length=255,
        blank=False,
        help_text=_("Nombre comercial de la empresa.")
    )
    representante_legal = models.OneToOneField(
        Representante,
        on_delete=models.CASCADE,
        help_text=_("Representante legal de la empresa.")
    )
    suscripcion = models.OneToOneField(
        Subscripcion,
        on_delete=models.CASCADE,
        help_text=_("Suscripción de la empresa.")
    )
    ruc = models.CharField(
        _('RUC'),
        max_length=13,
        blank=False,
        help_text=_("RUC de la empresa.")
    )
    direccion = models.CharField(
        _('Dirección'),
        max_length=200,
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

    class Meta:
        verbose_name = _("Empresa")
        verbose_name_plural = _("Empresas")

    def __str__(self) -> str:
        return f"{self.nombre_comercial} ({self.ruc})"

class Trabajador(Persona):
    """Modelo para almacenar información sobre trabajadores.

    Este modelo hereda de la clase Persona y agrega una relación de clave foránea
    con el modelo Empresa para asociar a un trabajador con una y solo una empresa.

    Atributos:
        - empresa: Relación de clave foránea con el modelo Empresa.
    """
    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.PROTECT,
        help_text=_("Empresa a la que está asociado el trabajador.")
    )

    def __str__(self) -> str:
        return f"{self.cedula} - {self.nombres} {self.apellidos}"
