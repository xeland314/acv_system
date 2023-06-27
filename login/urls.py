"""urls.py

Define los patrones de URL para la API de Usuarios.

Autor: Christopher Villamarín (@xeland314)

Dependencias:
- django.urls.path
- django.urls.include
- rest_framework.routers
- .views.UsuarioView
"""
from django.urls import path, include
from rest_framework import routers
from .views import EmpresaView, RepresentanteView, TrabajadorView

router = routers.DefaultRouter()
router.register(r"trabajadores", TrabajadorView, "trabajadores")
router.register(r'empresas', EmpresaView, basename="empresas")
router.register(r'representantes', RepresentanteView, basename="representantes")

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
