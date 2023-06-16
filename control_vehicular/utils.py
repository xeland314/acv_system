"""utils.py

El módulo `utils.py` define varias clases enumeradas
que se utilizan en el módulo `models.py` para representar diferentes tipos de datos.

El módulo `utils.py` incluye las siguientes clases enumeradas:

- `TipoVehiculo`: enumera los diferentes tipos de vehículos.
- `Combustible`: enumera los diferentes tipos de combustibles.
- `CondicionVehicular`: enumera las diferentes condiciones vehiculares.
- `PosicionLlanta`: enumera las diferentes posiciones de las llantas.
- `TipoLicencia`: enumera los diferentes tipos de licencias.
- `UnidadOdometro`: enumera las diferentes unidades que puede utilizar un odómetro.
"""

from datetime import datetime
from enum import Enum
import re
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
        """
        Devuelve una lista de tuplas con los valores y nombres de los tipos de combustibles.

        Cada tupla contiene el valor y el nombre de un tipo de combustible.
        Esta lista puede ser útil para usar en campos de elección en modelos de Django.

        Returns:
            List[Tuple[str, str]]: Una lista de tuplas con los valores
            y nombres de los tipos de combustibles.
        """
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
        """
        Devuelve una lista de tuplas con los valores y nombres de las condiciones vehiculares.

        Cada tupla contiene el valor y el nombre de una condición vehicular.
        Esta lista puede ser útil para usar en campos de elección en modelos de Django.

        Returns:
            List[Tuple[str, str]]: Una lista de tuplas con los valores
            y nombres de las condiciones vehiculares.
        """
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
        """
        Devuelve una lista de tuplas con los valores y nombres de las posiciones de las llantas.

        Cada tupla contiene el valor y el nombre de una posición de llanta.
        Esta lista puede ser útil para usar en campos de elección en modelos de Django.

        Returns:
            List[Tuple[str, str]]: Una lista de tuplas con los valores
            y nombres de las posiciones de las llantas.
        """
        return [(key.value, key.name) for key in cls]

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

    @classmethod
    def choices(cls) -> List[Tuple[str, str]]:
        """
        Devuelve una lista de tuplas con los valores y nombres de los tipos de licencias.

        Cada tupla contiene el valor y el nombre de un tipo de licencia.
        Esta lista puede ser útil para usar en campos de elección en modelos de Django.

        Returns:
            List[Tuple[str, str]]: Una lista de tuplas con los valores
            y nombres de los tipos de licencias.
        """
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
        """
        Devuelve una lista de tuplas con los valores y nombres de las unidades.

        Cada tupla contiene el valor y el nombre de una unidad.
        Esta lista puede ser útil para usar en campos de elección en modelos de Django.

        Returns:
            List[Tuple[str, str]]: Una lista de tuplas con los valores y nombres de las unidades.
        """
        return [(key.value, key.name) for key in cls]

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
