from django.contrib import admin

from login.admin import TrabajadorAdminPanel

from .models import (
    Bateria, Conductor, Licencia, Llanta,
    Kilometraje, Vehiculo, OperacionMantenimiento,
    HojaMantenimiento, Propietario
)

class BateriaAdminPanel(admin.ModelAdmin):
    icon_name = "battery_charging_full"

class ConductorAdminPanel(TrabajadorAdminPanel):
    pass

class HojaMantenimientoAdminPanel(admin.ModelAdmin):
    icon_name = "format_list_numbered"

class LicenciaAdminPanel(admin.ModelAdmin):
    icon_name = "recent_actors"

class LlantaAdminPanel(admin.ModelAdmin):
    icon_name = "radio_button_checked"

class KilometrajeAdminPanel(admin.ModelAdmin):
    icon_name = "plus_one"

class PropietarioAdminPanel(TrabajadorAdminPanel):
    pass

class OperacionMantenimientoAdminPanel(admin.ModelAdmin):
    icon_name = "build"

class VehiculoAdminPanel(admin.ModelAdmin):
    icon_name = "directions_car"

admin.site.register(Bateria, BateriaAdminPanel)
admin.site.register(Conductor, ConductorAdminPanel)
admin.site.register(HojaMantenimiento, HojaMantenimientoAdminPanel)
admin.site.register(Licencia, LicenciaAdminPanel)
admin.site.register(Llanta, LlantaAdminPanel)
admin.site.register(Kilometraje, KilometrajeAdminPanel)
admin.site.register(OperacionMantenimiento, OperacionMantenimientoAdminPanel)
admin.site.register(Propietario, PropietarioAdminPanel)
admin.site.register(Vehiculo, VehiculoAdminPanel)
