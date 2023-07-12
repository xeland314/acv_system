"""
tests.py

Este módulo define los tests para el proyecto.

Autor: Christopher Villamarín (@xeland314)
Dependencias: django.test.TestCase, django.contrib.auth.models.User,
    rest_framework.test.APIClient, .models.Persona, .utils.es_una_cedula_valida,
    .utils.es_un_numero_de_telefono_valido
"""
from datetime import date, timedelta
import random
import unittest

from django.test import TestCase

from .exceptions import CedulaInvalida
from .validators import (
    es_una_cedula_valida,
    es_un_numero_de_telefono_valido,
    es_mayor_de_edad,
    es_un_nombre_valido,
    generar_cedula_ecuatoriana,
    validar_cedula
)

class UtilsTestCase(TestCase):
    """Clase de pruebas para las funciones de utilidad."""

    def test_es_un_nombre_valido(self):
        """ Prueba la función es_un_nombre_valido
        Verifica si el nombre de una persona solo consta de caracteres
        y no incluye números u otros caracteres raros.
        """
        #Casos Validos para nombres
        self.assertTrue(es_un_nombre_valido("Ricardo Becerra"))
        self.assertTrue(es_un_nombre_valido("Kevin Revelo"))
        self.assertTrue(es_un_nombre_valido("Romeo"))
        self.assertTrue(es_un_nombre_valido("DavidTorres"))

        #Casos Invalidos para nombres
        self.assertFalse(es_un_nombre_valido("Daniela21"))
        self.assertFalse(es_un_nombre_valido(" Santiag0"))
        self.assertFalse(es_un_nombre_valido("Rafael@01"))

        #Otros casos invalidos
        self.assertFalse(es_un_nombre_valido("")) #espacios vacios
        self.assertFalse(es_un_nombre_valido(" ")) #espacio en blanco

    def test_validacion_de_cedula(self):
        """Prueba la función validar_cedula.

        Verifica que la función validar_cedula lance la excepción CedulaInvalida
        para cada caso especial de entrada, incluyendo cédulas ecuatorianas inválidas.
        """
        # Casos inválidos de cédulas ecuatorianas
        self.assertRaises(
            CedulaInvalida, validar_cedula, "123456789"
        )
        self.assertRaises(
            CedulaInvalida, validar_cedula, "abcdefghij"
        )
        self.assertRaises(
            CedulaInvalida, validar_cedula, "123456789X"
        )
        self.assertRaises(
            CedulaInvalida, validar_cedula, "123456789X0"
        )
        self.assertRaises(
            CedulaInvalida, validar_cedula, "9999999999"
        )
        self.assertRaises(
            CedulaInvalida, validar_cedula, ""
        )
        self.assertRaises(
            CedulaInvalida, validar_cedula, " "
        )

    def test_cedula_valida_con_numero_aleatorio(self):
        """
        Prueba que se generen números de cédula de ciudadanía ecuatoriana válidos.

        La prueba se realiza de la siguiente manera:
        - Se genera un número de cédula de ciudadanía ecuatoriana aleatorio.
        - Se verifica que el número generado sea válido.
        """
        for _ in range(10000):
            self.assertTrue(es_una_cedula_valida(
                generar_cedula_ecuatoriana()
            ))

    def test_cedula_invalida_con_numero_aleatorio(self):
        """Prueba que se detecten números de cédula de ciudadanía ecuatoriana inválidos.

        La prueba se realiza de la siguiente manera:
        - Se generan 101 números aleatorios entre 10000 y 99999.
        - Se les agrega el prefijo "1789".
        - Se verifica que cada uno de estos números sea inválido.
        """
        for _ in range(101):
            numero_aleatorio = random.randint(10000, 99999)
            self.assertRaises(
                CedulaInvalida, validar_cedula,  f"1789{numero_aleatorio}"
            )

    def test_es_un_numero_de_telefono_valido(self):
        """Prueba la función es_un_numero_de_telefono_valido.

        Verifica si la función es_un_numero_de_telefono_valido devuelve
        el resultado esperado para diferentes casos de entrada,
        incluyendo números de teléfono ecuatorianos válidos e inválidos.
        """
        # Casos válidos de números de teléfono ecuatorianos
        self.assertTrue(es_un_numero_de_telefono_valido("0987129357"))
        self.assertTrue(es_un_numero_de_telefono_valido("593987129357"))
        self.assertTrue(es_un_numero_de_telefono_valido("+593987129357"))
        self.assertTrue(es_un_numero_de_telefono_valido("0991234567"))
        self.assertTrue(es_un_numero_de_telefono_valido("593991234567"))
        self.assertTrue(es_un_numero_de_telefono_valido("+593991234567"))

        # Casos inválidos de números de teléfono ecuatorianos
        self.assertFalse(es_un_numero_de_telefono_valido("123456789"))
        self.assertFalse(es_un_numero_de_telefono_valido("abcdefghij"))
        self.assertFalse(es_un_numero_de_telefono_valido("098712935"))
        self.assertFalse(es_un_numero_de_telefono_valido("59398712935"))
        self.assertFalse(es_un_numero_de_telefono_valido("+59398712935"))
        self.assertFalse(es_un_numero_de_telefono_valido("09912345678"))
        self.assertFalse(es_un_numero_de_telefono_valido("5939912345678"))
        self.assertFalse(es_un_numero_de_telefono_valido("+5939912345678"))

        # Otros casos inválidos
        self.assertFalse(es_un_numero_de_telefono_valido(""))  # Cadena vacía
        self.assertFalse(es_un_numero_de_telefono_valido(" "))  # Espacio en blanco

    def test_es_mayor_de_edad(self):
        """Prueba la función es_una_fecha_de_nacimiento_valida.

        Verifica si la función es_una_fecha_de_nacimiento_valida devuelve
        el resultado esperado para diferentes casos de entrada,
        incluyendo fechas de nacimiento válidas e inválidas.
        """
        hoy = date.today()
        # Ayer fue su cumpleaños #18
        edad_18_1 = hoy.replace(hoy.year - 18) - timedelta(days=1)
        # Hoy es el cumpleaños #18
        edad_18 = hoy.replace(hoy.year - 18)
        # Mañana será el cumpleaños #18
        edad_17 = hoy.replace(hoy.year - 18) + timedelta(days=1)
        # Casos válidos de fechas de nacimiento
        self.assertTrue(es_mayor_de_edad(edad_18_1))
        self.assertTrue(es_mayor_de_edad(edad_18))
        self.assertTrue(es_mayor_de_edad(hoy - timedelta(days=365*19)))
        self.assertTrue(es_mayor_de_edad(hoy - timedelta(days=365*20)))
        self.assertTrue(es_mayor_de_edad(hoy - timedelta(days=365*30)))

        # Casos inválidos de fechas de nacimiento
        self.assertFalse(es_mayor_de_edad(hoy))
        self.assertFalse(es_mayor_de_edad(edad_17))
        self.assertFalse(es_mayor_de_edad(hoy - timedelta(days=365*17)))
        self.assertFalse(es_mayor_de_edad(hoy - timedelta(days=365*16)))
        self.assertFalse(es_mayor_de_edad(hoy - timedelta(days=365*10)))

    def test_aleatorio_es_o_no_mayor_de_edad(self) -> None:
        """Prueba aleatoria de la función es_mayor_de_edad.

        La prueba se realiza de la siguiente manera:
        - Se generan casos de fechas de nacimiento válidas e inválidas.
        - Se comprueba si la función es_mayor_de_edad devuelve el resultado esperado.
        """
        hoy = date.today()
        for _ in range(10000):
            edad = random.randint(1, 100)
            fecha_nacimiento = hoy.replace(hoy.year - edad)
            if edad >= 18:
                self.assertTrue(es_mayor_de_edad(fecha_nacimiento))
            else:
                self.assertFalse(es_mayor_de_edad(fecha_nacimiento))

class TestSuite(TestCase):
    """
    Todos los tests agrupados en uno.
    """
    def suite(self):
        """Agrupar tests antes de ejecutar el comando:
            python3 manage.py test

        Returns:
            suite: unittest.TestSuite
        """
        suite = unittest.TestSuite()
        suite.addTest(UtilsTestCase('test_utils'))
        return suite

