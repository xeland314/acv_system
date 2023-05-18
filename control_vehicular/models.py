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
        es_profesional (bool): Indica si la licencia es profesional o no.

    Métodos:
        esta_vigente(): Retorna la validez de la licencia en el tiempo.
    """
    tipo = models.CharField(max_length=2, choices=TIPOS_LICENCIA)
    fecha_de_caducidad = models.DateField(blank=False)
    es_profesional = models.BooleanField(blank=False)

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
        - unidad_carburaje (float): La unidad de carburaje del vehículo.
        - combustible (str): El tipo de combustible del vehículo.
        - condicion (str): La condición vehicular del vehículo.
        - fotografia (ImageField): La fotografía del vehículo.
    """
    propietario = models.ForeignKey(
        Propietario, on_delete=models.CASCADE,
        related_name='vehiculos', default=1
    )
    marca = models.CharField('Marca', max_length=50)
    modelo = models.CharField('Modelo', max_length=50)
    placa = models.CharField('Placa', max_length=10, unique=True)
    anio_de_fabricacion = models.PositiveSmallIntegerField('Año de fabricación')
    color = models.CharField('Color', max_length=50)
    cilindraje = models.FloatField('Cilindraje')
    tonelaje = models.FloatField('Tonelaje')
    unidad_carburaje = models.FloatField('Unidad de carburaje')
    combustible = models.CharField('Combustible', max_length=30, choices=COMBUSTIBLES)
    condicion = models.CharField(
        'Condición vehicular', max_length=30, choices=CONDICIONES_VEHICULARES
    )
    fotografia = models.ImageField('Fotografía', upload_to='vehiculos', null=True, blank=True)

class Matricula(models.Model):
    """
    Representa la matrícula de un vehículo.

    Atributos:
        - propietario (Propietario): El propietario de la matrícula.
        - vehiculo (Vehiculo): El vehículo al que pertenece la matrícula.
        - matricula (str): El número de la matrícula.
        - foto (ImageField): La fotografía de la matrícula.
    """

    propietario = models.ForeignKey(Propietario, on_delete=models.SET_NULL, null=True)
    vehiculo = models.OneToOneField(
        Vehiculo, on_delete=models.CASCADE, related_name='matricula'
    )
    matricula = models.CharField('Matrícula', max_length=50, unique=True)
    foto = models.ImageField('Fotografía', upload_to='matriculas', null=True, blank=True)

class Llanta(models.Model):
    """
    Representa una llanta de un vehículo.

    Atributos:
        - vehiculo (Vehiculo): El vehículo al que pertenece la llanta.
        - codigo_de_fabricacion (str): El código de fabricación de la llanta.
        - posicion_respecto_al_vehiculo (str): La posición de la llanta respecto al vehículo.
    """

    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='llantas')
    codigo_de_fabricacion = models.CharField('Código de fabricación', max_length=50)
    posicion_respecto_al_vehiculo = models.CharField(
        'Posición respecto al vehículo', max_length=50, choices=POSICIONES_LLANTA
    )

class Bateria(models.Model):
    """
    Representa una batería de un vehículo.

    Atributos:
        - vehiculo (Vehiculo): El vehículo al que pertenece la batería.
        - codigo_de_fabricacion (str): El código de fabricación de la batería.
    """

    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='baterias')
    codigo_de_fabricacion = models.CharField('Código de fabricación', max_length=50)
