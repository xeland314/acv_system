"""
tests.py

Este módulo define los tests para control_vehicular.

Autor: Christopher Villamarín (@xeland314)
"""
import unittest

from django.test import TestCase

from .exceptions import (
    CodigoDotInvalido,
    PlacaVehicularInvalida
)
from .models import (
    validar_codigo_dot,
    validar_placa_vehicular
)
from .utils import (
    es_un_codigo_dot_valido,
    es_una_placa_de_vehiculo_valida,
    obtener_fecha_fabricacion
)

class UtilsTestCase(TestCase):
    """Clase de pruebas para las funciones de utilidad."""

    def test_es_una_placa_de_vehiculo_valida(self) -> None:
        """
        Prueba la función es_una_placa_de_vehiculo_valida con diferentes entradas.

        Verifica que la función devuelve True para placas de vehículos y motos válidas
        y False para placas con formatos inválidos.
        """
        self.assertTrue(es_una_placa_de_vehiculo_valida('ABC-1234'))
        self.assertTrue(es_una_placa_de_vehiculo_valida('AB-123'))
        self.assertFalse(es_una_placa_de_vehiculo_valida('ABCD-1234'))
        self.assertFalse(es_una_placa_de_vehiculo_valida('ABC-12345'))
        self.assertFalse(es_una_placa_de_vehiculo_valida('AB-123CD'))
        self.assertRaises(
            PlacaVehicularInvalida, validar_placa_vehicular, 'ABCD-1234'
        )
        self.assertRaises(
            PlacaVehicularInvalida, validar_placa_vehicular, 'ABC-12345'
        )
        self.assertRaises(
            PlacaVehicularInvalida, validar_placa_vehicular, 'AB-123CD'
        )

    def test_es_un_codigo_dot_valido(self) -> None:
        """
        Prueba la función es_un_codigo_dot_valido con diferentes entradas.

        Verifica que la función devuelve True para códigos DOT válidos y False para
        códigos DOT con formatos inválidos.
        """
        self.assertTrue(es_un_codigo_dot_valido('DOT-80CB-PWP5-0823'))
        self.assertFalse(es_un_codigo_dot_valido('DOT-80CB-PWP5-823'))
        self.assertFalse(es_un_codigo_dot_valido('DOT-80CB-PWP50823'))
        self.assertRaises(
            CodigoDotInvalido, validar_codigo_dot, 'DOT-80CB-PWP5-823'
        )
        self.assertRaises(
            CodigoDotInvalido, validar_codigo_dot, 'DOT-80CB-PWP50823'
        )

    def test_obtener_fecha_fabricacion(self) -> None:
        """
        Prueba la función obtener_fecha_fabricacion con diferentes entradas.

        Verifica que la función devuelve la fecha de fabricación correcta para un
        código DOT válido.
        """
        fecha_fabricacion = obtener_fecha_fabricacion('DOT-80CB-PWP5-0823')
        self.assertEqual(fecha_fabricacion.year, 2023)
        self.assertEqual(fecha_fabricacion.month, 2)
        self.assertEqual(fecha_fabricacion.day, 20)

class TestSuite(TestCase):
    """
    Todos los tests agrupados en uno.
    """
    def suite(self):
        """Agrupar tests antes de ejecutar el comando:
            `python3 manage.py test`

        Returns:
            suite: unittest.TestSuite
        """
        suite = unittest.TestSuite()
        suite.addTest(UtilsTestCase('test_utils_vehiculos'))
        return suite
