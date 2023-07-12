from django.contrib import admin

from .models import PerfilUsuario

# Modify Admin panel appearence:
admin.site.site_header = "Wan Way Tech - Admin"
admin.site.index_title = "Dashboard"
admin.site.site_title = "ACV - System"

@admin.register(PerfilUsuario)
class PerfilUsuarioPanel(admin.ModelAdmin):
    icon_name = "business"
