import coreapi
import coreschema
from rest_framework.schemas import AutoSchema

class ManualMantenimientoSchema(AutoSchema):

    def get_manual_fields(self, path: str, method):
        if path.endswith('/search_by/'):
            return [
                coreapi.Field(
                    name='vehiculo_id',
                    required=True,
                    location='query',
                    schema=coreschema.Integer(
                        title='Vehiculo ID',
                        description=(
                            'ID del vehiculo del cual desea'
                            ' obtener el manual de mantenimiento'
                        )
                    )
                )
            ]
        return super().get_manual_fields(path, method)

class SistemaSchema(AutoSchema):
    def get_manual_fields(self, path: str, method):
        if path.endswith('/search_by/'):
            return [
                coreapi.Field(
                    name='manual_mantenimiento_id',
                    required=True,
                    location='query',
                    schema=coreschema.Integer(
                        title='Manual Mantenimiento ID',
                        description=(
                            'ID del manual de mantenimiento para'
                            ' el que se desean obtener los sistemas'
                        )
                    )
                )
            ]
        return super().get_manual_fields(path, method)

class SubsistemaSchema(AutoSchema):
    def get_manual_fields(self, path: str, method):
        if path.endswith('/search_by/'):
            return [
                coreapi.Field(
                    name='sistema_id',
                    required=True,
                    location='query',
                    schema=coreschema.Integer(
                        title='Sistema ID',
                        description='ID del sistema para el que se desean obtener los subsistemas'
                    )
                )
            ]
        return super().get_manual_fields(path, method)

class OperacionMantenimientoSchema(AutoSchema):
    def get_manual_fields(self, path: str, method):
        if path.endswith('/search_by/'):
            return [
                coreapi.Field(
                    name='subsistema_id',
                    required=True,
                    location='query',
                    schema=coreschema.Integer(
                        title='Subsistema ID',
                        description=(
                            'ID del subsistema para el que se desean'
                            ' obtener las operaciones de mantenimiento'
                        )
                    )
                )
            ]
        return super().get_manual_fields(path, method)
