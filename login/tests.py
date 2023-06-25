"""
tests.py

Este módulo define los tests para el proyecto.

Autor: Christopher Villamarín (@xeland314)
Dependencias: django.test.TestCase, django.contrib.auth.models.User,
    rest_framework.test.APIClient, .models.Persona, .utils.es_una_cedula_valida,
    .utils.es_un_numero_de_telefono_valido
"""
from datetime import date, timedelta
import unittest, random
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from .models import Persona
from .exceptions import CedulaInvalida
from .utils import (
    es_una_cedula_valida, es_un_numero_de_telefono_valido,
    es_una_fecha_de_nacimiento_valida, es_un_nombre_valido,
)

class UtilsTestCase(TestCase):
    """Clase de pruebas para las funciones de utilidad."""

    def test_es_un_nombre_valido(self):
        """
        
        """
        #Casos Validos para nombres
        self.assertTrue(es_un_nombre_valido("Ricardo Becerra"))
        self.assertTrue(es_un_nombre_valido("Kevin Revelo"))

        #Casos Invalidos para nombres
        self.assertFalse(es_un_nombre_valido("Romeo"))
        self.assertFalse(es_un_nombre_valido("Daniela21"))
        self.assertFalse(es_un_nombre_valido(" Santiag0"))
        self.assertFalse(es_un_nombre_valido("Rafael@01"))

        #Otros casos invalidos
        self.assertFalse(es_un_nombre_valido("")) #espacios vacios
        self.assertFalse(es_un_nombre_valido(" ")) #espacio en blanco
        self.assertFalse(es_un_nombre_valido("DavidTorres"))
        

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

    

    def testAleatorio_es_un_numero_de_telefono_valido(self):
        """
        Prueba aleatoria de la función es_un_numero_de_telefono_valido.

        Esta función realiza una prueba aleatoria generando casos de números de teléfono válidos e inválidos.
        Verifica si la función es_un_numero_de_telefono_valido devuelve el resultado esperado para cada caso generado.

        Cada caso se genera de la siguiente manera:
        1. Se generan 10 casos aleatorios en total.
        2. Para cada caso:
        - Se selecciona aleatoriamente un número de teléfono válido de una lista predefinida.
        - Se verifica si la función devuelve True para el número de teléfono válido.
        - Se genera un número de teléfono inválido seleccionando aleatoriamente una secuencia de dígitos.
        - Se verifica si la función devuelve False para el número de teléfono inválido.

        Esta prueba tiene como objetivo asegurar el comportamiento adecuado de la función es_un_numero_de_telefono_valido
        en diferentes casos de entrada, incluyendo números de teléfono ecuatorianos válidos e inválidos.
        """
        for _ in range(10):
        # Generar un número de teléfono aleatorio válido
            numero_valido = random.choice([
                "0987129357",
                "593987129357",
                "+593987129357",
                "0991234567",
                "593991234567",
                "+593991234567"
        ])

        # Verificar si la función devuelve el resultado esperado
        self.assertTrue(es_un_numero_de_telefono_valido(numero_valido))

        # Generar un número de teléfono aleatorio inválido
        numero_invalido = ""
        for _ in range(random.randint(1, 10)):
            numero_invalido += random.choice(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])

        # Verificar si la función devuelve el resultado esperado
        self.assertFalse(es_un_numero_de_telefono_valido(numero_invalido))

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

    def testAleatorio_es_una_fecha_de_nacimiento_valida(self) -> None:
        """
        Prueba aleatoria de la función es_una_fecha_de_nacimiento_valida.

        Esta función realiza una prueba aleatoria generando casos de fechas de nacimiento válidas e inválidas.
        Verifica si la función es_una_fecha_de_nacimiento_valida devuelve el resultado esperado para cada caso generado.

        Cada caso se genera de la siguiente manera:
        1. Se obtiene la fecha actual.
        2. Se generan 10 casos aleatorios en total.
        3. Para cada caso:
        - Se genera una edad aleatoria entre 1 y 100 años.
        - Se calcula la fecha de nacimiento restando la cantidad de días correspondiente a la edad generada a la fecha actual.
        - Si la edad es mayor o igual a 18 años, se verifica si la función devuelve True para la fecha de nacimiento.
        De lo contrario, se verifica si la función devuelve False.

        Esta prueba tiene como objetivo asegurar el comportamiento adecuado de la función es_una_fecha_de_nacimiento_valida
        en diferentes casos de entrada, incluyendo fechas de nacimiento válidas e inválidas.

        """

        hoy = date.today()

        for _ in range(10):
        # Generar una fecha de nacimiento aleatoria entre 1 y 100 años atrás
            edad = random.randint(1, 100)
            fecha_nacimiento = hoy - timedelta(days=365*edad)

        # Verificar si la función devuelve el resultado esperado
            if edad >= 18:
                self.assertTrue(es_una_fecha_de_nacimiento_valida(fecha_nacimiento))
            else:
                self.assertFalse(es_una_fecha_de_nacimiento_valida(fecha_nacimiento))


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
