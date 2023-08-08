"""
Módulo de URLs para operaciones.

Autor: Christopher Villamarín (@xeland314)
"""

from django.urls import path, include
from rest_framework import routers

from .views import OrdenTrabajoView

router = routers.DefaultRouter()
router.register(r'ordenes_trabajo', OrdenTrabajoView, basename='ordenes_trabajo')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
