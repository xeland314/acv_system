"""Custom exceptions for a Django project.

This module defines several custom exceptions that can be used
in a Django project to handle specific error conditions.
The exceptions are subclasses of DRF's `ValidationError` and
can be used to return 400 Bad Request responses with descriptive
error messages when using DRF to build an API.

Author:
    Christopher Villamarín (@xeland314)

Dependencies:
    - django.utils.translation.gettext_lazy
    - rest_framework.serializers.ValidationError
"""
from django.utils.translation import gettext_lazy as _
from rest_framework.serializers import ValidationError

class CodigoDotInvalido(ValidationError):
    """Raised when a DOT code is invalid.

    This exception is raised when the DOT code being validated does not meet the expected format.
    It is a subclass of DRF's `ValidationError` and can be used to
    return a 400 Bad Request response with a descriptive error message
    when using DRF to build an API.

    Args:
        detail (str): A custom error message (optional).
        params (dict): Additional context for the error message (optional).
    """
    def __init__(self, detail=None, params=None):
        if detail is None:
            detail = "El código DOT no cumple con el formato esperado."
        super().__init__(_(detail), params)


class PlacaVehicularInvalida(ValidationError):
    """Raised when a vehicle license plate is invalid.

    This exception is raised when the vehicle license plate being validated does not meet the expected format.
    It is a subclass of DRF's `ValidationError` and can be used to
    return a 400 Bad Request response with a descriptive error message
    when using DRF to build an API.

    Args:
        detail (str): A custom error message (optional).
        params (dict): Additional context for the error message (optional).
    """
    def __init__(self, detail=None, params=None):
        if detail is None:
            detail = "La placa vehicular no cumple con el formato esperado."
        super().__init__(_(detail), params)

class Fecha_Fabricacion_Invalida(ValidationError):
    """
    Initializes the exception instance.

    Parameters:
    - detail: Optional. A string specifying the detail message for the exception.
     If not provided, the default message "El año de fabricacion no cumple con el formato esperado."
              will be used.
    - params: Optional. A dictionary of additional parameters to be included with the exception.

    """

    def __init__(self, detail=None, params=None):
        if detail is None:
            detail = "El año de fabricacion no cumple con el formato esperado."
        super().__init__(_(detail), params)

class CodigoBateriaInvalido(ValidationError):
    """
    Valida si un código de batería cumple con los requisitos establecidos.

    Args:
        codigo_bateria (str): El código de batería a validar.

    Returns:
        bool: True si el código de batería es válido, False en caso contrario.
    """

    def __init__(self, detail=None, params=None):
        if detail is None:
            detail = "El año de codigo de bateria no cumple con el formato esperado."
        super().__init__(_(detail), params)

        

