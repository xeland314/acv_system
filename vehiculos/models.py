from django.db import models
from django.utils.translation import gettext_lazy as _

from usuarios.models import PerfilUsuario

from .enums import (
    Combustible,
    CondicionVehicular,
    PosicionLlanta,
    UnidadCarburante,
    UnidadOdometro
)
from .validators import (
    validar_anio_fabricacion,
    validar_codigo_bateria,
    validar_codigo_dot,
    validar_placa_vehicular
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

class Vehiculo(models.Model):
    """
    Representa un vehículo.
    """
    id = models.BigAutoField(primary_key=True)
    propietario = models.ForeignKey(
        PerfilUsuario,
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
    unidad_carburante = models.CharField(
        _('Unidad carburante'),
        max_length=8,
        choices=UnidadCarburante.choices(),
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

    class Meta:
        verbose_name = _("Vehículo")
        verbose_name_plural = _("Vehículos")

    def __str__(self) -> str:
        return f"Vehículo #{self.id}: {self.placa} - {self.modelo} - {self.anio_de_fabricacion}"

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
