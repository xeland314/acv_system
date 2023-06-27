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

from login.models import Trabajador

from .exceptions import CodigoDotInvalido, PlacaVehicularInvalida, FechaFabricacionInvalida, CodigoBateriaInvalido, LicenciaCaducada
from .utils import (
    Combustible, CondicionVehicular,
    PosicionLlanta, TipoLicencia,
    UnidadOdometro,
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
        choices=TipoLicencia.choices(),
        help_text=_("El tipo de la licencia (A, B, C, etc.).")
    )
    fecha_de_emision = models.DateField(
        blank=False,
        help_text=_("La fecha de emisión de la licencia.")
    )
    fecha_de_caducidad = models.DateField(
        blank=False,
        help_text=_("La fecha de caducidad de la licencia."),
        validators=[validar_vigencia_licencia,]
    )
    puntos = models.PositiveSmallIntegerField(
        blank=False,
        help_text=_("Puntos vigentes de la licencia.")
    )

    def __str__(self):
        return f'{self.tipo} - {self.fecha_de_caducidad}'

    def esta_vigente(self):
        "Retorna la validez de la licencia en el tiempo."
        return date.today() <= self.fecha_de_caducidad

class Conductor(Trabajador):
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

def validar_anio_fabricacion(anio: int) -> None:
    """
    Valida si un año de fabricación es válido.

    Parámetros:
    - anio (int): El año de fabricación a validar.

    Excepciones:
    - FechaFabricacionInvalida: Si el año de fabricación no es válido.

    """
    if not es_un_anio_de_fabricacion_valido (anio):
        raise FechaFabricacionInvalida(
            f"El año {anio} de fabricación está fuera de los límites.",
            params={'value': anio}
        )

class Kilometraje(models.Model):
    """
    Representa el odómetro de un vehículo.

    Atributos:
        - vehiculo (Vehiculo): El vehículo al que pertenece el odómetro.
        - kilometraje (float): El kilometraje recorrido por el vehículo.
        - unidad (str): La unidad de medida del kilometraje.
        - fecha_inicial (DateField): La fecha inicial de uso del vehículo.
    """
    vehiculo = models.ForeignKey(
        'Vehiculo',
        related_name='bitacora_kilometraje',
        on_delete=models.CASCADE,
        help_text=_("El vehículo al que pertenece el odómetro.")
    )
    kilometraje = models.DecimalField(
        _('Kilometraje'),
        max_digits=10,
        decimal_places=2,
        blank=False,
        help_text=_("El kilometraje recorrido por el vehículo.")
    )
    unidad = models.CharField(
        _('Unidad'),
        max_length=10,
        blank=False,
        choices=UnidadOdometro.choices(),
        help_text=_("La unidad de medida del kilometraje.")
    )
    fecha = models.DateField(
        _('Fecha'),
        blank=False,
        help_text=_("La fecha en la que se registro X kilometraje.")
    )

    class Meta:
        verbose_name = _("Kilometraje")
        verbose_name_plural = _("Kilometrajes")

    def __str__(self):
        return f'{self.vehiculo}: {self.kilometraje} {self.unidad} - {self.fecha}'

class Propietario(Trabajador):
    """
    Representa un conductor.

    Atributos:
        - heredados de Persona.

    Métodos:
        __str__(): Retorna una representación en string del propietario.
    """
    class Meta:
        verbose_name = _("Propietario")
        verbose_name_plural = _("Propietarios")

    def __str__(self):
        return f'{self.cedula} - {self.nombres} {self.apellidos}'

