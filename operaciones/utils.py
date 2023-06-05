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
