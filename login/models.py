from django.contrib.auth.models import User
from django.db import models

from .utils import NIVELES_EDUCACION, ESTADOS_CIVILES

class Persona(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombres = models.CharField('Nombres', max_length=150, blank=False)
    apellidos = models.CharField('Apellidos', max_length=150, blank=False)
    cedula = models.CharField('Cédula', max_length=10, blank=False)
    email = models.EmailField('Email', max_length=100, blank=True)
    telefono = models.CharField('Teléfono', max_length=15, blank=True)
    fecha_nacimiento = models.DateField('Fecha de nacimiento', blank=False)
    nivel_educacion = models.CharField(
        'Nivel de educación', max_length=30, choices=zip(NIVELES_EDUCACION, NIVELES_EDUCACION)
    )
    estado_civil = models.CharField(
        'Estado Civil', max_length=20, choices=zip(ESTADOS_CIVILES, ESTADOS_CIVILES)
    )
    fotografia = models.ImageField('Fotografía', null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.cedula} - {self.nombres} {self.apellidos}"
