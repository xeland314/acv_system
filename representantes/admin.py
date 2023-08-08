from django.contrib import admin
from .models import Representante

@admin.register(Representante)
class RepresentantePanel(admin.ModelAdmin):
    icon_name = "business"
