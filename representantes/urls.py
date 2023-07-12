"""urls.py

Define los patrones de URL para la API de Representantes.

Autor: Christopher Villamarín (@xeland314)
"""
from django.urls import path, include
from rest_framework import routers
from .views import RepresentanteView

router = routers.DefaultRouter()
router.register(r'empresas', RepresentanteView, basename="represetantes")

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
