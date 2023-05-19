"""models.py

Este módulo define el modelo Persona para almacenar información
sobre personas en la base de datos.

Autor: Christopher Villamarín (@xeland314)
Dependencias: django.contrib.auth.models.User, django.db.models
"""
from datetime import date
from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .utils import (
    es_un_numero_de_telefono_valido, es_una_cedula_valida,
    es_una_fecha_de_nacimiento_valida,
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
        ValidationError: Si la cédula no es válida.
    """
    if not es_una_cedula_valida(cedula):
        raise ValidationError(
            _('%(value)s no es una cédula válida'),
            params={'value': cedula},
        )

def validar_fecha_de_nacimiento(fecha_nacimiento: date):
    """Valida si una fecha de nacimiento es válida.

    Esta función toma una fecha de nacimiento como argumento y verifica si es válida
    utilizando la función es_una_fecha_de_nacimiento_valida.
    Si la fecha de nacimiento no es válida, se lanza una excepción ValidationError.

    Args:
        fecha_nacimiento (date): La fecha de nacimiento a validar.

    Raises:
        ValidationError: Si la fecha de nacimiento no es válida.
    """
    if not es_una_fecha_de_nacimiento_valida(fecha_nacimiento):
        raise ValidationError(
            _('La persona debe ser mayor de edad'),
            params={'value': fecha_nacimiento},
        )

def validar_numero_de_telefono(telefono: str):
    """Valida si un número de teléfono es válido.

    Esta función toma un número de teléfono como argumento y verifica si es válido
    utilizando la función es_un_numero_de_telefono_valido del archivo utils.py.
    Si el número de teléfono no es válido, se lanza una excepción ValidationError.

    Args:
        telefono (str): El número de teléfono a validar.

    Raises:
        ValidationError: Si el número de teléfono no es válido.
    """
    if not es_un_numero_de_telefono_valido(telefono):
        raise ValidationError(
            _('%(value)s no es un número de teléfono válido'),
            params={'value': telefono},
        )

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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombres = models.CharField('Nombres', max_length=150, blank=False)
    apellidos = models.CharField('Apellidos', max_length=150, blank=False)
    cedula = models.CharField(
        'Cédula', max_length=10, blank=False, validators=[validar_cedula]
    )
    email = models.EmailField('Email', max_length=100, blank=False)
    telefono = models.CharField(
        'Teléfono', max_length=15, blank=False, validators=[validar_numero_de_telefono]
    )
    direccion = models.TextField('Dirección', blank=True)
    fecha_nacimiento = models.DateField(
        'Fecha de nacimiento', blank=False, validators=[validar_fecha_de_nacimiento]
    )
    nivel_educacion = models.CharField(
        'Nivel de educación', max_length=30, choices=NIVELES_EDUCACION
    )
    estado_civil = models.CharField(
        'Estado Civil', max_length=20, choices=ESTADOS_CIVILES
    )
    fotografia = models.ImageField('Fotografía', null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.cedula} - {self.nombres} {self.apellidos}"
