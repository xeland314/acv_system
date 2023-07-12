from enum import Enum
from typing import List, Tuple

class UnidadOdometro(Enum):
    """
    Enumeración de las diferentes unidades para medir un kilometraje.
    """
    KILOMETROS = 'km'
    MILLAS = 'mi'
    DIAS = 'días'
    SEMANAS = 'semanas'
    MESES = 'meses'

    @classmethod
    def choices(cls) -> List[Tuple[str, str]]:
        return [(key.value, key.name) for key in cls]

class Tareas(Enum):
    """
    Enumeración de las tareas de mantenimiento que se puede realizar
    en un vehículo dentro del manual de mantenimiento.
    """
    INSPECCIONAR = {
        'sigla': 'I',
        'descripcion': 'Inspeccionar y corregir oreemplazar de ser el caso.'
    }
    AJUSTAR = {
        'sigla': 'A',
        'descripcion': 'Ajustar.'
    }
    REEMPLAZAR = {
        'sigla': 'R',
        'descripcion': 'Reemplazar o cambiar'
    }
    TORQUE = {
        'sigla': 'T',
        'descripcion': 'Apretar al torque especificado.'
    }
    LUBRICAR = {
        'sigla': 'L',
        'descripcion': 'Lubricar y/o engrasar.'
    }

    @classmethod
    def choices(cls) -> List[Tuple[str, str]]:
        return [(key.value['sigla'], key.name) for key in cls]

    @classmethod
    def get_descripcion(cls, key: str) -> str:
        return cls[key].value['descripcion']
