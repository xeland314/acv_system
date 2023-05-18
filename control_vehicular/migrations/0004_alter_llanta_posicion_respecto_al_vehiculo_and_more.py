# Generated by Django 4.2.1 on 2023-05-18 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('control_vehicular', '0003_matricula_propietario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='llanta',
            name='posicion_respecto_al_vehiculo',
            field=models.CharField(choices=[('DERECHO_DELANTERO', 'Derecho delantero'), ('DERECHO_POSTERIOR', 'Derecho posterior'), ('DERECHO_POSTERIOR_EXTERIOR', 'Derecho posterior exterior'), ('DERECHO_POSTERIOR_INTERIOR', 'Derecho posterior interior'), ('IZQUIERDO_DELANTERO', 'Izquierdo delantero'), ('IZQUIERDO_POSTERIOR', 'Izquierdo posterior'), ('IZQUIERDO_POSTERIOR_EXTERIOR', 'Izquierdo posterior exterior'), ('IZQUIERDO_POSTERIOR_INTERIOR', 'Izquierdo posterior interior'), ('REPUESTO', 'Respuesto')], max_length=50, verbose_name='Posición respecto al vehículo'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='combustible',
            field=models.CharField(choices=[('GASOLINA', 'Gasolina'), ('DIESEL', 'Diésel'), ('GAS', 'Gas'), ('ELECTRICO', 'Eléctrico')], max_length=30, verbose_name='Combustible'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='condicion',
            field=models.CharField(choices=[('OPERABLE', 'Operable'), ('NO_OPERABLE', 'No operable'), ('EN_MANTENIMIENTO', 'En mantenimiento')], max_length=30, verbose_name='Condición vehicular'),
        ),
        migrations.CreateModel(
            name='Bateria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_de_fabricacion', models.CharField(max_length=50, verbose_name='Código de fabricación')),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='baterias', to='control_vehicular.vehiculo')),
            ],
        ),
    ]