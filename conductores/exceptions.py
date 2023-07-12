from django.utils.translation import gettext_lazy as _
from rest_framework.serializers import ValidationError

class LicenciaCaducada(ValidationError):
    """
    Representa una excepción que se produce cuando la licencia ha caducado.

    Args:
        detail (str): Detalle opcional que describe el error de la fecha de caducidad de la licencia.
        params (dict): Parámetros opcionales adicionales para el error.
    """

    def __init__(self, detail=None, params=None):
        """
        Inicializa una instancia de la excepción LicenciaCaducada.

        Args:
            detail (str): Detalle opcional que describe el error de la fecha de caducidad de la licencia.
            params (dict): Parámetros opcionales adicionales para el error.
        """
        if detail is None:
            detail = "La licencia está caducada."
        super().__init__(_(detail), params)
