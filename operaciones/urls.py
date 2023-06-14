"""
Módulo de URLs para operaciones.

Autor: Christopher Villamarín (@xeland314)
"""

from django.urls import path, include
from rest_framework import routers

from .views import (
    AperturaOrdenMovimientoView,
    CierreOrdenMovimientoView,
    OrdenTrabajoView
)

router = routers.DefaultRouter()
router.register(
    r'apertura_ordenes_movimiento',
    AperturaOrdenMovimientoView,
    basename='apertura_ordenes_movimiento'
)
router.register(
    r'cierre_ordenes_movimiento',
    CierreOrdenMovimientoView,
    basename='cierre_ordenes_movimiento'
)
router.register(r'ordenes_trabajo', OrdenTrabajoView, basename='ordenes_trabajo')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
