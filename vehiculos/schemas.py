import coreapi
import coreschema
from django.utils.translation import gettext_lazy as _
from rest_framework.schemas import AutoSchema

class BateriaFilterSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        if path == '/vehiculos/api/v1/baterias/buscar_por_vehiculo_id/':
            return [
                coreapi.Field(
                    name='vehiculo_id',
                    required=True,
                    location='query',
                    schema=coreschema.Integer(
                        title='Vehiculo ID',
                        description='El id del vehículo para buscar sus baterías.'
                    )
                )
            ]
        return super().get_manual_fields(path, method)

class KilometrajeFilterSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        if path in (
            '/vehiculos/api/v1/kilometrajes/buscar_por_vehiculo_id/',
            '/vehiculos/api/v1/kilometrajes/ultimo_buscar_por_vehiculo_id/'
        ):
            return [
                coreapi.Field(
                    name='vehiculo_id',
                    required=True,
                    location='query',
                    schema=coreschema.Integer(
                        title='Vehiculo ID',
                        description='El id del vehículo para buscar sus kilometrajes.'
                    )
                )
            ]
        return super().get_manual_fields(path, method)

class LlantaFilterSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        if path == '/vehiculos/api/v1/llantas/buscar_por_vehiculo_id/':
            return [
                coreapi.Field(
                    name='vehiculo_id',
                    required=True,
                    location='query',
                    schema=coreschema.Integer(
                        title='Vehiculo ID',
                        description='El id del vehículo para buscar sus llantas.'
                    )
                )
            ]
        return super().get_manual_fields(path, method)

class VehiculoFilterSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        if path == '/vehiculos/api/v1/vehiculos/buscar_por_propietario/':
            return [
                coreapi.Field(
                    name='propietario_id',
                    required=True,
                    location='query',
                    schema=coreschema.Integer(
                        title='Propietario ID',
                        description='El id del propietario para buscar los vehículos.'
                    )
                )
            ]
        return super().get_manual_fields(path, method)
