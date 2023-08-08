from django.contrib import admin

from .models import (
    ManualMantenimiento,
    Sistema,
    Subsistema,
    OperacionMantenimiento
)

@admin.register(ManualMantenimiento)
class ManualMantenimientoAdmin(admin.ModelAdmin):
    pass

@admin.register(Sistema)
class SistemaAdmin(admin.ModelAdmin):
    pass

@admin.register(Subsistema)
class SubsistemaAdmin(admin.ModelAdmin):
    pass

@admin.register(OperacionMantenimiento)
class OperacionMantenimientoAdmin(admin.ModelAdmin):
    pass
