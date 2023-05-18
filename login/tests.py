"""
tests.py

Este módulo define los tests para el proyecto.

Autor: Christopher Villamarín (@xeland314)
Dependencias: django.test.TestCase, django.contrib.auth.models.User,
    rest_framework.test.APIClient, .models.Persona, .utils.es_una_cedula_valida,
    .utils.es_un_numero_de_telefono_valido
"""
from datetime import date
import unittest
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from .models import Persona
from .utils import es_una_cedula_valida, es_un_numero_de_telefono_valido

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

        # Casos inválidos de cédulas ecuatorianas
        self.assertFalse(es_una_cedula_valida("123456789"))  # Cédula incompleta
        #self.assertFalse(es_una_cedula_valida("abcdefghij"))  # Cédula no numérica
        #self.assertFalse(es_una_cedula_valida("123456789X"))  # Cédula con carácter no numérico
        #self.assertFalse(es_una_cedula_valida("123456789X0"))  # Cédula con carácter no numérico
        #self.assertFalse(es_una_cedula_valida("0000000000"))  # Cédula con todos los dígitos iguales
        self.assertFalse(es_una_cedula_valida("9999999999"))  # Cédula con todos los dígitos iguales

        # Otros casos inválidos
        self.assertFalse(es_una_cedula_valida(""))  # Cadena vacía
        self.assertFalse(es_una_cedula_valida(" "))  # Espacio en blanco


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
        self.assertFalse(es_un_numero_de_telefono_valido("123456789"))  # Número demasiado corto
        self.assertFalse(es_un_numero_de_telefono_valido("abcdefghij"))  # Número no numérico
        self.assertFalse(es_un_numero_de_telefono_valido("098712935"))  # Número sin el dígito de control
        self.assertFalse(es_un_numero_de_telefono_valido("59398712935"))  # Número sin el dígito de control
        self.assertFalse(es_un_numero_de_telefono_valido("+59398712935"))  # Número sin el dígito de control
        self.assertFalse(es_un_numero_de_telefono_valido("09912345678"))  # Número demasiado largo
        self.assertFalse(es_un_numero_de_telefono_valido("5939912345678"))  # Número demasiado largo
        self.assertFalse(es_un_numero_de_telefono_valido("+5939912345678"))  # Número demasiado largo

        # Otros casos inválidos
        self.assertFalse(es_un_numero_de_telefono_valido(""))  # Cadena vacía
        self.assertFalse(es_un_numero_de_telefono_valido(" "))  # Espacio en blanco

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
            nivel_educacion='Superior',
            estado_civil='Soltero'
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
            'nivel_educacion': 'Superior',
            'estado_civil': 'Soltero',
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
