"""views.py

Este módulo define la vista PerfilView para listar y crear usuarios.

Autor: Christopher Villamarín (@xeland314)
"""
import coreapi
import coreschema
from django.utils.translation import gettext_lazy as _
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from .models import PerfilUsuario
from .serializers import PerfilSerializer

class UserFilterSchema(AutoSchema):

    def get_description(self, path: str, method):
        """
        Devuelve una descripción personalizada para la vista.
        """
        if path.endswith('/search_by/'):
            return 'Filtra los perfiles de usuario por empresa y rol.'
        return super().get_description(path, method)

    def get_manual_fields(self, path: str, method):
        """
        Devuelve una lista de campos personalizados para la vista.
        """
        extra_fields = []

        if path.endswith('search_by'):
            extra_fields = [
                coreapi.Field(
                    name='empresa_id',
                    required=True,
                    location='query',
                    schema=coreschema.Integer(
                        title='Empresa ID',
                        description='El id de la empresa de este usuario.'
                    ),
                    description='El id de la empresa a filtrar.'
                ),
                coreapi.Field(
                    name='role',
                    required=False,
                    location='query',
                    schema=coreschema.String(
                        title='Rol',
                        description='Rol del usuario dentro de la empresa.'
                    ),
                    description='El rol de los usuarios a filtrar.'
                )
            ]
        return super().get_manual_fields(path, method) + extra_fields

class PerfilView(ModelViewSet):
    """
    Perfiles de usuario
    """
    queryset = PerfilUsuario.objects.all()
    serializer_class = PerfilSerializer
    permission_classes =  [IsAuthenticated,]
    authentication_class = (TokenAuthentication,)

    @action(detail=False, methods=['get'], schema=UserFilterSchema())
    def search_by(self, request: Request):
        """Filtra los perfiles de usuario por empresa y rol.

        Args:
            request (Request): La petición HTTP con los parámetros de búsqueda.

        Returns:
            Response: Una respuesta HTTP con los datos serializados de los perfiles
            que coinciden con los criterios de búsqueda, o un mensaje de error si
            los parámetros son incorrectos.

        Raises:
            ValidationError: Si los parámetros de búsqueda no son válidos.
        """
        empresa_id = request.query_params.get('empresa_id')
        role = request.query_params.get('role')

        if empresa_id and role:
            queryset = PerfilUsuario.objects.filter(empresa_id=empresa_id, role=role)
        elif empresa_id:
            queryset = PerfilUsuario.objects.filter(empresa_id=empresa_id)
        else:
            return Response(
                {"error": _("Parámetros de búsqueda incorrectos.")},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not queryset.exists():
            return Response(
                {"error": _("No se ha encontrado ningún usuario con este rol en esta empresa")},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = PerfilSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def search(self, request: Request):
        """
        Busca un usuario por su nombre de usuario,
        correo electrónico o número de cédula.

        Este método recibe como argumentos el nombre de usuario, el correo electrónico
        o el número de cédula del usuario a buscar,
        y devuelve la información del usuario correspondiente utilizando
        el serializador PerfilSerializer.

        Args:
            - username (str): El nombre de usuario del usuario a buscar.
            - email (str): El correo electrónico del usuario a buscar.
            - cedula (str): El número de cédula del usuario a buscar.

            Solo uno de estos parámetros debe ser proporcionado en cada llamada.
            Si se proporciona más de uno, solo se utilizará el primero.

        Returns:
            - Un objeto Response con la información del usuario en formato JSON,
            o un mensaje de error si ocurre algún problema.
        """
        username = request.query_params.get('username')
        email = request.query_params.get('email')
        cedula = request.query_params.get('cedula')

        if username:
            queryset = PerfilUsuario.objects.filter(username=username)
        elif email:
            queryset = PerfilUsuario.objects.filter(email=email)
        elif cedula:
            queryset = PerfilUsuario.objects.filter(cedula=cedula)
        else:
            return Response(
                {"error": _("Parámetros de búsqueda incorrectos.")},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not queryset.exists():
            return Response(
                {"error": _("No se ha encontrado ningún usuario con estos datos")},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = PerfilSerializer(queryset.first())
        return Response(serializer.data)
