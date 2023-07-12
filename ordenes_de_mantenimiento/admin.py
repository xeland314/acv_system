from django.contrib import admin
from .models import (
    AperturaOrdenMovimiento,
    CierreOrdenMovimiento,
)

@admin.register(AperturaOrdenMovimiento)
class AperturaOrdenMovimientoPanel(admin.ModelAdmin):
    icon_name = "assignment_late"

@admin.register(CierreOrdenMovimiento)
class CierreOrdenMovimientoPanel(admin.ModelAdmin):
    icon_name = "assignment_turned_in"
