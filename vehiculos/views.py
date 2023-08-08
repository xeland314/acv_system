from django.utils.translation import gettext_lazy as _
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from .schemas import (
    BateriaFilterSchema,
    KilometrajeFilterSchema,
    LicenciaFilterSchema,
    LlantaFilterSchema,
    VehiculoFilterSchema
)
from .serializers import (
    BateriaSerializer,
    LicenciaSerializer,
    LlantaSerializer,
    KilometrajeSerializer,
    VehiculoSerializer,
)
from .models import (
    Bateria, Licencia, Llanta,
    Vehiculo, Kilometraje,
)

class BateriaView(viewsets.ModelViewSet):
    """
    Clase que define la vista para listar y crear baterías.
    """
    queryset = Bateria.objects.all()
    serializer_class = BateriaSerializer

    @action(detail=False, methods=['get'], schema=BateriaFilterSchema())
    def search_by(self, request: Request):
        """Busca baterías por vehículo.

        Esta función busca baterías en la base de datos que pertenecen al vehículo
        especificado en el parámetro `vehiculo_id` de la petición HTTP.

        Args:
            request (Request): La petición HTTP con el parámetro de búsqueda.

        Returns:
            Response: Una respuesta HTTP con los datos serializados de las baterías
            que pertenecen al vehículo especificado, o un mensaje de error si no se
            encontraron baterías o si el parámetro de búsqueda es incorrecto.
        """
        vehiculo_id = request.query_params.get('vehiculo_id')

        if not vehiculo_id:
            return Response(
                {"error": _("Parámetro de búsqueda incorrecto: vehiculo_id es obligatorio.")},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            baterias = Bateria.objects.filter(vehiculo_id=vehiculo_id)
            serializer = BateriaSerializer(baterias, many=True)
            return Response(serializer.data)
        except Bateria.DoesNotExist:
            return Response(
                {"error": _("No se encontraron baterías para el vehículo especificado.")},
                status=status.HTTP_404_NOT_FOUND
            )

class LlantaView(viewsets.ModelViewSet):
    """
    Clase que define la vista para listar y crear llantas.
    """
    queryset = Llanta.objects.all()
    serializer_class = LlantaSerializer

    @action(detail=False, methods=['get'], schema=LlantaFilterSchema())
    def search_by(self, request: Request):
        """Busca llantas por vehículo.

        Esta función busca llantas en la base de datos que pertenecen al vehículo
        especificado en el parámetro `vehiculo_id` de la petición HTTP.

        Args:
            request (Request): La petición HTTP con el parámetro de búsqueda.

        Returns:
            Response: Una respuesta HTTP con los datos serializados de las llantas
            que pertenecen al vehículo especificado, o un mensaje de error si no se
            encontraron llantas o si el parámetro de búsqueda es incorrecto.
        """
        vehiculo_id = request.query_params.get('vehiculo_id')

        if not vehiculo_id:
            return Response(
                {"error": _("Parámetro de búsqueda incorrecto: vehiculo_id es obligatorio.")},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            llantas = Llanta.objects.filter(vehiculo_id=vehiculo_id)
            serializer = LlantaSerializer(llantas, many=True)
            return Response(serializer.data)
        except Llanta.DoesNotExist:
            return Response(
                {"error": _("No se encontraron llantas para el vehículo especificado.")},
                status=status.HTTP_404_NOT_FOUND
            )

class LicenciaView(viewsets.ModelViewSet):
    """
    Clase que define la vista para listar y crear licencias.
    """
    queryset = Licencia.objects.all()
    serializer_class = LicenciaSerializer

    @action(detail=False, methods=['get'], schema=LicenciaFilterSchema())
    def search_by(self, request: Request):
        """Busca licencias por conductor.

        Esta función busca licencias en la base de datos que pertenecen al conductor
        especificado en el parámetro `conductor_id` de la petición HTTP.

        Args:
            request (Request): La petición HTTP con el parámetro de búsqueda.

        Returns:
            Response: Una respuesta HTTP con los datos serializados de las licencias
            que pertenecen al conductor especificado, o un mensaje de error si no se
            encontraron licencias o si el parámetro de búsqueda es incorrecto.
        """
        conductor_id = request.query_params.get('conductor_id')

        if not conductor_id:
            return Response(
                {"error": _("Parámetro de búsqueda incorrecto: conductor_id es obligatorio.")},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            licencias = Licencia.objects.filter(conductor_id=conductor_id)
            serializer = LicenciaSerializer(licencias, many=False)
            return Response(serializer.data)
        except Licencia.DoesNotExist:
            return Response(
                {"error": _("No se encontraron licencias para el conductor especificado.")},
                status=status.HTTP_404_NOT_FOUND
            )

class KilometrajeView(viewsets.ModelViewSet):
    """
    Vista para gestionar los kilometrajes de los vehículos.
    """
    queryset = Kilometraje.objects.all()
    serializer_class = KilometrajeSerializer

    @action(detail=False, methods=['get'], schema=KilometrajeFilterSchema())
    def search_by(self, request: Request):
        """Busca kilometrajes por vehículo.

        Esta función busca kilometrajes en la base de datos que pertenecen al vehículo
        especificado en el parámetro `vehiculo_id` de la petición HTTP.

        Args:
            request (Request): La petición HTTP con el parámetro de búsqueda.

        Returns:
            Response: Una respuesta HTTP con los datos serializados de los kilometrajes
            que pertenecen al vehículo especificado, o un mensaje de error si no se
            encontraron kilometrajes o si el parámetro de búsqueda es incorrecto.
        """
        vehiculo_id = request.query_params.get('vehiculo_id')

        if not vehiculo_id:
            return Response(
                {"error": _("Parámetro de búsqueda incorrecto: vehiculo_id es obligatorio.")},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            kilometrajes = Kilometraje.objects.filter(vehiculo_id=vehiculo_id)
            serializer = KilometrajeSerializer(kilometrajes, many=True)
            return Response(serializer.data)
        except Kilometraje.DoesNotExist:
            return Response(
                {"error": _("No se encontraron kilometrajes para el vehículo especificado."),},
                status=status.HTTP_404_NOT_FOUND
            )

class VehiculoView(viewsets.ModelViewSet):
    """
    Vista para gestionar vehículos.
    """
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

    @action(detail=False, methods=['get'], schema=VehiculoFilterSchema())
    def search_by(self, request: Request):
        """Busca vehículos por propietario.

        Esta función busca vehículos en la base de datos que pertenecen al propietario
        especificado en el parámetro `propietario_id` de la petición HTTP.

        Args:
            request (Request): La petición HTTP con el parámetro de búsqueda.

        Returns:
            Response: Una respuesta HTTP con los datos serializados de los vehículos
            que pertenecen al propietario especificado, o un mensaje de error si no se
            encontraron vehículos o si el parámetro de búsqueda es incorrecto.
        """
        propietario_id = request.query_params.get('propietario_id')

        if not propietario_id:
            return Response(
                {"error": _("Parámetro de búsqueda incorrecto: propietario_id es obligatorio.")},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            vehiculos = Vehiculo.objects.filter(propietario_id=propietario_id)
            serializer = VehiculoSerializer(vehiculos, many=True)
            return Response(serializer.data)
        except Vehiculo.DoesNotExist:
            return Response(
                {"error": _("No se encontraron vehículos para el propietario especificado.")},
                status=status.HTTP_404_NOT_FOUND
            )
