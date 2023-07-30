from django.contrib import admin
from .models import Empresa, Funcionalidad, Suscripcion

@admin.register(Empresa)
class EmpresaPanel(admin.ModelAdmin):
    icon_name = "business"

@admin.register(Funcionalidad)
class FuncionalidadPanel(admin.ModelAdmin):
    pass

@admin.register(Suscripcion)
class SuscripcionPanel(admin.ModelAdmin):
    pass
