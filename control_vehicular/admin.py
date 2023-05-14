from django.contrib import admin

from .models import Conductor, Licencia, Matricula, Llanta

admin.site.register(Conductor)
admin.site.register(Licencia)
admin.site.register(Matricula)
admin.site.register(Llanta)