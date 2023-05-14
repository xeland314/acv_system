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
from .views import UsuarioView

router = routers.DefaultRouter()
router.register(r"users", UsuarioView, "users")

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
