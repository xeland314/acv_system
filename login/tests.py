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
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from .models import Persona
from .exceptions import CedulaInvalida
from .utils import (
    es_una_cedula_valida, es_un_numero_de_telefono_valido,
    es_una_fecha_de_nacimiento_valida
)

class UtilsTestCase(TestCase):
    """Clase de pruebas para las funciones de utilidad."""

    def test_es_una_cedula_valida(self):
        """Prueba la función es_una_cedula_valida.

        Verifica si la función es_una_cedula_valida devuelve
        el resultado esperado para diferentes casos de entrada,
        incluyendo cédulas ecuatorianas válidas e inválidas.
        """
        # Casos válidos de cédulas ecuatorianas
        self.assertTrue(es_una_cedula_valida("1753828696"))
        self.assertTrue(es_una_cedula_valida("0000000000"))

        # Casos inválidos de cédulas ecuatorianas
        self.assertRaises(
            CedulaInvalida, es_una_cedula_valida, "123456789"
        )
        self.assertRaises(
            CedulaInvalida, es_una_cedula_valida, "abcdefghij"
        )
        self.assertRaises(
            CedulaInvalida, es_una_cedula_valida, "123456789X"
        )
        self.assertRaises(
            CedulaInvalida, es_una_cedula_valida, "123456789X0"
        )
        self.assertRaises(
            CedulaInvalida, es_una_cedula_valida, "9999999999"
        )
        self.assertRaises(
            CedulaInvalida, es_una_cedula_valida, ""
        )
        self.assertRaises(
            CedulaInvalida, es_una_cedula_valida, " "
        )

    def test_aleatorio_es_una_cedula_valida(self):
        for i in range(101):
            numero_aleatorio = random.randint(10000, 99999)
            self.assertRaises(
            CedulaInvalida, es_una_cedula_valida,  f"1789{numero_aleatorio}"
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

    def test_es_una_fecha_de_nacimiento_valida(self):
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
        self.assertTrue(es_una_fecha_de_nacimiento_valida(edad_18_1))
        self.assertTrue(es_una_fecha_de_nacimiento_valida(edad_18))
        self.assertTrue(es_una_fecha_de_nacimiento_valida(hoy - timedelta(days=365*19)))
        self.assertTrue(es_una_fecha_de_nacimiento_valida(hoy - timedelta(days=365*20)))
        self.assertTrue(es_una_fecha_de_nacimiento_valida(hoy - timedelta(days=365*30)))

        # Casos inválidos de fechas de nacimiento
        self.assertFalse(es_una_fecha_de_nacimiento_valida(hoy))
        self.assertFalse(es_una_fecha_de_nacimiento_valida(edad_17))
        self.assertFalse(es_una_fecha_de_nacimiento_valida(hoy - timedelta(days=365*17)))
        self.assertFalse(es_una_fecha_de_nacimiento_valida(hoy - timedelta(days=365*16)))
        self.assertFalse(es_una_fecha_de_nacimiento_valida(hoy - timedelta(days=365*10)))

class ViewsTestCase(TestCase):
    """Clase de pruebas para las vistas."""

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.persona = Persona.objects.create(
            user=self.user,
            nombres='Test',
            apellidos='User',
            cedula='1753828695',
            email='test@example.com',
            fecha_nacimiento=date(2000, 1, 1),
            telefono='0987654321',
            direccion='Calle Principal',
            nivel_educacion='SUPERIOR',
            estado_civil='SOLTERO'
        )
        self.api_direcction = '/auth/api/v1/users/'

    def test_usuario_view_list(self):
        """Prueba la vista UsuarioView para listar usuarios.

        Verifica si la vista UsuarioView devuelve la lista de usuarios
        correctamente cuando se realiza una solicitud GET.
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.api_direcction)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['nombres'], 'Test')
        self.assertEqual(response.data[0]['apellidos'], 'User')

    def test_usuario_view_create(self):
        """Prueba la vista UsuarioView para crear usuarios.

        Verifica si la vista UsuarioView crea un nuevo usuario
        correctamente cuando se realiza una solicitud POST con datos válidos.
        """
        self.client.force_authenticate(user=self.user)
        data = {
            'nombres': 'John',
            'apellidos': 'Doe',
            'cedula': '1753828696',
            'email': 'johndoe@example.com',
            'telefono': '0987129357',
            'fecha_nacimiento': date(2000, 1, 1),
            'nivel_educacion': 'SUPERIOR',
            'estado_civil': 'SOLTERO',
            'contrasena': 'password',
            'contrasena2': 'password'
        }
        response = self.client.post(self.api_direcction, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Persona.objects.count(), 2)
        self.assertEqual(Persona.objects.last().nombres, 'John')
        self.assertEqual(Persona.objects.last().apellidos, 'Doe')

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
        suite.addTest(ViewsTestCase('test_login'))
        return suite
