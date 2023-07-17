from datetime import datetime
from .exceptions import LicenciaCaducada

def ha_caducado_la_licencia(fecha_caducidad: str):
    """
    Verifica si una licencia ha caducado en base a la fecha de caducidad proporcionada.

    Args:
        fechaCaducidad (str): Fecha de caducidad en formato 'YYYY-MM-DD'.

    Returns:
        bool: True si la licencia ha caducado, False en caso contrario.
    """
    # Obtener la fecha actual
    fecha_actual = datetime.now().date()
    # Comparar la fecha de caducidad con la fecha actual
    return fecha_caducidad > fecha_actual

def validar_vigencia_licencia(fechaCaducidad):
    """
    Valida la vigencia de una licencia en función de su fecha de caducidad.

    Args:
        fechaCaducidad (str): La fecha de caducidad de la licencia en formato 'YYYY-MM-DD'.

    Raises:
        LicenciaCaducada: Si la licencia ha caducado.
    """
    if not ha_caducado_la_licencia(fechaCaducidad):
        raise LicenciaCaducada(
            f"{fechaCaducidad} no es una fecha vigente",
            params={'value': fechaCaducidad}
        )
