from django.urls import include, path
from rest_framework import routers

from .views import (
    ManualMantenimientoViewSet,
    OperacionMantenimientoViewSet,
    SistemaViewSet,
    SubsistemaViewSet
)

router = routers.DefaultRouter()
router.register(r'manuales_mantenimiento', ManualMantenimientoViewSet)
router.register(r'sistemas', SistemaViewSet)
router.register(r'subsistemas', SubsistemaViewSet)
router.register(r'operaciones_mantenimiento', OperacionMantenimientoViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
