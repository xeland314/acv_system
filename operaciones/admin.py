from django.contrib import admin
from .models import (
    AperturaOrdenMovimiento,
    CierreOrdenMovimiento,
    OrdenTrabajo
)

class AperturaOrdenMovimientoPanel(admin.ModelAdmin):
    icon_name = "assignment_late"

class CierreOrdenMovimientoPanel(admin.ModelAdmin):
    icon_name = "assignment_turned_in"

class OrdenTrabajoPanel(admin.ModelAdmin):
    icon_name = "assignment"

admin.site.register(AperturaOrdenMovimiento, AperturaOrdenMovimientoPanel)
admin.site.register(CierreOrdenMovimiento, CierreOrdenMovimientoPanel)
admin.site.register(OrdenTrabajo, OrdenTrabajoPanel)
