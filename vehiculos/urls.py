"""
Módulo de URLs para el control vehicular.

Autor: Christopher Villamarín (@xeland314)
"""

from django.urls import path, include
from rest_framework import routers

from .views import (
    BateriaView,
    LlantaView,
    VehiculoView,
    KilometrajeView,
    PropietarioView
)

router = routers.DefaultRouter()
router.register(r'baterias', BateriaView, basename='baterias')
router.register(r'kilometrajes', KilometrajeView, basename='kilometrajes')
router.register(r'llantas', LlantaView, basename='llantas')
router.register(r'propietarios', PropietarioView, basename='propietarios')
router.register(r'vehiculos', VehiculoView, basename='vehiculos')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
