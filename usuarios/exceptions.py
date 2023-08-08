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

class CedulaInvalida(ValidationError):
    """Raised when a cédula is invalid.

    This exception is raised by the `es_una_cedula_valida` function
    when the cédula being validated does not meet the expected format.
    It is a subclass of DRF's `ValidationError` and can be used to
    return a 400 Bad Request response with a descriptive error message
    when using DRF to build an API.

    Args:
        detail (str): A custom error message (optional).
        params (dict): Additional context for the error message (optional).
    """
    def __init__(self, detail=None, params=None):
        if detail is None:
            detail = "La cédula no cumple con el formato esperado."
        super().__init__(_(detail), params)

class TelefonoInvalido(ValidationError):
    """Raised when a phone number is invalid.

    This exception is raised by the `PersonaSerializer.validate` method
    when the phone number being validated does not meet the expected format.
    It is a subclass of DRF's `ValidationError` and can be used to
    return a 400 Bad Request response with a descriptive error message
    when using DRF to build an API.

    Args:
        detail (str): A custom error message (optional).
        params (dict): Additional context for the error message (optional).
    """
    def __init__(self, detail=None, params=None):
        if detail is None:
            detail = "Número de teléfono inválido."
        super().__init__(_(detail), params)

class ErrorDeConfirmacionDeContrasena(ValidationError):
    """Raised when two passwords do not match.

    This exception is raised by the `PersonaSerializer.validate` method
    when the two passwords being validated do not match.
    It is a subclass of DRF's `ValidationError` and can be used to
    return a 400 Bad Request response with a descriptive error message
    when using DRF to build an API.

    Args:
        detail (str): A custom error message (optional).
    """
    def __init__(self, detail=None):
        if detail is None:
            detail = "Las contraseñas no coinciden."
        super().__init__(_(detail))

class FechaDeNacimientoInvalida(ValidationError):
    """Raised when a date of birth is invalid.

    This exception is raised by the `validar_fecha_de_nacimiento` function
    when the date of birth being validated is not valid according to the
    `es_una_fecha_de_nacimiento_valida` function.
    It is a subclass of DRF's `ValidationError` and can be used to
    return a 400 Bad Request response with a descriptive error message
    when using DRF to build an API.

    Args:
        detail (str): A custom error message (optional).
        params (dict): Additional context for the error message (optional).
    """
    def __init__(self, detail=None, params=None):
        if detail is None:
            detail = "La persona debe ser mayor de edad."
        super().__init__(_(detail), params)

class NombreInvalido(ValidationError):
    """
    Initializes a custom exception instance.

    Args:
        detail (str, optional): The detail message describing the exception.
        params (dict, optional): Additional parameters associated with the exception..
    """
    def __init__(self, detail=None, params=None):
        if detail is None:
            detail = "El nombre introducido no cumple con el formato esperado."
        super().__init__(_(detail), params)
