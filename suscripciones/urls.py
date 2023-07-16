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

from .views import FuncionalidadView, SubscripcionView

router = routers.DefaultRouter()
router.register(r'funcionalidades', FuncionalidadView, basename="funcionalidades")
router.register(r'suscripciones', SubscripcionView, basename="suscripciones")

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
