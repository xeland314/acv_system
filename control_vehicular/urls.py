"""
Módulo de URLs para el control vehicular.

Autor: Christopher Villamarín (@xeland314)
"""

from django.urls import path, include
from rest_framework import routers

from .views import (
    BateriaView, ConductorView, LicenciaView, LlantaView,
    VehiculoView, KilometrajeView, OperacionMatenimientoView,
    HojaMantenimientoView, PropietarioView
)

router = routers.DefaultRouter()
router.register(r'baterias', BateriaView, basename='baterias')
router.register(r'conductores', ConductorView, basename='conductores')
router.register(r'kilometrajes', KilometrajeView, basename='kilometrajes')
router.register(r'licencias', LicenciaView, basename='licencias')
router.register(r'llantas', LlantaView, basename='llantas')
router.register(r'propietarios', PropietarioView, basename='propietarios')
router.register(r'vehiculos', VehiculoView, basename='vehiculos')
router.register(
    r'operaciones-matenimiento',
    OperacionMatenimientoView,
    basename='operaciones_mantenimiento'
)
router.register(
    r'hojas-mantenimiento',
    HojaMantenimientoView,
    basename='hojas_mantenimiento'
)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
