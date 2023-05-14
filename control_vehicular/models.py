from datetime import date
from django.db import models

from .utils import Combustible, CondicionVehicular, PosicionLlanta, TipoLicencia
from login.models import Persona

class Licencia(models.Model):

    tipo = models.CharField(max_length=2, choices=[(tag.name, tag.value) for tag in TipoLicencia])
    fecha_de_caducidad = models.DateField()
    es_profesional = models.BooleanField()

    def __str__(self):
        return f'{self.tipo} - {self.fecha_de_caducidad}'

    def esta_vigente(self):
        "Retorna la validez de la licencia en el tiempo."
        return date.today() <= self.fecha_de_caducidad

class Conductor(Persona):

    licencia = models.OneToOneField(Licencia, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.cedula} - {self.nombres} {self.apellidos} - {self.licencia}'

class Vehiculo(models.Model):
    marca = models.CharField('Marca', max_length=50)
    modelo = models.CharField('Modelo', max_length=50)
    placa = models.CharField('Placa', max_length=10, unique=True)
    anio_de_fabricacion = models.PositiveSmallIntegerField('Año de fabricación')
    color = models.CharField('Color', max_length=50)
    cilindraje = models.FloatField('Cilindraje')
    tonelaje = models.FloatField('Tonelaje')
    unidad_carburaje = models.FloatField('Unidad de carburaje')
    combustible = models.CharField('Combustible', max_length=30, choices=zip(tuple(map(str, Combustible)), tuple(map(str, Combustible))))
    condicion = models.CharField('Condición vehicular', max_length=30, choices=zip(tuple(map(str, CondicionVehicular)), tuple(map(str, CondicionVehicular))))
    fotografia = models.ImageField('Fotografía', upload_to='vehiculos', null=True, blank=True)

class Matricula(models.Model):
    vehiculo = models.OneToOneField(Vehiculo, on_delete=models.CASCADE, related_name='matricula')
    matricula = models.CharField('Matrícula', max_length=50, unique=True)
    foto = models.ImageField('Fotografía', upload_to='matriculas', null=True, blank=True)

class Llanta(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='llantas')
    codigo_de_fabricacion = models.CharField('Código de fabricación', max_length=50)
    posicion_respecto_al_vehiculo = models.CharField('Posición respecto al vehículo', max_length=50, choices=zip(tuple(map(str, PosicionLlanta)), tuple(map(str, PosicionLlanta))))
