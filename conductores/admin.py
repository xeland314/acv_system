from django.contrib import admin

from usuarios.admin import PerfilUsuarioPanel

from .models import (
    Conductor, Licencia
)

@admin.register(Conductor)
class ConductorPanel(PerfilUsuarioPanel):
    pass

@admin.register(Licencia)
class LicenciaAdminPanel(admin.ModelAdmin):
    icon_name = "recent_actors"
