"""utils.py

Este módulo define varias clases y funciones de utilidad para el proyecto,
incluyendo clases de enumeración para representar
estados civiles y niveles de educación, y funciones
para validar cédulas y números de teléfono en Ecuador.

Autor: Christopher Villamarín (@xeland314)
Dependencias: enum.Enum, re
"""

from datetime import date
from enum import Enum
import re

class EstadoCivil(Enum):
    """
    Clase enumeración para representar los diferentes estados civiles.
    """

    CASADO = "Casado"
    DIVORCIADO = "Divorciado"
    SOLTERO = "Soltero"
    UNION_LIBRE = "Unión Libre"
    VIUDO = "Viudo"

class NivelEducacion(Enum):
    """
    Clase enumeración para representar los diferentes niveles de educación.
    """

    GENERAL_BASICA = "General Básica"
    BACHILLERATO = "Bachillerato"
    SUPERIOR = "Superior"

# Lista con los valores de la clase enumeración EstadoCivil
ESTADOS_CIVILES = [(tag.value, tag.name) for tag in EstadoCivil]

# Lista con los valores de la clase enumeración NivelEducacion
NIVELES_EDUCACION = [(tag.value, tag.name) for tag in NivelEducacion]

def es_una_cedula_valida(cedula: str) -> bool:
    """Verifica si una cédula ecuatoriana es válida.

    Esta función toma como argumento una cadena de texto
    que representa una cédula ecuatoriana y
    devuelve un valor booleano que indica si la cédula es válida o no.
    La función utiliza el algoritmo de validación
    de cédulas ecuatorianas para verificar la validez de la cédula.

    Args:
        cedula (str): La cédula a validar.

    Returns:
        bool: `True` si la cédula es válida, `False` en caso contrario.
    """
    coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]

    if len(cedula) != 10:
        return False

    tercer_digito = int(cedula[2])
    if tercer_digito < 0 or tercer_digito > 5:
        return False

    total = 0
    for i in range(9):
        valor = int(cedula[i]) * coeficientes[i]
        total += valor // 10 + valor % 10
    verificador = total % 10
    if verificador == 0:
        return int(cedula[9]) == verificador

    return int(cedula[9]) == (10 - verificador)

def es_una_fecha_de_nacimiento_valida(fecha_nacimiento: date) -> bool:
    """Verifica si una fecha de nacimiento es válida.

    Esta función toma una fecha de nacimiento como argumento y verifica si
    la persona es mayor de edad (mayor o igual a 18 años).

    Args:
        fecha_nacimiento (date): La fecha de nacimiento a validar.

    Returns:
        bool: True si la fecha de nacimiento es válida, False en caso contrario.
    """
    hoy = date.today()
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    if edad >= 18:
        return True
    elif edad == 17 and hoy.month == fecha_nacimiento.month and hoy.day == fecha_nacimiento.day:
        anos_bisiestos = 0
        for year in range(fecha_nacimiento.year, hoy.year):
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                anos_bisiestos += 1
        dias = (hoy - fecha_nacimiento).days - anos_bisiestos
        return dias >= 365 * 18
    else:
        return False

def es_un_numero_de_telefono_valido(telefono: str) -> bool:
    """Verifica si un número de teléfono o celular en Ecuador es válido.

    Esta función toma como argumento una cadena de texto
    que representa un número de teléfono o celular en Ecuador
    y devuelve un valor booleano que indica si el número es válido o no.
    La función utiliza una expresión regular para verificar
    si el número cumple con el formato esperado.

    Args:
        telefono (str): El número de teléfono o celular a validar.

    Returns:
        bool: `True` si el número es válido, `False` en caso contrario.
    """
    patron = r"^(593|\+593|0)9\d{8}$"
    return bool(re.match(patron, telefono))
