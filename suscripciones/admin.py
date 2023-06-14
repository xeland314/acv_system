from django.contrib import admin
from .models import (
    Empresa,
    Funcionalidad,
    Representante,
    Subscripcion
)

admin.site.register(Empresa)
admin.site.register(Funcionalidad)
admin.site.register(Representante)
admin.site.register(Subscripcion)
