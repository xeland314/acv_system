"""utils.py

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

from enum import Enum

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

COMBUSTIBLES = [(tag.name, tag.value) for tag in Combustible]
TIPOS_VEHICULO = [(tag.name, tag.value) for tag in TipoVehiculo]
CONDICIONES_VEHICULARES = [(tag.name, tag.value) for tag in CondicionVehicular]
POSICIONES_LLANTA = [(tag.name, tag.value) for tag in PosicionLlanta]
TIPOS_LICENCIA = [(tag.name, tag.value) for tag in TipoLicencia]
