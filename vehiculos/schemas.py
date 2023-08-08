import coreapi
import coreschema
from django.utils.translation import gettext_lazy as _
from rest_framework.schemas import AutoSchema

class BateriaFilterSchema(AutoSchema):
    def get_manual_fields(self, path: str, method):
        if path.endswith('/search_by/'):
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
    def get_manual_fields(self, path: str, method):
        if path.endswith('/search_by/'):
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

class LicenciaFilterSchema(AutoSchema):
    def get_manual_fields(self, path: str, method):
        if path.endswith('/search_by/'):
            return [
                coreapi.Field(
                    name='conductor_id',
                    required=True,
                    location='query',
                    schema=coreschema.Integer(
                        title='Conductor ID',
                        description='El id del conductor para buscar sus licencias.'
                    )
                )
            ]
        return super().get_manual_fields(path, method)

class LlantaFilterSchema(AutoSchema):
    def get_manual_fields(self, path: str, method):
        if path.endswith('/search_by/'):
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
    def get_manual_fields(self, path: str, method):
        if path.endswith('/search_by/'):
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
