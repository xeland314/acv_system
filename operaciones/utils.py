"""utils.py

Este módulo define varias clases y funciones de utilidad para el proyecto,
incluyendo clases de enumeración para representar
los estados de cumplimiento

Autor: Christopher Villamarín (@xeland314)
Dependencias: enum.Enum
"""

from enum import Enum
from typing import List, Tuple

class EstadoCumplimiento(Enum):
    """Clase enumeración para representar el cumplimiento de una inspección."""
    PENDIENTE = "Pendiente"
    CUMPLIDO = "Cumplido"

    @classmethod
    def choices(cls) -> List[Tuple[str, str]]:
        """
        Devuelve una lista de tuplas con los valores y nombres de los estados de cumplimiento.

        Cada tupla contiene el valor y el nombre de un estado de cumplimiento.
        Esta lista puede ser útil para usar en campos de elección en modelos de Django.

        Returns:
            List[Tuple[str, str]]: Una lista de tuplas con los valores
            y nombres de los estados de cumplimiento.
        """
        return [(key.value, key.name) for key in cls]

class TipoMantenimiento(Enum):
    """
    Clase enumeración para representar el tipo de mantenimiento
    que debe realizar un vehículo.
    """
    PREVENTIVO_CONSERVATIVO = "Preventivo conservativo"
    PREVENTIVO_PREDICTIVO = "Preventivo predictivo"
    CORRECTIVO = "Correctivo"
    RESTAURATIVO = "Restaurativo"

    @classmethod
    def choices(cls) -> List[Tuple[str, str]]:
        """
        Devuelve una lista de tuplas con los valores y nombres de los tipos de mantenimiento.

        Cada tupla contiene el valor y el nombre de un tipo de mantenimiento.
        Esta lista puede ser útil para usar en campos de elección en modelos de Django.

        Returns:
            List[Tuple[str, str]]: Una lista de tuplas con los valores
            y nombres de los tipos de mantenimiento.
        """
        return [(key.value, key.name) for key in cls]
