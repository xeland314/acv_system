"""
Módulo de URLs para las bitácoras.

Autor: Christopher Villamarín (@xeland314)
"""
from django.urls import path, include
from rest_framework import routers
from .views import (
    DispositivoViewSet, CuentaApiViewSet, EstadoDispositivoViewSet, AlarmaViewSet
)

router = routers.DefaultRouter()
router.register(r'dispositivos', DispositivoViewSet, basename='dispositivos')
router.register(r'cuentas', CuentaApiViewSet, basename='cuentas')
router.register(r'estados', EstadoDispositivoViewSet, basename='estados')
router.register(r'alarmas', AlarmaViewSet, basename='alarmas')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
