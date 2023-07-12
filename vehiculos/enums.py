from enum import Enum
from typing import List, Tuple

class Combustible(Enum):
    """
    Enumeración de los diferentes tipos de combustibles.
    """
    GASOLINA = "Gasolina"
    DIESEL = "Diésel"
    GAS = "Gas"
    ELECTRICO = "Eléctrico"

    @classmethod
    def choices(cls) -> List[Tuple[str, str]]:
        return [(key.value, key.name) for key in cls]

class CondicionVehicular(Enum):
    """
    Enumeración de las diferentes condiciones vehiculares.
    """
    OPERABLE = "Operable"
    NO_OPERABLE = "No operable"
    EN_MANTENIMIENTO = "En mantenimiento"

    @classmethod
    def choices(cls) -> List[Tuple[str, str]]:
        return [(key.value, key.name) for key in cls]

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

    @classmethod
    def choices(cls) -> List[Tuple[str, str]]:
        return [(key.value, key.name) for key in cls]

class UnidadOdometro(Enum):
    """
    Enumeración de las diferentes unidades para medir un kilometraje.
    """
    KILOMETROS = 'km'
    MILLAS = 'mi'
    DIAS = 'días'

    @classmethod
    def choices(cls) -> List[Tuple[str, str]]:
        return [(key.value, key.name) for key in cls]
