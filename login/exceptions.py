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
    """
    def __init__(self, detail=None):
        if detail is None:
            detail = "La cédula no cumple con el formato esperado."
        super().__init__(detail)
