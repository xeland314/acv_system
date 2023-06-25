"""
tests.py

Este módulo define los tests para control_vehicular.

Autor: Christopher Villamarín (@xeland314)
"""
import random
import unittest

from django.test import TestCase

from .exceptions import (
    CodigoDotInvalido,
    PlacaVehicularInvalida,
    FechaFabricacionInvalida,
    CodigoBateriaInvalido,
    LicenciaCaducada
)
from .models import (
    validar_codigo_dot,
    validar_placa_vehicular,
    validar_anio_fabricacion,
    validar_codigo_bateria,
    validar_vigencia_licencia,

)
from .utils import (
    es_un_codigo_dot_valido,
    es_una_placa_de_vehiculo_valida,
    es_un_anio_de_fabricacion_valido,
    es_un_codigo_bateria_valido,
    obtener_fecha_fabricacion,
    ha_caducado_la_licencia
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

    def test_es_anio_fabricacion(self) -> None:
        self.assertTrue(es_un_anio_de_fabricacion_valido(1992))
        self.assertTrue(es_un_anio_de_fabricacion_valido(2000))
        self.assertFalse(es_un_anio_de_fabricacion_valido(2099))
        self.assertRaises(
            FechaFabricacionInvalida, validar_anio_fabricacion, 1500
        )
        self.assertRaises(
            FechaFabricacionInvalida, validar_anio_fabricacion, 2025
        )
        
    def test_es_codigo_bateria(self) -> None:
        self.assertTrue(es_un_codigo_bateria_valido("POWR2022"))
        self.assertTrue(es_un_codigo_bateria_valido("MAXPOWER99"))
        self.assertFalse(es_un_codigo_bateria_valido("BATERIA"))
        self.assertRaises(
            CodigoBateriaInvalido, validar_codigo_bateria, "PW120"
        )
        self.assertRaises(
            CodigoBateriaInvalido, validar_codigo_bateria, "1283944"
        )

    def test_vigencia_licencia(self) -> None:
        """
        Prueba la funcionalidad de vigencia de la licencia.

        Realiza una serie de pruebas para verificar si la función ha_caducado_la_licencia y la excepción LicenciaCaducada funcionan correctamente.

        Returns:
        None
        """
        self.assertTrue(ha_caducado_la_licencia('2025-08-19'))
        self.assertFalse(ha_caducado_la_licencia('2005-12-19'))
        self.assertFalse(ha_caducado_la_licencia('2022-04-15'))
        self.assertRaises(
            LicenciaCaducada, validar_vigencia_licencia, '2019-11-29'
        )
        self.assertRaises(
            LicenciaCaducada, validar_vigencia_licencia, '2015-09-08'
        )

    def test_aleatorio_vigencia_licencia(self) -> None:
        for i in range(101):
            anio_aleatorio = random.randint(1990, 2022)
            mes_aleatorio = random.randint(1, 12)
            dia_aleatorio = random.randint(1, 25)

            self.assertRaises(
            LicenciaCaducada, validar_vigencia_licencia, str(anio_aleatorio) +
              "-" +str(mes_aleatorio) + "-" + str(dia_aleatorio)
        )


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
