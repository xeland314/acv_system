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
)

from .validators import (
    es_un_codigo_dot_valido,
    es_una_placa_de_vehiculo_valida,
    es_un_anio_de_fabricacion_valido,
    es_un_codigo_bateria_valido,
    obtener_fecha_fabricacion,
    validar_codigo_dot,
    validar_placa_vehicular,
    validar_anio_fabricacion,
    validar_codigo_bateria,
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
    
    def test_aleatorio_es_una_placa_de_vehiculo_valida(self) -> None:
        """Prueba aleatoria de la función es_una_placa_de_vehiculo_valida.

        Esta función prueba la validez de la función es_una_placa_de_vehiculo_valida
        en diferentes casos de entrada, verificando el formato de la placa.
        Se generan 1000 casos aleatorios de placas de vehículos y motos válidas e inválidas.
        Para cada caso, se verifica si la función devuelve el resultado esperado.
        """
        LETRAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        NUMEROS = "0123456789"
        for _ in range(1000):
            # Generar una placa de vehículo aleatoria válida
            letras = random.choices(LETRAS, k=3)
            numeros = random.choices(NUMEROS, k=random.choice([3, 4]))
            placa_valida = "".join(letras) + "-" + "".join(numeros)

            # Verificar la longitud de la placa válida
            self.assertTrue(len(placa_valida) == 7 or len(placa_valida) == 8)

            # Verificar si la función devuelve el resultado esperado para la placa válida
            self.assertTrue(es_una_placa_de_vehiculo_valida(placa_valida))

            # Generar una placa de vehículo aleatoria inválida cambiando una letra o un número en la placa válida
            posicion = random.randint(0, len(placa_valida) - 1)
            if placa_valida[posicion].isalpha():
                # Cambiar una letra por un número
                placa_invalida = placa_valida[:posicion] + random.choice(NUMEROS) + placa_valida[posicion + 1:]
            else:
                # Cambiar un número por una letra
                placa_invalida = placa_valida[:posicion] + random.choice(LETRAS) + placa_valida[posicion + 1:]

            # Verificar si la función devuelve el resultado esperado para la placa inválida
            self.assertFalse(es_una_placa_de_vehiculo_valida(placa_invalida))

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
        self.assertTrue(es_un_codigo_bateria_valido('POWR2022'))
        self.assertTrue(es_un_codigo_bateria_valido('MAXPOWER99'))
        self.assertFalse(es_un_codigo_bateria_valido('BATERIA'))
        self.assertRaises(
            CodigoBateriaInvalido, validar_codigo_bateria, "AS123"
        )
        self.assertRaises(
            CodigoBateriaInvalido, validar_codigo_bateria, "2023125"
        )
        self.assertRaises(
            CodigoBateriaInvalido, validar_codigo_bateria, "PW120"
        )
        self.assertRaises(
            CodigoBateriaInvalido, validar_codigo_bateria, "1283944"
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
