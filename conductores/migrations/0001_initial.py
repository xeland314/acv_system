# Generated by Django 4.2.1 on 2023-07-20 14:59

import conductores.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Licencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('F', 'F'), ('A1', 'A1'), ('C', 'C'), ('C1', 'C1'), ('D', 'D'), ('D1', 'D1'), ('E', 'E'), ('E1', 'E1')], help_text='El tipo de la licencia (A, B, C, etc.).', max_length=2)),
                ('fecha_de_emision', models.DateField(help_text='La fecha de emisión de la licencia.')),
                ('fecha_de_caducidad', models.DateField(help_text='La fecha de caducidad de la licencia.', validators=[conductores.validators.validar_vigencia_licencia])),
                ('puntos', models.PositiveSmallIntegerField(help_text='Puntos vigentes de la licencia.')),
            ],
        ),
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('perfilusuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='usuarios.perfilusuario')),
                ('licencia', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='conductores.licencia')),
            ],
            options={
                'verbose_name': 'Conductor',
                'verbose_name_plural': 'Conductores',
            },
            bases=('usuarios.perfilusuario',),
        ),
    ]
