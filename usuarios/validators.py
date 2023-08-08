from datetime import date
import random
import re

import phonenumbers

from .exceptions import (
    CedulaInvalida,
    FechaDeNacimientoInvalida,
    NombreInvalido,
    TelefonoInvalido
)


def calcular_digito_de_verificacion(cedula: str) -> int:
    """
    Calcula el dígito de verificación de una cédula de ciudadanía ecuatoriana.

    Args:
        - cedula (str): El número de cédula de ciudadanía ecuatoriana.
    Returns:
        - int: El dígito de verificación calculado.
    Based on: https://publiblog-ec.blogspot.com/2019/01/verificador-cedula-ciudadania.html
    """
    coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
    total = sum(map(
        lambda x: x[0] if x[0] < 10 else x[0] - 9,
        [(int(cedula[i]) * coeficientes[i],) for i in range(9)]
    ))
    return (10 - total % 10) % 10

def generar_cedula_ecuatoriana() -> str:
    """
    Genera un número de cédula de ciudadanía ecuatoriana válido.

    La cédula se genera de la siguiente manera:
    - Se genera el código de la provincia (los dos primeros dígitos).
    - Se genera el tercer dígito.
    - Se generan los siguientes seis dígitos.
    - Se calcula el dígito de verificación utilizando el algoritmo Módulo 10.

    Returns:
        Una cadena de texto que representa un número de cédula de ciudadanía ecuatoriana válido.
    """
    # Generate the first two digits (province code)
    codigo_provincial = random.randint(0, 24)
    if codigo_provincial == 0:
        codigo_provincial = 30
    cedula = str(codigo_provincial).zfill(2)

    # Generate the third digit
    tercer_digito = random.randint(0, 6)
    cedula += str(tercer_digito)

    # Generate the next six digits
    for _ in range(6):
        cedula += str(random.randint(0, 9))

    # Calculate the verification digit using the Module 10 algorithm
    coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
    total = 0
    for i in range(9):
        product = int(cedula[i]) * coeficientes[i]
        if product >= 10:
            product -= 9
        total += product
    digito_de_verificacion = (total % 10 != 0) * (10 - total % 10)

    # Add the verification digit to the id_number
    cedula += str(digito_de_verificacion)

    return cedula

def es_una_cedula_valida(cedula: str) -> bool:
    """Verifica si una cédula ecuatoriana es válida.
    
    Esta función toma como argumento una cadena de texto
    que representa una cédula ecuatoriana y
    devuelve un valor booleano que indica si la cédula es válida o no.
    La función utiliza el algoritmo de validación
    de cédulas ecuatorianas para verificar la validez de la cédula.
    
    Args:
        - cedula (str): La cédula a validar.
    Returns:
        - bool: `True` si la cédula es válida, `False` en caso contrario.
    """
    # Check if the id_number has 10 digits and only contains numeric characters
    if not cedula.isdigit() or len(cedula) != 10:
        return False
    # Check if the first two digits are between 0 and 24 or equal to 30
    codigo_provincial = int(cedula[:2])
    if not (0 <= codigo_provincial <= 24 or codigo_provincial == 30):
        return False
    # Check if the third digit is less than or equal to 6
    tercer_digito = int(cedula[2])
    if tercer_digito > 6:
        return False
    # Calculate the verification digit using the Module 10 algorithm
    digito_de_verificacion_calculado = calcular_digito_de_verificacion(cedula)
     # Check if the calculated verification digit matches the given verification digit
    return digito_de_verificacion_calculado == int(cedula[9])

