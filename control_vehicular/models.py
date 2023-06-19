"""
Modelos de Django para el manejo de información de conductores, vehículos, matrículas y llantas.

Autor: Christopher Villamarín (@xeland314)

Dependencias:
    - Django 3.2.4
    - El modelo Persona del módulo login.models
    - El módulo utils.py para definir constantes TIPOS_LICENCIA,
        COMBUSTIBLES, CONDICIONES_VEHICULARES y POSICIONES_LLANTA.
"""
import datetime

from datetime import date
from django.db import models
from django.utils.translation import gettext_lazy as _

from login.models import Persona

from .exceptions import CodigoDotInvalido, PlacaVehicularInvalida, FechaFabricacionInvalida, CodigoBateriaInvalido, LicenciaCaducada
from .utils import (
    COMBUSTIBLES, CONDICIONES_VEHICULARES,
    POSICIONES_LLANTA, TIPOS_LICENCIA,
    es_un_codigo_dot_valido,
    es_una_placa_de_vehiculo_valida,
    es_un_anio_de_fabricacion_valido,
    es_un_codigo_bateria_valido,
    ha_caducado_la_licencia
)

def validar_vigencia_licencia(fechaCaducidad):
    """
    Valida la vigencia de una licencia en función de su fecha de caducidad.

    Argumentos:
    fechaCaducidad (str): La fecha de caducidad de la licencia en formato 'YYYY-MM-DD'.

    Lanza:
    LicenciaCaducada: Si la licencia ha caducado.
    """
    if not ha_caducado_la_licencia(fechaCaducidad):
        raise LicenciaCaducada(
            f"{fechaCaducidad} no es una fecha vigente",
            params={'value': fechaCaducidad}
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
        help_text=_("La fecha de caducidad de la licencia."),
        validators=[validar_vigencia_licencia,]
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

def validar_placa_vehicular(placa: str):
    """Valida si una placa vehicular es válida.

    Esta función toma una placa vehicular como argumento y verifica si es válida
    utilizando la función es_una_placa_vehicular_valida del archivo utils.py.
    Si la placa no es válida, se lanza una excepción ValidationError.

    Args:
        placa (str): La placa vehicular a validar.

    Raises:
        PlacaVehicularInvalida: Si la placa vehicular no es válida.
    """
    if not es_una_placa_de_vehiculo_valida(placa):
        raise PlacaVehicularInvalida(
            f"{placa} no es una placa vehicular válida.",
            params={'value': placa}
        )

def validar_anio_fabricacion(anio: int):
    """Valida si una placa vehicular es válida.

    Esta función toma una placa vehicular como argumento y verifica si es válida
    utilizando la función es_una_placa_vehicular_valida del archivo utils.py.
    Si la placa no es válida, se lanza una excepción ValidationError.

    Args:
        placa (str): La placa vehicular a validar.

    Raises:
        PlacaVehicularInvalida: Si la placa vehicular no es válida.
    """
    if not es_un_anio_de_fabricacion_valido (anio):
        raise FechaFabricacionInvalida(
            f"{anio} no es un año de fabricación válido.",
            params={'value': anio}
        )

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
        Persona,
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
        help_text=_("La placa del vehículo."),
        validators=[validar_placa_vehicular,]
    )
    anio_de_fabricacion = models.IntegerField(
        _('Año de fabricación'),
        help_text=_("El año de fabricación del vehículo."),
        validators=[validar_anio_fabricacion,]

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
        Persona,
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

    def __str__(self) -> str:
        """Devuelve una representación legible del objeto Matricula."""
        return str(self.matricula)



def validar_codigo_dot(codigo_dot: str):
    """Valida si un código DOT es válido.

    Esta función toma un código DOT como argumento y verifica si es válido
    utilizando la función es_un_codigo_dot_valido del archivo utils.py.
    Si el código DOT no es válido, se lanza una excepción ValidationError.

    Args:
        codigo_dot (str): El código DOT a validar.

    Raises:
        CodigoDotInvalido: Si el código DOT no es válido.
    """
    if not es_un_codigo_dot_valido(codigo_dot):
        raise CodigoDotInvalido(
            f"{codigo_dot} no es un código DOT válido.",
            params={'value': codigo_dot}
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
        help_text=_("El código de fabricación de la llanta."),
        validators=[validar_codigo_dot,]
    )
    posicion_respecto_al_vehiculo = models.CharField(
        _('Posición respecto al vehículo'),
        max_length=50,
        choices=POSICIONES_LLANTA,
        help_text=_("La posición de la llanta respecto al vehículo.")
    )

    def __str__(self) -> str:
        """Devuelve una representación legible por humanos del objeto Llanta."""
        return f"Llanta {self.posicion_respecto_al_vehiculo} de {self.vehiculo}"

class Bateria(models.Model):
    """
    Representa una batería de un vehículo.

    Atributos:
        - vehiculo (Vehiculo): El vehículo al que pertenece la batería.
        - codigo_de_fabricacion (str): El código de fabricación de la batería.
    """
def validar_codigo_bateria(codigo_bateria: str):
    """Valida si una placa vehicular es válida.

    Esta función toma una placa vehicular como argumento y verifica si es válida
    utilizando la función es_una_placa_vehicular_valida del archivo utils.py.
    Si la placa no es válida, se lanza una excepción ValidationError.

    Args:
        placa (str): La placa vehicular a validar.

    Raises:
        PlacaVehicularInvalida: Si la placa vehicular no es válida.
    """
    if not es_un_codigo_bateria_valido (codigo_bateria):
        raise CodigoBateriaInvalido(
            f"{codigo_bateria} no es un código de batería válido.",
            params={'value': codigo_bateria}
        )
    vehiculo = models.ForeignKey(
        Vehiculo,
        on_delete=models.CASCADE,
        related_name='baterias',
        help_text=_("El vehículo al que pertenece la batería.")
    )
    codigo_de_fabricacion = models.CharField(
        _('Código de fabricación'),
        max_length=50,
        help_text=_("El código de fabricación de la batería."),
        validators=[validar_codigo_bateria,]
    )

    def __str__(self) -> str:
        """Devuelve una representación legible por humanos del objeto Bateria."""
        return f"Batería de {self.vehiculo}"
