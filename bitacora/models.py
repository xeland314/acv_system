from django.db import models

class Dispositivo(models.Model):
    imei = models.CharField(max_length=50)
    device_name = models.CharField(max_length=100)
    is_wireless = models.BooleanField(default=False)
    device_type = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50, blank=True)

class CuentaApi(models.Model):
    account_id = models.IntegerField()
    account = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    parent_account_id = models.IntegerField()

class EstadoDispositivo(models.Model):
    cuenta = models.ForeignKey(
        CuentaApi,
        on_delete=models.CASCADE,
        related_name="estados_cuenta"
    )
    dispositivo = models.ForeignKey(
        Dispositivo,
        on_delete=models.CASCADE,
        related_name="estados_dispositivo"
    )
    status = models.CharField(max_length=50)
    lng = models.CharField(max_length=20)
    lat = models.CharField(max_length=20)
    speed = models.IntegerField()
    course = models.IntegerField()
    acc_status = models.BooleanField()
    license_number = models.CharField(max_length=50)
    vin = models.CharField(max_length=50)
    end_time = models.BigIntegerField()
    platform_end_time = models.BigIntegerField()
    activate_time = models.BigIntegerField()
    status_time_desc = models.BigIntegerField()
    signal_time = models.BigIntegerField()
    gps_time = models.BigIntegerField()
    position_type = models.CharField(max_length=50)
    is_wireless = models.BooleanField(default=False)
    sim = models.CharField(max_length=50)
    ext_voltage = models.IntegerField()
    car_owner = models.CharField(max_length=100)
    contract_number = models.CharField(max_length=100)
    sim_end_time = models.IntegerField()
    charge_percentage = models.IntegerField()

class Alarma(models.Model):
    dispositivo = models.ForeignKey(
        Dispositivo,
        on_delete=models.CASCADE,
        related_name="alarmas_dispositivo"
    )
    lng = models.CharField(max_length=20)
    lat = models.CharField(max_length=20)
    time = models.BigIntegerField()
    alarm_code = models.CharField(max_length=50)
    alarm_time = models.BigIntegerField()
    device_type = models.SmallIntegerField()
    alarm_type = models.SmallIntegerField()
    position_type = models.CharField(max_length=50)
    speed = models.SmallIntegerField()
    course = models.SmallIntegerField()
