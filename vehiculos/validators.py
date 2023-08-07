from datetime import date, datetime
import re

from .exceptions import (
    CodigoBateriaInvalido,
    CodigoDotInvalido,
    FechaFabricacionInvalida,
    LicenciaCaducada,
    PlacaVehicularInvalida, 
)

def es_una_placa_de_vehiculo_valida(placa: str) -> bool:
    """
    Esta función solo verifica si el formato de la placa es válido.
    No verifica si la placa está registrada en el SRI o ANT.
    """
    patron_vehiculo = r'^[A-Z]{3}\-\d{3,4}$'
    patron_moto = r'^[A-Z]{2}\-\d{3}[A-Z]?$'
    return bool(re.match(patron_vehiculo, placa)) or bool(re.match(patron_moto, placa))

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
    """Verifica si un código de batería es válido.

    Args:
        - codigo_bateria (str): El código de batería a verificar.
    Returns:
        - bool: True si el código de batería es válido, False en caso contrario.
    """
    patron = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
    return bool(re.match(patron, codigo_bateria))

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

def validar_placa_vehicular(placa: str):
    """Valida si una placa vehicular es válida.

    Esta función toma una placa vehicular como argumento y verifica si es válida
    utilizando la función es_una_placa_vehicular_valida del archivo utils.py.
    Si la placa no es válida, se lanza una excepción ValidationError.

    Args:
        placa (str): La placa vehicular a validar.

    Raises:
        PlacaVehicularInvalida: Si la placa vehicular no es válida.
    """
    if not es_una_placa_de_vehiculo_valida(placa):
        raise PlacaVehicularInvalida(
            f"{placa} no es una placa vehicular válida.",
            params={'value': placa}
        )

def validar_anio_fabricacion(anio: int) -> None:
    """
    Valida si un año de fabricación es válido.

    Parámetros:
    - anio (int): El año de fabricación a validar.

    Excepciones:
    - FechaFabricacionInvalida: Si el año de fabricación no es válido.

    """
    if not es_un_anio_de_fabricacion_valido (anio):
        raise FechaFabricacionInvalida(
            f"El año {anio} de fabricación está fuera de los límites.",
            params={'value': anio}
        )

def validar_codigo_bateria(codigo_bateria: str) -> None:
    """
    Valida si un código de batería es válido.

    Parámetros:
    - codigo_bateria (str): El código de batería a validar.

    Excepciones:
    - CodigoBateriaInvalido: Si el código de batería no es válido.

    """
    if not es_un_codigo_bateria_valido(codigo_bateria):
        raise CodigoBateriaInvalido(
            f"{codigo_bateria} no es un código de batería válido.",
            params={'value': codigo_bateria}
        )

def validar_codigo_dot(codigo_dot: str):
    """Valida si un código DOT es válido.

    Esta función toma un código DOT como argumento y verifica si es válido
    utilizando la función es_un_codigo_dot_valido del archivo utils.py.
    Si el código DOT no es válido, se lanza una excepción ValidationError.

    Args:
        codigo_dot (str): El código DOT a validar.

    Raises:
        CodigoDotInvalido: Si el código DOT no es válido.
    """
    if not es_un_codigo_dot_valido(codigo_dot):
        raise CodigoDotInvalido(
            f"{codigo_dot} no es un código DOT válido.",
            params={'value': codigo_dot}
        )

def ha_caducado_la_licencia(fecha_caducidad: date):
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

def validar_vigencia_licencia(fecha_caducidad):
    """
    Valida la vigencia de una licencia en función de su fecha de caducidad.

    Args:
        fechaCaducidad (str): La fecha de caducidad de la licencia en formato 'YYYY-MM-DD'.

    Raises:
        LicenciaCaducada: Si la licencia ha caducado.
    """
    if not ha_caducado_la_licencia(fecha_caducidad):
        raise LicenciaCaducada(
            f"{fecha_caducidad} no es una fecha vigente",
            params={'value': fecha_caducidad}
        )
