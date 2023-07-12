"""
Módulo de URLs para el control vehicular.

Autor: Christopher Villamarín (@xeland314)
"""

from django.urls import path, include
from rest_framework import routers

from .views import (
    ConductorView, LicenciaView
)

router = routers.DefaultRouter()
router.register(r'conductores', ConductorView, basename='conductores')
router.register(r'licencias', LicenciaView, basename='licencias')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
