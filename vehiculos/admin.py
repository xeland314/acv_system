from django.contrib import admin

from .models import (
    Bateria, Kilometraje, Licencia, Llanta, Vehiculo
)

@admin.register(Bateria)
class BateriaAdminPanel(admin.ModelAdmin):
    icon_name = "battery_charging_full"

@admin.register(Licencia)
class LicenciaAdminPanel(admin.ModelAdmin):
    icon_name = "recent_actors"

@admin.register(Llanta)
class LlantaAdminPanel(admin.ModelAdmin):
    icon_name = "radio_button_checked"

@admin.register(Kilometraje)
class KilometrajeAdminPanel(admin.ModelAdmin):
    icon_name = "plus_one"

@admin.register(Vehiculo)
class VehiculoAdminPanel(admin.ModelAdmin):
    icon_name = "directions_car"
