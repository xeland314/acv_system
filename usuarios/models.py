from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from empresas.models import Empresa

from .enums import (
    EstadoCivil,
    NivelEducacion,
    Roles
)
from .validators import (
    validar_cedula,
    validar_fecha_de_nacimiento,
    validar_numero_de_telefono
)

class PerfilUsuario(models.Model):
    """
    La clase PerfilUsuario representa el perfil de un usuario en el sistema.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    empresa = models.ForeignKey(
        Empresa,
        related_name="trabajadores",
        on_delete=models.CASCADE,
        help_text=_("Empresa en la que labora el trabajador.")
    )
    role = models.CharField(
        _('Rol'),
        max_length=30,
        blank=False,
        choices=Roles.choices(),
        help_text=_('Rol de un usuario en el sistema.')
    )
    cedula = models.CharField(
        _('Cédula'),
        max_length=10,
        blank=False,
        validators=[validar_cedula],
        help_text=_("Cédula de la persona.")
    )
    email = models.EmailField(
        _('Email'),
        max_length=127,
        blank=False,
        help_text=_("Email de la persona.")
    )
    telefono = models.CharField(
        _('Teléfono'),
        max_length=13,
        blank=False,
        validators=[validar_numero_de_telefono],
        help_text=_("Teléfono de la persona.")
    )
    direccion = models.TextField(
        _('Dirección'),
        blank=True,
        help_text=_("Dirección de la persona.")
    )
    fecha_nacimiento = models.DateField(
        _('Fecha de nacimiento'),
        blank=False,
        validators=[validar_fecha_de_nacimiento],
        help_text=_("Fecha de nacimiento de la persona.")
    )
    nivel_educacion = models.CharField(
        _('Nivel de educación'),
        max_length=30,
        choices=NivelEducacion.choices(),
        help_text=_("Nivel de educación de la persona.")
    )
    estado_civil = models.CharField(
        _('Estado Civil'),
        max_length=20,
        choices=EstadoCivil.choices(),
        help_text=_("Estado civil de la persona.")
    )
    fotografia = models.ImageField(
        _('Fotografía'),
        null=True,
        blank=True,
        help_text=_("Fotografía opcional de la persona.")
    )

    class Meta:
        verbose_name = _("Perfil de usuario")
        verbose_name_plural = _("Perfiles de usuario")

    def __str__(self):
        return f"{self.email}"
