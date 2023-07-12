from django.contrib import admin
from .models import OrdenTrabajo

@admin.register(OrdenTrabajo)
class OrdenTrabajoPanel(admin.ModelAdmin):
    icon_name = "assignment"