class Vehiculo(models.Model):
    """
    Representa un vehículo.

    Atributos:
        - cilindraje (float): El cilindraje del vehículo.
        - tonelaje (float): El tonelaje del vehículo.
        - unidad_carburante (float): La unidad de carburante del vehículo.
        - combustible (str): El tipo de combustible del vehículo.
        - condicion (str): La condición vehicular del vehículo.
        - marca (str): La marca del vehículo.
        - modelo (str): El modelo del vehículo.
        - placa (str): La placa del vehículo.
        - anio_de_fabricacion (int): El año de fabricación del vehículo.
        - color (str): El color del vehículo.
        - matricula (str): El número de la matrícula.
        - foto_matricula(ImageField): La fotografía de la matrícula.
        - foto_vehiculo (ImageField): La fotografía del vehículo.
    """
    id = models.BigAutoField(primary_key=True)
    propietario = models.ForeignKey(
        Propietario,
        on_delete=models.CASCADE,
        related_name='vehiculos',
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
    anio_de_fabricacion = models.PositiveIntegerField(
        _('Año de fabricación'),
        help_text=_("El año de fabricación del vehículo."),
        validators=[validar_anio_fabricacion,]

    )
    cilindraje = models.DecimalField(
        _('Cilindraje'),
        max_digits=10,
        decimal_places=4,
        help_text=_("El cilindraje del vehículo.")
    )
    color = models.CharField(
        _('Color'),
        max_length=50,
        help_text=_("El color del vehículo.")
    )
    combustible = models.CharField(
        _('Combustible'),
        max_length=30,
        choices=Combustible.choices(),
        help_text=_("El tipo de combustible del vehículo.")
    )
    condicion = models.CharField(
        _('Condición vehicular'),
        max_length=30,
        choices=CondicionVehicular.choices(),
        help_text=_("La condición vehicular del vehículo.")
    )
    foto_matricula = models.ImageField(
        _('Fotografía de la matrícula'),
        upload_to='vehiculos',
        null=True,
        blank=True,
        help_text=_("La fotografía de la matrícula.")
    )
    foto_vehiculo = models.ImageField(
        _('Fotografía del vehículo'),
        upload_to='vehiculos',
        null=True,
        blank=True,
        help_text=_("La fotografía del vehículo.")
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
    numero_de_chasis = models.CharField(
        _('Número del chasis'),
        max_length=20,
        unique=True,
        help_text=_("Número de chasis del motor."),
    )
    placa = models.CharField(
        _('Placa'),
        max_length=10,
        unique=True,
        help_text=_("La placa del vehículo."),
        validators=[validar_placa_vehicular,]
    )
    tonelaje = models.DecimalField(
        _('Tonelaje'),
        max_digits=10,
        decimal_places=2,
        help_text=_("El tonelaje del vehículo.")
    )
    unidad_carburante = models.DecimalField(
        _('Unidad carburante'),
        max_digits=10,
        decimal_places=4,
        help_text=_("La unidad de carburante del vehículo.")
    )

    def agregar_kilometraje(self, valor, unidad):
        """
        Agrega un nuevo registro de kilometraje al odómetro del vehículo.

        Args:
            valor (float): El valor del kilometraje a agregar.
            unidad (str): La unidad de medida del kilometraje.
        """
        Kilometraje.objects.create(valor=valor, unidad=unidad, vehiculo=self)

    @property
    def bitacora(self):
        """
        Retorna la bitácora de kilometraje del vehículo ordenada por fecha.

        Returns:
            QuerySet: La bitácora de kilometraje del vehículo ordenada por fecha.
        """
        return self.bitacora_kilometraje.order_by('-fecha')

    class Meta:
        verbose_name = _("Vehículo")
        verbose_name_plural = _("Vehículos")

    def __str__(self) -> str:
        return f"Vehículo #{self.id}: {self.placa} - {self.modelo} - {self.anio_de_fabricacion}"


class HojaMantenimiento(models.Model):
    """
    Representa una hoja de mantenimiento para un vehículo.

    Atributos:
        - vehiculo (Vehiculo): El vehículo al que pertenece la hoja de mantenimiento.
        - operaciones (list[Operacion]): Las operaciones de mantenimiento a realizar en el vehículo.
    """
    vehiculo = models.OneToOneField(
        Vehiculo,
        on_delete=models.CASCADE,
        help_text=_("El vehículo al que pertenece la hoja de mantenimiento.")
    )
    frecuencia_minima = models.DecimalField(
        _('Frecuencia mínima'),
        max_digits=10,
        decimal_places=2,
        blank=False,
        help_text=_("El kilometraje/tiempo mínimo en el que se deben realizar las operaciones.")
    )
    final_ciclo = models.DecimalField(
        _('Final de ciclo de mantenimiento'),
        max_digits=10,
        decimal_places=2,
        blank=False,
        help_text=_("El kilometraje/tiempo límite que marca el fin de cada ciclo de mantenimiento.")
    )
    unidad = models.CharField(
        _('Unidad'),
        max_length=10,
        blank=False,
        choices=UnidadOdometro.choices(),
        help_text=_("La unidad de medida del kilometraje.")
    )

    class Meta:
        verbose_name = _("Hoja de mantenimiento")
        verbose_name_plural = _("Hojas de mantenimiento")

    def __str__(self):
        return (
            f'{self.vehiculo}'
            f' - Frecuencia mínima: {self.frecuencia_minima} {self.unidad}'
            f' - Final de ciclo: {self.final_ciclo} {self.unidad}'
        )

class OperacionMantenimiento(models.Model):
    """
    Representa una operación de mantenimiento.

    Atributos:
        - hoja_mantenimiento: Hoja de mantenimiento a la que pertenece
        esta operacion de mantenimiento.
        - tarea (str): La tarea a realizar en la operación.
        - sistema (str): El sistema del vehículo al que pertenece la operación.
        - sub_sistema (str): El sub-sistema del vehículo al que pertenece la operación.
        - frecuencia (float): La frecuencia en el que se debe realizar la operación.
        - unidad (str): La unidad de medida de la frecuencia: horas, km, etc.
    """
    hoja_mantenimiento = models.ForeignKey(
        HojaMantenimiento,
        on_delete=models.CASCADE,
        related_name='operaciones_de_mantenimiento',
        help_text=_("Hoja mantenimiento a la que pertenece este mantenimiento.")
    )
    tarea = models.CharField(
        _('Tarea'),
        max_length=50,
        blank=False,
        help_text=_("La tarea a realizar en la operación.")
    )
    sistema = models.CharField(
        _('Sistema'),
        max_length=50,
        blank=False,
        help_text=_("El sistema del vehículo al que pertenece la operación.")
    )
    sub_sistema = models.CharField(
        _('Sub-sistema'),
        max_length=50,
        blank=False,
        help_text=_("El sub-sistema del vehículo al que pertenece la operación.")
    )
    frecuencia = models.DecimalField(
        _('Frecuencia'),
        max_digits=10,
        decimal_places=2,
        blank=False,
        help_text=_("El kilometraje/tiempo en el que se debe realizar la operación.")
    )
    unidad = models.CharField(
        _('Unidad'),
        max_length=10,
        blank=False,
        choices=UnidadOdometro.choices(),
        help_text=_("La unidad de medida del kilometraje.")
    )

    class Meta:
        verbose_name = _("Operación de mantenimiento")
        verbose_name_plural = _("Operaciones de mantenimiento")

    def __str__(self):
        return f'{self.tarea}: {self.sub_sistema} cada {self.frecuencia} {self.unidad}'


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
        choices=PosicionLlanta.choices(),
        help_text=_("La posición de la llanta respecto al vehículo.")
    )

    def __str__(self) -> str:
        """Devuelve una representación legible por humanos del objeto Llanta."""
        return f"Llanta {self.posicion_respecto_al_vehiculo} de {self.vehiculo}"

def validar_codigo_bateria(codigo_bateria: str) -> None:
    """
    Valida si un código de batería es válido.

    Parámetros:
    - codigo_bateria (str): El código de batería a validar.

    Excepciones:
    - CodigoBateriaInvalido: Si el código de batería no es válido.

    """

    if not es_un_codigo_bateria_valido(codigo_bateria):
        raise CodigoBateriaInvalido(
            f"{codigo_bateria} no es un código de batería válido.",
            params={'value': codigo_bateria}
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
        help_text=_("El código de fabricación de la batería."),
        validators=[validar_codigo_bateria,]
    )

    def __str__(self) -> str:
        """Devuelve una representación legible por humanos del objeto Bateria."""
        return f"Batería de {self.vehiculo}"
