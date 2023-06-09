"""utils.py

Este módulo define varias clases y funciones de utilidad para el proyecto,
incluyendo clases de enumeración para representar
los estados de cumplimiento

Autor: Christopher Villamarín (@xeland314)
Dependencias: enum.Enum
"""

from enum import Enum

class EstadoCumplimiento(Enum):
    """Clase enumeración para representar el cumplimiento de una inspección."""
    PENDIENTE = "Pendiente"
    CUMPLIDO = "Cumplido"

class TipoMantenimiento(Enum):
    """
    Clase enumeración para representar el tipo de mantenimiento
    que debe realizar un vehículo.
    """
    PREVENTIVO_CONSERVATIVO = "Preventivo conservativo"
    PREVENTIVO_PREDICTIVO = "Preventivo predictivo"
    CORRECTIVO = "Correctivo"
    RESTAURATIVO = "Restaurativo"

# Lista con los valores de la clase enumeración EstadoCumplimiento
ESTADOS_CUMPLIMIENTO = [(tag.name, tag.value) for tag in EstadoCumplimiento]

# Lista con los valores de la clase enumeración TipoMantenimiento
TIPOS_MANTENIMIENTO = [(tag.name, tag.value) for tag in TipoMantenimiento]

from datetime import date, timedelta

class Intervalo:

    def __init__(self, values: list):
        self.values = values

    def generate_interval(self, index: int) -> list:
        max_value = max(self.values)
        interval = self.values[index]
        result = [i for i in range(0, max_value + 1, interval)]
        return result

    def get_interval_subdivision(self, value: int) -> tuple:
        if value < 0:
            raise ValueError("Value must be greater than or equal to 0")
        interval = self.values[0]
        max_value = max(self.values)
        if value == 0:
            return (0, interval)
        min_value = (value // interval) * interval
        max_value = min_value + interval
        return (min_value, max_value)

    def get_the_closest_major(self, value: int) -> int:
        subdivision = self.get_interval_subdivision(value)
        max_value = subdivision[1]
        submultiples = [i for i in self.values if max_value % i == 0]
        return max(submultiples)

    def get_the_nearest_minor(self, value: int) -> int:
        if value < self.values[0]:
            return None
        subdivision = self.get_interval_subdivision(value)
        min_value = subdivision[0]
        submultiples = [i for i in self.values if min_value % i == 0]
        return max(submultiples)

class IntervaloTiempo:
    
    def __init__(self, values: list, start_date: date):
        self.values = values
        self.start_date = start_date

    def get_interval_subdivision(self, value: date) -> tuple:
        interval = self.values[0]
        max_value = max(self.values)
        if value == self.start_date:
            return (self.start_date, self.start_date + timedelta(days=interval))
        min_value = value - timedelta(days=(value - self.start_date).days % interval)
        max_value = min_value + timedelta(days=interval)
        return (min_value, max_value)

    def get_the_closest_major(self, value: date) -> int:
        subdivision = self.get_interval_subdivision(value)
        max_value = subdivision[1]
        submultiples = [i for i in self.values if (max_value - self.start_date).days % i == 0]
        if not submultiples:
            raise ValueError("No submultiple found")
        return max(submultiples)

    def get_the_nearest_minor(self, value: date) -> int:
        if value <= self.start_date + timedelta(self.values[0]):
            return None
        subdivision = self.get_interval_subdivision(value)
        min_value: date = subdivision[0]
        submultiples = [i for i in self.values if (min_value - self.start_date).days % i == 0]
        if not submultiples:
            raise ValueError("No submultiple found")
        return max(submultiples)