def es_bisiesto(year: int) -> bool:
    """Verifica si un año es bisiesto.
    
    Args:
        - year (int): El año a verificar.
    Returns:
        - bool: True si el año es bisiesto, False en caso contrario.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def contar_anios_bisiestos(desde: int, hasta: int) -> int:
    """Cuenta la cantidad de años bisiestos entre dos años.
    
    Args:
        - desde (int): El año inicial.
        - hasta (int): El año final.
    Returns:
        - int: La cantidad de años bisiestos entre los dos años (incluyendo los años inicial y final).
    """
    return sum([1 for year in range(desde, hasta) if es_bisiesto(year)])

def es_mayor_de_edad(fecha_nacimiento: date) -> bool:
    """Verifica si una fecha de nacimiento corresponde a una persona mayor de edad.
    
    Args:
        - fecha_nacimiento (date): La fecha de nacimiento a validar.
    Returns:
        - bool: True si la fecha de nacimiento corresponde a una persona mayor de edad, False en caso contrario.
    """
    hoy = date.today()
    edad = hoy.year - fecha_nacimiento.year - (
        (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day)
    )
    if edad >= 18:
        return True
    elif edad == 17 and hoy.month == fecha_nacimiento.month and hoy.day == fecha_nacimiento.day:
        anos_bisiestos = contar_anios_bisiestos(fecha_nacimiento.year, hoy.year)
        dias = (hoy - fecha_nacimiento).days - anos_bisiestos
        return dias >= 365 * 18
    else:
        return False

def es_un_numero_de_telefono_valido(telefono: str) -> bool:
    """
    Verifica si un número de teléfono o celular en Ecuador es válido.

    Args:
        - telefono (str): El número de teléfono o celular a validar.
    Returns:
        - bool: True si el número es válido, False en caso contrario.
    """
    try:
        parsed_number = phonenumbers.parse(telefono, "EC")
        return phonenumbers.is_valid_number(parsed_number)
    except phonenumbers.phonenumberutil.NumberParseException:
        return False

def es_un_nombre_valido(nombres:str) -> bool:
    """
    Verifica si un nombre es válido según ciertos criterios.
    Args:
        - nombres (str): El nombre a validar.
    Returns:
        - bool: True si el nombre es válido, False en caso contrario.
    """
    if nombres.strip() == "":
        return False
    patron = re.compile(r'^[A-Za-zÁ-ú ]+$')
    if patron.match(nombres):
        palabras = nombres.count(' ') + 1
        if palabras >= 1:
            return True
    return False

def validar_cedula(cedula: str):
    """Valida si una cédula es válida.

    Esta función toma una cédula como argumento y verifica si es válida
    utilizando la función es_una_cedula_valida del archivo utils.py.
    Si la cédula no es válida, se lanza una excepción ValidationError.

    Args:
        cedula (str): La cédula a validar.

    Raises:
        CedulaInvalida: Si la cédula no es válida.
    """
    if not es_una_cedula_valida(cedula):
        raise CedulaInvalida(
            f"{cedula} no es una cédula válida.",
            params={'value': cedula}
        )

def validar_fecha_de_nacimiento(fecha_nacimiento: date):
    """Valida si una fecha de nacimiento es válida.

    Esta función toma una fecha de nacimiento como argumento y verifica si es válida
    utilizando la función es_una_fecha_de_nacimiento_valida.
    Si la fecha de nacimiento no es válida, se lanza una excepción ValidationError.

    Args:
        fecha_nacimiento (date): La fecha de nacimiento a validar.

    Raises:
        FechaDeNacimientoInvalida: Si la fecha de nacimiento no es válida.
    """
    if not es_mayor_de_edad(fecha_nacimiento):
        raise FechaDeNacimientoInvalida(params={'value': fecha_nacimiento})

def validar_numero_de_telefono(telefono: str):
    """Valida si un número de teléfono es válido.

    Esta función toma un número de teléfono como argumento y verifica si es válido
    utilizando la función es_un_numero_de_telefono_valido del archivo utils.py.
    Si el número de teléfono no es válido, se lanza una excepción ValidationError.

    Args:
        telefono (str): El número de teléfono a validar.

    Raises:
        TelefonoInvalido: Si el número de teléfono no es válido.
    """
    if not es_un_numero_de_telefono_valido(telefono):
        raise TelefonoInvalido(params={'value': telefono})

def validar_nombres_apellidos(nombres: str):
    """
    Valida los nombres o apellidos según ciertos criterios.

    Args:
        nombres (str): Los nombres o apellidos a validar.

    Raises:
        NombreInvalido: Si el nombre o apellido no es válido.
    """

    if not es_un_nombre_valido(nombres):
        raise NombreInvalido(params={'value': nombres})

