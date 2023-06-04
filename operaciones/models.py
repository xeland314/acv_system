from django.db import models
from django.utils.translation import gettext_lazy as _

from control_vehicular.models import Vehiculo, Conductor
from login.models import Persona

class Administrador(Persona):

    class Meta:
        verbose_name = _("Administrador")
        verbose_name_plural = _("Administradores")

class Responsable(Persona):
    
    class Meta:
        verbose_name = _("Responsable")
        verbose_name_plural = _("Responsables")

class OrdenTrabajo(models.Model):
    fecha_emision = models.DateField(auto_now=True, blank=False)
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    tipo_mantenimiento = models.CharField(max_length=20, choices=[("Preventivo", "Preventivo"), ("Correctivo", "Correctivo"), ("Restaurativo", "Restaurativo")])
    tipo_trabajo = models.TextField()
    cumplimiento = models.CharField(max_length=20, choices=[("Pendiente", "Pendiente"), ("Cumplido", "Cumplido")])

    class Meta:
        verbose_name = _("Orden de trabajo")
        verbose_name_plural = _("Órdenes de trabajo")

    def __str__(self) -> str:
        return ""

class OrdenMovimiento(models.Model):
    fecha_emision = models.DateField(auto_now=True, blank=False)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE)
    itineario = models.TextField()
    detalle_comision = models.TextField()
    fecha_retorno = models.DateField()
    km_retorno = models.IntegerField()
    km_actual = models.IntegerField()
    cumplimiento = models.CharField(max_length=20, choices=[("Sí", "Sí"), ("No", "No")])

    class Meta:
        verbose_name = _("Orden de movimiento")
        verbose_name_plural = _("Órdenes de movimiento")

    def __str__(self) -> str:
        return ""
