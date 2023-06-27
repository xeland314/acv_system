"""models.py

Este módulo define el modelo Persona para almacenar información
sobre personas en la base de datos.

Autor: Christopher Villamarín (@xeland314)
Dependencias: django.contrib.auth.models.User, django.db.models
"""
from datetime import date
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from suscripciones.models import Subscripcion
from .exceptions import (
    CedulaInvalida, FechaDeNacimientoInvalida, TelefonoInvalido
)
from .utils import (
    es_un_numero_de_telefono_valido, es_una_cedula_valida,
    es_una_fecha_de_nacimiento_valida,
    EstadoCivil, NivelEducacion
)

def validar_cedula(cedula: str):
    """Valida si una cédula es válida.

    Esta función toma una cédula como argumento y verifica si es válida
    utilizando la función es_una_cedula_valida del archivo utils.py.
    Si la cédula no es válida, se lanza una excepción ValidationError.

    Args:
        cedula (str): La cédula a validar.

    Raises:
        CedulaInvalida: Si la cédula no es válida.
    """
    if not es_una_cedula_valida(cedula):
        raise CedulaInvalida(
            f"{cedula} no es una cédula válida.",
            params={'value': cedula}
        )

def validar_fecha_de_nacimiento(fecha_nacimiento: date):
    """Valida si una fecha de nacimiento es válida.

    Esta función toma una fecha de nacimiento como argumento y verifica si es válida
    utilizando la función es_una_fecha_de_nacimiento_valida.
    Si la fecha de nacimiento no es válida, se lanza una excepción ValidationError.

    Args:
        fecha_nacimiento (date): La fecha de nacimiento a validar.

    Raises:
        FechaDeNacimientoInvalida: Si la fecha de nacimiento no es válida.
    """
    if not es_una_fecha_de_nacimiento_valida(fecha_nacimiento):
        raise FechaDeNacimientoInvalida(params={'value': fecha_nacimiento})

def validar_numero_de_telefono(telefono: str):
    """Valida si un número de teléfono es válido.

    Esta función toma un número de teléfono como argumento y verifica si es válido
    utilizando la función es_un_numero_de_telefono_valido del archivo utils.py.
    Si el número de teléfono no es válido, se lanza una excepción ValidationError.

    Args:
        telefono (str): El número de teléfono a validar.

    Raises:
        TelefonoInvalido: Si el número de teléfono no es válido.
    """
    if not es_un_numero_de_telefono_valido(telefono):
        raise TelefonoInvalido(params={'value': telefono})

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

class Trabajador(models.Model):
    """Modelo para almacenar información sobre personas.

    Este modelo hereda de django.db.models.Model y define varios campos
    para almacenar información sobre una persona, como su nombre, apellidos,
    cédula, email, teléfono, fecha de nacimiento, nivel de educación y estado civil.
    También tiene un campo para almacenar una fotografía opcional.

    Atributos:
        - id: Clave primaria del modelo.
        - user: Relación uno a uno con el modelo User de Django.
        - nombres: Nombres de la persona.
        - apellidos: Apellidos de la persona.
        - cedula: Cédula de la persona.
        - email: Email de la persona.
        - telefono: Teléfono de la persona.
        - fecha_nacimiento: Fecha de nacimiento de la persona.
        - nivel_educacion: Nivel de educación de la persona.
        - estado_civil: Estado civil de la persona.
        - fotografia: Fotografía opcional de la persona.
    """

    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        help_text=_("Relación uno a uno con el modelo User de Django.")
    )
    empresa = models.ForeignKey(
        Empresa,
        related_name="trabajadores",
        on_delete=models.CASCADE,
        help_text=_("Empresa en la que labora el trabajador.")
    )
    nombres = models.CharField(
        _('Nombres'),
        max_length=150,
        blank=False,
        help_text=_("Nombres de la persona.")
    )
    apellidos = models.CharField(
        _('Apellidos'),
        max_length=150,
        blank=False,
        help_text=_("Apellidos de la persona.")
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
        max_length=100,
        blank=False,
        help_text=_("Email de la persona.")
    )
    telefono = models.CharField(
        _('Teléfono'),
        max_length=15,
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
        verbose_name = _("Trabajador")
        verbose_name_plural = _("Trabajadores")

    def __str__(self) -> str:
        return f"{self.cedula} - {self.nombres} {self.apellidos}"

class Representante(Trabajador):
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
