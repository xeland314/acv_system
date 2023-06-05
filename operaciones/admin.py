from django.contrib import admin
from .models import (
    Administrador, AperturaOrdenMovimiento, CierreOrdenMovimiento,
    OrdenTrabajo, Responsable
)

admin.site.register(Administrador)
admin.site.register(AperturaOrdenMovimiento)
admin.site.register(CierreOrdenMovimiento)
admin.site.register(OrdenTrabajo)
admin.site.register(Responsable)
