"""urls.py

Define los patrones de URL para la API de Empresas.

Autor: Christopher Villamarín (@xeland314)
"""
from django.urls import path, include
from rest_framework import routers
from .views import EmpresaView, FuncionalidadView, SuscripcionView

router = routers.DefaultRouter()
router.register(r'empresas', EmpresaView, basename="empresas")
router.register(r'funcionalidades', FuncionalidadView, basename="funcionalidades")
router.register(r'suscripciones', SuscripcionView, basename="suscripciones")

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
