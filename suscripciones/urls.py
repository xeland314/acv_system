"""urls.py

Define los patrones de URL para la API de Suscripciones.

Este módulo define patrones de URL para las vistas FuncionalidadView, EmpresaView,
RepresentanteView y SubscripcionView utilizando un objeto router de la clase
DefaultRouter.

Autor: Christopher Villamarín (@xeland314)

Dependencias:
- django.urls.path
- django.urls.include
- rest_framework.routers
- .views.EmpresaView
- .views.FuncionalidadView
- .views.RepresentanteView
- .views.SubscripcionView
"""

from django.urls import path, include
from rest_framework import routers

from .views import EmpresaView, FuncionalidadView, RepresentanteView, SubscripcionView

router = routers.DefaultRouter()
router.register(r'funcionalidades', FuncionalidadView, basename="funcionalidades")
router.register(r'empresas', EmpresaView, basename="empresas")
router.register(r'representantes', RepresentanteView, basename="representantes")
router.register(r'subscripciones', SubscripcionView, basename="suscripciones")

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
