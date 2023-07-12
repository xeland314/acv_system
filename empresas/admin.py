from django.contrib import admin
from .models import Empresa

@admin.register(Empresa)
class EmpresaPanel(admin.ModelAdmin):
    icon_name = "business"
