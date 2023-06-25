"""
utils.py

El módulo `utils.py` define varias clases enumeradas
que se utilizan en el módulo `models.py` para representar diferentes tipos de datos.

El módulo `utils.py` incluye las siguientes clases enumeradas:

- `TipoVehiculo`: enumera los diferentes tipos de vehículos.
- `Combustible`: enumera los diferentes tipos de combustibles.
- `CondicionVehicular`: enumera las diferentes condiciones vehiculares.
- `PosicionLlanta`: enumera las diferentes posiciones de las llantas.
- `TipoLicencia`: enumera los diferentes tipos de licencias.

También se incluyen las siguientes variables que contienen
las opciones posibles de cada enumeración:

- `COMBUSTIBLES`: una lista de tuplas con las opciones posibles de combustible.
- `TIPOS_VEHICULO`: una lista de tuplas con las opciones posibles de tipo de vehículo.
- `CONDICIONES_VEHICULARES`: una lista de tuplas con las opciones
    posibles de condiciones vehiculares.
- `POSICIONES_LLANTA`: una lista de tuplas con las opciones posibles de posiciones de llantas.
- `TIPOS_LICENCIA`: una lista de tuplas con las opciones posibles de tipos de licencia.
"""

from datetime import datetime
from enum import Enum
import re

class TipoVehiculo(Enum):
    """
    Enumeración de los diferentes tipos de vehículos.
    """
    CAMION = "Camión"
    CAMIONETA = "Camioneta"
    AUTOMOVIL = "Automóvil"
    MOTOCICLETA = "Motocicleta"
    BUS = "Bus"
    TRACTOR = "Tractor"

class Combustible(Enum):
    """
    Enumeración de los diferentes tipos de combustibles.
    """
    GASOLINA = "Gasolina"
    DIESEL = "Diésel"
    GAS = "Gas"
    ELECTRICO = "Eléctrico"

class CondicionVehicular(Enum):
    """
    Enumeración de las diferentes condiciones vehiculares.
    """
    OPERABLE = "Operable"
    NO_OPERABLE = "No operable"
    EN_MANTENIMIENTO = "En mantenimiento"

class PosicionLlanta(Enum):
    """
    Enumeración de las diferentes posiciones de las llantas.
    """
    DERECHO_DELANTERO = "Derecho delantero"
    DERECHO_POSTERIOR = "Derecho posterior"
    DERECHO_POSTERIOR_EXTERIOR = "Derecho posterior exterior"
    DERECHO_POSTERIOR_INTERIOR = "Derecho posterior interior"
    IZQUIERDO_DELANTERO = "Izquierdo delantero"
    IZQUIERDO_POSTERIOR = "Izquierdo posterior"
    IZQUIERDO_POSTERIOR_EXTERIOR = "Izquierdo posterior exterior"
    IZQUIERDO_POSTERIOR_INTERIOR = "Izquierdo posterior interior"
    REPUESTO = "Respuesto"

class TipoLicencia(Enum):
    """
    Enumeración de los diferentes tipos de licencias.
    """
    A = 'A'
    B = 'B'
    F = 'F'
    A1 = 'A1'
    C = 'C'
    C1 = 'C1'
    D = 'D'
    D1 = 'D1'
    E = 'E'
    E1 = 'E1'

COMBUSTIBLES = [(tag.value, tag.name) for tag in Combustible]
TIPOS_VEHICULO = [(tag.value, tag.name) for tag in TipoVehiculo]
CONDICIONES_VEHICULARES = [(tag.value, tag.name) for tag in CondicionVehicular]
POSICIONES_LLANTA = [(tag.value, tag.name) for tag in PosicionLlanta]
TIPOS_LICENCIA = [(tag.value, tag.name) for tag in TipoLicencia]

