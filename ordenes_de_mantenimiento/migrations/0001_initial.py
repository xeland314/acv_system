# Generated by Django 4.2.1 on 2023-07-27 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('conductores', '0001_initial'),
        ('vehiculos', '0001_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AperturaOrdenMovimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_de_emision_orden', models.DateField(auto_now=True, help_text='Fecha de emisión de la orden de movimiento')),
                ('fecha_salida_vehiculo', models.DateField(help_text='Fecha de salida del vehículo')),
                ('itinerario', models.TextField(help_text='Itinerario o viaje')),
                ('detalle_comision', models.TextField(help_text='Detalle de la comisión')),
                ('conductor', models.ForeignKey(help_text='El conductor que va a conducir el vehículo de la orden de apertura.', on_delete=django.db.models.deletion.PROTECT, related_name='aperturas_conductor', to='conductores.conductor')),
                ('kilometraje_salida', models.OneToOneField(help_text='Kilometraje del vehículo al momento de la salida', on_delete=django.db.models.deletion.CASCADE, to='vehiculos.kilometraje')),
                ('persona', models.ForeignKey(help_text='Responsable de emitir la orden de mantenimiento', on_delete=django.db.models.deletion.PROTECT, to='usuarios.perfilusuario')),
                ('vehiculo', models.ForeignKey(help_text='El vehículo del cual se abre la orden de movimiento.', on_delete=django.db.models.deletion.PROTECT, to='vehiculos.vehiculo')),
            ],
            options={
                'verbose_name': 'Apertura de orden de movimiento',
                'verbose_name_plural': 'Aperturas de órdenes de movimiento',
            },
        ),
        migrations.CreateModel(
            name='CierreOrdenMovimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_de_cierre_orden', models.DateField(auto_now=True, help_text='Fecha del cierre de la orden de movimiento')),
                ('fecha_retorno_vehiculo', models.DateField(help_text='Fecha de retorno del vehículo')),
                ('cumplimiento', models.CharField(choices=[('Pendiente', 'PENDIENTE'), ('Cumplido', 'CUMPLIDO')], help_text='Estado de cumplimiento de la orden de movimiento', max_length=20)),
                ('apertura', models.OneToOneField(help_text='Apertura de la orden de movimiento a la que se vincula el cierre de la misma', on_delete=django.db.models.deletion.PROTECT, to='ordenes_de_mantenimiento.aperturaordenmovimiento')),
                ('kilometraje_retorno', models.OneToOneField(help_text='Kilometraje del vehículo al momento del retorno', on_delete=django.db.models.deletion.CASCADE, to='vehiculos.kilometraje')),
            ],
            options={
                'verbose_name': 'Cierre de orden de movimiento',
                'verbose_name_plural': 'Cierres de órdenes de movimiento',
            },
        ),
    ]
