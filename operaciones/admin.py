from django.contrib import admin
from .models import (
    Administrador, OrdenMovimiento, OrdenTrabajo,
    Responsable
)

admin.site.register(Administrador)
admin.site.register(OrdenMovimiento)
admin.site.register(OrdenTrabajo)
admin.site.register(Responsable)
