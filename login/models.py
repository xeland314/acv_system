"""models.py

Este módulo define el modelo Persona para almacenar información
sobre personas en la base de datos.

Autor: Christopher Villamarín (@xeland314)
Dependencias: django.contrib.auth.models.User, django.db.models
"""

from django.contrib.auth.models import User
from django.db import models

from .utils import NIVELES_EDUCACION, ESTADOS_CIVILES

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
    cedula = models.CharField('Cédula', max_length=10, blank=False)
    email = models.EmailField('Email', max_length=100, blank=False)
    telefono = models.CharField('Teléfono', max_length=15, blank=False)
    fecha_nacimiento = models.DateField('Fecha de nacimiento', blank=False)
    nivel_educacion = models.CharField(
        'Nivel de educación', max_length=30, choices=NIVELES_EDUCACION
    )
    estado_civil = models.CharField(
        'Estado Civil', max_length=20, choices=ESTADOS_CIVILES
    )
    fotografia = models.ImageField('Fotografía', null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.cedula} - {self.nombres} {self.apellidos}"
