from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from .models import (
    ManualMantenimiento,
    OperacionMantenimiento,
    Sistema,
    Subsistema
)
from .schemas import (
    ManualMantenimientoSchema,
    OperacionMantenimientoSchema,
    SistemaSchema,
    SubsistemaSchema
)
from .serializers import (
    ManualMantenimientoSerializer,
    OperacionMantenimientoSerializer,
    SistemaSerializer,
    SubsistemaSerializer
)

class ManualMantenimientoViewSet(ModelViewSet):
    """
    ViewSet para el modelo ManualMantenimiento.
    """
    queryset = ManualMantenimiento.objects.all()
    serializer_class = ManualMantenimientoSerializer

    @action(detail=False, methods=['get'], schema=ManualMantenimientoSchema())
    def by_vehiculo(self, request: Request):
        vehiculo_id = request.query_params.get('vehiculo_id')
        if not vehiculo_id:
            return Response(
                {"error": "vehiculo_id is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            manual = self.queryset.get(vehiculo_id=vehiculo_id)
            serializer = ManualMantenimientoSerializer(manual)
            return Response(serializer.data)
        except ManualMantenimiento.DoesNotExist:
            return Response(
                {"error": "ManualMantenimiento not found"},
                status=status.HTTP_404_NOT_FOUND
            )

class SistemaViewSet(ModelViewSet):
    """
    ViewSet para el modelo Sistema.
    """
    queryset = Sistema.objects.all()
    serializer_class = SistemaSerializer

    @action(detail=False, methods=['get'], schema=SistemaSchema())
    def by_manual_mantenimiento(self, request: Request):
        manualmantenimiento_id = request.query_params.get('manual_mantenimiento_id')
        if not manualmantenimiento_id:
            return Response(
                {"error": "manualmantenimiento_id is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        queryset = self.queryset.filter(manualmantenimiento_id=manualmantenimiento_id)
        if not queryset.exists():
            return Response(
                {"error": "Sistemas not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = SistemaSerializer(queryset, many=True)
        return Response(serializer.data)

class SubsistemaViewSet(ModelViewSet):
    """
    ViewSet para el modelo Subsistema.
    """
    queryset = Subsistema.objects.all()
    serializer_class = SubsistemaSerializer

    @action(detail=False, methods=['get'], schema=SubsistemaSchema())
    def by_sistema(self, request: Request):
        sistema_id = request.query_params.get('sistema_id')
        if not sistema_id:
            return Response(
                {"error": "sistema_id is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        queryset = self.queryset.filter(sistema_id=sistema_id)
        if not queryset.exists():
            return Response(
                {"error": "Subsistemas not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = SubsistemaSerializer(queryset, many=True)
        return Response(serializer.data)

class OperacionMantenimientoViewSet(ModelViewSet):
    """
    ViewSet para el modelo OperacionMantenimiento.
    """
    queryset = OperacionMantenimiento.objects.all()
    serializer_class = OperacionMantenimientoSerializer

    @action(detail=False, methods=['get'], schema=OperacionMantenimientoSchema())
    def by_subsistema(self, request: Request):
        subsistema_id = request.query_params.get('subsistema_id')
        if not subsistema_id:
            return Response(
                {"error": "subsistema_id is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        queryset = self.queryset.filter(subsistema_id=subsistema_id)
        if not queryset.exists():
            return Response(
                {"error": "Operaciones not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = OperacionMantenimientoSerializer(queryset, many=True)
        return Response(serializer.data)
