from django.contrib import admin

from .models import (
    Bateria, Conductor, Licencia, Llanta,
    Matricula, Odometro, Vehiculo, Operacion,
    HojaMantenimiento
)

admin.site.register(Bateria)
admin.site.register(Conductor)
admin.site.register(Licencia)
admin.site.register(Llanta)
admin.site.register(Matricula)
admin.site.register(Odometro)
admin.site.register(Vehiculo)
admin.site.register(Operacion)
admin.site.register(HojaMantenimiento)
