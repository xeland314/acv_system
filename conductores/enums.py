from enum import Enum
from typing import List, Tuple

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
        return [(key.value, key.name) for key in cls]