def es_una_placa_de_vehiculo_valida(placa: str) -> bool:
    """
    Esta función solo verifica si el formato de la placa es válido.
    No verifica si la placa está registrada en el SRI o ANT.
    """
    patron_vehiculo = r'^[A-Z]{3}\-\d{4}$'
    patron_moto = r'^[A-Z]{2}\-\d{3}[A-Z]?$'
    return bool(re.match(patron_vehiculo, placa) or re.match(patron_moto, placa))

def es_un_codigo_dot_valido(codigo: str) -> bool:
    """
    Verifica si un código DOT tiene el formato correcto.

    Un código DOT (Departamento de Transporte) se encuentra
    en el flanco de las llantas de los automóviles y proporciona
    información sobre la llanta, incluyendo su fecha de fabricación.
    Un código DOT válido tiene el formato `DOT-XXXX-XXXX-XXXX`,
    donde `X` puede ser una letra mayúscula o un dígito.

    Args:
        codigo (str): El código DOT a verificar.

    Returns:
        bool: True si el código DOT tiene el formato correcto, False en caso contrario.
    """

    patron = r'^DOT-[A-Z0-9]{4}-[A-Z0-9]{4}-\d{4}$'
    return bool(re.match(patron, codigo))

def es_un_anio_de_fabricacion_valido(anio: int):
    """
    Valida si el año de fabricación de un vehículo es válido.

    Args:
    anio (int): El año de fabricación a validar.

    Returns:
    bool: True si el año de fabricación es válido, False en caso contrario.
    """
    anio_actual = datetime.now().year
    return anio > 1900 and anio <= anio_actual

    
def es_un_codigo_bateria_valido(codigo_bateria: str):
    """
    Verifica si un código de batería es válido.
    Args:
        codigo_bateria (str): El código de batería a verificar.
    Returns:
        bool: True si el código de batería es válido, False en caso contrario.
    """
    # Expresión regular para validar el código de batería
    patron = r'^(?=.*\d)(?=.*[a-zA-Z])[\w\d]{8,}$'
    # Comprobar si el código de batería coincide con el patrón
    coincidencia = re.match(patron, codigo_bateria)
    # Devolver True si hay coincidencia, False si no hay coincidencia
    return bool(coincidencia)

    
def obtener_fecha_fabricacion(codigo_dot: str) -> datetime:
    """
    Obtiene la fecha de fabricación de una llanta a partir de su código DOT.

    Un código DOT (Departamento de Transporte) se encuentra
    en el flanco de las llantas de los automóviles y proporciona
    información sobre la llanta, incluyendo su fecha de fabricación.
    Los últimos cuatro dígitos del código DOT indican
    la fecha de fabricación de la llanta: 
    los primeros dos dígitos indican la semana del año
    en que fue fabricada y los últimos dos dígitos indican el año.

    Args:
        codigo_dot (str): El código DOT de la llanta.

    Returns:
        datetime: La fecha de fabricación de la llanta.
    """
    # Extraer la fecha de fabricación del código DOT
    fecha_fabricacion_str = codigo_dot[-4:]
    semana_fabricacion = int(fecha_fabricacion_str[:2])
    anio_fabricacion = int(fecha_fabricacion_str[2:])

    # Calcular la fecha de fabricación
    fecha_fabricacion = datetime.strptime(
        f'20{anio_fabricacion}-W{semana_fabricacion}-1', '%Y-W%W-%w'
    )

    return fecha_fabricacion


def ha_caducado_la_licencia(fechaCaducidad: str):
    """
    Verifica si una licencia ha caducado en base a la fecha de caducidad proporcionada.

    Args:
        fechaCaducidad (str): Fecha de caducidad en formato 'YYYY-MM-DD'.

    Returns:
        bool: True si la licencia ha caducado, False en caso contrario.
    """
    # Obtener la fecha actual
    fecha_actual = datetime.now().date()
    # Convertir la fecha de caducidad a objeto de fecha
    fecha_caducidad = datetime.strptime(fechaCaducidad, '%Y-%m-%d').date()
    # Comparar la fecha de caducidad con la fecha actual
    return fecha_caducidad > fecha_actual

    

