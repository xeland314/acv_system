from django.contrib import admin
from .models import (
    Funcionalidad,
    Subscripcion
)

class FuncionalidadAdminPanel(admin.ModelAdmin):
    icon_name = "add_box"

class SuscripcionAdminPanel(admin.ModelAdmin):
    icon_name = "access_time"

admin.site.register(Funcionalidad, FuncionalidadAdminPanel)
admin.site.register(Subscripcion, SuscripcionAdminPanel)
