from django.contrib import admin
from .models import (
    AperturaOrdenMovimiento,
    CierreOrdenMovimiento,
    OrdenTrabajo
)

admin.site.register(AperturaOrdenMovimiento)
admin.site.register(CierreOrdenMovimiento)
admin.site.register(OrdenTrabajo)
