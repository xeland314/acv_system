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

from .exceptions import (
    CedulaInvalida, FechaDeNacimientoInvalida, TelefonoInvalido, NombreInvalido,
)
from .utils import (
    es_un_numero_de_telefono_valido, es_una_cedula_valida,
    es_una_fecha_de_nacimiento_valida, es_un_nombre_valido,
    NIVELES_EDUCACION, ESTADOS_CIVILES
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
    

def validar_nombres_apellidos(nombres:str):
    """
    Valida los nombres o apellidos según ciertos criterios.

    Args:
        nombres (str): Los nombres o apellidos a validar.

    Raises:
        NombreInvalido: Si el nombre o apellido no es válido.
    """

    if not es_un_nombre_valido(nombres):
        raise NombreInvalido(params={'value': nombres})

class Persona(models.Model):
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
    nombres = models.CharField(
        _('Nombres'),
        max_length=150,
        blank=False,
        help_text=_("Nombres de la persona."),
        validators=[validar_nombres_apellidos]
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
        choices=NIVELES_EDUCACION,
        help_text=_("Nivel de educación de la persona.")
    )
    estado_civil = models.CharField(
        _('Estado Civil'),
        max_length=20,
        choices=ESTADOS_CIVILES,
        help_text=_("Estado civil de la persona.")
    )
    fotografia = models.ImageField(
      _('Fotografía'),
      null=True,
      blank=True,
      help_text=_("Fotografía opcional de la persona.")
    )

    def __str__(self) -> str:
        return f"{self.cedula} - {self.nombres} {self.apellidos}"
