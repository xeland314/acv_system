from django.contrib import admin

from .models import (
    Empresa,
    Representante,
    Trabajador
)

# Modify Admin panel appearence:
admin.site.site_header = "Wan Way Tech - Admin"
admin.site.index_title = "Dashboard"
admin.site.site_title = "ACV - System"

class EmpresaAdminPanel(admin.ModelAdmin):
    icon_name = "business"

class RepresentanteAdminPanel(admin.ModelAdmin):
    icon_name = "supervisor_account"

class TrabajadorAdminPanel(admin.ModelAdmin):
    icon_name = "assignment_ind"

# Register your models here.
admin.site.register(Empresa, EmpresaAdminPanel)
admin.site.register(Representante, RepresentanteAdminPanel)
admin.site.register(Trabajador, TrabajadorAdminPanel)
