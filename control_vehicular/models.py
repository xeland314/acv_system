"""
Modelos de Django para el manejo de información de conductores, vehículos, matrículas y llantas.

Autor: Christopher Villamarín (@xeland314)

Dependencias:
    - Django 3.2.4
    - El modelo Persona del módulo login.models
    - El módulo utils.py para definir constantes TIPOS_LICENCIA,
        COMBUSTIBLES, CONDICIONES_VEHICULARES y POSICIONES_LLANTA.
"""

from datetime import date
from django.db import models
from django.utils.translation import gettext_lazy as _

from login.models import Persona

from .utils import (
    COMBUSTIBLES, CONDICIONES_VEHICULARES,
    POSICIONES_LLANTA, TIPOS_LICENCIA
)

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
        choices=TIPOS_LICENCIA,
        help_text=_("El tipo de la licencia (A, B, C, etc.).")
    )
    fecha_de_caducidad = models.DateField(
        blank=False,
        help_text=_("La fecha de caducidad de la licencia.")
    )

    def __str__(self):
        return f'{self.tipo} - {self.fecha_de_caducidad}'

    def esta_vigente(self):
        "Retorna la validez de la licencia en el tiempo."
        return date.today() <= self.fecha_de_caducidad

class Conductor(Persona):
    """
    Representa un conductor.

    Atributos:
        - heredados de Persona.
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

class Propietario(Persona):
    """
    Representa un propietario de un vehículo.

    Atributos:
        heredados de Persona.
    """

class Vehiculo(models.Model):
    """
    Representa un vehículo.

    Atributos:
        - propietario (Propietario): El propietario del vehículo.
        - marca (str): La marca del vehículo.
        - modelo (str): El modelo del vehículo.
        - placa (str): La placa del vehículo.
        - anio_de_fabricacion (int): El año de fabricación del vehículo.
        - color (str): El color del vehículo.
        - cilindraje (float): El cilindraje del vehículo.
        - tonelaje (float): El tonelaje del vehículo.
        - unidad_carburante (float): La unidad de carburante del vehículo.
        - combustible (str): El tipo de combustible del vehículo.
        - condicion (str): La condición vehicular del vehículo.
        - fotografia (ImageField): La fotografía del vehículo.
    """
    propietario = models.ForeignKey(
        Propietario,
        on_delete=models.CASCADE,
        related_name='vehiculos',
        default=1,
        help_text=_("El propietario del vehículo.")
    )
    marca = models.CharField(
        _('Marca'),
        max_length=50,
        help_text=_("La marca del vehículo.")
    )
    modelo = models.CharField(
        _('Modelo'),
        max_length=50,
        help_text=_("El modelo del vehículo.")
    )
    placa = models.CharField(
        _('Placa'),
        max_length=10,
        unique=True,
        help_text=_("La placa del vehículo.")
    )
    anio_de_fabricacion = models.PositiveSmallIntegerField(
        _('Año de fabricación'),
        help_text=_("El año de fabricación del vehículo.")
    )
    color = models.CharField(
        _('Color'),
        max_length=50,
        help_text=_("El color del vehículo.")
    )
    cilindraje = models.FloatField(
        _('Cilindraje'),
        help_text=_("El cilindraje del vehículo.")
    )
    tonelaje = models.FloatField(
        _('Tonelaje'),
        help_text=_("El tonelaje del vehículo.")
    )
    unidad_carburante = models.FloatField(
        _('Unidad carburante'),
        help_text=_("La unidad de carburante del vehículo.")
    )
    combustible = models.CharField(
        _('Combustible'),
        max_length=30,
        choices=COMBUSTIBLES,
        help_text=_("El tipo de combustible del vehículo.")
    )
    condicion = models.CharField(
        _('Condición vehicular'),
        max_length=30,
        choices=CONDICIONES_VEHICULARES,
        help_text=_("La condición vehicular del vehículo.")
    )
    fotografia = models.ImageField(
        _('Fotografía'),
        upload_to='vehiculos',
        null=True,
        blank=True,
        help_text=_("La fotografía del vehículo.")
    )

    def __str__(self) -> str:
        return f'{self.marca} - {self.placa} - {self.propietario}'

class Matricula(models.Model):
    """
    Representa la matrícula de un vehículo.

    Atributos:
        - propietario (Propietario): El propietario de la matrícula.
        - vehiculo (Vehiculo): El vehículo al que pertenece la matrícula.
        - matricula (str): El número de la matrícula.
        - foto (ImageField): La fotografía de la matrícula.
    """

    propietario = models.ForeignKey(
        Propietario,
        on_delete=models.SET_NULL,
        null=True,
        help_text=_("El propietario de la matrícula.")
    )
    vehiculo = models.OneToOneField(
        Vehiculo,
        on_delete=models.CASCADE,
        related_name='matricula',
        help_text=_("El vehículo al que pertenece la matrícula.")
    )
    matricula = models.CharField(
        _('Matrícula'),
        max_length=50,
        unique=True,
        help_text=_("El número de la matrícula.")
    )
    foto = models.ImageField(
        _('Fotografía'),
        upload_to='matriculas',
        null=True,
        blank=True,
        help_text=_("La fotografía de la matrícula.")
    )

class Llanta(models.Model):
    """
    Representa una llanta de un vehículo.

    Atributos:
        - vehiculo (Vehiculo): El vehículo al que pertenece la llanta.
        - codigo_de_fabricacion (str): El código de fabricación de la llanta.
        - posicion_respecto_al_vehiculo (str): La posición de la llanta respecto al vehículo.
    """

    vehiculo = models.ForeignKey(
        Vehiculo,
        on_delete=models.CASCADE,
        related_name='llantas',
        help_text=_("El vehículo al que pertenece la llanta.")
    )
    codigo_de_fabricacion = models.CharField(
        _('Código de fabricación'),
        max_length=50,
        help_text=_("El código de fabricación de la llanta.")
    )
    posicion_respecto_al_vehiculo = models.CharField(
        _('Posición respecto al vehículo'),
        max_length=50,
        choices=POSICIONES_LLANTA,
        help_text=_("La posición de la llanta respecto al vehículo.")
    )

class Bateria(models.Model):
    """
    Representa una batería de un vehículo.

    Atributos:
        - vehiculo (Vehiculo): El vehículo al que pertenece la batería.
        - codigo_de_fabricacion (str): El código de fabricación de la batería.
    """

    vehiculo = models.ForeignKey(
        Vehiculo,
        on_delete=models.CASCADE,
        related_name='baterias',
        help_text=_("El vehículo al que pertenece la batería.")
    )
    codigo_de_fabricacion = models.CharField(
        _('Código de fabricación'),
        max_length=50,
        help_text=_("El código de fabricación de la batería.")
    )
