from django.contrib import admin

from .models import (
    Bateria, Conductor, Licencia, Llanta,
    Kilometraje, Vehiculo, OperacionMantenimiento,
    HojaMantenimiento, Propietario
)

admin.site.register(Bateria)
admin.site.register(Conductor)
admin.site.register(Licencia)
admin.site.register(Llanta)
admin.site.register(Kilometraje)
admin.site.register(Vehiculo)
admin.site.register(OperacionMantenimiento)
admin.site.register(HojaMantenimiento)
admin.site.register(Propietario)
